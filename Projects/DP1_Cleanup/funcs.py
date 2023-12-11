def count_files_and_folders(directory:str) -> dict:
    '''
    
    '''
    import os
    from collections import Counter

    file_counter = Counter()
    folder_counter = Counter()
    full_paths = Counter() #?

    def proccess_path(path:str):
        for root, dirs, files in os.walk(path):
            for folder in dirs:
                folder_counter[folder] += 1
            for file in files:
                file_counter[file] += 1
                full_paths[file] = os.path.join(root, file) #?

    proccess_path(directory)
    return file_counter, folder_counter

def get_old_files(directory:str, threshold:int=365) -> list:
    '''
    Identify files in a given directory that have not been modified or accessed in the last 'threshold' days - default of 365 if not otherwise specified
    '''
    import os
    from datetime import datetime, timedelta
    old_files = []
 
    # Calculate treshold date
    threshold_date = datetime.now() - timedelta(days=threshold)

    # Directory walk
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            modificiaiton_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            access_time = datetime.fromtimestamp(os.path.getatime(file_path))

            if modificiaiton_time < threshold_date and access_time < threshold_date:
                old_files.append(file_path)

    return old_files

def remove_files(*args) -> None:
    '''
    Reads in a list of filepaths supplied by some other function, and iterates over those filepaths. If they exist, they will be deleted. Could potentially retool to work from a file
    '''
    '''
    with open(file) as f:
        for line in f:
            if os.path.exists(line):
                os.remove(line)
            else:
                print("Filepath not found")
                continue
    '''
    import os
    for arg in args:
        if os.path.exists(arg):
            os.remove(arg)
        else:
            print("Filepath not found")
            continue

def simpleRecursiveCopy(source_path:str, destination_path:str) -> None:
    '''
    Function to recursively copy a directory structure from source_path to destination_path.
    Note: destination_path must not already exist and will be created by the function; will return error if given extan path
    '''
    import shutil
    try:
        src = source_path
        dest = destination_path
        destination = shutil.copytree(src,dest)
    except Exception as e:
        print("Error: {e}")
        return None

def pauseRecursiveCopy(source_dir:str, destination_dir:str) -> None:
    """
    Recursively copy the entire directory structure from source_dir to destination_dir
    pausing for 5 seconds after each file copy in order to stop from generating too much network traffic too quickly.

    Parameters:
    - source_dir: The source directory to be copied.
    - destination_dir: The destination directory where the copy will be placed.
    """
    import os
    import shutil
    import time
    # Create the destination directory if it doesn't exist
    try:
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

    # Walk through the source directory
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                source_path = os.path.join(root, file)
                relative_path = os.path.relpath(source_path, source_dir)
                destination_path = os.path.join(destination_dir, relative_path)

                # Create destination directory structure if not exists
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)

                # Copy the file
                shutil.copy2(source_path, destination_path)

                # Pause for 5 seconds
                time.sleep(5)
    except Exception as e:
        print(f"Error encountered:\n {e}")

if __name__ == "__main__":
    pauseRecursiveCopy("~/share/", "~/testcopy/")

