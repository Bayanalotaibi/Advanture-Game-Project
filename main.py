import time
import random
'''This game is about player journey to his/her deputy
ceremony at the king Palace in the Great Island,
an Island controled by the villin (king servent)
who tries to stop player from attending the ceremony
by controling the enviorment of the great Island
Defind lists and functions, Lists, the start of the game choices'''
# Roads Leading to the Palace
roads = ['Sea Road', 'Forest Road']  # 'Sky Road', 'Valley Road']
# Random Environment
randomEnvironment = ["Thunder Storm", "Forest Fire", "Over Clouds", "SandStorm"]
# A shell will be randomly selected and you have one  change to change it so it suits the environment
shell = ["Fire Shell", "Water Shell", "Air Shell"]  # "Earth Shell",'''
# Game Outputs/Results
Results = ["won", "Lost"]
# Functinos


def printTime(message):
    print(message)
    time.sleep(1)


def invalid():
    print ("invalid input, please try again!")
    print ("")
    print (restarting())


def restarting():
    restart = input('Play Again ? (yes/no)\n\n').lower()
    if restart == "yes":
        Play()
    else:
        exit()


def Play():  # Game
    print(starter())

# Game Introducation
print("Welcome to the Game of Advanture\n\n")
time.sleep(2)
print("The Game of thrill and mystory takes you to a world of fun and thrill\n\n")
time.sleep(2)
print("You were named the deputy of the crown, and you need to reach the King's"
      "Palace on the day of the ceremony to become the next King!\n\n")
time.sleep(2)
print("\nThe King's Palace Located in the Great Island,\nthere are multiple ways "
     "leads to the Palace.... \nBut be careful, there are people who don't want you "
     "there, \nand they will not allow you to be the next king,using your\nshell "
     "try finding a safer road for your journey\n\n")
time.sleep(5)


# Game Start
def starter():
    inputing = input("Are you Ready to Start the Game ? (yes/no)\n\n").lower()
    if inputing.lower() == "yes":
        inputing = input("""You Are on Your Way to your deputy ceremony at the king Palace
        choose your road:
        -1 sea
        -2 forest
        -3 sky
        -4 valley\n
          """).lower()
        if inputing == "1":
            storyDirection = random.choice(randomEnvironment)
            print(storyDirection)
            inputing = ""
            inputing = input()
            inputing = input("""you are in your way to the Palace and you know the villin is waiting for you.
            choice:
            -1 Enter ther Great Island
            -2 Leave the Island
            """).lower()
            if inputing == "1":
            inputing = input("Your Shell is " + random.choice(shell) + " (to preced click Enter)")
            inputing = ""
            inputing = input("Do you want to change your shell ?(yes/no)\n").lower()
            if inputing.lower() == "yes":
            inputing = input("Your Shell is " + random.choice(shell) + " (to preced click Enter)")
            inputing = ""
            else:
                inputing = input("You Are Heading to the Palace using the choosen road and you have the protuction shell, your journey has strted (to preced click Enter)")
            time.sleep(1)
            print("you are facing challenging situation...")
            inputing = input("The villin is using his all almight to block your way, want to change the plan ? (yes/no)\n").lower()
            if inputing.lower() == "yes":
            inputing = input("""You are facing death.
              choice your plan
              -1 stop and withindraw
              -2 change route
              -3 continue the journey
              -4 throw shell and travel lighter
                """).lower()
            if inputing == "1":
                        story = print (random.choice(Results))
                        printTime("")
                        Print("You have Arraived and now you can be the next King")
                        printTime("")
                        print("You Win")
                        printTime("")
                        print(restarting())
            elif inputing == "2":
                        story = print (random.choice(Results))
                        printTime("")
                        Print("You have been injerd and need to rest")
                        printTime("")
                        print("You Lost")
                        printTime("")
                        print(restarting())
            elif inputing == "3":
                        story = print (random.choice(Results))
                        printTime("")
                        Print("You have made it you are the next king")
                        printTime("")
                        print("You Win")
                        printTime("")
                        print(restarting())
            elif inputing == "4":
                        story = print (random.choice(Results))
                        printTime("")
                        Print("You have died")
                        printTime("")
                        print("You Lost")
                        printTime("")
                        print(restarting())
            else:
                print("You have died!")

        elif inputing == "2":
            storyDirection = random.choice(randomEnvironment)
            print(storyDirection)
            inputing = ""
            inputing = input()
            inputing = input("""you are in your way to the Palace and you know the villin is waiting for you.
            choice:
            -1 Enter ther Great Island
            -2 Leave the Island
            """).lower()
            if inputing == "1":
            inputing = input("Your Shell is " + random.choice(shell) + " (to preced click Enter)")
            inputing = ""
            inputing = input("Do you want to change your shell ?(yes/no)\n").lower()
            if inputing.lower() == "yes":
            inputing = input("Your Shell is " + random.choice(shell) + " (to preced click Enter)")
            inputing = ""
            else:
                inputing = input("You Are Heading to the Palace using the choosen road and you have the protuction shell, your journey has strted (to preced click Enter)")
            time.sleep(1)
            print("you are facing challenging situation...")
            inputing = input("The villin is using his all almight to block your way, want to change the plan ? (yes/no)\n").lower()
            if inputing.lower() == "yes":
            inputing = input("""You are facing death.
              choice your plan
              -1 stop and withindraw
              -2 change route
              -3 continue the journey
              -4 throw shell and travel lighter
                """).lower()
            if inputing == "1":
                        story = print (random.choice(Results))
                        printTime("")
                        Print("You have Arraived and now you can be the next King")
                        printTime("")
                        print("You Win")
                        printTime("")
                        print(restarting())
            elif inputing == "2":
                        story = print (random.choice(Results))
                        printTime("")
                        Print("You have been injerd and need to rest")
                        printTime("")
                        print("You Lost")
                        printTime("")
                        print(restarting())
            elif inputing == "3":
                        story = print (random.choice(Results))
                        printTime("")
                        Print("You have made it you are the next king")
                        printTime("")
                        print("You Win")
                        printTime("")
                        print(restarting())
            elif inputing == "4":
                        story = print (random.choice(Results))
                        printTime("")
                        Print("You have died")
                        printTime("")
                        print("You Lost")
                        printTime("")
                        print(restarting())
            else:
                print("You have died!")

        elif inputing == "3":
            storyDirection = random.choice(randomEnvironment)
            print(storyDirection)
            inputing = ""
            inputing = input()
            inputing = input("""you are in your way to the Palace and you know the villin is waiting for you.
            choice:
            -1 Enter ther Great Island
            -2 Leave the Island
            """).lower()
            if inputing == "1":
            inputing = input("Your Shell is " + random.choice(shell) + " (to preced click Enter)")
            inputing = ""
            inputing = input("Do you want to change your shell ?(yes/no)\n").lower()
            if inputing.lower() == "yes":
            inputing = input("Your Shell is " + random.choice(shell) + " (to preced click Enter)")
            inputing = ""
            else:
                inputing = input("You Are Heading to the Palace using the choosen road and you have the protuction shell, your journey has strted (to preced click Enter)")
            time.sleep(1)
            print("you are facing challenging situation...")
            inputing = input("The villin is using his all almight to block your way, want to change the plan ? (yes/no)\n").lower()
            if inputing.lower() == "yes":
            inputing = input("""You are facing death.
              choice your plan
              -1 stop and withindraw
              -2 change route
              -3 continue the journey
              -4 throw shell and travel lighter
                """).lower()
            if inputing == "1":
                        story = print (random.choice(Results))
                        printTime("")
                        Print("You have Arraived and now you can be the next King")
                        printTime("")
                        print("You Win")
                        printTime("")
                        print(restarting())
            elif inputing == "2":
                        story = print (random.choice(Results))
                        printTime("")
                        Print("You have been injerd and need to rest")
                        printTime("")
                        print("You Lost")
                        printTime("")
                        print(restarting())
            elif inputing == "3":
                        story = print (random.choice(Results))
                        printTime("")
                        Print("You have made it you are the next king")
                        printTime("")
                        print("You Win")
                        printTime("")
                        print(restarting())
            elif inputing == "4":
                        story = print (random.choice(Results))
                        printTime("")
                        Print("You have died")
                        printTime("")
                        print("You Lost")
                        printTime("")
                        print(restarting())
            else:
                print("You have died!")

        elif inputing == "4":
            storyDirection = random.choice(randomEnvironment)
            print(storyDirection)
            inputing = ""
            inputing = input()
            inputing = input("""you are in your way to the Palace and you know the villin is waiting for you.
            choice:
            -1 Enter ther Great Island
            -2 Leave the Island
            """).lower()
            if inputing == "1":
            inputing = input("Your Shell is " + random.choice(shell) + " (to preced click Enter)")
            inputing = ""
            inputing = input("Do you want to change your shell ?(yes/no)\n").lower()
            if inputing.lower() == "yes":
            inputing = input("Your Shell is " + random.choice(shell) + " (to preced click Enter)")
            inputing = ""
            else:
                inputing = input("You Are Heading to the Palace using the choosen road and you have the protuction shell, your journey has strted (to preced click Enter)")
            time.sleep(1)
            print("you are facing challenging situation...")
            inputing = input("The villin is using his all almight to block your way, want to change the plan ? (yes/no)\n").lower()
            if inputing.lower() == "yes":
            inputing = input("""You are facing death.
              choice your plan
              -1 stop and withindraw
              -2 change route
              -3 continue the journey
              -4 throw shell and travel lighter
                """).lower()
            if inputing == "1":
                        story = print (random.choice(Results))
                        printTime("")
                        Print("You have Arraived and now you can be the next King")
                        printTime("")
                        print("You Win")
                        printTime("")
                        print(restarting())
            elif inputing == "2":
                        story = print (random.choice(Results))
                        printTime("")
                        Print("You have been injerd and need to rest")
                        printTime("")
                        print("You Lost")
                        printTime("")
                        print(restarting())
            elif inputing == "3":
                        story = print (random.choice(Results))
                        printTime("")
                        Print("You have made it you are the next king")
                        printTime("")
                        print("You Win")
                        printTime("")
                        print(restarting())
            elif inputing == "4":
                        story = print (random.choice(Results))
                        printTime("")
                        Print("You have died")
                        printTime("")
                        print("You Lost")
                        printTime("")
                        print(restarting())
            else:
                print("You have died!")

        else:
            print(invalid())
    elif inputing.lower() == "no":
        print('Comeback Once you are ready\n')
        printTime("")
        print('You are leaving the game...\n')
        printTime("")
        print('Bye, till the next time!')
    else:
        print(invalid())
Play()
