import os


def rename_images(directory_path):
    # Ensure the provided path is a directory
    if not os.path.isdir(directory_path):
        print(f"Error: {directory_path} is not a valid directory.")
        return

    # Get a list of all files in the directory
    files = os.listdir(directory_path)

    # Filter out non-image files (you can customize this if needed)
    image_files = [
        file
        for file in files
        if file.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".bmp"))
    ]

    # Rename each image file sequentially
    for count, old_name in enumerate(image_files, start=1):
        extension = os.path.splitext(old_name)[1]
        new_name = f"{count}{extension}"

        # Construct the full paths for the old and new names
        old_path = os.path.join(directory_path, old_name)
        new_path = os.path.join(directory_path, new_name)

        # Check if the new name already exists
        while os.path.exists(new_path):
            count += 1
            new_name = f"{count}{extension}"
            new_path = os.path.join(directory_path, new_name)

        # Rename the file
        os.rename(old_path, new_path)

        print(f"Renamed: {old_name} -> {new_name}")


if __name__ == "__main__":
    # Provide the path to your image directory here
    image_directory = r"D:\product"

    # Call the function to rename images in the specified directory
    rename_images(image_directory)
