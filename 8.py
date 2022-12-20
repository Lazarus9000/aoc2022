# Open the file in read mode
with open("8-input.txt", "r") as f:
    # Read the contents of the file into a string
    contents = f.read()

# Split the string into a list of lines
lines = contents.splitlines()

# Create an empty 2D list
characters = []

# Iterate over the list of lines
for line in lines:
    # Split the line into a list of characters and append it to the 2D list
    characters.append(list(line))

#print(characters)

viscount = 0

height = len(characters[1:-1])
width = len(characters[0][1:-1])

for i in range(height):
    for j in range(width): 
        tree = characters[i+1][j+1]
        #print(str(j+1) + ", " + str(i+1) + " = " + tree)
        visible = True
        
        west = True
        for x in range(j+1):
            test = characters[i+1][x]
            #print(str(x) + " - " + str(test))
            if test >= tree:
                west = False
        
        east = True
        for x in range(j+2, width+2):
            test = characters[i+1][x]
            #print(str(x) + " - " + str(test))
            if test >= tree:
                east = False
        
        north = True
        for y in range(i+1):
            if characters[y][j+1] >= tree:
                north = False
        
        south = True
        for y in range(i+2, height+2):
            if characters[y][j+1] >= tree:
                south = False
        
        
        
        if north or south or east or west :
            #print(west)
            #print(east)
            #print(north)
            #print(south)
            
            visible = True
            #print("visible!")
        else:
            visible = False

        if visible:
            #print(str(j+1) + ", " + str(i+1) + " = " + tree + " is visible!")
            viscount += 1

viscount

print(viscount)

print(height+1)
print(width+1)
viscount += 2*(height+1)+2*(width+1)
print("part1: " + str(viscount))

maxscenic = 0
for i in range(height):
    for j in range(width): 
        tree = characters[i+1][j+1]
        #print(str(j+1) + ", " + str(i+1) + " = " + tree)
        #print(range(max(0,j-2), j+1))
        
        west = 0
        for x in range(j+1):
            test = characters[i+1][j-x]
            #print(str(x) + " - " + str(test))
            west += 1
            if test >= tree:
                break
        
        east = 0 
        #print(range(j+2, min(width+2,j+5)))
        for x in range(j+2, width+2):
        
            test = characters[i+1][x]
            #print(str(x) + " - " + str(test))
            east += 1
            if test >= tree:
                break
        #print(east)
        
        north = 0
        #print(range(max(0,i-2), i+1))
        for y in range(i+1):
            test = characters[i-y][j+1]
            #print(str(y) + " - " + str(test))
            north += 1
            if test >= tree:
                break
        #print(north)
        
        south = 0 
        
        #print(range(j+2, min(width+2,j+5)))
        for y in range(i+2, height+2):
        
            test = characters[y][j+1]
            #print(str(y) + " - " + str(test))
            south += 1
            if test >= tree:
                break
        #print(south)
        
        scenic = north*west*east*south
        if scenic > maxscenic:
            maxscenic = scenic
            
print(maxscenic)
        