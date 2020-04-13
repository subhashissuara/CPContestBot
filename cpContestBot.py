# ------------------------------
#   Author: Subhashis Suara
# ------------------------------

import os
import shutil
import string

# -------------------------------- CONFIGURE YOUR PERSONAL DETAILS AFTER THIS COMMENT --------------------------------

# Give your parent directory location in which you want to create your contest directory
parentDir = ""  # Example: - "D:/Everything CS/CP/CodeForces"

# Give your template name
templateName = ""  # Example: - "template.cpp"

# Give your template directory along with template file name
sourceTemplate = ""  # Example: - "D:/Everything CS/CP/CodeForces/template.cpp"

# -------------------------------- CONFIGURE YOUR PERSONAL DETAILS BEFORE THIS COMMENT --------------------------------

contestDir = input("Enter the contest name or number: ")
contestPath = os.path.join(parentDir, contestDir)

try:
    os.mkdir(contestPath)
    print(f"Contest {contestDir} directory created!\n")
except OSError as error:
    print(error)
    exit()

beforeRename = os.path.join(contestPath, templateName)

try:
    numProbs = int(input("Enter the number of problems (Max 26): "))
    for elem in range(numProbs):
        shutil.copy(sourceTemplate, contestPath)
        fileName = string.ascii_lowercase[elem]
        afterRename = os.path.join(contestPath, f"{fileName}.cpp")
        os.rename(beforeRename, afterRename)
    print("Solution files with your template have been created successfully! All the best! :)")
    input("\nPress any key to exit...")

# If source and destination are same
except shutil.SameFileError:
    print("Source and destination represents the same file!")

# If destination is a directory.
except IsADirectoryError:
    print("Destination is a directory!")

# If there is any permission issue
except PermissionError:
    print("Permission denied!")

# For other errors
except:
    print("Error occurred while copying file!")
