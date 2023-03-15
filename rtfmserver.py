from http.server import BaseHTTPRequestHandler
import mididevice
import cgi
import sounds
import spamfilter

# TODO - This should be class member
MIDI_DEVICE = mididevice.MidoDevice()
SPAM_FILER = spamfilter.SpamFilter(1)

class RtfmServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # get the form data
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'GET',
                     'CONTENT_TYPE': self.headers['Content-Type'], })
        
        print(self.client_address[0])
        print(self.path)
        if self.path.endswith("mystyle.css"):
            with open("mystyle.css", 'r') as css_file:
                css = css_file.read()

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(css, "utf-8"))
            return
        else:
            self.soundmap=sounds.get_sounds()
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            # TODO - html_generator.py
            self.wfile.write(bytes("<meta charset=\"UTF-8\">", "utf-8"))
            self.wfile.write(bytes("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">", "utf-8"))
            self.wfile.write(bytes("<html><head><title>D&D MusicBox</title></head>", "utf-8"))
            self.wfile.write(bytes("<link rel=\"stylesheet\" href=\"mystyle.css\">", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("</br>", "utf-8"))
            self.wfile.write(bytes("<iframe name=\"votar\" style=\"display:none;\"></iframe>", "utf-8"))
            self.wfile.write(bytes("<form action=\"0.0.0.0:8080/api/rtfm\" method=\"post\" target=\"votar\">", "utf-8"))
            
            # Sound buttons
            self.wfile.write(bytes(f"<p>", "utf-8"))
            last_group = str()
            for sound in sorted(self.soundmap, key=sounds.get_group):
                group = sounds.get_group(sound)
                if last_group != group:
                    last_group = group
                    self.wfile.write(bytes(f"</p>", "utf-8"))
                    self.wfile.write(bytes(f"<p align='center'><font><b>{group}</b></font></p>", "utf-8"))
                    self.wfile.write(bytes(f"<p align='center'>", "utf-8"))
                   
                name = sound["name"]
                self.wfile.write(bytes(f"<button type='submit' name='state' value='{name}'>{name}</button>", "utf-8"))
            
            self.wfile.write(bytes(f"</p>", "utf-8"))
            self.wfile.write(bytes("</form></p>", "utf-8"))
            self.wfile.write(bytes("</body>", "utf-8"))


    def do_POST(self):
        # get the form data
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'], })

        print("POST : " + str(self.client_address))

        
        # check path
        if self.path.endswith('/api/rtfm'):
            # Command callbacks
            sound = sounds.find_sound(form["state"].value)
            if sound is not None:
                print(sound)
                name, channel, note, cc, group = sounds.get_sound_info(sound)

                # TODO - SpamFilter config to allow any group to bypass it
                if group != 'Admin' and not SPAM_FILER.is_authorized(self.client_address[0]):
                    print("SPAM ALERT: " + str(self.client_address))
                    return
                
                if note is not None:
                    MIDI_DEVICE.send_note_on_off(channel, note)
                elif cc is not None:
                    MIDI_DEVICE.send_cc(channel, cc)

            else:
                print("Unknown Command: " + str(form["state"].value))

            return

        # otherwise return 404 not found
        self.send_response(404)
        self.end_headers()
        self.wfile.write("not found")
