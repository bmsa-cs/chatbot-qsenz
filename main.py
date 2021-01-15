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
    print("Why did the chicken cross the road...")
    time.sleep(4)
    print("to get to the other side!")
  elif q3 == "no" or q3 == "no"
elif q2 == "stop" or q2 == "stop talking" or q2 == "stop talking to me":
  print("Alright then, chatbot Bristol powering off...")
else:
  print("Sorry, im not sure how to respond to this.")
