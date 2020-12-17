#/usr/bin/env python3

from playsound import playsound
from time import sleep

from alphabet_counter import alphabet_counter

# dictionary storing morsecode
morsecode_dict = {
    "a": ".-", "b": "-...", "c": "-.-.",
    "d": "-..", "e": ".", "f": "..-.",
    "g": "--.", "h": "....", "i": "..",
    "j": ".---", "k": "-.-", "l": ".-..",
    "m": "--", "n": "-.", "o": "---",
    "p": ".--.", "q": "--.-", "r": ".-.",
    "s": "...", "t": "-", "u": "..-",
    "v": "...-", "w": ".--", "x": "-..-",
    "y": "-.--", "z": "--..","0": "-----",
    "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....",
    "7": "--...", "8": "---..", "9": "----.",
    ".": ".-.-.-", ",": "--..--", "?": "..--..",
    "'": ".----.", "!": "-.-.--", "/": "-..-.",
    "(": "-.--.", ")": "-.--.-", "&": ".-...",
    ":": "---...", ";": "-.-.-.", "=": "-...-",
    "+": ".-.-.", "-": "-....-", "_": "..--.-",
    '"': ".-..-.", "$": "...-..-", "@": ".--.-.",
    "¿":"..-.-", "¡": "--...-", "start": "-.-.-",
    "end": "...-.-",}

# user Input
messege = input("Your messege:  ")
alphabet_counter(messege)		
# converting to lowercase
# as the dictionary has no
# uppercase character as key
messege = messege.lower()

# creating a list of all the
# characters in the user's input string
messege_list = list(messege)

# translating the messege
# into a string encoded as morsecode
morse_string = ''
for i in messege:
    if i == ' ':
        morse_string += '/ '
    else:
        morse_string += morsecode_dict[i]
        morse_string += ' '
print("\n⭕ Morse Code:  " + morse_string) # printing out the translation
#exit() # comment out to only display the translation

# Soundplay
print("\n░░░ Playing Sound ░░░")

def morse_sound(morsecode):
    for i in morsecode:
        if i == ".":
            playsound('dot.wav')
            sleep(0.05)
        elif i == "-":
            playsound('dash.wav')
            sleep(0.1)
        elif i == " ":
            sleep(0.3)
        elif i == "/":
            playsound('space.wav')
    playsound('space.wav')

# Turn on/off start and end signals
signals = 0 # '0' -> on

if signals == 0:
	# Start Signal of audio output
	print("\n⭕ Start signal:")
	print("Morse Code: ", morsecode_dict['start'])
	morse_sound(list(morsecode_dict['start']))

# creating a list of the
# morsecode characters playing
# that as as on audio output
print("\n⭕ Main Messege:")
print("Morse Code: ", morse_string)  
morse_sound(list(morse_string))

if signals == 0:
	# End signal of audio output
	print("\n⭕ End of work:")
	print("Morse Code: ", morsecode_dict['end'])
	morse_sound(list(morsecode_dict['end']))