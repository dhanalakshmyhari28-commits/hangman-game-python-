"""
Task 3: Task Automation with Python Scripts
--------------------------------------------
Move all .jpg files from a source folder to a destination folder.

Key concepts used: os, shutil, file handling, error handling
"""

import os
import shutil


def move_jpg_files(source_folder, destination_folder):
    """
    Move all .jpg files from source_folder to destination_folder.
    Creates the destination folder if it doesn't exist.
    Returns the number of files moved.
    """
    moved_count = 0

    # Check if source folder exists
    if not os.path.isdir(source_folder):
        print(f"Error: Source folder '{source_folder}' does not exist.")
        return moved_count

    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        try:
            os.makedirs(destination_folder)
            print(f"Destination folder '{destination_folder}' created.")
        except OSError as e:
            print(f"Error: Could not create destination folder. {e}")
            return moved_count

    # Loop through files in source folder
    try:
        files = os.listdir(source_folder)
    except OSError as e:
        print(f"Error: Could not read source folder. {e}")
        return moved_count

    for file_name in files:
        # Check for .jpg extension (case-insensitive)
        if file_name.lower().endswith(".jpg"):
            source_path = os.path.join(source_folder, file_name)
            destination_path = os.path.join(destination_folder, file_name)

            # Skip if it's not actually a file (e.g., a folder named something.jpg)
            if not os.path.isfile(source_path):
                continue

            try:
                # Avoid overwriting an existing file at destination
                if os.path.exists(destination_path):
                    print(f"Skipped (already exists at destination): {file_name}")
                    continue

                shutil.move(source_path, destination_path)
                print(f"Moved: {file_name}")
                moved_count += 1

            except PermissionError:
                print(f"Error: Permission denied while moving '{file_name}'.")
            except FileNotFoundError:
                print(f"Error: '{file_name}' not found (may have been removed).")
            except shutil.Error as e:
                print(f"Error: Could not move '{file_name}'. {e}")
            except Exception as e:
                print(f"Unexpected error moving '{file_name}': {e}")

    return moved_count


def main():
    print("=== Move .jpg Files From One Folder To Another ===\n")

    source_folder = input("Enter the source folder path: ").strip()
    destination_folder = input("Enter the destination folder path: ").strip()

    try:
        moved_count = move_jpg_files(source_folder, destination_folder)
        print(f"\nDone. Total .jpg files moved: {moved_count}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
