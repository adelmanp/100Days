#!/usr/bin/python3

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiple(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiple,
    "/": divide,
  }

def find_operator():
  for key in operations:
    print(key)
  return input("Pick an operation from the line above: ")  

def print_answer(x, y, operator, answer):
  print(f"{x} {operation_symbol} {y} = {answer}")

def provide_number():
  num = float(input("Please enter a number? \n"))
  return num

def cal_answer(x, y, operation):
  answer = operations[operation_symbol](x, y)
  print(f"{x} {operation} {y} = {answer}")
  return answer

def calculator():
  num = provide_number()
  operation_symbol = find_operator()
  num2 = provide_number()
  answer = cal_answer(num, num2, operation_symbol)
  again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exist.: ")
  if again == "y":
    num = answer
    again = True
  else:
    again = False
    
  while again: 
    print(f"What operation would you like to preform on {answer}")
    operation_symbol = find_operator()
    num2 = provide_number()
    answer = cal_answer(num, num2, operation_symbol)
    again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exist.: ")
    if again == "y":
      num = answer
      again = True
    else:
      again = False
      
  
calculator()
