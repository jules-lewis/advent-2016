'''
------------------------------------------------------------------------------
ADVENT OF CODE 2016 - DAY 8: Two-Factor Authentication
------------------------------------------------------------------------------

You come across a door implementing what you can only assume is an 
implementation of two-factor authentication after a long game of requirements 
telephone.

To get past the door, you first swipe a keycard (no problem; there was one on 
a nearby desk). Then, it displays a code on a little screen, and you type 
that code on a keypad. Then, presumably, the door unlocks.

Unfortunately, the screen has been smashed. After a few minutes, you've taken 
everything apart and figured out how it works. Now you just have to work 
out what the screen would have displayed.

The magnetic strip on the card you swiped encodes a series of instructions 
for the screen; these instructions are your puzzle input. The screen is 
50 pixels wide and 6 pixels tall, all of which start off, and is capable 
of three somewhat peculiar operations:

rect AxB turns on all of the pixels in a rectangle at the top-left of the 
screen which is A wide and B tall.

rotate row y=A by B shifts all of the pixels in row A (0 is the top row) 
right by B pixels. Pixels that would fall off the right end appear at the 
left end of the row.

rotate column x=A by B shifts all of the pixels in column A (0 is the left 
column) down by B pixels. Pixels that would fall off the bottom appear at 
the top of the column.

For example, here is a simple sequence on a smaller screen:

rect 3x2 creates a small rectangle in the top-left corner:

###....
###....
.......

rotate column x=1 by 1 rotates the second column down by one pixel:

#.#....
###....
.#.....

rotate row y=0 by 4 rotates the top row right by four pixels:

....#.#
###....
.#.....

rotate column x=1 by 1 again rotates the second column down by one pixel, 
causing the bottom pixel to wrap back to the top:

.#..#.#
#.#....
.#.....

As you can see, this display technology is extremely powerful, and will 
soon dominate the tiny-code-displaying-screen market. That's what the 
advertisement on the back of the display tries to convince you, anyway.

There seems to be an intermediate check of the voltage used by the display: 
after you swipe your card, if the screen did work, how many pixels should be 
lit?

------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------

You notice that the screen is only capable of displaying capital letters; in 
the font it uses, each letter is 5 pixels wide and 6 tall.

After you swipe your card, what code is the screen trying to display?

------------------------------------------------------------------------------
NOTES
------------------------------------------------------------------------------


'''

import time
from copy import deepcopy

#Timing: Start
start = time.perf_counter()

PIX_ON = 'O'
PIX_OFF = ' '

def print_screen(screen):
    #A prettier output for Part 2
    print()
    for row in screen:
        raw_str = ''.join(row)
        out_str = ''
        for n in range(len(raw_str)):
            out_str += raw_str[n]
            if n % 5 == 4:
                out_str += ' '
        print(out_str)
    print()

def draw_rect(screen, arg):
    #Typical instruction: "rect 1x2", arg is "1x2"
    x, y = arg.split('x')
    for i in range(int(x)):
        for j in range(int(y)):
            screen[j][i] = PIX_ON

def rotate_list(l, offset):
    return l[offset:] + l[:offset]

def rotate_row(screen, arg):
    #Typical instruction: 'rotate row y=0 by 5', arg is ['y=0', 'by', '5']
    row_index = int(arg[0].split('=')[1])
    offset = int(arg[-1])
    screen[row_index] = rotate_list(screen[row_index], 50-offset)

def rotate_col(screen, arg):
    #Typical instruction: 'rotate column x=35 by 3', arg is ['x=35', 'by', '3']
    col_index = int(arg[0].split('=')[1])
    offset = int(arg[-1])
    col = [screen[n][col_index] for n in range(6)]
    col = rotate_list(col, 6-offset)
    for row in range(6):
        screen[row][col_index] = col[row]

def count_pixels(screen):
    pix_count = 0
    for row in screen:
        pix_count += sum(c == PIX_ON for c in row)
    return pix_count

with open('txt/day08.txt') as f:
    code = [line.strip().split() for line in f]

row = [PIX_OFF] * 50
screen = [deepcopy(row) for i in range(6)]

for line in code:
    if line[0] == 'rect':
        draw_rect(screen, line[1])
    elif line[1] == 'row':
        rotate_row(screen, line[2:])
    elif line[1] == 'column':
        rotate_col(screen, line[2:])
    else:
        print(f'ERROR: Haven\'t catered for {line}')

#Part 1
print(count_pixels(screen))

#Part 2
print_screen(screen)

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")
