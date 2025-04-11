import requests #library needed to interact with the API
import json #library needed to convert the data into a JSON format
api_key = 'c4d69dd993618ac74a49f967895e4a00'
base_url = f'https://superheroapi.com/api/{api_key}'

#Group A
num = 0
group_A = [] #empty list in which the members of group A will be stored
while num < 3:
    name = input("Enter the name of the character you want to add to group A: ")
    url = f'{base_url}/search/{name}' #API URL to search for the inputted character
    response = requests.get(url) #get a response from the API
    data = response.json() #converting the response to JSON format

    #Function below returns all characters that match the name inputted by the user
    if data.get('response') == 'success':
        print("Matching Characters:")
        for i, result in enumerate(data['results']):
            full_name = result.get('biography', {}).get('full-name', 'Unknown')
            print(f"{i}: {result['name']} (Full Name: {full_name})")
            #^ Full Name is printed to differentiate between characters with the same name
        
        while True: #Handles invalid power stats
            try:
                #Function below asks the user to select the number of the character they want to select
                #The selected character is then added to group A
                choice = int(input("Select the number of the character you want to add to group A: "))
                if 0 <= choice < len(data['results']):
                    character = data['results'][choice]

                    #Obtaining the power stats of the selected character
                    stats_url = f"{base_url}/{character['id']}/powerstats"
                    stats_response = requests.get(stats_url)
                    stats_data = stats_response.json()

                    #Checks if the power stats are available
                    if stats_data.get('response') == 'success' and all(
                        stats_data.get(stat, 'null') != 'null' for stat in ['intelligence', 'strength', 'speed', 'durability', 'power', 'combat']
                    ):
                        group_A.append(character['name'])
                        print(f"{character['name']} added to group A.")
                        power_stats = {stat: int(stats_data[stat]) for stat in ['intelligence', 'strength', 'speed', 'durability', 'power', 'combat']}
                        print(f"Power Stats: {power_stats}")
                        num += 1
                        break #exits the loop if valid statistics are found
                    else:
                        print(f"{character['name']} does not have valid power stats. Please select another character.")
                        break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    else: 
        print("No matching characters found. Please try again.")
        if num == 3:
            break

print("\nGroup A:")
for member in group_A:
    print(member)


#Group B (Same code, just with different variable names)
num2 = 0
group_B = [] 
while num2 < 3:
    name2 = input("Enter the name of the character you want to add to group B: ")
    url2 = f'{base_url}/search/{name2}'
    response2 = requests.get(url2)
    data2 = response2.json()

    if data2.get('response') == 'success':
        print("Matching Characters:")
        for i, result in enumerate(data2['results']):
            full_name = result.get('biography', {}).get('full-name', 'Unknown')
            print(f"{i}: {result['name']} (Full Name: {full_name})")
        
        while True:
            try:
                choice2 = int(input("Select the number of the character you want to add to group B: "))
                if 0 <= choice2 < len(data2['results']):
                    character2 = data2['results'][choice2]
                
                    #Checks if the inputted character is already in group A
                    if character2['name'] in group_A:
                        print(f"{character2['name']} is already in group A. Please select another character.")
                        break

                    stats_url2 = f"{base_url}/{character2['id']}/powerstats"
                    stats_response2 = requests.get(stats_url2)
                    stats_data2 = stats_response2.json()

                    if stats_data2.get('response') == 'success' and all(
                        stats_data2.get(stat, 'null') != 'null' for stat in ['intelligence', 'strength', 'speed', 'durability', 'power', 'combat']
                    ):
                        group_B.append(character2['name'])
                        print(f"{character2['name']} added to group B.")
                        power_stats2 = {stat: int(stats_data2[stat]) for stat in ['intelligence', 'strength', 'speed', 'durability', 'power', 'combat']}
                        print(f"Power Stats: {power_stats2}")
                        num2 += 1
                        break
                    else:
                        print(f"{character2['name']} does not have valid power stats. Please select another character.")
                        break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    else:
        print("No matching characters found. Please try again.")
        if num2 == 3:
            break

print("\nGroup B:")
for member2 in group_B:
    print(member2)


