

# Jerome 
# Sight reading generator
# May 29th 2024
# this program uses text and input to get data from user about music related things and it gives musicains a place to warm up and and improve their skill by sight reading



# import cv2 and music 21 for making the sheet music 
import music21
import random 
import sys
import cv2
import numpy as np
from music21 import *
# variables 





# introduction funciton 
def intro():
    print("Hello and welcome to my sight reading generator")

  # introduces how things work and how to interact with the progroam 
    print("this program uses just text and typing for inputs")

  # asks user if they want to start the program or not
    Userint = input("would you like to start yes or no").lower()
    # quits the progroam if no
    if Userint == "no":
        sys.exit()
    # anything else goes to menu 
    else:
        menu()


# menu/parameters function 
def menu():
    # global to use these variables later in other functions when needed
    global  Userkey, Usertime, Userskill, UserIns
    print("This is the menu where you pick your parameters!")

  # ask user for the parameters they want to use 

  # what instrument do you play?
    print("What Instrument do you play?")
    print("Here are options")
    print("Alto sax, tenor sax, trumpet, piano, clarinet, Tromebone")
    UserIns = input(" please type which one as shown ").lower()
     # what time signature are you comfortable with?(4/4, 3/4, 2/4,, etc))
    print(" What time signature would you like? ")
    Usertime = input(" 4/4,  3/4, 2/4 -type as shown").lower()
     # what key signatures(sharps and flats) are you comfortable with?
    print(" What Key signature would you like? ")
    Userint = input(" Sharp  or Flat ? - type as shown").lower()
    if Userint == "sharp":
         Userkey = int(input(" How many sharps, 0-7 "))
    elif Userint == "flat":
        Userkey = int(input(" How many flats, 0-7 "))
    else:
        Userkey = 0
    print("next please rate your skill based of these pieces of music")
    print("Press 'o' to exit images")
    print("top is pro, middle is intermedite and bottom is easy")
  # rate your skill based off images of music being displayed 1-3
    # music links easy -(https://recordersupport.weebly.com/hot-cross-buns.html) intermediate-(https://musescore.com/user/2538606/scores/4455576) "pro-'(https://musescore.com/user/32782471/scores/6789059)
    # load the images 
    img1 = cv2.imread('MUSIC22.png')
    # display the images on screen 
    Hori = np.concatenate((img1),axis=1)
    cv2.imshow('Horizontal',Hori)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    Userskill = input("Pro, Intermediate, Easy").lower()
    # ask if user would like to warm up with scales or rhythm? or go to sight reading?
    print("Would you like to warm up with scales or rhythm or generate music?")
    Userint = input("generate, rhythm, scales").lower()
    # if scales take user to scales function
    if Userint == "scales":
        scales()
            
     # elif rhythm take user to rhythm function 
    elif Userint == "rhythm":
        rhythm()
            
        # else user goes to sight reading function
    else:
        SightReading()





# Scales function 
def scales():
    # Loads scales
    # Clarient scales 
    Clarinetimg1 = cv2.imread('Clarinet_page-00011.png')
    Clarinetimg2 = cv2.imread('Clarinet_page-00022.jpg')
    # Trumpet 
    Trumpetimg1 = cv2.imread('trumpet_page-00011.jpg')
    Trumpetimg2 = cv2.imread('trumpet_page-00022.jpg')
    # tromebone 
    tromeboneimg1 = cv2.imread('tromebone_page-00011.jpg')
    tromeboneimg2 = cv2.imread('tromebone_page-00022.jpg')
    # alto sax
    altosaximg1 = cv2.imread('Altosax_page-00011.jpg')
    altosaximg2 = cv2.imread('Altosax_page-00022.jpg')
    # tenor sax
    tenorsaximg1 = cv2.imread('Tenorsax_page-00011.jpg')
    tenorsaximg2 = cv2.imread('Tenorsax_page-00022.jpg')
    # piano 
    Pianoimg1 = cv2.imread('Pianoscales1.png')

    # if user selcects alto sax they get scales in the key of eb which the alto sax plays in, they get the right scales
    if UserIns == "piano":
        Vert = np.concatenate((Pianoimg1),axis=1)
        cv2.imshow('Vertical',Vert)
        # waitkey means wait for 'o' to be pressed and once presses all windows are destroyed
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif UserIns == "alto sax":
        Vert = np.concatenate((altosaximg1),axis=1)
        Vert2 = np.concatenate((altosaximg2),axis=1)
        cv2.imshow('Vertical',Vert)
        cv2.imshow('Vertical2',Vert2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif UserIns == "tenor sax":
        Vert = np.concatenate((tenorsaximg1),axis=1)
        Vert2 = np.concatenate((tenorsaximg2),axis=1)
        cv2.imshow('Vertical',Vert)
        cv2.imshow('Vertical2',Vert2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif UserIns == "clarinet":
        Vert = np.concatenate((Clarinetimg1),axis=1)
        Vert2 = np.concatenate((Clarinetimg2),axis=1)
        cv2.imshow('Vertical',Vert)
        cv2.imshow('Vertical2',Vert2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif UserIns == "tromebone":
        Vert = np.concatenate((tromeboneimg1),axis=1)
        Vert2 = np.concatenate((tromeboneimg2),axis=1)
        cv2.imshow('Vertical',Vert)
        cv2.imshow('Vertical2',Vert2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        
    elif UserIns == "trumpet":
        Vert = np.concatenate((Trumpetimg1),axis=1)
        Vert2 = np.concatenate((Trumpetimg2),axis=1)
        cv2.imshow('Vertical',Vert)
        cv2.imshow('Vertical2',Vert2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    # once dome with the scales ask user if they want rhythms or sight reading and take them to desired function 
    print("would you like rhythm or generator?")
    Userint = input("Rhythm or Generator")
    if Userint == "rhythm":
        rhythm()
    else:
        SightReading()
    

# rhythm function 

def rhythm():
    print("Here are some rhythm musics to practice")
    # and ask if they want a metronome to play with 

    # display music pieces
    rhythmimg = cv2.imread('rhythm2.png')
    Vert = np.concatenate((rhythmimg),axis=1)
    cv2.imshow('vertical', Vert)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("would you like to sight read or go back to scales?")
    Userint = input("music or scales").lower()
    if Userint == "scales":
        scales()
    else:
        SightReading()

# sight reading function 
def SightReading():
    # generates and displays sheet music based off the parameters the user chose
    # sets the key and time signatures
    sight_reading = stream.Score()
    Key_sig = key.KeySignature(Userkey)
    Time_sig = meter.TimeSignature(Usertime)
    sight_reading.insert(0,Time_sig)

    # these if statements determine amount of bars 
    if Userskill == "pro":
        # quarter, half and eighth notes and 16ths 
        print("pro")
        num_bars = 14
    elif Userskill == "intermediate":
        num_bars = 10
        # quarter, half and eighth notes 
        print("intermediate")
    else:
        num_bars = 8
        print("Easy")
        # is simpiler only quarter  and half notes 
    # loop through untill each bar is filled with notes
    for i in range(num_bars):
        measure = stream.Measure()
        # gives conditions for lopps and once it runs though it displays made sheet music
        for k in range(random.randint(4,8)):
            note_value = random.choice([0.25, 0.5,])
            note_pitch_value = random.choice((Key_sig).getScale().getPitches())
            note_ob = note.Note(note_pitch_value)
            note_value_ob = duration.Duration(note_value)
            measure.append(note_ob)
        # adds the measure to the score is like a list it holds measures and notes
        sight_reading.append(measure)
        # displays the music
    sight_reading.show()



 




intro()
