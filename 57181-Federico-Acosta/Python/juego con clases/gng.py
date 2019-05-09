import random
import math

class ComputerAgainstHumanGame():
  def __init__(self):
    self.max_num = 100
    self.min_num = 1
    self.mitad = math.ceil(((self.max_num + self.min_num) - 1) / 2)
    self.input_text = f"Is it your number {self.mitad}?"
    self.is_playing = True

  def play(self, character):
    if character == "+":
      self.min_num = self.mitad
      self.mitad = math.ceil(((self.max_num + self.min_num) - 1) / 2)
      self.input_text = f"Is it your number {self.mitad}?"
    elif character == "-":
      self.max_num = self.mitad
      self.mitad = math.ceil(((self.max_num + self.min_num) - 1) / 2)
      self.input_text = f"Is it your number {self.mitad}?"
    elif character == "=":
      print("You win")
      self.is_playing = False
      return "I win"

class HumanAgainstComputerGame():
  
  def __init__(self):
    self.secret_number = random.randint(1, 100)
    self.is_playing = True
  
  def play(self, intento):
    num = int(intento)
    if num > self.secret_number:
      print("My number is smaller")
      return "My number is smaller"
    elif num < self.secret_number:
      print('My number is bigger')
      return 'My number is bigger'
    elif num == self.secret_number:
      self.is_playing = False
      return "You win"
      

