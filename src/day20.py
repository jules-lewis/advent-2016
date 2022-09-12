'''
------------------------------------------------------------------------------
ADVENT OF CODE 2016 - DAY 20: Firewall Rules
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

#First, merge the sorted bans, by looking at each successive ban and
#checking whether it overlaps with (or adjoins) the previous
merged = [data[0]]
for current_ban in data[1:]:
    previous_ban = merged[-1]
    if current_ban[0] <= previous_ban[1] + 1:
        previous_ban[1] = max(previous_ban[1], current_ban[1])
    else:
        merged.append(current_ban)

#With all the bans merged, we can simply sum up the gaps
safe_ips = 0
previous_rbound = merged[0][1]
for current_ban in merged[1:]:
    safe_ips += current_ban[0] - previous_rbound - 1
    previous_rbound = current_ban[1]
print(safe_ips)

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")