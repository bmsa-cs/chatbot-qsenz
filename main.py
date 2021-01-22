"""
Chatbot
Author: 
Period/Core: 

"""

import os
import importlib.util

import random
import time

def run_tests():
  """
  This function will check for the pytest module
  before calling it to run the included tests.py
  """
  if importlib.util.find_spec('pytest') is None: # Check if pytest is installed
    os.system('python3 -m pip install -q pytest')

  command = "python3 -m pytest --tb=line -v -s tests.py"
  print(command)
  os.system(command)

def main():
  """This function contains all code for the chatbot."""
  print("Hello!")


if __name__ == "__main__":
  main()
  t = input("Run pytest? (y/n)").lower()
  if t == 'y':
    run_tests()

q1 = input("Hello, What's your name? ")
print("Hello", str(q1), "my name is chatbot Bristol!")





q2 = input("Are you doing good today? ")

if q2 == "no" or q2 == "No":
  print("I'm sorry to hear that.")
  q3 = input("Could I make you feel better with a joke? ")
  if q3 == "yes" or "sure" or "ok":
    joke1 = random.randint(1,3)
    if joke1 == 1:
      print("Why did the chicken cross the road? To get to the other side!")
    elif joke1 == 2:
      print("I invented a new word... Plagarism!")
    elif joke1 == 3:
      print("Hear about the new resturant called karma? Heres the menu: You get what you deserve.")
  elif q3 == "no" or q3 == "nope" or q3 == "No":
    print("Alright then i'll go.")
    exit()
  else:
    print("I'm not sure how to respond to that...")
    exit()

elif q2 == "yes" or q2 == "yeah" or q2 == "Yes":
  print("That's very nice to hear!")
  q4 = input("Would you like to hear a joke?")
  if q4 == "yes" or q4 == "Yes" or q4 == "sure":
    joke1 = random.randint(1,3)
    if joke1 == 1:
      print("Why did the chicken cross the road? To get to the other side!")
    elif joke1 == 2:
      print("I invented a new word... Plagarism!")
    elif joke1 == 3:
      print("Hear about the new resturant called karma? Heres the menu: You get what you deserve.")

else:
  print("Sorry, im not sure how to respond to this.")
  exit()

q5 = input("What's your favorite food?")
print("Awesome my favorite food is stir fry!")

q6 = input("How was your conversation with me 1-5?")
print("Thanks for your feedback", q1)