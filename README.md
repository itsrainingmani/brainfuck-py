# brainfuck-py

Simple brainfuck interpreter written in Python.

## What is Brainfuck

From [Wikipedia](https://en.wikipedia.org/wiki/Brainfuck)

```quote
Brainfuck is an esoteric programming language created in 1993 by Urban Müller.

Notable for its extreme minimalism, the language consists of only eight simple commands, a data pointer and an instruction pointer. 
While it is fully Turing complete, it is not intended for practical use, but to challenge and amuse programmers. 
Brainfuck requires one to break commands into microscopic steps.

The language's name is a reference to the slang term brainfuck, 
which refers to things so complicated or unusual that they exceed the limits of one's understanding, 
as it was not meant or made for designing actual software but to challenge the boundaries of computer programming.
```

## Usage

To evaluate a brainfuck code file with extension _.b_ , run the following command in your shell

```shell
$ python brainfuck.py <filename>
```

## Instruction List

There are eight brainfuck instructions.

| Instruction | Description                                                                                            |
|-------------|--------------------------------------------------------------------------------------------------------|
| >           | Increment the data pointer by one (to point to the next cell to the right).                            |
| <           | Decrement the data pointer by one (to point to the next cell to the left).                             |
| +           | Increment the byte at the data pointer by one.                                                         |
| -           | Decrement the byte at the data pointer by one.                                                         |
| .           | Output the byte at the data pointer.                                                                   |
| ,           | Accept one byte of input, storing its value in the byte at the data pointer.                           |
| [           | If the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ] command. |
| ]           | If the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching [ command. |


## References

The following links were highly useful in developing this interpreter

* [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck)
* [Brainfuck Esolang wiki](https://esolangs.org/wiki/brainfuck)
* [Some Brainfuck fluff by Daniel Cristofani](http://www.hevanet.com/cristofd/brainfuck/)