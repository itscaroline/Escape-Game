#-------------------------------------------------------------------------------
# Name:        Adventure_Game_The_Mysterious_Mansion
# Purpose: To create an interactive chose-your-own adventure type game
#
# Author:      Caroline Chen
##-------------------------------------------------------------------------------

#Append rooms into room list
room_list = []

#Room 0 description
room = (["You are in the Grand Entrance. There is a passage to the North.", 2, None, None, None])
room_list .append(room)

#Room 1 description
room = (["You are in the Lavatory. There is a passage to your North and East.", 4, 2, None, None])
room_list .append(room)

#Room 2 description
room = (["You are in the South Hall. There is a passage in all directions.", 5, 3, 0, 1])
room_list .append(room)

#Room 3 description
room = (["You are in the Library. There is a passage to your North and West.", 6, None, None, 2])
room_list .append(room)

#Room 4 description
room = (["You are in the West Chamber. There is a passage to your East and South.", None, 5, 1, None])
room_list .append(room)

#Room 5 description
room = (["You are in the Central Hall. There is a passage in all directions.", 7, 6, 2, 4])
room_list .append(room)

#Room 6 description
room = (["You are in the East Chamber. There is a passage to your South and West.", None, None, 3, 5])
room_list .append(room)

#Room 7 description
room = (["You are in the Spiral Staircase. There is a passage to your North and South.", 9, None , 5 , None])
room_list .append(room)

#Room 8 description
room = (["You are in the Cellar. There is a passage to your North and East.", 11, 9, None, None])
room_list .append(room)

#Room 9 description
room = (["You are in the North Hall. There is a passage to your East, South and West.", None, 10, 7, 8])
room_list .append(room)

#Room 10 description
room = (["You are in the Attic. There is a passage to your North.", 12, None, None, 9 ])
room_list .append(room)

#Room 11 description
room = (["You are in the Secret Room. There is a passage to your South.", None, None, 8, None ])
room_list .append(room)

#Room 12 description
room = (["You are in the Dungeon.", None, None, None, None ])
room_list .append(room)


#List of items
i_list = []
books = (["Library: Room 3", "The Lord of the Flies Book", "Julius Caesar Book", "Eleanor & Park Book"])
i_list.append(books)

items = (["Items", "Mini Pig Figurine", "Crystal Ball", "Comics"])
i_list.append(items)

hints = (["Hints Items", "Fire Wood", "Political Newspaper", "Car Manual"])
i_list.append(hints)


#Defining fuctions for interactive elements for each room
#Introduction Statements:
def intro():
    print"Welcome to the Adventure Game!\nYou were hitch hiking in the Forest of Freedom when you spot a trail of dark cloked figures rush into a clearing."
    print "You immediately follow them into the clearing to find a house. You see a shadowy figure dart into the house. You decide to follow.\n"
    print '''

                .-'     '-.
     _______ .'    __/  / '.      ___________
       ___ ____    \/`-/    \  __________________
     __ _____      /) /      ;  _____ ---- _____
     ____  |       /_\\      |
           ;       _///      ;
            \     /_|      _/_
             '.   ______  |__||  ____
     _______   '-/\     `-|__||___________
    ____ ___    /__\      |__|| _______ ______
    ___        /____\     |__||      _______
              /___   \    |__||\
             /____`-.-\   |__|| \
            /___ __ ___\  |__|/  \       _________
           /____| /|____\         \    ___  ______
          /__   |_\|`.___\         \  ____ ____ ___
         /___`-.| <|______\         \
        /__.-' _|__|_______\        _\_      __
       /__________________  \ ..--""   `--.-' /\
        /                 / /"               //\\
       /_________________/.|________________/ //\\
    ___||_ __ __ __ _ _||_ |_-__ _ __ _ __.-|/|/|_____
       ||_|  |__|\ |_| || ||_| >|_|  |_| _|_|||/|
       ||_|__|__| ||_|_||_||_|/_|_|__| |< |_||//|
       ||_|< |__|.||_| || ||_|  |_|  |_|_\|_| //
       ||_|_\|__| ||_|_||_||\|_/|_|__|_|__|_|//
       ||_______|_||___||__|________________|/
       || / / / / / / /||//|________________|jro
      /||/_/_/_/_/_/_/_||/ /         _
      |__________________|/

      '''

    print " *** The Adventure has began ***\n "
    r_name = raw_input("What is your name?")
    name =r_name.capitalize()
    print "Welcome,", name, ", to the Mysterious Mansion."
    print '''When you enter you feel eyes watching your every step.\nYou have entered the Grand Entrance. Sounds can be heard in whispers. It's pitch black too. '''
    print "Luckily, you have a glow in the dark compass, but you can only go north(n), east(e), south(s) or west(w)"\

#printing inventory in list
def printI():
    print "In your bag you have:"
    for i in range(len(inventory)):
        print "{0}. {1}\n" .format(i+1, inventory[i])

#Lavatory
def lavatory():
    #items
    a = raw_input("You have found something.\nOK")
    inventory.append(i_list[2][1])
    printI()

    #Note
    print "\nYou find a note."
    raw_a = raw_input("Pick up note?")
    a =raw_a.upper()
    if a == 'YES' or 'Y':
        print "\"Find you way past the Cellar. There is something there waiting for you.\" "

#South Hall
def sHall():
    print "\nYou walk into a giant spider web. Suddendly, an enormous tarantula crawls towards."

    #question
    r_ans = raw_input("You deside to:\n(R) Run or (C) Continue:")
    answer = r_ans.upper()
    #print answer

    if answer == 'R' or 'RUN':
        #answer == True
        print "You have escaped the tarantula"

    elif answer == 'C' or 'Continue':
        #answer == False
        print "You have been eaten by the tarantula.\n ***Try Again***"
        #break
    else:
        None

#Library
def library():
    #Book collection
    a = raw_input("You have found a book.\nOK")
    if score >= 0 and score <= 4:
        inventory.append(i_list[0][1])
    elif score > 4 and score <=8:
        inventory.append(i_list[0][2])
    elif score > 4:
        inventory.append(i_list[0][3])
    else:
        print "Else"

    printI()

    #note
    print "\nA book falls from the shelf. A piece of paper slips out."
    raw_a = raw_input("Pick up note?")
    a =raw_a.upper()
    if a == 'YES' or 'Y':
        print "\"Go to ...........\"[the note is ripped] "

#West Chamber
def wChamber():
    a = raw_input("You have found something.OK")
    inventory.append(i_list[1][1])
    printI()

    #note
    print "\nThere is a yellow sticky note on the wall."
    raw_a = raw_input("Pick up note?")
    a =raw_a.upper()
    if a == 'YES' or 'Y':
        print " [note is ripped]\" not west, not south, not east of the......\"[note is ripped]"

#Central Hall
def cHall():
    print "The floor creaks as you walk.Your hear a thump."
    a = raw_input("You have found something.\nOK")
    inventory.append(i_list[1][2])
    printI()


#East Chamber
def eChamber():
    a = raw_input("You have found something.\nOK")
    inventory.append(i_list[1][3])
    printI()

    #note
    print "\nThere is a pink sticky note on the wall."
    raw_a = raw_input("Pick up note?")
    a =raw_a.upper()
    if a == 'YES' or 'Y':
        print "\"Go past the Attic. There will be something you should see.\" "

#North Hall
def nHall():
    a = raw_input("You have found something.\nOK")
    inventory.append(i_list[2][2])
    printI()

    #note
    print "\nYou have entered the second floor of the mansion. The floor creaks as you walk."

#Stair Case
def sCase():
    #question
    print "Portraits are hung along the wall.You feel them watching you as you move."
    print "\nSuddenly, a black cat jumps out and attacks you."
    r_ans = raw_input("You deside to:\n(R) Run or (C) Continue:")
    answer = r_ans.upper()

    #troubleshoot
    #print answer

    if answer == 'R' or 'RUN':
        #answer == True
        print "You have escaped the cat."

    elif answer == 'C' or 'Continue':
        #answer == False
        print "You have been eaten by the cat.\n ***Try Again***"
        #break
#Cellar
def cellar():
    print "Dust sweaps accross your face. Mysterious items fill the room."
    raw_a = raw_input("Continue exploring room?")
    a =raw_a.upper()
    if a == 'YES' or 'Y':
        print '''

         (                                (
                )           )        (                   )
              (                       )      )            .---.
          )              (     .-""-.       (        (   /     \
         ( .-""-.  (      )   / _  _ \        )       )  |() ()|
          / _  _ \   )        |(_\/_)|  .---.   (        (_ 0 _)
          |(_)(_)|  ( .---.   (_ /\ _) /     \    .-""-.  |xxx|
          (_ /\ _)   /     \   |v==v|  |<\ />|   / _  _ \ '---'
           |wwww|    |(\ /)|(  '-..-'  (_ A _)   |/_)(_\|
           '-..-'    (_ o _)  )  .---.  |===|    (_ /\ _)
                      |===|  (  /     \ '---'     |mmmm|
                      '---'     |{\ /}|           '-..-'
                                (_ V _)
                                 |"""|
                                 '---'

                                 '''
        print "\"Look where the books are.\" "

    else:
        print "It mysteriously disappeared"


#Attic
def attic():
    print "\nA gust of stale air blew by.Then, you hear a sudden burst of shrieking. "
    raw_a = raw_input("Continue exploring room?")
    a =raw_a.upper()
    if a == 'YES' or 'Y':
        print
        '''


        /\                 /\
       / \'._   (\_/)   _.'/ \            =/\                 /\=
      /_.''._'--('.')--'_.''._\           / \'._   (\_/)   _.'/ \
      | \_ / `;=/ " \=;` \ _/ |          / .''._'--(e.e)--'_.''. \
       \/ `\__|`\___/`|__/` \/          /.' _/ |`'=/ " \='`| \_ `.\
        `      \(/|\)/      `          /` .' `\;-,'\___/',-;/` '. '\
                " ` "                 /.-'       `\(/V\)/`       `-.\
            ,   ,_,   ,               `            "   "            `
           / `'=) (='` \       (,_    ,_,    _,)
          /.-.-.\ /.-.-.\      /|\`-._( )_.-'/|\
          `     `V`     `     / | \`-'/ \'-`/ | \
                             /__|.-'`-\ /-`'-.|__\


        '''
        print "Your an old womens voice,\"In the chamberto the north, we are going to test your worth. \" "

    else:
        print "It mysteriously disappeared"

#Secret Room
def sRoom():
    a = raw_input("You have found something.\nOK")
    inventory.append(i_list[2][3])
    printI()

    #note
    print "\"Dear,", name, "Check the room north of the attic.\n~ Anonymous\" "


#Dungeon function defined
def dungeon():
    a = raw_input("OH NO!!")
    print "\n The door suddenly closes behind you.\nYou are trapped.\n"
    print '''Someone walks in behind you and you feel a sudden shreak of coldness around your neck.\nA dagger
    \nThe person behind says:\"You have 30 seconds to answer\" '''
    print "\n.......................................\n.......................................\n......................................."

    raw_answer = raw_input("Are you ready?")
    answer = raw_answer.upper()

    if answer == "YES":
        print "\nCongratulation!\nYou have successfully completed the Adventure\nYour score was,",score
        print "You collected:"
        for i in range(len(inventory)):
            print "{0}. {1}\n" .format(i+1, inventory[i])
        print "It is a challenging game, so give yourself a pat on the back.\n\n"
        print '''



 #_                               THANK YOU                                d
 ##_                            for playing :)                            d#
 NN#p                                                                  j0NN
 40NNh_                                                              _gN#B0
 4JF@NNp_                                                          _g0WNNL@
 JLE5@WRNp_                                                      _g@NNNF3_L
 _F`@q4WBN@Np_                                                _gNN@ZL#p"Fj_
 "0^#-LJ_9"NNNMp__                                         _gN#@#"R_#g@q^9"
 a0,3_j_j_9FN@N@0NMp__                                __ggNZNrNM"P_f_f_E,0a
  j  L 6 9""Q"#^q@NDNNNMpg____                ____gggNNW#W4p^p@jF"P"]"j  F
 rNrr4r*pr4r@grNr@q@Ng@q@N0@N#@NNMpmggggmqgNN@NN@#@4p*@M@p4qp@w@m@Mq@r#rq@r
   F Jp 9__b__M,Juw*w*^#^9#""EED*dP_@EZ@^E@*#EjP"5M"gM@p*Ww&,jL_J__f  F j
 -r#^^0""E" 6  q  q__hg-@4""*,_Z*q_"^pwr""p*C__@""0N-qdL_p" p  J" 3""5^^0r-
   t  J  __,Jb--N""",  *_s0M`""q_a@NW__JP^u_p"""p4a,p" _F""V--wL,_F_ F  #

'''
    else:
        print '''
        \n
        "THAT IS THE WRONG ANSWER!!!!
        You will suffer the consequences" said the voice.

        The light suddenly turned on.
        Before you can see anything clearly.......

        You have died.


       *** Game Terminated ***
          Please Try Again

'''
#Main Program
intro()

#Initialize current room variable
done = False
inventory = []
current_room = 0
score = 0


#Loop the game
while done != True:

    #User Input
    predirection = raw_input("Which way do you want to go?")
    direction = predirection.lower()

    #Directions linking to rooms
    #Directions North
    if direction == 'n' or direction == 'north':

        #next_room = room_list
        next_room = room_list[current_room][1]

        if next_room == None:
            print  "You can't go that way."

        else:
            current_room = next_room
            print room_list[current_room][0]

    #Direction East
    elif direction == 'e' or direction == 'east':

        next_room = room_list[current_room][2]

        if next_room == None:
            print  "You can't go that way."

        else:
            current_room = next_room
            print room_list[current_room][0]

    #Direction South
    elif direction == 's' or direction == 'south':
        print room_list[current_room][0]

        next_room = room_list[current_room][3]
        if next_room == None:
            print  "You can't go that way."

        else:
            current_room = next_room
            print room_list[current_room][0]

    #Direction West
    elif direction == 'w' or direction == 'west':
        print room_list[current_room][0]

        next_room = room_list[current_room][4]
        if next_room == None:
            print  "You can't go that way."

        else:
            current_room = next_room
            print room_list[current_room][0]
    else:
       print "Invalid direction. Please try again"


    #Calling interactive room elements
    if current_room == 1:
        lavatory()
        score += 1

    elif current_room == 2:
        answer = None
        sHall()

    elif current_room == 3:
        library()
        score += 1

    elif current_room == 4:
        wChamber()
        score += 1

    elif current_room == 5:
        cHall()
        score += 1

    elif current_room == 6:
        eChamber()
        score += 1

    elif current_room == 7:
        sCase()
        score += 1

    elif current_room == 8:
        cellar()
        score += 1

    elif current_room ==9:
        nHall()
        score += 1

    elif current_room == 10:
        attic()
        score += 1

    elif current_room == 11:
        sRoom()
        score += 1

    elif current_room == 12:
        dungeon()
        break

    else:
        None
