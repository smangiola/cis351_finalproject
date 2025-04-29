# cis351_finalproject

#Introduction and Overview
This program asks a user to select three characters for two teams and determines which of those teams would win in a battle based on their combined power scores. This decision is based upon the sum of the combined value of each power statistic (Intelligence, Strength, Speed, Durability, Power, and Combat) of each team. Before the winner is determined, a series of checks is performed to ensure that the same character is not added more than once in a team. Additionally, an if-else statement is used to ensure that the inputted character does not have any missing power statistics data. The data used in this program is obtained through an API key from the Superhero API (linked in my PowerPoint presentation). This program is my final project for my CIS 351 course, with an intention of demonstrating my knowledge of both the Python language and API keys. 


#System Architecture 
This project was built on an HP laptop and is hosted on Github.


#Data Design
The data needed to ensure the program's functionality is obtained through an API key from the Superhero API. At the beginning of the program, two libraries are imported to help with the processing and usage of the data obtained from the API database. The requests library permits interaction with the API key, while the JSON library converts the received data in a JSON format. Also at the beginning of the program is the API key and url used to obtain the necessary data for team members. When the program obtains the name, full name, and power statistics of an inputted character, it first uses the url (written as base_url = f'https://superheroapi.com/api/{api_key}') from the API and enters the information it wants into a new url variable (for example, the url used to search for a character's name is url = f'{base_url}/search/{name}'). Then, it uses the response.get command on the url to get a response from the API database. Once a response is received, the data is then converted to a JSON format using the .json() command. The code below provides an example of this process when the program searches for a character's name:

import requests #library needed to interact with the API

import json #library needed to convert the data into a JSON format

api_key = 'c4d69dd993618ac74a49f967895e4a00'

base_url = f'https://superheroapi.com/api/{api_key}'

name = input("\nEnter the name of the character you want to add to Team A: ")

    url = f'{base_url}/search/{name}' #API URL to search for the inputted character
    
    response = requests.get(url) #get a response from the API
    
    data = response.json() #converting the response to JSON format
    
There is also a series of checks performed to ensure the validity of an inputted character's data. For example, an if-else statment is used to find any characters in the API database that match the name inputted by a user. If any matching characters are found, the program will output a list of the the names and full names of each character that match the inputted name. If no matching characters are found, the program will output "No matching characters found. Please try again” and ask the user to input another name. When each matching character is listed, a number is written right next to them. After the list is outputted, the user is then asked to enter the number of the character they would like to add to the team. If the user's input is not an integer, the program will output "Invalid input. Please enter a number” and ask the user to enter another number. If the user's input is not a number listed in the list, the program will output "Invalid choice. Please try again", and also ask the user to enter another number. An if-else statement is also used to ensure the inputted character is not missing any power statistics. This statement is written as the following (for Team A):
if stats_data.get('response') == 'success' and all(
                        stats_data.get(stat, 'null') != 'null' for stat in ['intelligence', 
                        'strength', 'speed', 'durability', 'power', 'combat']
                    ):
                        team_A.append({
                            'name': character['name'],
                            'full_name': full_name,
                            'power_stats': {stat: int(stats_data[stat]) for stat in ['intelligence', 
                            'strength', 'speed', 'durability', 'power', 'combat']}
                        })
                        print(f"{character['name']} ({full_name}) added to Team A.")
                        power_stats = {stat: int(stats_data[stat]) for stat in ['intelligence', 
                        'strength', 'speed', 'durability', 'power', 'combat']}
                        num += 1
                        break #exits the loop if valid statistics are found
                    else:
                        print(f"{character['name']} ({full_name}) does not have valid power stats. Please select another character.")
                        break
If all the character's power statistics are not empty (null), the character's name, full name, and power statistics are added to the team. If any power statistics are missing, the user will be asked to select another character. The program also checks if an inputted character is trying to be entered more than once by using an if statement that checks if the character has the same name and full name as another member of the team. If an inputted character has the same name and full name as another team member, the user will be asked to choose another character. The program asks the same thing if the user tries adding a character to Team B that is already in Team A. If the chosen character has no issues with their data or name, their name, full name, and power statistics are complied into a dictionary that is added to their team's list (called team_A for Team A and team_B for Team B). Once 3 members are added to both teams, the program creates an empty dictionary for both teams in which the combined power value of each power statistic from each member is stored. In other words, a for loop is used to iterate over each power statistic of each team member, which is then added to the empty dictionary. Each iteration of the for loop adds the value of a team member's power statistic to the empty dictionary. For example, if the intelligence value of Iron Man is 1, the empty dictionary will state that the team's combined intelligence score is 1. In the next two iterations, the intelligence values of the last two members are added to the combined intelligence score. If the intelligence values of the last two members are also 1, then the combined intelligence score for their team will be 3. This process is repeated for each power statistic for each team member. Once the total combined value of each power statistic is found, the sum() argument is used to find the sum of all the combined power values, which is called teamA_powersum for Team A and teamB_powersum for Team B. Then, the program uses an if-elif-else statement to determine the winner of the "battle", which is whoever has the higher combined power score:
if teamA_powersum > teamB_powersum:
    print("\nAfter making careful calculations, Team A is the winner!")
elif teamA_powersum < teamB_powersum:
    print("\nAfter making careful calculations, Team B is the winner!")
else:
    print("\nAfter making careful calculations, it's a tie!")


#Interface Design
As mentioned previously, the data needed to ensure the program's functionality is obtained through an API key from the SuperHero database. At the beginning of the program, two libraries are imported to help with the processing and usage of the data obtained from the API database. The requests library permits interaction with the API key, while the JSON library converts the received data in a JSON format. Also at the beginning of the program is the API key and url used to obtain the necessary data for team members. When the program obtains the name, full name, and power statistics of an inputted character, it first uses the url (written as base_url = f'https://superheroapi.com/api/{api_key}') from the API and enters the information it wants into a new url variable (for example, the url used to search for a character's name is url = f'{base_url}/search/{name}'). Then, it uses the response.get command on the url to get a response from the API database. Once a response is received, the data is then converted to a JSON format using the .json() command. The code below provides an example of this process when the program searches for a character's name:
import requests #library needed to interact with the API
import json #library needed to convert the data into a JSON format
api_key = 'c4d69dd993618ac74a49f967895e4a00'
base_url = f'https://superheroapi.com/api/{api_key}'
name = input("\nEnter the name of the character you want to add to Team A: ")
    url = f'{base_url}/search/{name}' #API URL to search for the inputted character
    response = requests.get(url) #get a response from the API
    data = response.json() #converting the response to JSON format
The program checks if the response from the API is a success or failure. If the response is thought to be a failure, the user will be asked to make another input. For example, if the name a user inputs does not match any characters' name in the database, the user will be asked to enter another name. Try-except blocks are used to handle ValueErrors originating from an invalid input, which occur when the user enters a number that is not in the outputted list of matching characters or their input is not a number. If a ValueError is found, the user will be asked to select another number.

#Component Design
The first four lines at the top of the code gather the necessary libraries and API data needed to ensure the program's functionality. The selection process for Team A and B is split into two blocks of code. The code for each block is almost identical, with the only differences being different variable names (to differentiate between the two teams) and an added if statement in Team B's code that checks if an inputted character is already in Team A (by checking if their name and full name are the same). Before the selection process begins, an empty list, in which the name, full name, and power statistics of each team member are added, is created. The series of checks that oversees the validity of the character's data (placed after the program obtains the data of the name the user inputs), is placed under a while loop that breaks once the num value is 3. Each time a character is added to a team, the num is incremented by 1. Placing the character selection process under the while loop prevents a user from adding more than 3 characters to a team. The series of if and if-else statements all have a purpose of ensuring that the character's data is valid. Furthermore, the else portions of the if-else statements and the try-except block share the purpose of handling cases in which the character's data is invalid. One input these blocks of code need is the name of a character they would like to add to a team, which will output a list of matching characters from the database (if any matching characters are found). An additional necessary input is the number of the specific character the user wants to add to a team from the outputted list, which will result in that character being added to the team (if they have valid power statistics and they are not a duplicate of another character). The next section of the code combines each power statistic of each team member so that the combined power score of each team can be found. The data needed for this section is the power statistics of each team member of each team. Before the combining of power statistics begins, each team is assigned an empty dictionary in which the combined value of each power statistic (Intelligence, Strength, Speed, Durability, Power, Combat) for both teams will be stored. The nested for loop (“for value in member['power_stats']:”) iterates over the value of each power statistic of a team member and adds them to the dictionary. The outer for loop allows this process to occur for each member of a team. Once all the combined values of each power statistic are calculated, they are added together using the sum() function to find the team’s total power score (called teamA_powersum for Team A and teamB_powersum for Team B). The final section compares the total power scores of both teams and outputs the winner of the "battle", which is whoever has the higher power score:
if teamA_powersum > teamB_powersum:
    print("\nAfter making careful calculations, Team A is the winner!")
elif teamA_powersum < teamB_powersum:
    print("\nAfter making careful calculations, Team B is the winner!")
else:
    print("\nAfter making careful calculations, it's a tie!")


#User Interface Design
There are multiple input statements included in the program that allow a user to interact with the code. When a user begins adding characters to a team, they can enter the name of a character they would like to include in their groups. (name = input("\nEnter the name of the character you want to add to Team A: "), name2 = input("\nEnter the name of the character you want to add to Team B: ")). Once the list of characters with a matching name are printed, a user can select the number of the specific character they would like to add to a team. (choice = int(input("Select the number of the character you want to add to Team A: ")), choice2 = int(input("Select the number of the character you want to add to Team B: "))). The program also uses the else portions of if-else statements to handle any issues with the inputted characters. For example, if the inputted name does not match any characters in the Superhero database, the user is given the option to enter a different name. Additionally, if the input the user enters when they are asked to enter the number of the character they would like to add to a team is not an integer or is not a number listed in the outputted list, the user is given the option to select a different number in the list. Furthermore, if the program finds any missing power statistics of the selected character, the user will be given the option to select a different character. The same option is given to users if they enter a character that is already in their team or if the character they are trying to add to Team B is already in Team A. 


#Assumptions and Dependencies
I assume that individuals using this program would access it through the "final_update" branch on the project's Github page. These users would then download the file onto their device and open it in a Python IDE that is able to run the program's code, such as Visual Studio Code. These users must ensure that they have the requests and JSON libraries downloaded, since both are essential for the program's functionality. Additionally, a Python interpreter must also be downloaded on their device, as Python is the language the program uses. 

#Glossary
JSON: A text-based format that represents structured data. It is easily readable by humans and machines, making it a great tool for data transmission between applications.
