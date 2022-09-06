'''
------------------------------------------------------------------------------
ADVENT OF CODE 2016 - DAY 10: 
------------------------------------------------------------------------------

You come upon a factory in which many robots are zooming around handing small 
microchips to each other.

Upon closer examination, you notice that each bot only proceeds when it has 
two microchips, and once it does, it gives each one to a different bot or 
puts it in a marked "output" bin. Sometimes, bots take microchips from 
"input" bins, too.

Inspecting one of the microchips, it seems like they each contain a single 
number; the bots must use some logic to decide what to do with each chip. You 
access the local control computer and download the bots' instructions (your 
puzzle input).

Some of the instructions specify that a specific-valued microchip should be 
given to a specific bot; the rest of the instructions indicate what a given 
bot should do with its lower-value or higher-value chip.

For example, consider the following instructions:

value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2

Initially, bot 1 starts with a value-3 chip, and bot 2 starts with a value-2 
chip and a value-5 chip.

Because bot 2 has two microchips, it gives its lower one (2) to bot 1 and 
its higher one (5) to bot 0.

Then, bot 1 has two microchips; it puts the value-2 chip in output 1 and 
gives the value-3 chip to bot 0.

Finally, bot 0 has two microchips; it puts the 3 in output 2 and the 5 in 
output 0.

In the end, output bin 0 contains a value-5 microchip, output bin 1 contains 
a value-2 microchip, and output bin 2 contains a value-3 microchip. In this 
configuration, bot number 2 is responsible for comparing value-5 microchips 
with value-2 microchips.

Based on your instructions, what is the number of the bot that is 
responsible for comparing value-61 microchips with value-17 microchips?

------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------

What do you get if you multiply together the values of one chip in each of 
outputs 0, 1, and 2?

------------------------------------------------------------------------------
NOTES
------------------------------------------------------------------------------


'''

import time
from copy import deepcopy

#Timing: Start
start = time.perf_counter()

bots = {}  
'''
Too lazy to write a Class! Individual bots have the following format:
{bot_number: [ [list of outputs], 
               [type of object the low value is going to, the low value], 
               [type of object the high value is going to, the high value] ]
'''
outputs = {}

#Load data
with open('txt/day10.txt') as f:
    #Sample data:
    #value 43 goes to bot 90
    #bot 148 gives low to output 19 and high to bot 156
    for line in f:
        line = line.strip().split()
        if 'value' in line:
            bot_no = int(line[-1])
            val = int(line[1])
            if bot_no not in bots:
                bots[bot_no] = [[val], [], []]
            else:
                bots[bot_no][0].append(val)
        else:
            bot_no = int(line[1])
            low = [line[5], int(line[6])]
            high = [line[10], int(line[11])]
            if bot_no not in bots:
                bots[bot_no] = [[], low, high]
            else:
                bots[bot_no][1] = low
                bots[bot_no][2] = high

def get_bot_with_two_vals(bots):
    for bot, vals in bots.items():
        if len(vals[0]) == 2:
            return bot
    return None

def send_output(val, dest):
    dest_type = dest[0]
    dest_num = int(dest[1])
    if dest_type == 'bot':
        if dest_num in bots:
            bots[dest_num][0].append(val)
        else:
            bots[dest_num][0] = [val]
    else: #'output'
        outputs[dest_num] = val

work_bot = get_bot_with_two_vals(bots)
while work_bot != None:
    vals = bots[work_bot]
    low_val, high_val = sorted(vals[0])
    if low_val == 17 and high_val == 61:
        print(f'PART 1: Found the robot! It\'s {work_bot}')
        #If we're just solving Part 1, we can stop as soon
        #as we've found this bot:
        #break 
    send_output(low_val, vals[1])
    send_output(high_val, vals[2])
    bots.pop(work_bot)
    work_bot = get_bot_with_two_vals(bots)

print(f'PART 2: {outputs[0] * outputs[1] * outputs[2]}')

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")
