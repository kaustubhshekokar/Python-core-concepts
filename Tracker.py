import json
import os

# This is the file where your data will live forever
FILE_NAME = "watchlist.json"

def load_data():
    """Reads the JSON file from your hard drive if it exists."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []  # If it's your first time running, return an empty list

def save_data(data):
    """Writes your list to the JSON file before closing."""
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)  # indent=4 makes the file easy to read

def main():
    print("🎬 Welcome to the CLI Entertainment Tracker 🎬")
    
    # Load your saved data the exact second the program starts
    my_list = load_data()
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Add a Movie/Series")
        print("2. View My List")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            print("\n--- Add an Entry ---")
            title = input("Enter the name of the movie/series: ")
            rating = input("Give it a rating (e.g., 8/10 or 'Awesome'): ")
            
            entry = {"title": title, "rating": rating}
            my_list.append(entry)
            
            print(f"✅ '{title}' has been added to your list!")
            save_data(my_list)
        elif choice == '2':
            print("\n--- My Watchlist ---")
            if len(my_list) == 0:
                print("Your list is currently empty. Go add something!")
            else:
                for index, item in enumerate(my_list, start=1):
                    print(f"{index}. {item['title']} - Rating: {item['rating']}")
                    
        elif choice == '3':
            print("\n>> Saving your data to the hard drive...")
            # Automatically trigger the save function right before we break the loop
            save_data(my_list)
            print(">> Exiting tracker. Goodbye!")
            break 
        else:
            print("\n>> Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()