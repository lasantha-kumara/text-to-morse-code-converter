morse_chart = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    "!": "-.-.--",
    "@": ".--.-.",
    "$": "...-..-",
    "%": "-..-.",
    "&": ".-...",
    "'": ".----.",
    ")": "-.--.-",
    "(": "-.--.",
    ";": "---...",
    ",": "--..--",
    "=": "-...-",
    ".": ".-.-.-",
    "-": "-....-",
    "+": ".-.-.",
    '"': ".-..-.",
    "?": "..--..",
    "/": "-..-."
}


def main():
    # get the username with uppercase letters
    text = input("Enter text to convert to morse code: ").upper()

    morse_code = ""

    for letter in text:
        # if letter is a space the add '/' to it
        if letter == " ":
            morse_code += "/"
        # else get letter from the morse chart
        else:
            morse_letter = morse_chart[letter]
            morse_code += morse_letter

        # add space after every letter
        morse_code += " "

    print("Your morse code is", morse_code)


main()
