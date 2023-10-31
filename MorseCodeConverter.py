import os

# Define the Morse code decoding dictionary
decoding = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
    "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....",
    "7": "--...", "8": "---..", "9": "----.",
    " ": " "
}

# Heading text
heading = """
 __  __                            _____             _          _____                                   _               
|  \/  |                          / ____|           | |        / ____|                                 | |              
| \  / |  ___   _ __  ___   ___  | |       ___    __| |  ___  | |       ___   _ __  __   __  ___  _ __ | |_   ___  _ __ 
| |\/| | / _ \ | '__|/ __| / _ \ | |      / _ \  / _` | / _ \ | |      / _ \ | '_\ \ \ / / / _ \| '__|| __| / _ \| '__|
| |  | || (_) || |   \__ \|  __/ | |____ | (_) || (_| ||  __/ | |____ | (_) || | | \ V / |  __/| |   | |_ |  __/| |   
|_|  |_| \___/ |_|   |___/ \___|  \_____| \___/  \__,_| \___|  \_____| \___/ |_| |_|\_/   \___||_|    \__| \___||_|
"""

# Clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(heading)

# Translate text to Morse code
def translate_to_morse(text):
    return ' '.join(decoding.get(char, '') for char in text)

# Print heading first time
print(heading)

# Main loop
while True:
    user_input = input("Enter a message to translate to Morse code (type 'exit' to quit, 'clear' to clear previous inputs): ").upper()

    if user_input == 'EXIT':
        break
    elif user_input == 'CLEAR':
        clear_console()
    else:
        morse = translate_to_morse(user_input)
        print(f"Morse Code: {morse}")
