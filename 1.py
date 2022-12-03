f = open("1-input.txt", "r")
input = f.read().splitlines() #read lines to list
readcount = 0 #count lines read
cal = [] #Array to hold sums
tempcal = 0 #temp var to calculate elf total cal

while readcount < len(input) - 1 :
    
    while input[readcount] != "" :
        tempcal += int(input[readcount]) #sum up calories!
        readcount += 1
        if(readcount > len(input) - 1) :
            break #ensures the reader doesn't go out of bounds
        #print(readcount)

    cal.append(tempcal) #Save temp in list
    readcount += 1 #increment line to read
    tempcal = 0 #reset temp cal
    
#print(sorted(cal))

print(sorted(cal)[len(cal)-1]) #most amount of calories

#Sum of top 3 most calories
print(sorted(cal)[len(cal)-1]+sorted(cal)[len(cal)-2]+sorted(cal)[len(cal)-3])
