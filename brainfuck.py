import argparse

commands = "+-><[].,#!"


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


def map_brackets(input, bm):
    stack = []
    for i in range(len(input)):
        if input[i] == "[":
            stack.append(i)
        elif input[i] == "]":
            v = stack.pop()
            bm[v] = i
            bm[i] = v


def interpret(s):

    # Check if the program has a matching number of '[' and ']' characters
    if not do_brackets_match(s):
        print("The input does not have a matching set of []. Exiting...")
        return

    bracket_map = {}
    map_brackets(s, bracket_map)
    # print(bracket_map)
    ptr = 0
    cells = [0]
    i = 0
    while i < len(s):
        c = s[i]
        if c == "+":
            cells[ptr] += 1 if cells[ptr] < 255 else 0
        elif c == "-":
            cells[ptr] -= 1 if cells[ptr] > 0 else 255
        elif c == ">":
            ptr += 1
            if ptr == len(cells):
                cells.append(0)
        elif c == "<":
            ptr -= 1 if ptr > 0 else 0
        elif c == ".":
            if cells[ptr] == 10:
                print("\n")
            else:
                print(chr(cells[ptr]), end="")
        elif c == ",":
            cells[ptr] = ord(input())
        elif c == "[":
            if cells[ptr] == 0:
                i = bracket_map[i]
        elif c == "]":
            if cells[ptr] != 0:
                i = bracket_map[i]
        elif c == "#":
            print("Ptr Location:", ptr)
            print("Cells -", cells)
            print("Bracket Map -"bracket_map)
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
