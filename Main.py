#############################################
# Name: Noorina Karimi
# Class: ICS3C
# Date: Friday Sept. 25
# Project Name: Week4Tournament
#
# Project Description: See the README file
#############################################

# THIS IS WHERE YOU CODE
print("Welcome to Week4Tournament!")
print("Your host today is Noorina so be sure to sit tight and give good answers.")
#Read in team 1 name
print("What is team 1? ")
team1 = input()
#Read in team 1 wins
print("How many wins does team 1 have? ")
wins1 = int(input())
#Read in team 1 losses
print("How many losses does team 1 have? ")
losses1 = int(input())
#Read in team 1 ties
print("How many ties does team 1 have? ")
ties1 = int(input())
#Read in team 2 name
print("What is team 2? ")
team2 = input()
#Read in team 2 wins
print("How many wins does team  2 have? ")
wins2 = int(input())
#Read in team 2 losses
print("How many losses does team  2 have? ")
losses2 = int(input())
#Read in team 2 ties
print("How many ties does team  2 have? ")
ties2 = int(input())
#Read in team 3 name
print("What is team 3? ")
team3 = input()
#Read in team 3 wins
print("How many wins does team  3 have? ")
wins3 = int(input())
#Read in team 3 losses
print("How many losses does team  3 have? ")
losses3 = int(input())
#Read in team 3 ties
print("How many ties does team  3 have? ")
ties3 = int(input())
#Read in team 4 name
print("What is team 4? ")
team4 = input()
#Read in team 4 wins
print("How many wins does team  4 have? ")
wins4 = int(input())
#Read in team 4 losses
print("How many losses does team  4 have? ")
losses4 = int(input())
#Read in team 4 ties
print("How many ties does team  4 have? ")
ties4 = int(input())
#Read in team 5 name
print("What is team 5? ")
team5 = input()
#Read in team 5 wins
print("How many wins does team  5 have? ")
wins5 = int(input())
#Read in team 5 losses
print("How many losses does team  5 have? ")
losses5 = int(input())
#Read in team 5 ties
print("How many ties does team  5 have? ")
ties5 = int(input())
#Read in team 6 name
print("What is team 6? ")
team6 = input()
#Read in team 6 wins
print("How many wins does team  6 have? ")
wins6 = int(input())
#Read in team 6 losses
print("How many losses does team  6 have? ")
losses6 = int(input())
#Read in team 6 ties
print("How many ties does team  6 have? ")
ties6 = int(input())
#Calculate the total points for team 1
totalp1 = wins1*2+ties1*1
print("Team Name:",team1,"Wins:",wins1,"Losses:",losses1,"Ties:",ties1,"Total Points: "+str(totalp1))
#Calculate the total points for team 2
totalp2 = wins2*2+ties2*1
print("Team Name:",team2,"Wins:",wins2,"Losses:",losses2,"Ties:",ties2,"Total points: "+str(totalp2))
#Calculate the total points for team 3
totalp3 = wins3*2+ties3*1
print("Team Name:",team3,"Wins:",wins3,"Losses:",losses3,"Ties:",ties3,"Total points: "+str(totalp3))
#Calculate the total points for team 4
totalp4 = wins4*2+ties4*1
print("Team Name:",team4,"Wins:",wins4,"Losses:",losses4,"Ties:",ties4,"Total points: "+str(totalp4))
#Calculate the total points for team 5
totalp5 = wins5*2+ties5*1
print("Team Name:",team5,"Wins:",wins5,"Losses:",losses5,"Ties:",ties5,"Total points: "+str(totalp5))
#Calculate the total points for team 6
totalp6 = wins6*2+ties6*1
print("Team Name:",team6,"Wins:",wins6,"Losses:",losses6,"Ties:",ties6,"Total points: "+str(totalp6))
#Find the team with the highest score
top_team_name = ""
max_points = -1
if totalp1 > max_points:
    max_points = totalp1
    top_team_name = team1
if totalp2 > max_points:
    max_points = totalp2
    top_team_name = team2
if totalp3 > max_points:
    max_points = totalp3
    top_team_name = team3
if totalp4 > max_points:
    max_points = totalp4
    top_team_name = team4
if totalp5 > max_points:
    max_points = totalp5
    top_team_name = team5
if totalp6 > max_points:
    max_points_name = totalp6
    top_team = team6
#Top team
print("Top team:",top_team_name,"is at the top of the standings. Congratulations to",top_team_name,"team!")
