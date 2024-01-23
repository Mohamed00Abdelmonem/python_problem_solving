import os
import glob

def get_image_files(folder_path):
    image_extensions = ['png', 'jpg', 'jpeg', 'webp']  # Add more extensions if needed
    image_files = []

    # Use glob to find files matching the specified extensions
    for extension in image_extensions:
        pattern = os.path.join(folder_path, f'*.{extension}')
        image_files.extend(glob.glob(pattern))

    return image_files

def main():
    folder_path = 'D:\course django 2023\Course\Django\Amazon Clone\AmazonClone\src\media_root\product_images'  # Replace with your folder path
    image_files = get_image_files(folder_path)

    # Append file names with extensions to a list
    image_list = [os.path.basename(file) for file in image_files]

    # Print or use the image list as needed
    print("List of image files:")
    print(image_list)
    print(len(image_list))

if __name__ == "__main__":
    main()
