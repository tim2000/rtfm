from rtfmserver import RtfmServer


if __name__ == "__main__":
    import socketserver

    PORT = 8080
    with socketserver.TCPServer(("", PORT), RtfmServer) as httpd: 
        print("serving at port", PORT)
        httpd.serve_forever()

    print("Server stopped.")
    