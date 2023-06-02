import argparse
import sys

# Globals
MAX_VAL = 255
MIN_VAL = 0
commands = "+-><[].,#!"
DEBUG = False

instructions = """\
Symbol:      >  
Instr:       Increment the data pointer by one (to point to the next cell to the right).

Symbol:      <  
Instr:       Decrement the data pointer by one (to point to the next cell to the left).

Symbol:      +  
Instr:       Increment the byte at the data pointer by one.

Symbol:      -  
Instr:       Decrement the byte at the data pointer by one.

Symbol:      .  
Instr:       Output the byte at the data pointer.

Symbol:      ,  
Instr:       Accept one byte of input, storing its value in the byte at the data pointer.

Symbol:      [  
Instr:       If the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ] command.

Symbol:      ]  
Instr:       If the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching [ command.
"""


def do_brackets_match(input):
    """
    Checks if there are a matching number of open and close brackets

    Parameters: 
    input (str): The input Brainfuck code string

    Returns:
    bool: True if the number of opening and closing brackets match, False otherwise.
    """
    stack = []
    for c in input:
        if c == "[":
            stack.append(c)
        elif c == "]":
            if not stack:
                return False
            else:
                stack.pop()
    return not stack


def map_brackets(input):
    """
    Generates a map of corresponding open and close [] positions in the input string.

    Parameters:
    input (str): The input Brainfuck code string

    Returns: 
    dict: A dictionary mapping open bracket indices to their corresponding close bracket indices and vice versa.
    """
    brackets = {}
    stack = []
    for idx, val in enumerate(input):
        if val == "[":
            stack.append(idx)
        elif val == "]":
            v = stack.pop()
            brackets[v] = idx
            brackets[idx] = v
    return brackets


def interpret(s: str):
    if not do_brackets_match(s):
        print("The input does not have a matching set of []. Exiting...")
        return

    bracket_map = map_brackets(s)

    ptr = 0  # Current cell index
    cells = [0 for i in range(100)]  # Array that holds cell values
    i = 0  # Position in brainfuck code

    # Main evaluation loop
    while i < len(s):
        c = s[i]

        if c == "+":
            if cells[ptr] == MAX_VAL:
                cells[ptr] = MIN_VAL
            else:
                cells[ptr] += 1

        elif c == "-":
            if cells[ptr] > MIN_VAL:
                cells[ptr] -= 1
            else:
                cells[ptr] = MAX_VAL

        elif c == ">":
            ptr += 1
            if ptr == len(cells):
                cells.append(0)

        elif c == "<":
            if ptr > 0:
                ptr -= 1

        elif c == ".":
            if cells[ptr] == 10:
                print("\n")
            else:
                sys.stdout.write(chr(cells[ptr] % 256))

        elif c == ",":
            try:
                cells[ptr] = ord(input())
            except TypeError:
                print("Please only input a single ASCII Character")
                return

        elif c == "[":
            if cells[ptr] == 0:
                i = bracket_map[i]

        elif c == "]":
            if cells[ptr] != 0:
                i = bracket_map[i]

        # The # command is used to print out the current state of the program
        # for debugging purposes
        elif DEBUG == True or c == "#":
            print("Ptr Location:", ptr)
            print("Cells -", cells)
            print("Bracket Map -", bracket_map)

        # Once the command has been evaluated, move on to the next command
        i += 1


def repl():
    print("Welcome to the Brainfuck REPL")
    print(
        "Here you can enter simple Brainfuck code and see the output immediately"
    )

    try:
        while True:
            brains = input('> ')
            if "help" in brains.lower():
                print(instructions)
            elif "exit" in brains.lower():
                print("\nExiting REPL ... ")
                return
            else:
                interpret(brains)
                print("")
    except KeyboardInterrupt:
        print("\nExiting REPL ... ")


def main():
    parser = argparse.ArgumentParser(
        description='A Brainfuck Interpreter written in Python',
        epilog='Good luck and may your Brain remain unscrambled')
    parser.add_argument('-f',
                        '--file',
                        help="The brainfuck file to interpret",
                        dest='filename')
    parser.add_argument('-d',
                        '--debug',
                        action='store_true',
                        help="run interpreter in debug mode",
                        dest='debug')
    args = parser.parse_args()

    if args.debug:
        print("Running in Debug Mode")
        global DEBUG
        DEBUG = True

    f = args.filename
    if f is None:
        repl()
    else:
        if not f.endswith(".b"):
            print(f"Please provide a Brainfuck file with extension .b | {f}")
            return

        input_lines = []
        try:
            with open(args.filename, "r") as bf:
                for line in bf:
                    input_lines.append(line)
        except FileNotFoundError:
            print(f"Specified Brainfuck file {f} not found")
            return
        except PermissionError:
            print(f"Do not have permission to read file - {f}")
            return

        interpret("".join(input_lines))
        print("")


if __name__ == "__main__":
    main()
