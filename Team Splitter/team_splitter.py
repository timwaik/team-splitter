#This program will take n number of names of people, and randomly assign them to n number of teams
import random
import sys
import os

def end_program(input):
    if input == ".....":
        sys.exit("Goodbye!")
    else:
        return input

def save_file():
    filename = input("Enter the name of your file!")
    filename = filename + ".txt"
    os.chdir(os.getcwd() + "\\Saved Teams")
    if os.path.exists(filename):
        print("File exists! Try again")
    else:
        save_file = open(filename, "w")
        for team in range(total_number_of_teams):
            write_team_name = "Team " + names_of_teams[team] + ": " + "\n"
            save_file.write(write_team_name)
            for name, team_name in list_of_sorted_teams.items():
                if team_name == names_of_teams[team]:
                    write_person_name = name + "\n"
                    save_file.write(name)
            save_file.write("\n")
        print("File " , filename , ".txt has been saved!")
        save_file.close()

while True:
    #Variables
    names_of_people = []
    names_of_teams = []
    list_of_sorted_teams = {}

    print("Welcome to the Team Splitter! You may enter fullstops 5 times [.....] at any moment to exit the program")

    while True:
        print("Enter the total number of people to split into teams:")
        total_number_of_people = end_program(input())
        try:
            total_number_of_people = int(total_number_of_people)
            break
        except ValueError:
            print("Thats not a number!")
    print("Great! There will be " , total_number_of_people , " being split this round.")

    while True:

        print("Enter the number of teams to randomly assign them to:")
        total_number_of_teams = end_program(input())
        try:
            total_number_of_teams = int(total_number_of_teams)
            if total_number_of_teams > total_number_of_people:
                print("Sorry you can't have more teams than people! It doesn't work like that!")
            else:
                print("You're splitting them into ", total_number_of_teams , " teams!")
                break
        except ValueError:
            print("Thats not a number!")


    print("Type in the names of the people being split.")

    for person_name in range(total_number_of_people):
        print("Person " , person_name + 1)
        while True:
            name = end_program(input())
            if name.lower() in names_of_people:
                print("You can't add that name, its already in the list!")
                print("Try again")
            elif name.isspace() or name == "":
                print("Your name can't be a blank!")
                print("Try again")
            else:
                print("Added " , name.lower() , "!")
                names_of_people.append(name.lower())
                break

    print("Here are the names of the people:")
    print(names_of_people)

    print("Now, type in the names of the teams you're forming")

    for team_name in range(total_number_of_teams):
        print("Team " , team_name + 1)
        while True:
            team = end_program(input())
            if team.lower() in names_of_teams:
                print("You can't add that team, its already in the list!")
                print("Try again")
            elif team.isspace() or team == "":
                print("Your team name can't be a blank!")
                print("Try again")
            else:
                print("Added " , team.lower() , "!")
                names_of_teams.append(team.lower())
                break

    print("Here are the names of the teams:")
    print(names_of_teams)

    #Determining how many people will be allocated to each team, and the remainder number to sort evenly among teams
    people_per_team = total_number_of_people//total_number_of_teams
    remainder_people = total_number_of_people%total_number_of_teams
    print("People will be divided by  " , people_per_team , " per team")
    print("The remaining " , remainder_people , " will be sorted out evenly among teams")


    #Shuffling the order of the list essentially creates a randomiser
    print("Sorting...\n")
    random.shuffle(names_of_people)

    #This part segments players equally among teams
    for team in range(total_number_of_teams):
        for person in range(people_per_team):
            list_of_sorted_teams[names_of_people[person]] = names_of_teams[team]
        for people in range(people_per_team):
            names_of_people.pop(0)

    #This part distributes the remaining number of people among the teams equally
    if remainder_people > 0:
        for person in range(remainder_people):
            remainder_team = random.sample(names_of_teams,remainder_people)
            list_of_sorted_teams[names_of_people[person]] = remainder_team[person]

    #This part prints out the teams and who is allocated to which team
    print("Teams have been sorted! Check them out below:\n")
    for team in range(total_number_of_teams):
        print(names_of_teams[team], ": ")
        for name, team_name in list_of_sorted_teams.items():
            if team_name == names_of_teams[team]:
                print(name)
        print("")

    #This part asks if you want to save your team. It will save it in a txt file
    while True:
        print("Do you want to save this team allocation?")
        confirmation = end_program(input("Type in [Yes] or [No]\n"))
        if (confirmation.lower() == "yes"):
            print("Saving your work in a text file..")
            print("Note: You won't be able to quit the program while saving")
            save_file()
            break
        elif (confirmation.lower() == "no"):
            print("Not going to save your work then")
            break
        else:
            print("Unacceptable command, try again")

    while True:
        print("Do you want to start again? If you don't this program will end")
        restart = end_program(input("Type in [Yes] to start, or [No] to quit. Alternatively you may enter the exit sequence [.....] to quit\n"))
        if (restart.lower() == "yes"):
            print("Restarting!\n")
            break
        elif (restart.lower() == "no"):
            sys.exit("Alright, goodbye!")
        else:
            print("Unacceptable command, try again!")
