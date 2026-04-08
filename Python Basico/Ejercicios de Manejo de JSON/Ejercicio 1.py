import json

def read_pokemon_collection (file_path):
    with open(file_path, 'r') as file:
        python_file = json.load(file)
    
    return python_file


def add_pokemon ():
    pokemon_collection = read_pokemon_collection('Pokemons.json')

    current_collection = {}
    current_collection['name'] = {}
    current_collection['name']['english'] = input("Enter the name of the new pokemon:")
    current_collection['level'] = int(input("Enter the level of the new pokemon:"))
    current_collection['type'] = [input("Enter the type of the new pokemon:")]
    current_collection['base'] = {}
    current_collection['base']['HP'] = int(input("Enter the base value for HP stat:"))
    current_collection['base']['Attack'] = int(input("Enter the base value for Attack stat:"))
    current_collection['base']['Defense'] = int(input("Enter the base value for Defense stat:"))
    current_collection['base']['Sp. Attack'] = int(input("Enter the base value for Sp. Attack stat:"))
    current_collection['base']['Sp. Defense'] = int(input("Enter the base value for Sp. Defense stat:"))
    current_collection['base']['Speed'] = int(input("Enter the base value for Speed stat:"))

    pokemon_collection.append(current_collection)

    return pokemon_collection


def save_new_pokemon ():
    updated_collection = add_pokemon()
    with open('Pokemons.json', 'w') as file:
        json.dump(updated_collection,file,indent=4)
    
    print(f'New Pokemon has been saved successfully!')

save_new_pokemon()





