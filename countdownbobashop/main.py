# author : JC
# tea shop

# all imports
import tkinter as tk
from tkinter import PhotoImage
import time
import replit
import random
import customer
from customer import Order
from tkinter import LEFT, RIGHT, TOP, BOTTOM, CENTER, RAISED, SUNKEN, GROOVE

# initalizing variables
global earned
earned = 0
global coins
coins = "none"
global selectedflavor
global shakecount
shakecount = 0
global delivery
delivery = "none"
selectedflavor = "none"
selectedtopping = "none"
selectedsize = "none"
gamestarted = "no"
global stopclock
stopclock = False

# clear(): clears console
def clear():
  time.sleep(0.5)
  replit.clear()

def updatecoins():
  global coins
  coins = str(earned) + " coins"
  coinslabel.configure(text = coins)
  coinslabel.pack()
  
# earnings(): determines wether or not an order was produced correctly and awards coins to the player based on that. The amount of coins a player has will show in a label of the tkinter window.
def earnings():
  global earned
  global delivery
  if delivery == "good":
    earned += 10
    updatecoins()
    clear()
  else:
    earned -= 10
    updatecoins()
    clear()
        
    
# loops until the player wins the game at earning 100 coins
def looporder():
  if earned != 50:
    global customer1
    global stopclock
    customer1 = customer.customers[random.randint(0,4)]
    customer.printorder(customer1)
    print("\n\033[0m")
    stopclock = False
    startcountdown()
    clear()
  else:
    clear()
    print("You won the game!")


# serve(): is called after the radiobutton "serve" is clicked. Checks if the requested order matches the produced order then calls the earning function.
def serve():
  global delivery
  global selectedflavor
  global selectedtopping
  global selectedsize
  global shakecount
  global gamestarted
  global stopclock
  stopclock = True
  # help im running out of variable names
  if gamestarted=="no":
    print("You can't serve a non-existent customer...")
  else:
    if selectedflavor == customer1.flavor and selectedtopping == customer1.topping and selectedsize == customer1.size:
      delivery = "good"
      clear()
      print("\"This is delicious!\"")
      if shakecount !=4:
        print("But it seems like my drink wasn't mixed well...")
        time.sleep(3)
    else:
      clear()
      print("\nCustomer left 1 star on yelp...\nThey wanted:")
      print(customer1.flavor + "," + customer1.topping + "," + customer1.size)
    shakecount = 0
    time.sleep(2)
    earnings()
    time.sleep(2)
    delivery = "none"
    # resetting checkboxes
    c1.deselect()
    c2.deselect()
    c3.deselect()
    tc1.deselect()
    tc2.deselect()
    tc3.deselect()
    sc1.deselect()
    sc2.deselect()
    sc3.deselect()
    c1.pack()
    c2.pack()
    c3.pack()
    tc1.pack()
    tc2.pack()
    tc3.pack()
    sc1.pack()
    sc2.pack()
    sc3.pack()
    l.configure(text = "Tea Flavor")
    tl.configure(text = "Topping")
    sl.configure(text = "Size")
    l.pack()
    tl.pack()
    sl.pack()
    shake.configure(text = 'SHAKE')
    shake.pack
    clear()
    looporder()

  
def shake():
  global shakecount
  global selectedflavor
  global selectedtopping
  if selectedflavor=="none" or selectedtopping=="none" or selectedsize=="none":
    print("You can't shake this container right now, something's not right...")
  else:
    shakecount += 1
    if shakecount == 4:
      shake.configure(text = 'STOP')
      shake.pack
    if shakecount > 4:
      print("- 1✰\nYou shook the drink too much")
    if shakecount == 9:
      clear()
      print("This drink now violates FDA policies. The customer has left.")
      time.sleep(3)
      shakecount = 0
      clear()
      earnings()
      looporder()
      # this is madness


# initalizing tkinter window, player is asked what they would like to name their shop and whatever they type will appear in the title bar of the window.
root = tk.Tk()
root.title(' ')
root.geometry( '550x600')
root.configure(background='#c6dba0')
root.attributes('-fullscreen', False)

img = tk.PhotoImage(file="cafe.png")
imglabel = tk.Label(root, image=img)
imglabel.place(x=-70, y=-80, relwidth=1.4, relheight=1)
imglabel.grid_anchor()

# frame for serve shake and coins label
controlswidget = tk.Frame(root, bg='white')
controlswidget.pack(side = TOP)

# frame for clock
clockframe = tk.Frame(root, bg='white')
clockframe.pack(side = TOP)

# this is where a player can see how many coins they've earned
coinslabel = tk.Label(controlswidget, bg ='#A2DFDC', fg ='#7B7DA9', width=20, height=2, font=("Comic Sans MS", 20, "bold"), text ='0 coins')
coinslabel.pack(side = RIGHT)

# clock to see time left to make current order
clockvar = tk.StringVar()
clock = tk.Label(clockframe, textvariable=clockvar, bg ='#A2DFDC', fg ='#7B7DA9', width=5, height=1, bd=4, font=("Comic Sans MS", 20, "bold"), text = '00:00')
clock.pack(side= RIGHT)
# clcok go tik tic
global clocktext
clocktext = ""

def updatecountdown():
  global clocktext
  clockvar.set(clocktext)
  root.update()

def startcountdown():
  global clocktext
  s = 20
  while s >= 0:
    minutes, seconds = divmod(s, 60)
    clocktext = '{:02d}:{:02d}'.format(minutes, seconds)
    time.sleep(1)
    s = s - 1
    if s < 10 and s > 4:
      clock.configure(fg = "#FC6A4B")
    if s < 5:
      clock.configure(fg = "#F90000")
    if stopclock == True:
      s = 20
      clocktext = '--:--'
      clock.configure(fg = "#FFFFFF")
      updatecountdown()
      break
    updatecountdown()
  time.sleep(1)
  clear()
  print("\033[0mToo slow! The customer left...")
  serve()
# a player will click this to submit their product to be checked
servebutton = tk.Radiobutton(controlswidget, text="SERVE", fg='white', activeforeground='green', indicatoron=0, bd=4, relief=tk.GROOVE, font=("Comic Sans MS", 15, "bold"), selectcolor = '#A2B4DF',cursor="box_spiral", command=serve)
servebutton.pack(side = TOP)

# shake radiobutton
shake = tk.Radiobutton(controlswidget, text="SHAKE", fg='white', activeforeground='green', indicatoron=0, bd=4, relief=tk.GROOVE, font=("Comic Sans MS", 15, "bold"), selectcolor = '#A2B4DF',cursor="box_spiral", command=shake)
shake.pack(side = TOP)

# groups for checkboxes, make the alignment look nicer
ph1= tk.Label(root)
ph1.pack(side = TOP)
flavorwidget = tk.Frame(root, bg='#A2DFCD')
flavorwidget.pack(side = TOP, anchor=tk.E)
#
ph2= tk.Label(root)
ph2.pack(side = TOP)
toppingwidget = tk.Frame(root, bg='#A2DFCD')
toppingwidget.pack(side = TOP, anchor=tk.E)
#
ph3 = tk.Label(root)
ph3.pack(side = TOP)
sizewidget = tk.Frame(root, bg='#A2DFCD')
sizewidget.pack(side = TOP, anchor=tk.E)

# tea flavor label
l = tk.Label(flavorwidget, bg='#A2B4DF', width=20, text='Tea Flavor')
l.pack()

# checking each box will show its corresponding text on the label but checking none or more than one will show an error message
def teaselection():
    global selectedflavor
    if (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 0):
        l.config(text='Mango')
        selectedflavor = "Mango tea"
    elif (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 0):
        l.config(text='Milk')
        selectedflavor = "Milk tea"
    elif (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 1):
        l.config(text='Matcha')
        selectedflavor = "Matcha tea"
    else:
        l.config(text='None or too many')
        selectedflavor = "none"

      
# setting up checkboxes for the tea flavors
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
c1 = tk.Checkbutton(flavorwidget, text='Mango',variable=var1, onvalue=1, offvalue=0,  bg='#A2DFCD', command=teaselection)
c1.pack()
c2 = tk.Checkbutton(flavorwidget, text='Milk', variable=var2, onvalue=1, offvalue=0, bg='#A2DFCD', command=teaselection)
c2.pack()
c3 = tk.Checkbutton(flavorwidget, text='Matcha', variable=var3, onvalue=1, offvalue=0, bg='#A2DFCD', command=teaselection)
c3.pack()
#---------^Flavor^------v-Topping-v-----------------

tl = tk.Label(toppingwidget, bg='#A2B4DF', width=20, text='Topping')
tl.pack()
# literally copy&paste and hardcoding all this because i absolutely do not want to make another class for this
def toppingsselection():
    global selectedtopping
    if (tvar1.get() == 1) & (tvar2.get() == 0) & (tvar3.get() == 0):
        tl.config(text='Boba')
        tl.pack()
        selectedtopping = "Boba"
    elif (tvar1.get() == 0) & (tvar2.get() == 1) & (tvar3.get() == 0):
        tl.config(text='Whipped Cream')
        tl.pack()
        selectedtopping = "Whipped Cream"
    elif (tvar1.get() == 0) & (tvar2.get() == 0) & (tvar3.get() == 1):
        tl.config(text='Lychee Jelly')
        tl.pack() 
        selectedtopping = "Lychee Jelly"
    else:
        tl.config(text='None or too many')
        tl.pack()
        selectedtopping = "none"

# checkboxes for toppigns
tvar1 = tk.IntVar()
tvar2 = tk.IntVar()
tvar3 = tk.IntVar()
tc1 = tk.Checkbutton(toppingwidget, text='Boba',variable=tvar1, onvalue=1, offvalue=0, bg='#A2DFCD', command=toppingsselection)
tc1.pack()
tc2 = tk.Checkbutton(toppingwidget, text='Whipped Cream', variable=tvar2, onvalue=1, offvalue=0, bg='#A2DFCD', command=toppingsselection)
tc2.pack()
tc3 = tk.Checkbutton(toppingwidget, text='Lychee Jelly', variable=tvar3, onvalue=1, offvalue=0, bg='#A2DFCD', command=toppingsselection)
tc3.pack()

#---------^Topping^------v-Size-v-----------------
sl = tk.Label(sizewidget, bg='#A2B4DF', width=20, text='Size')
sl.pack()

def sizeselection():
    global selectedsize
    if (svar1.get() == 1) & (svar2.get() == 0) & (svar3.get() == 0):
        sl.config(text='Small')
        sl.pack()
        selectedsize = "Small"
    elif (svar1.get() == 0) & (svar2.get() == 1) & (svar3.get() == 0):
        sl.config(text='Medium')
        sl.pack()
        selectedsize = "Medium"
    elif (svar1.get() == 0) & (svar2.get() == 0) & (svar3.get() == 1):
        sl.config(text='Large')
        sl.pack()
        selectedsize = "Large"
    else:
        sl.config(text='None or too many')
        sl.pack()
        selectedsize = "none"

# checkboxes for sizes
svar1 = tk.IntVar()
svar2 = tk.IntVar()
svar3 = tk.IntVar()
sc1 = tk.Checkbutton(sizewidget, text='Small', variable=svar1, onvalue=1, offvalue=0, bg='#A2DFCD', command=sizeselection)
sc1.pack()
sc2 = tk.Checkbutton(sizewidget, text='Medium', variable=svar2, onvalue=1, offvalue=0, bg='#A2DFCD', command=sizeselection)
sc2.pack()
sc3 = tk.Checkbutton(sizewidget, text='Large', variable=svar3, onvalue=1, offvalue=0, bg='#A2DFCD', command=sizeselection)
sc3.pack()



name = input("What would you like to name your shop?\n")
root.title(name)
clear()
print("Today is the grand opening of " + name.upper() + "!\nYour goal is to earn 50 coins. Press enter to continue.")
enter = input("")
clear()
print("Here comes your first customer...")
time.sleep(.8)
clear()
print("Don't forget to shake the drinks before you serve them!\nUse the SHAKE button in the top left corner.\nGood Luck!")
time.sleep(5)
clear()
gamestarted = "yes"

looporder()

    
root.mainloop()