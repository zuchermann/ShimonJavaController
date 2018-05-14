import music21

def main_notes():
    filename = get_first_xml_filename()
    parsefile = parse_file_music21(filename)
    notes_dict = {0 : "C", 1 : "C#", 2 : "D", 3 : "D#", 4 : "E", 5 : "F", 6 : "F#", 7 : "G", 8: "G#", 9 : "A", 10 : "A#", 11 : "B"}
    numberNotes_dict = {"C" : 0, "C#" : 0, "D" : 0,  "D#" : 0, "E" : 0, "F" : 0, "F#" : 0, "G" : 0, "G#" : 0, "A" : 0, "A#" : 0, "B" : 0}
    total_num_notes = 0
    numNotes(parsefile, notes_dict, numberNotes_dict)
    for i in range(0, len(numberNotes_dict)):
        print("{} has been played {} times".format(notes_dict[i], int(numberNotes_dict[notes_dict[i]])))
        total_num_notes += int(numberNotes_dict[notes_dict[i]])
    print("There are a total of {} notes in {}".format(total_num_notes, filename))


def get_first_xml_filename():
    filename = input("What is the name of the first XML file you want to parse? ")
    return filename + '.xml'

def get_second_xml_filename():
    filename = input("What is the name of the second XML file you want to parse? ")
    return filename + '.xml'

def parse_file_music21(filename):
    music21_parsefile = music21.converter.parse(filename, format='musicxml')
    return music21_parsefile

def numNotes(parsefile, notes_dict, numberNotes):
    '''
    make major and minor
    or different keys
    '''
    notes = [n for n in parsefile.recurse()]
    for x in notes:
        if type(x) == music21.note.Note:
            note = x.step
            numberNotes[note] += 1 
