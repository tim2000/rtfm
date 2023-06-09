# RTFM 
## Goals

RTFM have originally been designed to allow players of a physical role play game to trigger sounds. 

To enforce the immersion of the game, any player will be able to connect to the local Wifi and access an internet page. 
This page is filled with buttons and allow anyone to trigger sound samples or ambiances.

## Basic design 

RTFM have two main components:
1. WebServer => Handle the HTML/CSS webpage and the HTTP requests
2. MidiDevice => Mount a virtual MIDI device, which can send Notes and CC events

When the WebServer receives HTTP Post events, it parses it to know what button is being pushed. The event is translated into Midi.

The MIDI mapping of each sounds is described in mapping.json where you can select if the sound will be triggered using a notes on/off event or a CC. You can also specify the MIDI channel to use. 
You can also use the "group" field in mapping.json to improve the HTML page, which is quickly required if you have more than 10 samples. 

## Use

RTFM requires both mido and pytemidi. They are both retrievable using pip.
I use Python 3.9 - other versions are untested (but any Python3 should work)

You need to prepare a DAW or similar that will listen the MIDI device and play the sounds. 
I personally use Bitwig with a DrumRack. The file mapping.json is an exemple of mine, this needs to be customized for your setup. 


## TODO

### New Features
1. Implement players.json where you can defined access rights by character
2. Background music player - Like samples, but with On/Off capabilities - and a tracking of the curently playing musics
3. Auto-update Bitwig DrumRack from sample files contains in a directory (ease the curently - manualy done - required steps)
4. Global config (http port to be used, spam filter time, ...)
### WebSever Improvments
1. Implement HTML Filter by group
2. Improve CSS
### MidiDevice Improvments
1. Notes and CC only send one event (curently we do ON/sleep/OFF with fixed value for the CC)
