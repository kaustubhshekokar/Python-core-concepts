import json
import os

FILE_NAME = "watchlist.json"

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def main():
    print("🎬 Welcome to the CLI Entertainment Tracker V2 🎬")
    
    my_list = load_data()
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Add an Entry")
        print("2. View My List")
        print("3. Delete an Entry")  # --- NEW OPTION ---
        print("4. Exit")             # Shifted to option 4
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            print("\n--- Add an Entry ---")
            title = input("Enter the name of the movie/series: ")
            rating = input("Give it a rating (e.g., 8/10): ")
            
            # --- NEW: Ask for the Category ---
            print("Is this a Movie or a Series?")
            print("1. Movie\n2. Series")
            type_choice = input("Choose 1 or 2: ")
            
            # Set the category based on input
            if type_choice == '1':
                media_type = "Movie"
            elif type_choice == '2':
                media_type = "Series"
            else:
                media_type = "Other"
            
            # Pack the new data structure
            entry = {"title": title, "rating": rating, "type": media_type}
            my_list.append(entry)
            
            print(f"✅ [{media_type}] '{title}' has been added!")
            save_data(my_list)
            
        elif choice == '2':
            print("\n--- My Watchlist ---")
            if len(my_list) == 0:
                print("Your list is currently empty.")
            else:
                for index, item in enumerate(my_list, start=1):
                    # Use .get() to safely handle older entries that don't have a 'type'
                    m_type = item.get('type', 'Uncategorized')
                    print(f"{index}. [{m_type}] {item['title']} - Rating: {item['rating']}")
                    
        elif choice == '3':
            # --- NEW: Delete Logic ---
            print("\n--- Delete an Entry ---")
            if len(my_list) == 0:
                print("Your list is empty. Nothing to delete.")
            else:
                # Show the list so the user knows what number to pick
                for index, item in enumerate(my_list, start=1):
                    print(f"{index}. {item['title']}")
                
                # Use a try-except block to prevent crashes if the user types a letter instead of a number
                try:
                    del_num = int(input("\nEnter the number to delete (or 0 to cancel): "))
                    
                    if del_num == 0:
                        print(">> Deletion cancelled.")
                    elif 1 <= del_num <= len(my_list):
                        # .pop() removes the item and we subtract 1 because Python lists start at index 0
                        removed_item = my_list.pop(del_num - 1)
                        save_data(my_list)
                        print(f"🗑️ Permanently deleted '{removed_item['title']}'.")
                    else:
                        print(">> Invalid number. No item deleted.")
                except ValueError:
                    print(">> Error: Please enter a valid number.")
                    
        elif choice == '4':
            print("\n>> Saving data and shutting down...")
            save_data(my_list)
            print(">> Goodbye!")
            break 
        else:
            print("\n>> Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()