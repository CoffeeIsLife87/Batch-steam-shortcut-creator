LineToRead = 1
counter = 0
amount = input("amount of games installed from itch")
file = open("apps.txt", 'r')
while (counter < amount):
    file.readline
    print (file.read())
