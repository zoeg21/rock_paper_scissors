#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 21:39:49 2017

This program is a basic rock, paper, scissors game that allows a user
to continue playing against the computer until they wish to stop.
@author: Zoe Gordin
"""
import random
class RPS(object):
   

    def __init__(self):
         self.compWins = 0
         self.userWins = 0
         self.tieCount = 0
         self.winner = ""
    """generates a random throw between rock, paper, and scissor
    indicated by r s or p"""
    def RandomThrow():
        throwChoices = ['r', 'p', 's']
        whichThrow = random.randint(0,2)
        return throwChoices[whichThrow]

    def setComputerThrow():
        compThrow = RPS.RandomThrow()
        return compThrow

    def setUserThrow():
        userThrow = input('What would you like to throw? ')
        userThrow.lower
        if(userThrow!='r' and userThrow!='p' and userThrow!='s'and userThrow!='z'):
            print(userThrow)
            userThrow = input('Please enter a valid throw: r, p, s, or z. ')
        return userThrow
        
    def printRules():
        print('Here are the rules of the game: scissor cuts paper,'+
              'paper covers rock, and rock crushes scissors.')
        print('Play either "r" for rock, "p" for paper, or "s" for scissors.' )
        print('If you want to stop playing, enter a "z".')
            
    def findWinner(self,uThrow, cThrow):
        #this 2D array stores all combinations of of throws, excepting ties
        #it will be used to succinctly determine whether the user or the computer has won
        triumph = {'r':{'p':0, 's': 1}, 'p':{'r': 1, 's': 0}, 's':{'r': 0, 'p':1}}
        
    
        if(cThrow == uThrow):
            self.winner = "It's a tie!"
            self.tieCount+=1
        else:
            if(triumph[uThrow][cThrow] == 0):
                self.compWins+=1
                self.winner = 'Computer won!'
            else:
                self.userWins+=1
                self.winner = 'User won!'
        return self.winner
    
    def winStats(self):
        total = (self.userWins + self.compWins + self.tieCount)
        userPercent = (self.userWins/total) * 100.0
        tiePercent = (self.tieCount/total) * 100.0
        print('user won {0:.2f}'.format(userPercent) +'% of the games, and {0:.2f}'.format(tiePercent)+'% of the games were ties.')
        print("The computer, playing randomly, tends to win more than a human user due to a user's attempt to use strategy, so don't feel bad about losing!")
        print("Ties should be about 1/5 of the total number of rounds, but will probably end up being less.")
   
    
    def main(self): 
        RPS.printRules()
        user = RPS.setUserThrow()
        #loop iterates, continuing the game until the user wants to stop
        while(user!='z'):
            print('You threw: %s'%user)
            computer = RPS.setComputerThrow()
            print('The computer threw: %s'%computer)
            win = self.findWinner(user, computer)
            print(win)
            user = RPS.setUserThrow()
            
        print("You won %d"%self.userWins + " time(s).")
        print("The computer won won %d"%self.compWins + " time(s).")
        print("you tied %d"%self.tieCount + " time(s).")
        self.winStats()
        print("Thanks for playing!")
rps = RPS()
rps.main()

            
          
        
        
        
        
    
    
    


