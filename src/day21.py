'''
------------------------------------------------------------------------------
ADVENT OF CODE 2016 - DAY 21: Scrambled Letters and Hash
------------------------------------------------------------------------------

The computer system you're breaking into uses a weird scrambling function to 
store its passwords. It shouldn't be much trouble to create your own 
scrambled password so you can add it to the system; you just have to 
implement the scrambler.

The scrambling function is a series of operations (the exact list is 
provided in your puzzle input). Starting with the password to be scrambled, 
apply each operation in succession to the string. The individual operations 
behave as follows:

swap position X with position Y       
-- the letters at indexes X and Y (counting from 0) should be swapped.

swap letter X with letter Y           
-- the letters X and Y should be swapped (regardless of where they appear 
   in the string).

rotate left/right X steps             
-- the whole string should be rotated; for example, one right rotation 
   would turn abcd into dabc.

rotate based on position of letter X  
-- the whole string should be rotated to the right based on the index of 
   letter X (counting from 0) as determined before this instruction does 
   any rotations. Once the index is determined, rotate the string to the 
   right one time, plus a number of times equal to that index, plus one 
   additional time if the index was at least 4.

reverse positions X through Y         
-- the span of letters at indexes X through Y (including the letters at 
   X and Y) should be reversed in order.

move position X to position Y         
-- the letter which is at index X should be removed from the string, 
   then inserted such that it ends up at index Y.

For example, suppose you start with abcde and perform the following operations:

swap position 4 with position 0 swaps the first and last letters, producing 
  the input for the next step, ebcda.

swap letter d with letter b swaps the positions of d and b: edcba

reverse positions 0 through 4 causes the entire string to be reversed: abcde

rotate left 1 step shifts all letters left one position, causing the first 
  letter to wrap to the end of the string: bcdea

move position 1 to position 4 removes the letter at position 1 (c), then 
  inserts it at position 4 (the end of the string): bdeac

move position 3 to position 0 removes the letter at position 3 (a), then 
  inserts it at position 0 (the front of the string): abdec.

rotate based on position of letter b finds the index of letter b (1), 
  then rotates the string right once plus a number of times equal to that 
  index (2): ecabd.

rotate based on position of letter d finds the index of letter d (4), 
  then rotates the string right once, plus a number of times equal to 
  that index, plus an additional time because the index was at least 4, 
  for a total of 6 right rotations: decab.

After these steps, the resulting scrambled password is decab.

Now, you just need to generate a new scrambled password and you can 
access the system. Given the list of scrambling operations in your puzzle 
input, what is the result of scrambling abcdefgh?

------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------


------------------------------------------------------------------------------
NOTES
------------------------------------------------------------------------------

Puzzle input = abcdefgh

'''

import time

#Timing: Start
start = time.perf_counter()

#Load the data
with open('txt/day21.txt') as f:
    data = [line.strip().split() for line in f.readlines()]

input = 'abcdefgh'
print(input)
print('——————————')

for line in data:
    instruction = ' '.join(line[0:2])
    if instruction == 'rotate right':
        '''
        offset = int(line[2])
        if offset > 0:
            split = len(input) - offset
            input = input[split:] + input[:split]
            print(f'{instruction} {offset}')
            print(input)
            print('——————————')
        '''
    elif instruction == 'rotate left':
        '''
        offset = int(line[2])
        if offset > 0:
            input = input[offset:] + input[:offset]
            print(f'{instruction} {offset}')
            print(input)
            print('——————————')
        '''
    elif instruction == 'swap letter':
        '''
        input = input.replace(line[2], '#')
        input = input.replace(line[5], line[2])
        input = input.replace('#', line[5])
        print(f'{instruction} {line[2]} with {line[5]}')
        print(input)
        print('——————————')
        '''
    elif instruction == 'swap position':
        '''
        copy = ''
        s1 = int(line[2])
        s2 = int(line[5])
        for i in range(len(input)):
            if i == s1:
                copy += input[s2]
            elif i == s2:
                copy += input[s1]
            else:
                copy += input[i]
        input = copy
        print(f'{instruction} {line[2]} with {line[5]}')
        print(input)
        print('——————————')
        '''
    else:
        print(f'NOT HANDLING: {instruction}')


#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")