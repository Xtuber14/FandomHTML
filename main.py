import sys
import time
import pyperclip

VERSION = 'v1.2'
WELCOME_MESSAGE = f'Welcome to FandomHTML {VERSION}'
INITIAL_OPTIONS = (
    "1. Add <br>\n2. Add <br> from a file .txt\nPress X to exit"
)

def convert_newlines_to_br(input_text):
    return input_text.replace('\n', '<br>')

def convert_newlines_to_brn(input_text):
    return input_text.replace('\n', '<br>\n')

def get_input_lines():
    print("Enter your text (type 'X' on a new line to exit input):")
    input_lines = []

    while True:
        line = input()
        if line == 'X':
            break
        input_lines.append(line)

    return '\n'.join(input_lines)

def process_option_1():
    input_text = get_input_lines()

    # Convert and print the modified text
    output_text = convert_newlines_to_br(input_text)
    print(output_text)
    pyperclip.copy(output_text)
    print('Text copied to clipboard')
    time.sleep(5)

def process_option_2():
    filepath = input('Paste here the path for the file: ')
    filepath = filepath.replace('"', "")
    
    try:
        with open(filepath, "r") as file:
            content = file.read()

        output_text = convert_newlines_to_brn(content)

        with open(filepath, "a") as file:
            file.write("\n\n" + output_text)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", str(e))

def main():
    print(WELCOME_MESSAGE)
    print(INITIAL_OPTIONS)
    init_welcome = input()

    if init_welcome == '1':
        process_option_1()
    elif init_welcome == '2':
        process_option_2()
    elif init_welcome == 'X':
        sys.exit()

if __name__ == '__main__':
    main()
