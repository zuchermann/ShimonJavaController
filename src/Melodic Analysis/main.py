#author: Shannon Hwu

'''
MUST INSTALL MIDO PACKAGE FOR PYTHON TO USE:
command in terminal: pip install mido
'''
from mido import MidiFile
import music21

def main_notes():
    filename = get_midi_filename()
    numNotes(filename)

def main_rhythm():
    filename1 = get_first_xml_filename()
    filename2 = get_second_xml_filename()
    parsefile1 = parse_file_music21(filename1)
    parsefile2 = parse_file_music21(filename2)
    rhythm_dictionary1 = {}
    rhythm_dictionary2 = {}
    create_rhythm_array(parsefile1, rhythm_dictionary1)
    create_rhythm_array(parsefile2, rhythm_dictionary2)
#     calculate_complexity(rhythm_dictionary)

# numNotes gotta convert to xml first
#     numNotes(filename1)
#     numNotes(filename2)
    
def create_rhythm_array(parsefile, rhythm_dictionary):
    notes = [n for n in parsefile.recurse()]
    rhythms = []
    for x in notes:
        note_rhythm = x.duration.type
        if (note_rhythm != "maxima" and note_rhythm != "zero" and note_rhythm != "whole"):
            rhythms.append(note_rhythm)
            
    for note_rhythm in rhythms:
        if (note_rhythm in rhythm_dictionary):
            rhythm_dictionary[note_rhythm] += 1
        else:
            rhythm_dictionary[note_rhythm] = 1
    print(rhythms)
    print(rhythm_dictionary)

# def calculate_rhythm_complexity(rhythm_dictionary):
#     print(0)

def get_midi_filename():
    filename = input("What is the name of the MIDI file you want to parse? ")
    return filename + '.mid'

def get_first_xml_filename():
    filename = input("What is the name of the first XML file you want to parse? ")
    return filename + '.xml'

def get_second_xml_filename():
    filename = input("What is the name of the second XML file you want to parse? ")
    return filename + '.xml'


def parse_file_music21(filename):
    music21_parsefile = music21.converter.parse(filename, format='musicxml')
    return music21_parsefile

# def note_type(parsefile):
#     type = parsefile.getElementsByTagName("type")
# 
#     library of note rhythms.....
# 
# def is_rest(note):
#     return len(note.getElementsByTagName("rest")) > 0



#############################

def numNotes(filename):
    notes = {0 : "C", 1 : "C#", 2 : "D", 3 : "D#", 4 : "E", 5 : "F", 6 : "F#", 7 : "G", 8: "G#", 9 : "A", 10 : "A#", 11 : "B"}
    numberNotes = {"C" : 0, "C#" : 0, "D" : 0,  "D#" : 0, "E" : 0, "F" : 0, "F#" : 0, "G" : 0, "G#" : 0, "A" : 0, "A#" : 0, "B" : 0}

    '''
    make major and minor
    or different keys
    '''
    numNotes = 0
#     filename = filename + '.mid'
    midiFile = MidiFile(filename)
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


main_notes()
main_rhythm()
