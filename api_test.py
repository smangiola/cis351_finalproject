import requests #library needed to interact with the API
import json #library needed to convert the data into a JSON format
api_key = 'c4d69dd993618ac74a49f967895e4a00'
base_url = f'https://superheroapi.com/api/{api_key}'


#Group A
num = 0
group_A = [] #empty list in which the members of group A will be stored
while num < 3:
    name = input("\nEnter the name of the character you want to add to group A: ")
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
                    full_name = character.get('biography', {}).get('full-name', 'Unknown')
                
                    #Check if the character is already in the group
                    if any(
                        member['name'] == character['name'] and member['full_name'] == full_name
                        for member in group_A
                    ):
                        print(f"{character['name']} ({full_name}) is already in group A. Please select another character.")
                        break

                    #Provide feedback if the character has no full name
                    #This will not be outputted if the character's full name is left blank
                    if full_name == 'Unknown':
                        print(f"Note: {character['name']} does not have a full name listed.")


                    #Obtaining the power stats of the selected character
                    stats_url = f"{base_url}/{character['id']}/powerstats"
                    stats_response = requests.get(stats_url)
                    stats_data = stats_response.json()

                    #Checks if the power stats are available
                    if stats_data.get('response') == 'success' and all(
                        stats_data.get(stat, 'null') != 'null' for stat in ['intelligence', 'strength', 'speed', 'durability', 'power', 'combat']
                    ):
                        group_A.append({
                            'name': character['name'],
                            'full_name': full_name,
                            'power_stats': {stat: int(stats_data[stat]) for stat in ['intelligence', 'strength', 'speed', 'durability', 'power', 'combat']}
                        })
                        print(f"{character['name']} ({full_name}) added to group A.")
                        power_stats = {stat: int(stats_data[stat]) for stat in ['intelligence', 'strength', 'speed', 'durability', 'power', 'combat']}
                        num += 1
                        break #exits the loop if valid statistics are found
                    else:
                        print(f"{character['name']} ({full_name}) does not have valid power stats. Please select another character.")
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
    print(f"{member['name']} ({member['full_name']})")


#Group B (Same code, just with different variable names)
num2 = 0
group_B = [] 
while num2 < 3:
    name2 = input("\nEnter the name of the character you want to add to group B: ")
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
                    full_name2 = character2.get('biography', {}).get('full-name', 'Unknown')
                
                    #Checks if the inputted character is already in group A
                    if any(
                        member['name'] == character2['name'] and member['full_name'] == full_name2
                        for member in group_A
                    ):
                        print(f"{character2['name']} ({full_name2}) is already in group A. Please select another character.")
                        break

                    if any(
                        member['name'] == character2['name'] and member['full_name'] == full_name2
                        for member in group_B
                    ):
                        print("That character is already in group B. Please select another name.")
                        break

                    if full_name2 == 'Unknown':
                        print(f"Note: {character2['name']} does not have a full name listed.")

                    stats_url2 = f"{base_url}/{character2['id']}/powerstats"
                    stats_response2 = requests.get(stats_url2)
                    stats_data2 = stats_response2.json()

                    if stats_data2.get('response') == 'success' and all(
                        stats_data2.get(stat, 'null') != 'null' for stat in ['intelligence', 'strength', 'speed', 'durability', 'power', 'combat']
                    ):
                        group_B.append({
                            'name': character2['name'],
                            'full_name': full_name2,
                            'power_stats': {stat: int(stats_data2[stat]) for stat in ['intelligence', 'strength', 'speed', 'durability', 'power', 'combat']}
                        })
                        print(f"{character2['name']} ({full_name2}) added to group B.")
                        power_stats2 = {stat: int(stats_data2[stat]) for stat in ['intelligence', 'strength', 'speed', 'durability', 'power', 'combat']}
                        num2 += 1
                        break
                    else:
                        print(f"{character2['name']} ({full_name2}) does not have valid power stats. Please select another character.")
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
    print(f"{member2['name']} ({member2['full_name']})")


#Combine power stats of all members in both groups
#Group A
groupA_powerstats = {} #empty dictionary in which the combined value of each power stat for Group A will be stored
for member in group_A:
    for value in member['power_stats']:
        if value in groupA_powerstats:
            groupA_powerstats[value] += member['power_stats'][value]
        else:
            groupA_powerstats[value] = member['power_stats'][value]

groupA_powersum = sum(groupA_powerstats.values())

#Group B - same code, just different variable names
groupB_powerstats = {}
for member2 in group_B:
    for value2 in member2['power_stats']:
        if value2 in groupB_powerstats:
            groupB_powerstats[value2] += member2['power_stats'][value2]
        else:
            groupB_powerstats[value2] = member2['power_stats'][value2]

groupB_powersum = sum(groupB_powerstats.values())


#Compare the two groups and print the winner
#Group A
print("\nIt's time to fight!")
print("\nThese are the total values of each power statistic for Group A:")
for stat, value in groupA_powerstats.items():
    print(f"{stat[0].upper() + stat[1:]}: {value}")
print(f"This makes the total power score of Group A {groupA_powersum}.")

#Group B - same code, just different variable names
print("\nThese are the total values of each power statistic for Group B:")
for stat2, value2 in groupB_powerstats.items():
    print(f"{stat2[0].upper() + stat2[1:]}: {value2}")
print(f"This makes the total power score of Group B {groupB_powersum}.")

if groupA_powersum > groupB_powersum:
    print("\nAfter making careful calculations, Group A is the winner!")
elif groupA_powersum < groupB_powersum:
    print("\nAfter making careful calculations, Group B is the winner!")
else:
    print("\nAfter making careful calculations, it's a tie!")