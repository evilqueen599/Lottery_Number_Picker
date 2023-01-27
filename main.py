# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import random
powerPicks =  int (input("How many for Powerball?: "))
megaPicks = int (input("How many for Mega Millions?"))

for i in range (powerPicks):
    num_list = random.sample(range(1, 69), 5,)
    num_list.sort()
    power_num = random.sample(range(1, 26), 1)
    print("Draw Numbers :", num_list, "-", "Powerball :", power_num)

for i in range (megaPicks):
    num_list = random.sample(range(1, 70), 5,)
    num_list.sort()
    mega_num = random.sample(range(1, 25), 1)
    print("Draw Numbers :", num_list, "-", "Mega Ball :", mega_num)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
