import os

def create_folders():
    # Define the path to the data folder
    data_folder = "./data"
    
    # Create data folder if it doesn't exist
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
    
    # Characters for folder names
    characters = [str(i) for i in range(10)] + [chr(ord('A') + i) for i in range(26)]
    
    # Create folders
    for char in characters:
        folder_path = os.path.join(data_folder, char)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

if __name__ == "__main__":
    create_folders()
    print("Folders created successfully.")
