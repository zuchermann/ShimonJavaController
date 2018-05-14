import music21

def main_rhythm():
    filename1 = get_first_xml_filename()
    filename2 = get_second_xml_filename()
    parsefile1 = parse_file_music21(filename1)
    parsefile2 = parse_file_music21(filename2)
    rhythm_dictionary1 = {}
    rhythm_dictionary2 = {}
    create_rhythm_array(parsefile1, rhythm_dictionary1)
    create_rhythm_array(parsefile2, rhythm_dictionary2)
    complexity1 = calculate_rhythm_complexity(rhythm_dictionary1)
    complexity2 = calculate_rhythm_complexity(rhythm_dictionary2)
    if complexity1 > complexity2:
        print(filename1 + " is more rhythmically complex than " + filename2)
    elif complexity2 > complexity1:
        print(filename2 + " is more rhythmically complex than " + filename1)
    else:
        print("These two files have the same rhythmic complexity")

def get_first_xml_filename():
    filename = input("What is the name of the first XML file you want to parse? ")
    return filename + '.xml'

def get_second_xml_filename():
    filename = input("What is the name of the second XML file you want to parse? ")
    return filename + '.xml'

def parse_file_music21(filename):
    music21_parsefile = music21.converter.parse(filename, format='musicxml')
    return music21_parsefile

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

def calculate_rhythm_complexity(rhythm_dictionary):
    result = 0
    eighth_weight = 8
    quarter_weight = 4
    sixteenth_weight = 16
    for note_rhythm in rhythm_dictionary:
        if note_rhythm == "eighth":
            result += rhythm_dictionary[note_rhythm] * eighth_weight
        elif note_rhythm == "quarter":
            result += rhythm_dictionary[note_rhythm] * quarter_weight
        elif note_rhythm == "16th":
            result += rhythm_dictionary[note_rhythm] * sixteenth_weight
    return result
