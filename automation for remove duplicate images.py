
import os

directory_path = r"D:\wallpaper"

files = os.listdir(directory_path)

for file_name in files:
    if "Copy" in file_name:
        file_path = os.path.join(directory_path, file_name)
        
        try:
            os.remove(file_path)
            print(f"Removed: {file_path}")
        except Exception as e:
            print(f"Error removing {file_path}: {e}")
