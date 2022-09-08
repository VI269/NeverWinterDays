from random import randint, choice
from os import system
from time import sleep
import platform
import json


def wait(dur):
    sleep(dur)


def clearConsole():
    if platform.system() == 'win32':
        system('cls')
    else:
        system('clear')


def loading(msg, dur):
    for i in range(0, dur * 3):
        clearConsole()
        print(f"{msg}.")
        wait(1 / 3)
        clearConsole()
        print(f"{msg}..")
        wait(1 / 3)
        clearConsole()
        print(f"{msg}...")
        wait(1 / 3)
        clearConsole()


class Inventory:
    def __init__(self):
        self.inv = {
            'cheese': 0,
            'bread': 0,
            "mushroom stew": 0,
            'porridge': 0,
            'water': 0,
            'grapes': 0,
            'milk': 0,
            'apple': 0,
            'fig': 0,
            'bacon': 0,
            'ham': 0,
            'rice': 0,
            'money': 100
        }

    def getValue(self, food):
        try:
            return self.inv[food]
        except KeyError:
            print("Invalid Input")

    def changeValue(self, item, num):
        self.inv[item] += num

    def menu(self):
        for item in self.inv.keys():
            text = item[0].upper() + item[1:]
            if item == 'mushroom stew':
                text = 'Mushroom Stew'
            print(f"[{text}]:[{self.getValue(item)}]")
            continue


inv = Inventory()


class Health:
    def __init__(self):
        self.health = 20

    def getHeath(self):
        return self.health

    def verify(self):
        if self.health > 20:
            self.health = 20
        elif self.health < 0:
            self.health = 0

    def changeHealth(self, val):
        self.health += val
        self.verify()


health = Health()


class Hunger:
    def __init__(self):
        self.hunger = 20

    def getHunger(self):
        return self.hunger

    def verify(self):
        if self.hunger > 20:
            self.hunger = 20
        elif self.hunger < 0:
            self.hunger = 0
        if self.hunger == 0:
            health.changeHealth(-4)
            print("You lost some health because your hunger is low. This can kill you.")

    def changeHunger(self, val):
        self.hunger += val
        self.verify()


class UI:
    def __init__(self):
        pass

    @staticmethod
    def divider():
        print('══✿══╡°˖✧✿✧˖°╞══✿══')

    @staticmethod
    def dividerReturn():
        return '══✿══╡°˖✧✿✧˖°╞══✿══'

    @staticmethod
    def midPrint(text):
        print(f'[{text}]')

    @staticmethod
    def midReturn(text):
        return f'[{text}]'


class Shop:
    def __init__(self):
        self.stock = {}
        self.prices = {}

    def menu(self):
        string = ''
        for item in self.stock.keys():
            for price in self.prices.keys():
                string = string + (
                    f'[{item[0].upper() + item[1:]}][Available:|{self.stock[item]}|Cost:|₪{self.prices[price]}|]\n\n')
                break
        return string

    def update(self, value):
        for item in self.stock.keys():
            self.stock[item] += value

    def newItem(self, name, avl, price):
        self.stock[name] = avl
        self.prices[name] = price

    def delItem(self, name):
        del self.stock[name]
        del self.prices[name]

    @staticmethod
    def calcPrice(self, item, quan):
        try:
            return self.prices[item] * quan
        except KeyError:
            return False

    @staticmethod
    def checkOutPossible(price):
        if price > inv.getValue('money'):
            return False
        else:
            return True


# Object Creation

# Health is created as "health"

ui = UI()
hunger = Hunger()
shop = Shop()

print("Note: Caps DON'T Matter.")
wait(2)
clearConsole()

pathtoFile = input("Please enter your system path to this folder. If it is already saved press enter: ")

if pathtoFile == '':
    with open('path.txt', 'w') as f:
        f.write(pathtoFile)

else:
    pass

running = True
setup = True
# So if you want to end the game do: running = False
while setup:
    clearConsole()
    ui.divider()
    print("SETUP: \nNew Save - L\nLoad Save - S\n")
    command = input("[L/N]>>> ").lower()
    if command == 'n':
        clearConsole()
        name = input("[Save Name]>>> ")
        with open('path.txt', 'r') as f:
            ptf = f.read()
        with open(f'{ptf}/saves/{name}.json') as f:
            pass

quit()
