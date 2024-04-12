import winsound

winsound.Beep(500,1000)

input_string = input("Enter Morse code:")
morse_string = ""

morse_dict = {'A': '.-',
            'B': '-...',
            'C': '-.-.',
            'D': '-..',
            'E': '.',
            'F': '..-.',
            'G': '--.',
            'H': '....',
            'I': '..',
            'J': '.---',
            'K': '-.-',
            'L': '.-..',
            'M': '--',
            'N': '-.',
            'O': '---',
            'P': '.--.',
            'Q': '--.-',
            'R': '.-.',
            'S': '...',
            'T': '-',
            'U': '..-',
            'V': '...-',
            'W': '.--',
            'X': '-..-',
            'Y': '-.--',
            'Z': '--..',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.',
            '0': '-----',
            ' ': '/',
    }

for letter in input_string.upper():
    morse_string += morse_dict[letter]
    morse_string += " "
   
for letter in morse_string:
    if letter == '.':
        winsound.Beep(800,500)
    if letter == '-':
        winsound.Beep(800,1000)
    if letter == '/':
        winsound.Beep(50,1000)
    if letter == ' ':
        winsound.Beep(50,300)
