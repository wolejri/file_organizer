import os
import shutil

#to run this python file, use first check the python version on your computer by running
# 1. python3 --version or python --version
# 2. if python exists, you can run python(3) file_organizer.py - the (3) signifies you can use python or python3
#3. if it doesn't exist, download python from https://www.python.org/downloads/


try:
    #replace "Desktop" with any directory you want to organize i.e "Documents", also you can make expanduser's paramaeter as an input, so you dont have to manually change the parameter
    user_home = os.path.expanduser("~")
    target_folder = os.path.join(user_home, "Desktop")

    extensions = {item.split(".")[-1] for item in os.listdir(target_folder) if os.path.isfile(os.path.join(target_folder, item))}

    for extension in extensions:
        if not os.path.exists(os.path.join(target_folder, extension)):
            os.mkdir(os.path.join(target_folder, extension))

    for item in os.listdir(target_folder):
        item_path = os.path.join(target_folder, item)

        if os.path.isfile(item_path):
            file_extension = item.split(".")[-1]

            # Check if the destination directory has the same name as the file
            if file_extension == item:
                # Handle this case differently, e.g., by skipping the file
                print(f"Skipping '{item}' as it's a directory name.")
                continue

            shutil.move(item_path, os.path.join(target_folder, file_extension, item))

except Exception as e:
    raise e




#This method takes in the file name that you would like to organize, you can uncomment this method and comment the top one if you would like to proceed.

# import os
# import shutil

# def organize_files(target_folder):
#     try:
#         extensions = {item.split(".")[-1] for item in os.listdir(target_folder) if os.path.isfile(os.path.join(target_folder, item))}

#         for extension in extensions:
#             if not os.path.exists(os.path.join(target_folder, extension)):
#                 os.mkdir(os.path.join(target_folder, extension))

#         for item in os.listdir(target_folder):
#             item_path = os.path.join(target_folder, item)

#             if os.path.isfile(item_path):
#                 file_extension = item.split(".")[-1]

#                 # Check if the destination directory has the same name as the file
#                 if file_extension == item:
#                     # Handle this case differently, e.g., by skipping the file
#                     print(f"Skipping '{item}' as it's a directory name.")
#                     continue

#                 shutil.move(item_path, os.path.join(target_folder, file_extension, item))

#     except Exception as e:
#         raise e

# if __name__ == "__main__":
#     user_input = input("Enter the folder path you want to organize: ")
#     organize_files(user_input)
