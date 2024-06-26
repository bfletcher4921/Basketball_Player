# Author: Brandi Fletcher
# Section: CIS 225 01 
# Date: 11/16/23
# File: bplayer_app.py
'''Create a program to test your class. Name this separate file 
bplayer_app.py and at the top import your BaseballPlayer class. 
Inside the main function (be sure to use the homework_program.py template) 
create three objects instantiated from the class. Go to roarlions.com and 
choose three current baseball players and use their names, position and 
jersey number to make this a more realistic simulation.

Place the three player objects into a list. Code up three loops. The first 
loop must display each player's name. The second must display jerseys and 
the third displays the positions.

Make sure that if you added a fourth player to your list everything would 
work and display the attributes of all four players. In other words, 
don't hard-code anything (like the fact that your object list has 3 objects).'''

from bplayer import BaseballPlayer
#import BaseballPlayer class
def main():
    #add player1
    player1 = BaseballPlayer()
    player1.name = 'Drew Hudson'
    player1.jersey_number = 2
    player1.position = 'infield'
    
    #add player2
    player2 = BaseballPlayer()
    player2.name = 'Gehrig Frei'
    player2.jersey_number = 4
    player2.position = 'shortstop'
    
    #add player3
    player3 = BaseballPlayer()
    player3.name = 'Kyle Machado'
    player3.jersey_number = 5
    player3.position = 'infield'
    
    #input players into list
    players = [player1, player2, player3]
    #print each player in list 
    print("Player names:")
    for i in players:
        print(i.name)
    print()
    print("Player numbers:")
    for j in players:
        print(j.jersey_number)
    print()
    print("Player positons")
    for k in players:
        print(k.position)
main()