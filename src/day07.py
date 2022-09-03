'''
------------------------------------------------------------------------------
ADVENT OF CODE 2016 - DAY 7: Internet Protocol Version 7
------------------------------------------------------------------------------

While snooping around the local network of EBHQ, you compile a list of IP 
addresses (they're IPv7, of course; IPv6 is much too limited). You'd like to 
figure out which IPs support TLS (transport-layer snooping).

An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. 
An ABBA is any four-character sequence which consists of a pair of two 
different characters followed by the reverse of that pair, such as xyyx or 
abba. However, the IP also must not have an ABBA within any hypernet 
sequences, which are contained by square brackets.

For example:

abba[mnop]qrst supports TLS (abba outside square brackets).
abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even 
  though xyyx is outside square brackets).
aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters 
  must be different).
ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even 
  though it's within a larger string).

How many IPs in your puzzle input support TLS?

------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------

You would also like to know which IPs support SSL (super-secret listening).

An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in 
the supernet sequences (outside any square bracketed sections), and a 
corresponding Byte Allocation Block, or BAB, anywhere in the hypernet 
sequences. An ABA is any three-character sequence which consists of the 
same character twice with a different character between them, such as xyx 
or aba. A corresponding BAB is the same characters but in reversed positions: 
yxy and bab, respectively.

For example:

aba[bab]xyz supports SSL (aba outside square brackets with corresponding 
  bab within square brackets).
xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
aaa[kek]eke supports SSL (eke in supernet with corresponding kek in 
  hypernet; the aaa sequence is not related, because the interior character 
  must be different).
zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a 
  corresponding bzb, even though zaz and zbz overlap).

How many IPs in your puzzle input support SSL?

------------------------------------------------------------------------------
NOTES
------------------------------------------------------------------------------


'''

import time

#Timing: Start
start = time.perf_counter()

data = []

def has_abba(check):
    for i in range(len(check)-3):
        if check[i] == check[i+3]:
            if check[i+1] == check[i+2]:
                if check[i] != check[i+1]:
                    return True
    return False

def get_aba(supernet):
    aba = []
    for part in supernet:
        for i in range(len(part)-2):
            if part[i] == part[i+2]:
                if part[i] != part[i+1]:
                    aba.append(part[i:i+3])
    return aba

def check_bab(aba, hypernet):
    for aba_to_check in aba:
        rev = ''.join([aba_to_check[1], aba_to_check[0], aba_to_check[1]])
        if sum(rev in part for part in hypernet) > 0:
            return True
    return False

with open('txt/day07.txt') as f:
    for line in f:
        line = line.strip()
        hypernet = []
        while '[' in line:
            find_l = line.find('[')
            find_r = line.find(']', find_l+1)
            hypernet.append(line[find_l + 1:find_r])
            line = line[:find_l] + '~' + line[find_r+1:]
        data.append([line.split('~'), hypernet])

#Part 1
valid_addresses = 0
for address in data:
    supernet, hypernet = address
    #Addresses aren't valid if they have ABBA in the hypernet
    if sum(has_abba(part) for part in hypernet) == 0:
        if sum(has_abba(part) for part in supernet):
            valid_addresses += 1 
print(valid_addresses)

#Part 2
valid_addresses = 0
for address in data:
    supernet, hypernet = address
    aba = get_aba(supernet)
    if len(aba) > 0:
        if check_bab(aba, hypernet):
            valid_addresses += 1
print(valid_addresses)

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")
