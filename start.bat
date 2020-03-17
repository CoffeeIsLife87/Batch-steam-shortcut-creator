@rem cd "C:\Users\your user name\desktop\autoItchtoSteamlibrary"
@rem sets the active directory to the one with the python script
cd "C:\Users\heros\OneDrive\Documents\GitHub\autoItchtoSteamlibrary"

@rem runs scanning tool to check for .exe files
python scan.py

pause

@rem If you have itch games installed on a second drive then change the B: to whatever drive you use
@rem B:
@rem cd "B:\itch apps"
