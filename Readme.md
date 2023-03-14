# RTFM 
## Goals

RTFM have originally been designed to allow players of a physical role play game to trigger sounds. 

To enforce the immersion of the game, any player will be able to connect to the local Wifi and access an internet page. 
This page is filled with buttons and allow anyone to trigger sound samples or ambiances.

## Basic design 

RTFM have two main components:
1. WebServer => Handle the displayu of the webpage and the HTTP requests
2. MidiDevice => Mount a virtual MIDI device, which can send Notes and CC events

When the WebServer receives HTTP Post events, it parses it to know what button is being pushed. The event is translated into Midi.

The MIDI mapping of each sounds is described in mapping.json where you can select if the sound is trigger using a notes on/off event or a CC. You can also specify the MIDI channel to use. 
You can also the "group" field in mapping.json to improve the HTML page, which is quickly required if you have more than 10 semples. 

## Use

RTFM requires both mido and pytemidi. They are both retrievable using pip.
I use Python 3.9 - other versions are untested (but any Python3 should work)

You need to prepare a DAW or similar that will listen the MIDI device and play the sounds. 
I personally use Bitwig with and a DrumRack. The ampping.json is mine, and will need to be customized. 


## TODO

- Implement HTML Filter by group
- Improve CSS
- Implement players.json where you can defined access rights by character
- Background music player - Like samples, but with On/Off capabilities - and a tracking of the curently playing musics
- Auto-update Bitwig DrumRack from sample files contains in a directory (ease the curently - manualy done - required steps)
