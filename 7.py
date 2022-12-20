import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(3000)

def foldersize(current_folder):
    print(current_folder)
    if folder_structure[current_folder]["subfolders"] == [] or folder_structure[current_folder]["summed"]:
        #print("no subfolders found - " + str(folder_structure[current_folder]["totalsize"]))
        folder_structure[current_folder]["summed"] = True
        return folder_structure[current_folder]["totalsize"]
    else :    
        for subfolders in folder_structure[current_folder]["subfolders"]:
            folder_structure[current_folder]["totalsize"] += foldersize(subfolders)    
    
    #print(current_folder + " " + str(folder_structure[current_folder]["totalsize"]))
    folder_structure[current_folder]["summed"] = True
    return folder_structure[current_folder]["totalsize"]



# Open the input file
with open("7-input.txt", "r") as input_file:
  # Read the contents of the file
  input_string = input_file.read()

# Parse the output of the `cd` and `ls` commands
output_lines = input_string.split("\n")

# Create a dictionary to store the folder structure
folder_structure = {}
current_folder = ""

# Iterate over each line of the output
path = "/"
folder_structure["/"] = {"files": [], "subfolders": [], "size": 0, "totalsize": 0, "summed": False}
for line in output_lines[1:]:
  #print(line)
  # If the line starts with "cd", update the current folder
  if line.startswith("$ cd .."):
    asdf = ""
    path = path.rsplit("/", 2)[0] + "/"
    if path == "" :
        path = "/"
  elif line.startswith("$ cd "):  
    
    current_folder = line[5:]
    path += current_folder + "/"
    # Initialize the current folder in the folder structure dictionary
    if path in folder_structure.keys():
        asdf = str(folder_structure[path])
    else:
        folder_structure[path] = {"files": [], "subfolders": [], "size": 0, "totalsize": 0, "summed": False}
    #folder_structure[current_folder] = {"size": []}
    #folder_structure[current_folder] = {"subfolders": []}
  # If the line starts with "ls", parse the list of files
  elif line[0].isdigit() :
    #file in current folder
    files = line[:].split(" ")
    folder_structure[path]["files"].append(files)
    folder_structure[path]["size"] += int(files[0])
    
    #folder_structure[current_folder][size] = files[1]
  elif line.startswith("dir "):
    folder_structure[path]["subfolders"].append(path + line[4:] + "/")
  else:
    asdf = ""
    #print("Line not used - " + line)
  #elif line.startswith("$ ls "):
    
    #files = line[:].split(" ")
    # Store the list of files in the current folder
    #folder_structure[current_folder]["files"] = files
  #print(path)

#print(folder_structure)
#print("zgczmvng")
#print(folder_structure["zgczmvng"])

#for subs in folder_structure["/"]["subfolders"]:
#    print(foldersize(subs))


count = 0
for folder in folder_structure:
    totalsize = folder_structure[folder]["size"]
    subcount = 0
    for subfolder in folder_structure:
        #print(str(folder) + " and " + str(subfolder))
        if folder == subfolder :
            asdf = ""
            #print("same folder found, ignoring")
        elif subfolder.startswith(folder):
            #print("subfolder found, adding")
            totalsize += folder_structure[subfolder]["size"]
        else:
            asdf = ""
            #print("not a subfolder")
    folder_structure[folder]["totalsize"] = totalsize

#print(folder_structure["zgczmvng"])
print("sizes calced")
#print(folder_structure)

# Iterate over each folder in the folder structure dictionary
sum = 0
for folder, folder_data in folder_structure.items():
  #print(folder + " " + str(folder_structure[folder]["totalsize"]))
  # Initialize the total size of the files in the folder
  if folder_structure[folder]["totalsize"] <= 100000:
    print(folder + ": " + str(folder_structure[folder]))
    if(folder == "zln"):
        print("zln found")
    sum += folder_structure[folder]["totalsize"]


print("part 1 : " + str(sum))

totalspace = 70000000
availablespace = totalspace - folder_structure["/"]["totalsize"]
print(availablespace)
spaceneeded = 30000000 - availablespace
print(spaceneeded)
smallestfolder = ""
smallestsize = totalspace
for folder in folder_structure:
    if folder_structure[folder]["totalsize"] > spaceneeded and folder_structure[folder]["totalsize"] < smallestsize :
        smallestsize = folder_structure[folder]["totalsize"]
        smallestfolder = folder

print(folder_structure[smallestfolder])