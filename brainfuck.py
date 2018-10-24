import argparse

# BRAINFUCK LANGUAGE COMMAND REFERENCE

# The '+' command increments the value of the cell indicated by the pointer

# The '-' command decrements the value of the cell indicated by the pointer

# The '>' command moves the pointer to the next cell to the right

# The '<' command moves the pointer to the next cell to the left

# The '[' command checks the value of the cell indicated by the pointer and,
#       if its value is zero, control passes not to the next command, but
#       to the command following the matching ']' command.

# The ']' command checks the value of the cell indicated by the pointer and,
#       if its value is nonzero, control passes not to the next command, but
#       to the command following the matching '[' command.

# The '.' command outputs the value of the cell indicated by the pointer

# The ',' command requests one byte of input and sets the cell indicated by
#       the pointer to the value received, if any

commands = "+-><[].,#!"


def is_bounds_valid(input):
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


def map_bounds(input, bm):
    stack = []
    for i in range(len(input)):
        if input[i] == "[":
            stack.append(i)
        elif input[i] == "]":
            v = stack.pop()
            bm[v] = i


def interpret(s):

    # Check if the program has a matching number of '[' and ']' characters
    if not is_bounds_valid(s):
        print("The input does not have a matching set of []. Exiting....")
        return
    else:
        bracket_map = {}
        map_bounds(s, bracket_map)
        # print(bracket_map)
        bracket_stack = []
        ptr = 0
        cells = [0 for i in range(30000)]
        i = 0
        while i < len(s):
            if s[i] not in commands:
                i += 1
            else:
                if s[i] == "+":
                    cells[ptr] += 1
                    i += 1
                elif s[i] == "-":
                    if cells[ptr] > 0:
                        cells[ptr] -= 1
                    i += 1
                elif s[i] == ">":
                    ptr += 1
                    i += 1
                elif s[i] == "<":
                    if ptr > 0:
                        ptr -= 1
                    i += 1
                elif s[i] == ".":
                    if cells[ptr] == 10:
                        print("\n")
                    else:
                        print(chr(cells[ptr]), end="")
                    i += 1
                elif s[i] == ",":
                    ioval = input()
                    cells[ptr] = ord(ioval)
                    i += 1
                elif s[i] == "[":
                    if cells[ptr] == 0:
                        i = bracket_map[i] + 1
                        if len(bracket_stack) > 0:
                            bracket_stack.pop()
                    else:
                        if (i, bracket_map[i]) not in bracket_stack:
                            bracket_stack.append((i, bracket_map[i]))
                        i += 1
                elif s[i] == "]":
                    if cells[ptr] > 0:
                        i = bracket_stack[-1][0]
                    else:
                        if len(bracket_stack) > 0:
                            bracket_stack.pop()
                        i += 1
                elif s[i] == "#":
                    print("Ptr Location:", ptr, cells[0:10])
                    i += 1


def main():
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

    bf_input = ""
    try:
        with open(args.filename, "r") as bf:
            bf_input = bf.readline()
            interpret(bf_input)
    except FileNotFoundError:
        print("Specified Brainfuck file not found")
        return


if __name__ == "__main__":
    main()
