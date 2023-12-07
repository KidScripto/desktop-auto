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
    for arg in args:

