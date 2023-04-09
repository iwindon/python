#Ask for input for source and destination directories
source = input("Enter the source directory: ")
destination = input("Enter the destination directory: ")

# Function to iterate through all directories and copy mkv files to a new directory
def copy_all_mkv_files(source, destination):
    import os
    import shutil
    for directory in os.listdir(source):
        for file in os.listdir(os.path.join(source, directory)):
            if file.endswith('.mkv'):
                shutil.copy(os.path.join(source, directory, file), destination)

copy_all_mkv_files(source, destination)

# Function to iterate through all directories and create variables based on seasons with S01, S02, etc. then copy mkv files to a new directory with each season in a separate folder
def copy_all_mkv_files_seasons(source, destination):
    import os
    import shutil
    for directory in os.listdir(source):
        for file in os.listdir(os.path.join(source, directory)):
            if file.endswith('.mkv'):
                if 'S01' in file:
                    shutil.copy(os.path.join(source, directory, file), os.path.join(destination, 'S01'))
                elif 'S02' in file:
                    shutil.copy(os.path.join(source, directory, file), os.path.join(destination, 'S02'))
                elif 'S03' in file:
                    shutil.copy(os.path.join(source, directory, file), os.path.join(destination, 'S03'))
                elif 'S04' in file:
                    shutil.copy(os.path.join(source, directory, file), os.path.join(destination, 'S04'))
                elif 'S05' in file:
                    shutil.copy(os.path.join(source, directory, file), os.path.join(destination, 'S05'))
                elif 'S06' in file:
                    shutil.copy(os.path.join(source, directory, file), os.path.join(destination, 'S06'))
                elif 'S07' in file:
                    shutil.copy(os.path.join(source, directory, file), os.path.join(destination, 'S07'))
                elif 'S08' in file:
                    shutil.copy(os.path.join(source, directory, file), os.path.join(destination, 'S08'))
                elif 'S09' in file:
                    shutil.copy(os.path.join(source, directory, file), os.path.join(destination, 'S09'))
                elif 'S10' in file:
                    shutil.copy(os.path.join(source, directory, file), os.path.join(destination, 'S10'))
                elif 'S11' in file:
                    shutil.copy(os.path.join(source, directory, file), os.path.join(destination, 'S11'))
                elif 'S12' in file:
                    shutil.copy(os.path.join(source, directory, file), os.path.join(destination, 'S12'))
                elif 'S13' in file:
                    shutil.copy(os.path.join(source, directory, file), os.path.join(destination, 'S13'))
                elif 'S14' in file:
                    shutil.copy(os.path.join(source, directory, file), os.path.join(destination, 'S14'))
                elif 'S15' in file:
                    shutil.copy(os.path.join(source, directory, file), os.path.join(destination, 'S15'))
                elif 'S16' in file:
                    shutil.copy