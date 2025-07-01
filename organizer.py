import os
import shutil
CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.pptx'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Scripts': ['.py', '.sh', '.c', '.cpp'],
    'Archives': ['.zip', '.tar', '.gz'],
    'Others': []
}

def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return 'Others'

def organize_directory(path):
    if not os.path.isdir(path):
        print("Invalid directory path.")
        return
    
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            category = get_category(file)
            category_folder = os.path.join(path, category)
            os.makedirs(category_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(category_folder, file))
            print(f"Moved: {file} → {category}/")

if __name__ == "__main__":
    directory = input("Enter the directory to organize: ").strip()
    organize_directory(directory)
