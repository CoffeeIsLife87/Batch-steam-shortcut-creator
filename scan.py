result = ("")
import os
for root, dirs, files in os.walk("B:\itch apps"):
    for file in files:
        if file.endswith(".exe"):
             result = (os.path.join(root, file))
             print (result)
    
