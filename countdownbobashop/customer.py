import random
import time
import replit

class Order:
  global names
  global welcomes
  global flavors
  global toppings
  global sizes
  global earned
  global separator
  global customer1
  global randomize
  #lists of possibilities, this is where customer1 chooses its random identity and order from
  names = ['Harry', 'Paul', 'Joe']
  flavors = ['Mango tea', 'Milk tea', 'Matcha tea']
  toppings = ["Boba", "Whipped Cream", "Lychee Jelly"]
  sizes = ["Small", "Medium", "Large"]
  welcomes = [
    "\"Boy, it sure is a hot day, can't wait to get some tea...\"\n",
    "\"What a lovely shop! I think I'll take a...\"\n",
    "\"Boba has got to be the best drink ever!\"\n",
    "\"I'm having such a great day, this cup of tea will make it even better!\"\n",
    "\"Hello there, can I get a cup of tea please?\"\n",
    "\"I'm gonna get the coolest instagram picture with my tea!\"\n"
  ]

  def randomize():
    global customer1
    customer1 = Order(names[random.randint(0,2)], welcomes[random.randint(0,5)], flavors[random.randint(0,2)], toppings[random.randint(0,2)], sizes[random.randint(0,2)])
  
  # initalizes every object giving it its attributes based on whatever is in the parenthesis- which is all random as seen below
  def __init__(self, name, welcome, flavor, topping, size):
    self.name = name
    self.welcome = welcome
    self.flavor = flavor
    self.topping = topping
    self.size = size


customers = []
n = 0
while n < 5:
  customers.append(Order(names[random.randint(0,2)], welcomes[random.randint(0,5)], flavors[random.randint(0,2)], toppings[random.randint(0,2)], sizes[random.randint(0,2)]))
  n = n + 1
  
def clear():
  time.sleep(0.5)
  replit.clear()
  
def printorder(self):
  randomize()
  print("Customer: " + self.name + "\n")
  print(self.welcome)
  time.sleep(4)
  clear()
  print(self.name + "'s order:")
  print("\033[94m")
  print(self.flavor)
  print(self.topping)
  print(self.size)
  print("\033[0m")