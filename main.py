import sys
import time
version = 'v1.0\n'
output_text = ''
welcome = 'Welcome to FandomHTML ' + version
initial_message = '1. Add <br>\n2. Add <br> from a file .txt (WIP)\nPress X to exit'

def convert_newlines_to_br(input_text):
    return input_text.replace('\n', '<br>')

# Start Program
print(welcome + initial_message)
init_welcome = input()

if init_welcome == '1':
    print("Enter your text (type 'X' on a new line to exit input):")
    input_lines = []

    while True:
        line = input()
        if line == 'X':
            break
        input_lines.append(line)

    input_text = '\n'.join(input_lines)

    # Convert and print the modified text
    output_text = convert_newlines_to_br(input_text)
    print(output_text)
    time.sleep(30)
if init_welcome == 'X':
    sys.exit()