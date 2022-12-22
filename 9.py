import copy
# Open the file in read mode
with open("9-input.txt", "r") as f:
    # Read the contents of the file into a string
    contents = f.read()

def setxy(x,y,array,value):
    array[y] = replacer(array[y], value, x)

def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]
    
# Split the string into a list of lines
lines = contents.splitlines()
limits = 2000
positions = []
for i in range(limits):
    positions.append(".")
    for j in range(limits-1):
        positions[i] = positions[i] + "."

#positions[9] = replacer(positions[9], "X", 1)
#setxy(0,9,positions,"X")
initx = int((limits-1)/2)
inity = int((limits-1)/2)

visited = copy.deepcopy(positions)
#print(positions)
#print(positions[9])
currenthx = initx
currenthy = inity
currenttx = initx
currentty = inity
lasthx = initx
lasthy = inity
lasttx = initx
lastty = inity

notinitial = False
# Iterate over the list of lines
for line in lines:
    input = line.split(" ")
    steps = int(input[1])
    dir = input[0]
    # Split the line into a list of characters and append it to the 2D list
    print("instruction: " + line)
    for i in range (steps):
        if dir == "R":
            currenthx += 1
        
        if dir == "L":
            currenthx -= 1
            
        if dir == "U":
            currenthy -= 1
        
        if dir == "D":
            currenthy += 1    
        
        if notinitial:
            if abs(currenthx - currenttx) > 1 or abs(currenthy - currentty) > 1:
                if currenthy == currentty:
                    if currenthx > currenttx:
                        currenttx += 1
                    else:   
                        currenttx -= 1
                        
                elif currenthx == currenttx:
                    if currenthy > currentty:
                        currentty += 1
                    else  : 
                        currentty -= 1
                else:
                    if currenthy > currentty:
                        currentty += 1
                    else  : 
                        currentty -= 1
                        
                    if currenthx > currenttx:
                        currenttx += 1
                    else  : 
                        currenttx -= 1
                        
        
        print("head: " + str(currenthx) + ", " + str(currenthy))
        print("tail: " + str(currenttx) + ", " + str(currentty))
        
        
        setxy(lasttx,lastty,visited,"#")
        setxy(lasttx,lastty,positions,"#")
        lasttx = currenttx
        lastty = currentty
        
        setxy(lasthx,lasthy,positions,".")
        lasthx = currenthx
        lasthy = currenthy
        
        setxy(initx,inity,positions,"s")
        setxy(currenttx,currentty,positions,"T")
        setxy(currenthx,currenthy,positions,"H")
        
        notinitial = True
        
        #print(positions)

count = 0
for line in visited:
    for char in line:
        if char == "#":
            count += 1
print("part1 - count")
print(count)
print("for some reason the answer is one to low")
print(count+1)
#print(visited)
        