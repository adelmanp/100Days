#!/usr/bin/python3

from sys import exit
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
fork = input("You've come to a fork in the road, would you like to go left or right? ")
if fork.lower() != "left" :
  print("You fell off a cliff and died. Game Over.")
  exit()
else:
  swim = input("You come to a river crossing, would you like to swim or wait? ")

if swim.lower() != "wait":
  print("You tired to swim accross but were eatten by piranhas. Game Over.")
  exit()
else:
  print(
    """
    While you waited a farry apraoched you and offered to let you cross. 
    While trying to find your room you come accress three doors, 
    A Red Door, A Blue Door, and A Yellow Door
    """
  )
  door = input("Which door do you choose, Red, Blue, or Yellow? ")

if door.lower()  == "red":
  print(
    """
    You walked in to the boiler room as a boiler exploaded.
    The explsion killed you instantly.
    Game Over.
    """
  )
  exit()
elif door.lower() == "blue":
  print(
    """
    You open the door to find Davy Jones himself.
    He takes you prision and forces you to work on his ship the Flying Dutchman.
    Game Over.
    """
  )
  exit()
elif door.lower() == "yello":
  print(
    """
    You find a cosy cabin to wait in while you cross the river.
    Upon debaring from the ferry you notice something reflecting in the sand.
    you dig it up to find a buried treasure chest
    """
  )
  exit()
else:
  print(
    """
    While crossing the river the ship was sunk by a giant squid.
    Game Over.
    """
  )
  exit()