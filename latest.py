#!/usr/bin/env python
import random

def main():
    """Start a genre of music guessing game."""
    print("Guess the genre!")
    
    genre = [
        
         "classic music", 
         "jazz",
         "rock music",
         "hip hop music",
         "rhythm and blues",
         "electronic dance music"
         ]

    
    x = random.choice(genre)
    guess=None
    
    while x != guess:
         
      
     max_trial=4
    trial =0
    score=100
    while trial<max_trial:
        guess = int(input('Guess a genre:'))
        max_trial += 1
        score +=20
        if x ==guess:
            print('Congratulations! You won!')
            break
    else:
        print('sorry you lost')        
       
main()

        
    
