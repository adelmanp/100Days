#!/usr/bin/python3

import logging

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

guest_list = []

# open starting file
with open("./Input/Names/invited_names.txt", "r") as names:
    for line in names:
        guest_list.append(line.strip())
logger.debug(f'Guest List: {guest_list}')

# create an invite and save to new file
with open("./Input/Letters/starting_letter.txt", 'r') as letter_file:
    letter = letter_file.read()
    for name in guest_list:
        new_letter = letter.replace('[name]', name)
        with open(f'./Output/ReadyToSend/invite_{name}', 'w') as invite:
            invite.write(new_letter)
