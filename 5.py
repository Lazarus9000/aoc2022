import copy
# initialize a list of empty lists to hold the characters for each column
columns = [[] for _ in range(9)]

# read the first 8 lines of the file

with open('5-input.txt') as f:
    for i in range(8):
        # remove the first character from the line
        line = f.readline()[1:]
        #print(line)
        # iterate over the remaining characters in the line
        j = 0
        place = 0
        while j <= len(line):
            
            # if the character is not a space, add it to the corresponding column
            # and skip the next three characters
            #print(j)
            #print(line[j])
            if line[j] != ' ':
                #print("char found")
                columns[place].append(line[j])
                
                
                #if j > 33 :
                #    break
            j += 4
            place += 1

#print(columns)

i = 0
while i < len(columns) :
    columns[i].reverse()
    #print(columns[i])
    i += 1
    
#print(columns)
columnspt2 = copy.deepcopy(columns)
#print(columnspt2)

    
with open('5-input.txt') as f:
    for i, line in enumerate(f):
        #print(i)
        if i > 9 :
            #print(line)
            inputs = line.split(' ')
            stacks = int(inputs[1])
            fromcol = int(inputs[3])-1
            tocol = int(inputs[5])-1
            j = 0
            while j < stacks :
                if 0 == len(columns[fromcol]) :
                    break
                columns[tocol].append(columns[fromcol][-1])
                columns[fromcol].pop(-1)
                j += 1
            #print(columns)
#print(columns)

answer = ""
for i in columns :
    answer += i[-1]

#print(answer)

#print("pt2")
#print(columnspt2)
with open('5-input.txt') as f:
    for i, line in enumerate(f):
        #print(i)
        if i > 9 :
            #print(line)
            inputs = line.split(' ')
            stacks = int(inputs[1])
            fromcol = int(inputs[3])-1
            tocol = int(inputs[5])-1
            
            if(stacks > len(columnspt2[fromcol])) :
                #print("entire stack")
                
                columnspt2[tocol].extend(columnspt2[fromcol])
                columnspt2[fromcol] = []
            else :
                #print("part of stack")
                columnspt2[tocol].extend(columnspt2[fromcol][-stacks:])
                i = 0
                while i < stacks :
                    columnspt2[fromcol].pop(-1)
                    i += 1
            
            
            #print(columnspt2)
print(columnspt2)

answer2 = ""
for i in columnspt2 :
    answer2 += i[-1]

print(answer2)