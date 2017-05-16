#!/usr/bin/env python2

#Rock Paper Scissors lizard spock

import random  # determine what move the computer will throw
import time # utilize dates and times

#set each move as a variable to a number
rock = 1
paper = 2
scissors = 3
lizard = 4
spock = 5

#text representation of rules
names = { rock: "Rock", paper: "Paper", scissors: "Scissors", lizard: "Lizard", spock: "Spock" }
rules = { rock: scissors, paper: rock, scissors: paper, lizard: spock, spock: scissors, scissors: lizard, lizard: paper, paper: spock, spock: rock }

# set variable to keep track of scores
player_score = 0
computer_score = 0

# start game;; start a while loop that will allow us to play the game
def start():
    print "Let's play a game of Rock, Paper, Scissors, Lizard, Spock"
    print "\n"
    print "Here are the Rules...\nAs Sheldon explains:\nScissors cuts paper, Paper covers rock, Rock crushes lizard,"
    print "Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper,"
    print "Paper disproves Spock, Spock vaporizes Rock, and as it always has, Rock crushes Scissors."
    while game():
        pass
    scores()

# called upon from above start function
# determines player move by calling move function below
def game():
    player = move()
    computer = random.randint(1, 5) #sets computer move to get an int between 1 and 5
    result(player, computer) # then passes player and computer move, stored as int onto result function
    return play_again()

# obtain an integrer from player
# the while loop accounts for the player making an unsupported entry
# we are setting player variable to be created with raw_input
def move():
    while True:
        print
        player = raw_input("Rock = 1\nPaper = 2\nScissors = 3\nLizard = 4\nSpock = 5\nMake a move: ")
        try:
            player = int(player)
            if player in (1,2,3,4,5): # proper error handling
                           return player
        except ValueError:
                           pass
        print "Mere Mortal!! You are supposed to enter 1,2,3,4 or 5!"
                           

def result(player, computer):
        print "1...."
        time.sleep(1)
        print "2...."
        time.sleep(2)
        print "Computer picked {0}!".format(names[computer]) # {0}wil be printed text of computers move
        global player_score, computer_score # calling scores we set earlier; global allows variable to be used changed outside of function
        if player == computer:
            print "Tie Game!"
        else:
            if rules[player] == computer: #use rules list from earlier to see if losing move to the player's move is the same as computers
                           print "You victory is assured, Captain"
                           player_score += 1 # add one to the player score variable
            else:
                           print "The Computer laughs at you; as you realize you have been defeated"
                           computer_score += 1

def play_again():
        answer = raw_input("Would you like to play again? y/n: ")
        if answer in ("y", "Y", "yes", "Yes", "Hell yes"):
                           return answer
        else:
                           print "Next, time then, Human!"

def scores():
                           global player_score, computer_score
                           print "HIGH SCORES"
                           print "Player: ", player_score
                           print "Computer: ", computer_score

# allows for script to be run from command line + can be called from other code
if __name__ == '__main__':
                           start()
                           

