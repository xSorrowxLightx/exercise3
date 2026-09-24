#EXERCISE 1

def print_right(text, spaces):
    spaces -= len(text)
    whtspc = ""
    while spaces > 0:
        whtspc += " "
        spaces -= 1
    print(whtspc, text)

print_right("Hello world", 40)

"""Tbh i dont understand how this ^ works. How does the value of spaces in 'spaces' 
transfer to the 'whtspc' variable? i took apart the program and the only thing that
worked was exactly what you wrote. Later edit: thinking abt it, is the 'while' loop 
being like a currency converter, taking the 'spaces' 'tokens' and turning it into 
'whtspc' 'tokens'? i feel like that might be right."""

#EXERCISE 2

def triangle(str):
    print(str)
    print(str * 2)
    print(str * 3)
    print(str * 4)
    print(str * 5)

triangle("hi ")

#EXERCISE 3

def rectangle(str, width, height):
    for sqr in range(height):
        print(str * width)

rectangle("hi", 4, 4)

"""admittedly, needed ur help for this one. I knew how to repeat the str (like above)
but had no idea how to repeat the print as determined by the input. this exercise
kinda made 'for' a little easier to understand!"""

#EXERCISE 4

def bottle_verse(num):
    while num > 0:
        print(f"{num} bottles of beer on the wall,")
        print(f"{num} bottles of beer!")
        print(f"Take one down, pass it around,")
        num -= 1
        print(f"{num} bottles of beer on the wall!")

bottle_verse(5)