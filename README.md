# Brainfuck Interpreter in Python


```text
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
```

## Usage

To evaluate a brainfuck code file with extension _.b_ , run the following command in your shell

```shell
$ python brainfuck.py <filename>
```

## Brainfuck Command List

There are eight brainfuck commands.

* The + command increments (increases by one) the value of the cell indicated by the pointer. If that cell was already at its maximum value, it may (or may not) assume its minimum value.
* The - command decrements (decreases by one) the value of the cell indicated by the pointer. If that cell was already at its minimum value, it may (or may not) assume its maximum value.
* The > command moves the pointer to the next cell to the right. If the pointer was already at the rightmost cell (if any) the results are unpredictable.
* The < command moves the pointer to the next cell to the left. If the pointer was already at the leftmost cell, the results are unpredictable.
* The [ command checks the value of the cell indicated by the pointer, and if its value is zero, control passes not to the next command, but to the command following the matching ']' command.
* The ] command checks the value of the cell indicated by the pointer, and if its value is nonzero, control passes not to the next command, but to the command following the matching '[' command.
* The . command outputs the value of the cell indicated by the pointer. If that value will not fit in a byte it may first be reduced modulo 256.
* The , command requests one byte of input, and sets the cell indicated by the pointer to the value received, if any.

## References

The following links were highly useful in developing this interpreter

* [Brainfuck Esolang wiki](https://esolangs.org/wiki/brainfuck)
* [Some Brainfuck fluff by Daniel Cristofani](http://www.hevanet.com/cristofd/brainfuck/)