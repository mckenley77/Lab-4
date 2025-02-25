import requests


BASE_URL = "https://api.pokemontcg.io/v2/"


def fetch_cards_by_type(pokemon_type):

    url = f"{BASE_URL}cards"

    params = {"q": f"types:{pokemon_type}"}  
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data['data']:
            return data['data']
        else:
            print(f"No cards found for type {pokemon_type}.")
            return []
    else:
        print("Error fetching data")
        return []


def create_deck(cards):

    deck = []

    for card in cards:
       
        if card['supertype'] == 'Pokémon': 
            deck.append({
                'id': card['id'],  
                'name': card['name'],
                'types': card.get('types', ['N/A']), 
                'rarity': card.get('rarity', 'N/A'),
                'set': card['set']['name'],
                'image_url': card['images']['small']
            })
    return deck


def display_deck(deck):
    if deck:
        print("\nYour Deck:")
        for card in deck:
            print(f"ID: {card['id']}") 
            print(f"Name: {card['name']}")
            print(f"Type: {', '.join(card['types'])}")
            print(f"Rarity: {card['rarity']}")
            print(f"Set: {card['set']}")
            print("-" * 50)
    else:
        print("No cards found to build the deck.")


def main():

    print("Welcome to the Pokemon TCG Deck Builder! This Deck Builder will display Pokemon based on the type you enter.")

    pokemon_type = input("Enter a Pokemon type: ")

    cards = fetch_cards_by_type(pokemon_type)

    deck = create_deck(cards)

    display_deck(deck)


if __name__ == "__main__":
    main()
