import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    # Handle command-line arguments
    if len(sys.argv) == 1:
        # No font specified — pick a random one
        font = random.choice(fonts)
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
        # Valid font argument
        font = sys.argv[2]
    else:
        sys.exit("Invalid usage")

    # Set the chosen font
    figlet.setFont(font=font)

    # Ask user for text and print it
    text = input("Input: ")
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
