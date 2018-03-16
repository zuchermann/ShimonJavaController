#author: Shannon Hwu
#version: 1.0

'''
MUST INSTALL MIDO PACKAGE FOR PYTHON TO USE:
command in terminal: pip install mido
                     pip install music21
'''
from mido import MidiFile
from music21 import *

def inputFileName():
    filename = input("What is the name of the MIDI file you want to parse? ")
    numNotes(filename)
#     music21(filename)

# def music21(filename):
#     filename = filename + '.mid'
#     file = converter.parse(filename)
#     print(file)
#     notes = []
#     for element in file.recurse():
#         msg = str(element)
#         msg = msg.replace("<", "")
#         msg = msg.replace(">", "")
#         msgList = msg.split(" ")
#         if (msgList[0] == 'music21.note.Note'):
#             print(element.type)
#             print(msgList[1])
# #         print(msgList)
        
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
    binaryString = ""
    for track in range(1, len(midiFile.tracks)):
        for msg in midiFile.tracks[track]:
#             print(msg)
            msg = str(msg)
            msgList = msg.split(" ")
            if len(msgList) ==  5:
                tempNoteVelocityList = msgList[3].split("=")
                noteVelocity = tempNoteVelocityList[1]
                if (noteVelocity != "0"):
                    print("note velocity = " + noteVelocity)
                    tempNoteTimeList = msgList[4].split("=")
                    noteTime = tempNoteTimeList[1]
                    print("note time = " + noteTime)
                    
                    # need to make into division?? based on note time??
                    # should be a length of 64
                    if (noteTime == "55"): #eighth note
                        binaryString += "1"
                    elif (noteTime == "165"): #quarter note
                        binaryString += "10"
                
                
                noteList = msgList[2].split("=")
#                 print(noteList)
                try:
                    noteNo = int(noteList[1])
                    note = notes[noteNo % 12]
                    numberNotes[note] += 1
#                     print(note)
                    numNotes += 1
                except:
                    pass
    numNotes = int(numNotes/2)
    for i in range(0, len(numberNotes)):
        numberNotes[notes[i]] /= 2
        print("{} has been played {} times".format(notes[i], int(numberNotes[notes[i]])))
    print("There are a total of {} notes in {}".format(numNotes, filename))
    print(binaryString)
inputFileName()
