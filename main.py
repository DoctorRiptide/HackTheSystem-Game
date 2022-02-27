# Property of DoctorRiptide ;)
# I have developed this game as just a mini project.
# I appreciate any feedback or suggestions to the game or
# code itself. Enjoy!!!

import sys
import time
import random
import os
from colorama import Fore
import json

# Set achievements
all_achievements = {
  "Escapist" : "Escape from the cops",
  "Busted" : "Get caught by the cops.",
  "Access granted" : "Get the pin right",
  "Access denied" : "Get the pin wrong",
  "10gb homework folder ;)" : "Access the homework.img file",
  "Script Kiddie" : "DDOS The firewall",
  "Robot Army" : "Fail the captcha",
  "You suck at typing" : "Put in a wrong option",
  "Mission Complete" : "Get access to Trump's twitter"
}

# Clear the console
def clear():
  command = 'clear'
  if os.name in ('nt', 'dos'): # Check machine type
    command = 'cls'
  os.system(command)

# Flush typing
def flushType(text, *,color=None, speed=0.2): # Kwargs not nessasary

  text = text + '\n'
  
  if color != None:
    color = color.upper()
    
  if color not in ('RED', 'GREEN'): # Basic color setting
    for char in str(text):
      print(Fore.WHITE + char, end='')
      sys.stdout.flush()
      time.sleep(speed)

  elif color == 'RED': # Red color setting
    for char in str(text):
      print(Fore.RED + char , end='')
      sys.stdout.flush()
      time.sleep(speed)

  elif color == 'GREEN': # Green color setting
    for char in str(text):
      print(Fore.RED + char, end='')
      sys.stdout.flush()
      time.sleep(speed)

# Intro
flushType(text="Welcome to Hack the system.\n",  speed=0.01, color='green')
flushType(text="This game features achievements, different endings, interactive drives, bossfights and more! Enjoy...", speed=0.02, color="red")

time.sleep(5)

clear()

# Preferences
typing_speed = None
difficulty = None
name = None

# Typing speed options
print(Fore.WHITE + 'Set a typing speed: ')
print('(1) None')
flushType(text="(2) Slow", speed=0.3)
flushType(text="(3) Medium", speed=0.03)
flushType(text="(4) Fast [Reccomended]", speed=0.009)
selection_speed = str(input(Fore.GREEN + 'Make a selection : '))

# Typing speed selection
if selection_speed == '1':
  typing_speed = 0.0001
elif selection_speed == '2':
  typing_speed = 0.3
elif selection_speed == '3':
  typing_speed = 0.03
elif selection_speed == '4':
  typing_speed = 0.009
else:
  print(Fore.RED + 'Invalid option. Auto selected fast! :)')
  typing_speed = 0.009
time.sleep(2)

# Name 
clear()
flushType(text="What is your name (keep it under 12 chars)", speed=typing_speed)
name_selection = input(Fore.GREEN + 'Enter here : ')

if int(len(name_selection)) > 8:
  flushType(text="Your name was too long. It has been auto selected as Dave.", color='red', speed=typing_speed)
  name = 'Dave'
  
elif name_selection == None:
  flushType(text="You did not enter a name. It has been auto selected to Pete", color='red', speed=typing_speed)

time.sleep(2)

clear()

achievement = []

win = False

def Credit():
  clear()
  print("""
 __  __     ______     ______     __  __        ______   __  __     ______        ______     __  __     ______     ______   ______     __    __    
/\ \_\ \   /\  __ \   /\  ___\   /\ \/ /       /\__  _\ /\ \_\ \   /\  ___\      /\  ___\   /\ \_\ \   /\  ___\   /\__  _\ /\  ___\   /\ "-./  \   
\ \  __ \  \ \  __ \  \ \ \____  \ \  _"-.     \/_/\ \/ \ \  __ \  \ \  __\      \ \___  \  \ \____ \  \ \___  \  \/_/\ \/ \ \  __\   \ \ \-./\ \  
 \ \_\ \_\  \ \_\ \_\  \ \_____\  \ \_\ \_\       \ \_\  \ \_\ \_\  \ \_____\     \/\_____\  \/\_____\  \/\_____\    \ \_\  \ \_____\  \ \_\ \ \_\ 
  \/_/\/_/   \/_/\/_/   \/_____/   \/_/\/_/        \/_/   \/_/\/_/   \/_____/      \/_____/   \/_____/   \/_____/     \/_/   \/_____/   \/_/  \/_/ 
                                                                                                                                                   
        """)
  time.sleep(3)
  clear()
  print(Fore.YELLOW + "A creation by DoctorRiptide...")
  time.sleep(3)
  clear()
  print("Grace : 'That game was very fun! '")
  time.sleep(3)
  clear()
  print("More updates coming soon!")
  

def GameSummary(name, win):
  clear()
  
  time.sleep(2)
  
  if win == True:
    win = Fore.GREEN + "Win!"
    
  else:
    win = Fore.RED + "Lost :("
    
  print(Fore.YELLOW + "Name : " + Fore.GREEN + str(name))
  print(Fore.YELLOW + "Victory status : " + Fore.GREEN + win)
  print(Fore.YELLOW + "Achievements : " + Fore.GREEN + achievement[0])
  
  for item in achievement:
    if item == achievement[0]:
      continue
    print(item)

  time.sleep(2)

  Credit()

  sys.exit()

flushType(text="You are a hacker trying to get access to Donald Trump's twitter account. To start off, you need to get access to his C:\\ Drive...\n", speed=typing_speed)

flushType(text="The best way of getting to his C drive is by fighting his firewall...", color='red', speed=typing_speed)

time.sleep(3)

# Set the game as a class to break up into smaller parts
class Gameplay:
  def __init__(self, name, typing_speed):
    self.name = name
    self.speed = typing_speed

  # Endings

  # Robot Ending
  def robotEnding(self, name):
    print(Fore.BLUE + "\nYou sit and cry in despair...\n")
    time.sleep(1)
    print(Fore.BLUE + "You hear a loud crash at the door. \n")
    time.sleep(1)
    print("""
                             Annihilate.
                           ,'
              .-----.
            ,' -   - `.
    _ _____/   
  \_____ _
   /_||   ||`-._____.-`||   ||-\
  / _||===||           ||===|| _\
 |- _||===||===========||===||- _|
 \___||___||___________||___||___/
  \\|///   \_:_:_:_:_:_/   \\\|//
  |   _|    |_________|    |   _|
  |   _|   /( ======= )\   |   _|
  \\||//  /\ `-.___.-' /\  \\||//
   (o )  /_ '._______.' _\  ( o)
  /__/ \ |    _|   |_   _| / \__\
  ///\_/ |_   _|   |    _| \_/\\\
 ///\\_\ \    _/   \    _/ /_//\\\
 \\|//_/ ///|\\\   ///|\\\ \_\\|//
         \\\|///   \\\|///
         /-  _\\   //   _\
         |   _||   ||-  _|
       ,/\____||   || ___/\,
      /|\___`\,|   |,/'___/|\
      |||`.\\ \\   // //,'|||
      \\\\_//_//   \\_\\_//// 
          
          """)
    time.sleep(2)
    print(Fore.YELLOW + "\nYou gained an achievement : Robot Army")
    achievement.append("Robot Army")
    time.sleep(2)
    GameSummary(name=self.name, win=False)
    
  # Escape ending
  def escapeEnding(self, name):
    print(Fore.BLUE + "You run out of your door and sprint to the nearest airport.")
    time.sleep(3)
    print(Fore.BLUE + "\nYou got on the eariliest plane to barbados and lived a very nice life :)")
    print("""
                 
        __ _.--..--._ _
     .-' _/   _/\_   \_'-.
    |__ /   _/\__/\_   \__|
       |___/\_\__/  \___|
              \__/
              \__/
               \__/
                \__/
             ____\__/___
       . - '             ' -.
      /                      \
~~~~~~~  ~~~~~ ~~~~~  ~~~ ~~~  ~~~~~
  ~~~   ~~~~~   ~!~~   ~~ ~  ~ ~ ~

          """)
    time.sleep(2)
    print(Fore.YELLOW + "You gained an achievement : Escapist")
    achievement.append("Escapist")
    win = True
    GameSummary(name=self.name, win=win)

  # Trump Twitter Ending
  def trumpEnding(self, name):
    clear()
    print(Fore.BLUE + "Do you : \n(1) Delete Trumps twitter\n(2) Sell his account")
    sel = input(Fore.GREEN + "Make a selection: ")
    print('\n')
    
    if str(sel) == '1':
      print(Fore.GREEN + "Its for the best...")
      time.sleep(2)
      print(Fore.YELLOW + "You gained an achievement : Mission Complete")
      achievement.append("Mission Complete")
      GameSummary(name=self.name, win=True)
      
    elif str(sel) == '2':
      print(Fore.YELLOW + "You gained an achievement : Mission Complete")
      achievement.append("Mission Complete")
      time.sleep(2)
      print(Fore.RED + "With all that money you -- ")
      escapeEnding(name=self.name)

    else: 
      print(Fore.YELLOW + "You gained an achievement : You suck at typing")
      achievement.append("You suck at typing")
      time.sleep(2)
      GameSummary(name=self.name, win=True)
      
  # Police ending
  def copEnding(self, name):
    print(Fore.BLUE + "Your electricity goes out...\n")
    
    time.sleep(3)
    
    print(Fore.RED + "Your door smashes open. Police surround you. '{} PUT YOUR HANDS UP'\n".format(self.name))
    
    time.sleep(3)
    
    print(Fore.WHITE + """
          
                   ____            ____            ____
                  /....\          /....\          /....\
          .-.    |::::::|    .-. |::::::|    .-. |::::::|
          | |    |::::::|    | | |::::::|    | | |::::::|
          | |    (`:'':')    | | (`:'':')    | | (`:'':')
          | |   _--|__|--__  | |.--|__|--__  | |_--|__|--__
          | |  |   ________|_|_|_  ________|_|_|_  ________|_____
          | | /    |            |  |            |  |            |
          | |/  /  |            |  |            |  |            |
          |_| |/|  |            |  |            |  |            |
         (===)| |  | FBI        |  | FBI        |  | FBI        |
         `==='  |`-|            |`-|            |`-|            |
          | |   |`-|            |`-|            |`-|            |
          |_|   |  |            |  |            |  |            |
                |  |            |  |            |  |            |
                |  |            |  |            |  |            |
                |`-|            |`-|            |`-|            |
                |__|            |__|            |__|            |
                /_ |            |_ |            |_ |            |
               |___`-__________-'__`-__________-'__`-__________-'
The allegiance has failed
          """)

    time.sleep(2)
    
    print(Fore.YELLOW + "You gained an achievement : Busted")
    achievement.append("Busted")    

    GameSummary(name=self.name, win=False)

  def captcha(self, name):
    clear()
    flushType(text="\nYou are so close... All you have to do now is verify. Are you a robot?", speed=typing_speed)
    robot = input("(y/n): ")
    
    if 'y' in robot:
      print(Fore.RED + '\nREALLY??')
      time.sleep(2)
      self.robotEnding(name=self.name)
      return

    elif 'n' in robot:
      print(Fore.GREEN + "\nYou now have access to Trumps's twitter")
      time.sleep(2)
      self.trumpEnding(name=self.name)
    
  # Enter pin section
  def enterPin(self, name, typing_speed):
    clear()
    pin = 3987 
  
    time.sleep(3)

    clear()

    print("""
          ------------------------------
          |     *    *     *     *     |
          |----------------------------|
          |        |           |       |
          |    1   |     2     |   3   | 
          |        |           |       |
          |----------------------------|
          |        |           |       |
          |    4   |     5     |   6   |
          |        |           |       |
          |----------------------------|
          |        |           |       |
          |    7   |     8     |   9   |
          |        |           |       |
          |----------------------------|
          |              0             |
          ------------------------------
          """)

    flushType(text="\n Mainframe: Enter the correct 4 digit admin pin.", color='red', speed=typing_speed)
    print('\n ')
  
    attempts = 3

    access = False

    iterate = '1234'

    # Monitor attempts    
    for i in iterate:
      if attempts == -1:
        break
        
      pin_entry = input(Fore.GREEN + '\nC:/User/AdminLogin : ')

      # Attempt if statement
      if str(pin) != str(pin_entry):
        flushType(text='\nPin was incorrect. You have {} more attempts'.format(attempts), speed=typing_speed, color='red')
        attempts = attempts - 1
        continue
      
      if str(pin) == str(pin_entry):
        access = True

      if access == True:
        print(Fore.GREEN + '\nYou have gained access.')
        time.sleep(2)
        print(Fore.YELLOW + "\nYou gained an achievement : Access Granted\n")
        achievement.append("Access Granted")
        time.sleep(2)
        self.captcha(name=self.name)
        break

    if access == False:
      flushType(text="\nYou have been banned from the system and the authorities are aware of your location.", color='red', speed=typing_speed)
      time.sleep(3)
      print(Fore.YELLOW + "\nYou gained an achievement : Access Denied")
      achievement.append("Access denied")
      time.sleep(2)
      clear()

      print(Fore.WHITE + 'Options:')
      flushType(text="(1) Give up and watch some TV", speed=typing_speed)
      flushType(text="(2) Escape and flee the country.", speed=typing_speed)
      selection_run = input(Fore.GREEN + 'Make a selection: ')

      # Ending
      if '1' in str(selection_run):
        clear()
        print(Fore.BLUE + 'You sit down to watch TV but --- \n')
        time.sleep(1)
        self.copEnding(name=self.name)

      # Ending 2
      if '2' in str(selection_run):
        clear()
        print(Fore.BLUE + 'You pack your bags and get ready for your escape... \n')
        chance = None
        chance = random.randint(1,3)
        
        # Cop ending
        if chance == 1:
          self.copEnding(name=self.name)
          
        elif chance == 2:
          self.escapeEnding(name=self.name)

  def files(self, name, speed):
    clear()

    next = False
    
    drive = True
    folder1 = False
    folder2 = False
    folder3 = False
    file_view = False
    
    flushType(text="Look for the 4 digit passcode. Type in the FULL NAME of the folder you want to view. Continue when you have the code.", speed=typing_speed)
    time.sleep(5)
    print(Fore.BLUE + 'File Manager')
    
    with open('file_content.json', 'r') as file:
      data = json.load(file)

    while True:
      clear()
      
      if next == True:
        break 
      
      if drive == True:
        print(Fore.WHITE + 'Drive : ' + Fore.BLUE + "C:\\ \n")
        print(Fore.WHITE + "Pick a folder or type continue to start the next task\n")
        
        for f in data["C:\\"]:
          flushType(text=f + '\n', speed=self.speed, color='red')
        print(Fore.BLUE + " >> Continue >> \n ")
        
        folder_pick = input(Fore.GREEN + 'Make a selection : ')

        if folder_pick.lower() == 'continue':
          print('done')
          next = True
          self.enterPin(name=self.name, typing_speed=self.speed)

        elif folder_pick.lower() == 'folder1' or folder_pick.lower() == '3':
          folder1 = True
          drive = False
          clear()

        elif folder_pick.lower() == 'folder2' or folder_pick.lower() == '3':
          folder2 = True
          drive = False
          clear()

        elif folder_pick.lower() == 'folder3' or folder_pick.lower() == '3':
          folder3 = True
          drive = False
          clear()

        else:
          print(Fore.RED + "Invalid folder name.")
          time.sleep(2)
          continue

      if True in (folder1, folder2, folder3):
        if folder1 == True:
          folder = 'Folder1'
          
        elif folder2 == True:
          folder = 'Folder2'
          
        else:
          folder = 'Folder3'
        
        while True:
          clear()

          print(Fore.WHITE + 'Drive : ' + Fore.BLUE + "C:\\{} \n".format(folder))
          print(Fore.WHITE + "Pick a folder, type continue to start the next task or type back to go back to the C:\\ drive\n")

          drive1 = data["C:\\"]
          
          for file in drive1[folder]:
            flushType(text=file + '\n', speed=self.speed, color='red')
          print(Fore.BLUE + " << Back <<\t\t>> Continue >> \n ")
          
          file_pick = input(Fore.GREEN + '(include the file extension) Make a selection: ')

          pass2 = False
          
          if file_pick.lower() == 'back':
            folder1 = False
            folder2 = False
            folder3 = False
            drive = True
            break

          elif file_pick.lower() == 'continue':
            next = True
            self.enterPin(name=self.name, typing_speed=self.speed)

          elif file_pick.lower() == "passcode.enc":
            clear()
            flushType(text="\nThis file is encrypted. Please enter the encryption password or go back.", speed = self.speed, color='red')
            
            while True:
              pass_encrypt = input(Fore.GREEN + "Enter here: ")
              
              if pass_encrypt == "back":
                break
                
              elif pass_encrypt != "admin123":
                print(Fore.RED + "Incorrect...")
                
              else:
                file_pick = "passcode.enc"   
                pass2 = True
                break
          
          file1 = drive1[folder]
          
          while True:
            clear()

            if pass2 == False:
              if file_pick == 'passcode.enc':
                break

            if file_pick == "homework.img":
              print(Fore.YELLOW + "You gained an achievement : 10gb homework folder ;)")
              time.sleep(3)
              achievement.append("10gb homework folder ;)")

            clear()
            
            try:
              print(Fore.WHITE + 'Drive : ' + Fore.BLUE + "C:\\{}\\{} \n".format(folder, file_pick))
              print(Fore.WHITE + "Read the contents, type continue to start the next task or type back to go back to the C:\\ drive\n")
              print(Fore.BLUE + "File Contents :")
              print(Fore.WHITE + '\n' + file1[file_pick.lower()])
              print(Fore.BLUE + '\n << Back <<\t\t>> Continue >>')

            except Exception:
              print(Fore.RED + "Invalid file name")
              time.sleep(2)
              break
            
            file_fin = input(Fore.GREEN + 'Make a selection : ')
            
            if file_fin.lower() == 'back':
              if folder == 'Folder1':
                folder1 = True

              elif folder == "Folder2":
                folder2 = True

              elif folder == "Folder3":
                folder3 = True

              break

            elif file_fin.lower() == "continue":
              next = True
              self.enterPin(name=self.name, typing_speed=self.speed)

  def getDrive(self, name, typing_speed):
    time.sleep(3)
    clear()
    i = 0
    baseHp = 100
    wallHp = 200
    
    while i < 1:
      clear()
      print(Fore.GREEN + "Your HP : {}".format(baseHp))
      print(Fore.RED + "Firewall HP : {}\n".format(wallHp))
      print(Fore.WHITE + "Options : ")  
      print("(1) Attack")
      print("(2) Defend")
      print("(3) DDOS ;)\n")
      select1 = input(Fore.GREEN + "Make a selection: ")

      if select1 == '3':
        clear()
        flushType(text="To my suprise that worked... You now have access to Donald's C Drive...\n", speed=self.speed, color='green')
        time.sleep(2)
        print(Fore.YELLOW + 'You gained an achievement : Script Kiddie')
        achievement.append("Script Kiddie")
        time.sleep(2)
        clear()
        self.files(name=self.name, speed=self.speed)
        return

      elif select1 == '2':
        clear()
        flushType(text="\nYou will now take less damage...", speed=self.speed, color='green')
        time.sleep(2)
        clear()
        damage = None
        damage = random.randint(25, 50)
        damageX = damage * 0.62 
        damage = damage - damageX
        baseHp = baseHp - damage
        if baseHp < 0:
          print(Fore.RED + "\nYou were caught red handed and now the police know where you are..\n")
          time.sleep(2)
          self.copEnding(name=self.name)
          return
        print(Fore.RED + "\nThe firewall attacked and did {} damage...".format(damage))
        time.sleep(2)

      elif select1 == '1':
        clear()
        damd = None
        damd = random.randint(50, 100)
        wallHp = wallHp - damd
        print(Fore.GREEN + "\nYou dealt {} damage.".format(damd))
        time.sleep(2)
        if wallHp < 0:
          clear()
          print(Fore.GREEN + "The firewall is down. Going into the C: Drive...")
          time.sleep(2)
          clear()
          self.files(name=self.name, speed=self.speed)
          return
        time.sleep(2)
        clear()
        damage = random.randint(25, 50)
        baseHp = baseHp - damage
        print(Fore.RED + "\nThe firewall attacked and did {} damage...".format(damage))
        time.sleep(2)
        if baseHp < 0:
          print(Fore.RED + "\nYou were caught red handed and now the police know where you are..\n")
          time.sleep(2)
          self.copEnding(name=self.name)
          return

gameplay = Gameplay(name, typing_speed)
gameplay.getDrive(name=name, typing_speed=typing_speed)
