"""
batch_rename.py
A simple script to rename all .jpg files in a specified directory to a consistent format.
Usage: python batch_rename.py
"""

import os

def batch_rename_images(folder_path):
    """
    Rename all .jpg files in the given folder_path to 'image_0.jpg', 'image_1.jpg', etc.
    """
    if not os.path.exists(folder_path):
        print(f"Error: The directory '{folder_path}does not exsit.")
        return
    
    files = os.listdir(folder_path)
    count = 0
    for file in files:
        if file.lower().endswith(".jpg"):
            old_path = os.path.join(folder_path, file)
            new_filename = f"image_{count}.jpg"
            new_path = os.path.join(folder_path, new_filename)
            os.rename(old_path, new_path)
            count += 1
    print(f"Renamed {count} .jpg files successfully.")

if __name__ == "__main__":
    target_folder = "./images"  # You can change this path
    batch_rename_images(target_folder)
