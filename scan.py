import sys
result = ()
apps = open('apps.txt', 'w')
import os
for root, dirs, files in os.walk("B:\itch apps"):
    for file in files:
        if file.endswith(".exe"):
             result = (os.path.join(root, file))
             apps = open('apps.txt', 'w')
             print(result, file = apps)
             
             
