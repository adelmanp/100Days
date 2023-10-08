#!/usr/bin/python3

print("Welocme to the TIP Calculator")
bill = float(input("Please enter the bill amount? \n$"))
tip = float(input("What precent tip would you like to leave? \n"))
people = int(input("Enter the number of people splitting the bill \n"))

tip_amount = (bill/people) * (tip * .01)
per_person= (bill/people) + tip_amount
amount_due = "{:.2f}".format(per_person)

print(f"Including a {tip}% tip each person owes {amount_due}")
