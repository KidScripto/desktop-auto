import os
from collections import Counter

def count_files_and_folders(directory):
    file_counter = Counter()
    folder_counter = Counter()

    def process_dir(path):
        for root, dirs, files in os.walk(path):
            for folder in dirs:
                folder_counter[folder] += 1
            for file in files:
                file_counter[file] += 1

    process_dir(directory)

    return file_counter, folder_counter

'''
# Main Function
def main():
    directory_path = input("Enter a directory path to search: ")
    treshold = int(input("Set a threshold on repetitions to report. Must be an integer"))
    try:
        if os.path.exists(directory_path) and os.path.isdir(directory_path):
            with open("directory_parser.txt", "r") as file:
                file_counter, folder_counter = count_files_and_folders(directory_path)
                file.write("File Counts:\n")
                for file_name, count in file_counter.items():
                    if count >= threshold:
                        file.write(f'{file_name}: {count}')
                file.write("Folder Counts:\n")
                for folder_name, count in folder_counter.items():
                    if count >= threshold:
                        file.write(f'{folder_name}: {count}')
    except Exception as e:
        print(f"Encountered error: {e}")
        return None
'''

if __name__ == "__main__":
    directory_path = input("Enter a directory path: ")

    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        file_counter, folder_counter = count_files_and_folders(directory_path)

        print("File counts:\n")
        for file_name, count in file_counter.items():
            print(f'{file_name}: {count}')
        
        print("Folder counts:\n")
        for folder_name, count in folder_counter.items():
            print(f'{folder_name}: {count}')
    else:
        print("Directory not found.")
