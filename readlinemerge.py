LineToRead = 1
counter = 0
amount = int(input("number of installed itch games"))
file = open("apps.txt", 'r')
print (" ")
while (counter < amount):
#    linetext = (file.readline(LineToRead))
#    print (linetext.read)
    if (file.readline(LineToRead) == ""):
            counter += 1
    else:
            file.readline(LineToRead)
            print (file.read())
            LineToRead = LineToRead + 1
