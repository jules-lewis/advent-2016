'''
------------------------------------------------------------------------------
ADVENT OF CODE 2016 - DAY 4: Security Through Obscurity
------------------------------------------------------------------------------

Finally, you come across an information kiosk with a list of rooms. Of course, 
the list is encrypted and full of decoy data, but the instructions to decode 
the list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by 
dashes) followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters 
in the encrypted name, in order, with ties broken by alphabetization. 

For example:

aaaaa-bbb-z-y-x-123[abxyz]   is a real room because the most common letters 
                             are a (5), b (3), and then a tie between x, y, 
                             and z, which are listed alphabetically.
a-b-c-d-e-f-g-h-987[abcde]   is a real room because although the letters 
                             are all tied (1 of each), the first five are 
                             listed alphabetically.
not-a-real-room-404[oarel]   is a real room.
totally-real-room-200[decoy] is not.

Of the real rooms from the list above, the sum of their sector IDs is 1514.

What is the sum of the sector IDs of the real rooms?

------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------

With all the decoy data out of the way, it's time to decrypt this list and 
get moving.

The room names are encrypted by a state-of-the-art shift cipher, which is 
nearly unbreakable without the right software. However, the information 
kiosk designers at Easter Bunny HQ were not expecting to deal with a master 
cryptographer like yourself.

To decrypt a room name, rotate each letter forward through the alphabet a 
number of times equal to the room's sector ID. A becomes B, B becomes C, Z 
becomes A, and so on. Dashes become spaces.

For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted 
name.

What is the sector ID of the room where North Pole objects are stored?

------------------------------------------------------------------------------
NOTES
------------------------------------------------------------------------------


'''

import time
import collections

#Timing: Start
start = time.perf_counter()

def decode(text, offset):
    '''
    Simple rotation decryption. We are told that the strings we'll
    be passed will comprise lower case characters or spaces. We don't
    need to decode the spaces, so we just add them on to the decoded
    text. We're also told that the rotation is always to the right 
    (i.e. the offset will always be positive.)
    '''
    decoded_text = ''
    for char in text:
        if char == ' ':
            decoded_text += ' '
        else:
            '''
            Character 'a' has an Ascii code of 97, with all the other lower
            case letters consecutive. What I'm doing here is to set 'a' to
            equal 1:
                ord(char) - 96  ---->  {a}
            then adding the offset, and applying modular division as I've
            likely gone over 26:
                ({a} + offset) % 26  ---->  {b}
            the converting this back in to a character, before adding it to
            the decoded string:
                decoded_text += chr({b} + 96)
            '''
            decoded_text += chr(((ord(char) - 96 + offset) % 26) + 96)
    return decoded_text

sector_id_total = 0
with open('txt/day04.txt') as f:

    for line in f:
    #Sample: vhehkyne-unggr-inkvatlbgz-813[gnehk]  ----> words / sector ID / checksum

        halved = line.strip().split('[')
        left = halved[0].split('-')
        sector_id = int(left[-1])
        room_name = ' '.join(left[:-1])

        #Part 2
        decoded = decode(room_name, sector_id)
        if 'north' in decoded:
            part2_out = f'Part 2: Sector ID {sector_id}, decoded text is "{decoded}"'

        checksum = halved[1][:-1]

        #We're using the Counter() object to total the occurrences of each letter in room_name
        room_name = room_name.replace(' ', '')
        counts = collections.Counter(room_name)
        #Unfortunately, Counter() doesn't sort its elements, but has a method for doing this:
        sorted_counts = counts.most_common()

        #sorted_counts will look a bit like this: [('h', 4), ('q', 4), ('d', 2), ('r', 2), ('l', 2) .... etc. ]
        #and when there are tied results, 'h' & 'q' for example, they should be added to the checksum in
        #alphabetical order.

        #We need to know when the count we're looking at changes, for example from 4 to 2 above. This way, we
        #can start building a little substring of letters with the same count, to add to the overall checksum
        cur_count = sorted_counts[0][1]    #i.e. the second item of the first tuple in the list
        full_sum = ''
        cur_letters = ''

        for key, value in sorted_counts:
            if value != cur_count:
                full_sum += ''.join(sorted(cur_letters))
                cur_letters = key
                cur_count = value
            else:
                cur_letters += key
        full_sum += ''.join(sorted(cur_letters))
        
        #We're only interested in the first five characters
        true_checksum = full_sum[:5]
        
        if checksum == true_checksum:
            sector_id_total += sector_id

#Results
print(f'Part 1: Sector ID {sector_id_total}')
print(part2_out)

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")
