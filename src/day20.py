'''
------------------------------------------------------------------------------
ADVENT OF CODE 2016 - DAY Day 20: Firewall Rules
------------------------------------------------------------------------------

You'd like to set up a small hidden computer here so you can use it to get 
back into the network later. However, the corporate firewall only allows 
communication with certain external IP addresses.

You've retrieved the list of blocked IPs from the firewall, but the list 
seems to be messy and poorly maintained, and it's not clear which IPs are 
allowed. Also, rather than being written in dot-decimal notation, they are 
written as plain 32-bit integers, which can have any value from 0 through 
4294967295, inclusive.

For example, suppose only the values 0 through 9 were valid, and that you 
retrieved the following blacklist:

5-8
0-2
4-7

The blacklist specifies ranges of IPs (inclusive of both the start and end 
value) that are not allowed. Then, the only IPs that this firewall allows 
are 3 and 9, since those are the only numbers not in any range.

Given the list of blocked IPs you retrieved from the firewall (your puzzle 
input), what is the lowest-valued IP that is not blocked?

------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------

How many IPs are allowed by the blacklist?

------------------------------------------------------------------------------
NOTES
------------------------------------------------------------------------------



'''

import time

#Timing: Start
start = time.perf_counter()

#Load data
data = []
with open('txt/day20.txt') as f:
    for line in f:
        line = line.strip()
        data.append([int(i) for i in line.split('-')])
data = sorted(data)

cur_min = 0
cur_max = 0

#Part 1
for d in data:
    lbound, rbound = d
    if lbound <= (cur_max + 1):
        cur_max = max(rbound, cur_max)
    else:
        print(cur_max + 1)
        break

#Part 2
allowed = [(0, 4294967295)]
for d in data:
    lbound, rbound = d
    new = []
    for a in allowed:
        #Are we taking a chunk out of the middle?
        if lbound > a[0] and rbound < a[1]:
            new.append((a[0], lbound))
            new.append((rbound, a[1]))
        #Are we taking a chunk off the left?
        elif rbound > a[0]:
            new.append((rbound, a[1]))
        #Are we taking a chunk off the right?
        elif lbound < a[1]:
            new.append((a[0], lbound))
        #This one isn't affected
        else:
            new.append(a)
    allowed = sorted(new)
print(allowed)

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")