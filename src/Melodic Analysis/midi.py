#author: Shannon Hwu
#version: 1.0

'''
MUST INSTALL MIDO PACKAGE FOR PYTHON TO USE:
command in terminal: pip install mido
'''
from mido import MidiFile

def inputFileName():
    filename = input("What is the name of the MIDI file you want to parse? ")
    type(filename)
    numNotes(filename)

def numNotes(filename):
    notes = {0 : "C", 1 : "C#", 2 : "D", 3 : "D#", 4 : "E", 5 : "F", 6 : "F#", 7 : "G", 8: "G#", 9 : "A", 10 : "A#", 11 : "B"}
    numberNotes = {"C" : 0, "C#" : 0, "D" : 0,  "D#" : 0, "E" : 0, "F" : 0, "F#" : 0, "G" : 0, "G#" : 0, "A" : 0, "A#" : 0, "B" : 0}
    
    '''
    make major and minor
    or different keys
    '''
    numNotes = 0
    filename = filename + '.mid'
    midiFile = MidiFile(filename)
#     print(midiFile)
    for track in range(1, len(midiFile.tracks)):
#         print(track)
        for msg in midiFile.tracks[track]:
#             print(msg)
            msg = str(msg)
            msgList = msg.split(" ")
            if len(msgList) ==  5:
#                 print(msgList)
                noteMsg = msgList[2]
                noteList = noteMsg.split("=")
#                 print(noteList)
                try:
                    noteNo = int(noteList[1])
                    note = notes[noteNo % 12]
                    numberNotes[note] += 1
#                     print(note)
#                     print(noteNo)
                    numNotes += 1
                except:
                    pass
    numNotes = int(numNotes/2)
    for i in range(0, len(numberNotes)):
        numberNotes[notes[i]] /= 2
        print("{} has been played {} times".format(notes[i], int(numberNotes[notes[i]])))
    print("There are a total of {} notes in {}".format(numNotes, filename))

inputFileName()
