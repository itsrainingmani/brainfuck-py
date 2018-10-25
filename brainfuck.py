import argparse
import re
import sys

commands = "+-><[].,#!"

# Checks if there are a matching number of open and close brackets
def do_brackets_match(input):
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


# Returns a map of corresponding open and close [] positions, going both ways
def map_brackets(input):
    brackets = {}
    stack = []
    for i in range(len(input)):
        if input[i] == "[":
            stack.append(i)
        elif input[i] == "]":
            v = stack.pop()
            brackets[v] = i
            brackets[i] = v
    return brackets


def interpret(s):

    # Check if the program has a matching number of '[' and ']' characters
    if not do_brackets_match(s):
        print("The input does not have a matching set of []. Exiting...")
        return

    bracket_map = map_brackets(s)

    ptr = 0  # Current cell index
    cells = [0]  # Array that holds cell values
    i = 0  # Position in brainfuck code

    # Main evaluation loop
    while i < len(s):
        c = s[i]

        # The + command increments the value of the cell indicated by the pointer
        # If that cell was already at its maximum value, it will assume its minimum
        if c == "+":
            if cells[ptr] == 255:
                cells[ptr] = 0
            else:
                cells[ptr] += 1

        # The - command decrements the value of the cell indicated by the pointer
        # If that cell was already at its minimum value, it will assume its maximum
        elif c == "-":
            if cells[ptr] > 0:
                cells[ptr] -= 1
            else:
                cells[ptr] = 255

        # The > command moves the pointer to the next cell to the right
        # If we reach the end of the cells list, we append an empty cell to the list
        elif c == ">":
            ptr += 1
            if ptr == len(cells):
                cells.append(0)

        # The < command moves the pointer to the next cell to the left.
        # If the pointer was already at the leftmost cell, nothing happens.
        elif c == "<":
            if ptr > 0:
                ptr -= 1

        # The . command outputs the value of the cell indicated by the pointer.
        # If that value will not fit in a byte it may first be reduced modulo 256.
        elif c == ".":
            if cells[ptr] == 10:
                print("\n")
            else:
                sys.stdout.write(chr(cells[ptr] % 256))

        # The , command requests one byte of input,
        # and sets the cell indicated by the pointer to the value received, if any.
        elif c == ",":
            cells[ptr] = ord(input())

        # The [ command checks the value of the cell indicated by the pointer.
        # If its value is zero, control passes not to the next command,
        # but to the command following the matching ']' command.
        elif c == "[":
            if cells[ptr] == 0:
                i = bracket_map[i]

        # The ] command checks the value of the cell indicated by the pointer,
        # and if its value is nonzero, control passes not to the next command,
        # but to the command following the matching '[' command.
        elif c == "]":
            if cells[ptr] != 0:
                i = bracket_map[i]

        # The # command is used to print out the current state of the program
        # for debugging purposes
        elif c == "#":
            print("Ptr Location:", ptr)
            print("Cells -", cells)
            print("Bracket Map -", bracket_map)

        # Once the command has been evaluated, move on to the next command
        i += 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="The brainfuck file to interpret")
    args = parser.parse_args()

    f = args.filename
    if f.count(".") == 0 or f.count(".") > 1:
        print("Invalid File")
        return
    else:
        if f[f.index(".") + 1 :] != "b":
            print("Please provide a Brainfuck file with extension .b")
            return

    brain_lines = []
    brainfuck = ""
    try:
        with open(args.filename, "r") as bf:
            for line in bf:
                filtered_line = re.sub("[^+-><\[\].,#!]", "", line)
                brain_lines.append(filtered_line)
    except FileNotFoundError:
        print("Specified Brainfuck file not found")
        return

    print(
        """
           _                 _               _                     _              _                   _         _                         _               _        
          / /\              /\ \            / /\                  /\ \           /\ \     _          /\ \      /\_\                     /\ \             /\_\      
         / /  \            /  \ \          / /  \                 \ \ \         /  \ \   /\_\       /  \ \    / / /         _          /  \ \           / / /  _   
        / / /\ \          / /\ \ \        / / /\ \                /\ \_\       / /\ \ \_/ / /      / /\ \ \   \ \ \__      /\_\       / /\ \ \         / / /  /\_\ 
       / / /\ \ \        / / /\ \_\      / / /\ \ \              / /\/_/      / / /\ \___/ /      / / /\ \_\   \ \___\    / / /      / / /\ \ \       / / /__/ / / 
      / / /\ \_\ \      / / /_/ / /     / / /  \ \ \            / / /        / / /  \/____/      / /_/_ \/_/    \__  /   / / /      / / /  \ \_\     / /\_____/ /  
     / / /\ \ \___\    / / /__\/ /     / / /___/ /\ \          / / /        / / /    / / /      / /____/\       / / /   / / /      / / /    \/_/    / /\_______/   
    / / /  \ \ \__/   / / /_____/     / / /_____/ /\ \        / / /        / / /    / / /      / /\____\/      / / /   / / /      / / /            / / /\ \ \      
   / / /____\_\ \    / / /\ \ \      / /_________/\ \ \   ___/ / /__      / / /    / / /      / / /           / / /___/ / /      / / /________    / / /  \ \ \     
  / / /__________\  / / /  \ \ \    / / /_       __\ \_\ /\__\/_/___\    / / /    / / /      / / /           / / /____\/ /      / / /_________\  / / /    \ \ \    
  \/_____________/  \/_/    \_\/    \_\___\     /____/_/ \/_________/    \/_/     \/_/       \/_/            \/_________/       \/____________/  \/_/      \_\_\   
                                                                                                                                                                  
    """
    )

    brainfuck = "".join(brain_lines)
    interpret(brainfuck)


if __name__ == "__main__":
    main()
