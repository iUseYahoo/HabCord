import os

def clear():
  if os.name == "nt":
    os.system("cls")
  elif os.name == "posix":
    os.system("clear")
  else:
    pass
    
clear()

print("== INSTALLING PYAUTOGUI ==")
os.system("pip install pyautogui")

print("== INSTALLING DISCORD ==")
os.system("pip install discord")

