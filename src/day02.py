'''
------------------------------------------------------------------------------
ADVENT OF CODE 2016 - DAY 2: Bathroom Security
------------------------------------------------------------------------------

You arrive at Easter Bunny Headquarters under cover of darkness. However, you 
left in such a rush that you forgot to use the bathroom! Fancy office 
buildings like this one usually have keypad locks on their bathrooms, so you 
search the front desk for the code.

"In order to improve security," the document you find says, "bathroom codes 
will no longer be written down. Instead, please memorize and follow the 
procedure below to access the bathrooms."

The document goes on to explain that each button to be pressed can be 
found by starting on the previous button and moving to adjacent buttons 
on the keypad: U moves up, D moves down, L moves left, and R moves right. 
Each line of instructions corresponds to one button, starting at the 
previous button (or, for the first line, the "5" button); press whatever 
button you're on at the end of each line. If a move doesn't lead to a button, 
ignore it.

You can't hold it much longer, so you decide to figure out the code as you 
walk to the bathroom. You picture a keypad like this:

    1 2 3
    4 5 6
    7 8 9

Suppose your instructions are:

    ULL
    RRDDD
    LURDL
    UUUUD

You start at "5" and move up (to "2"), left (to "1"), and left (you can't, 
and stay on "1"), so the first button is 1.

Starting from the previous button ("1"), you move right twice (to "3") and 
then down three times (stopping at "9" after two moves and ignoring the 
third), ending up with 9.

Continuing from "9", you move left, up, right, down, and left, ending 
with 8.

Finally, you move up four times (stopping at "2"), then down once, ending 
with 5.

So, in this example, the bathroom code is 1985.

Your puzzle input is the instructions from the document you found at the 
front desk. What is the bathroom code?

------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------

You finally arrive at the bathroom (it's a several minute walk from the lobby 
so visitors can behold the many fancy conference rooms and water coolers on 
this floor) and go to punch in the code. Much to your bladder's dismay, the 
keypad is not at all like you imagined it. Instead, you are confronted with
 the result of hundreds of man-hours of bathroom-keypad-design meetings:

    1
  2 3 4
5 6 7 8 9
  A B C
    D

You still start at "5" and stop when you're at an edge, but given the same 
instructions as above, the outcome is very different:

You start at "5" and don't move at all (up and left are both edges), ending 
at 5.

Continuing from "5", you move right twice and down three times (through "6", 
"7", "B", "D", "D"), ending at D.

Then, from "D", you move five more times (through "D", "B", "C", "C", "B"), 
ending at B.

Finally, after five more moves, you end at 3.

So, given the actual keypad layout, the code would be 5DB3.

Using the same instructions in your puzzle input, what is the correct 
bathroom code?

------------------------------------------------------------------------------
NOTES
------------------------------------------------------------------------------

- You start at 5

'''

import time

#Timing: Start
start = time.perf_counter()

#Load the puzzle data
with open('txt/day02.txt') as f:
    data = [line.strip() for line in f.readlines()]

#Part 1
code = ''
key = 5
for line in data:
    for c in line:
        if c == 'L':
            if key not in [1, 4, 7]:
                key -= 1
        elif c == 'R':
            if key not in [3, 6, 9]:
                key += 1
        elif c == 'U':
            if key not in [1, 2, 3]:
                key -= 3
        elif c == 'D':
            if key not in [7, 8, 9]:
                key += 3
        else:
            print(f'DATA ERROR: c = {c}')
    code += str(key)
print(code)


#Part 2
left  = {'3': '2', '4': '3', '6': '5', '7': '6', 
         '8': '7', '9': '8', 'B': 'A', 'C': 'B'}
right = {'2': '3', '3': '4', '5': '6', '6': '7', 
         '7': '8', '8': '9', 'A': 'B', 'B': 'C'}
up    = {'3': '1', '6': '2', '7': '3', '8': '4', 
         'A': '6', 'B': '7', 'C': '8', 'D': 'B'}
down  = {'1': '3', '2': '6', '3': '7', '4': '8', 
         '6': 'A', '7': 'B', '8': 'C', 'B': 'D'}
code = ''
key = '5'
for line in data:
    for c in line:
        if c == 'L':
            if key in left:
                key = left[key]
        elif c == 'R':
            if key in right:
                key = right[key]
        elif c == 'U':
            if key in up:
                key = up[key]
        elif c == 'D':
            if key in down:
                key = down[key]
        else:
            print(f'DATA ERROR: c = {c}')
    code += key
print(code)

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")
