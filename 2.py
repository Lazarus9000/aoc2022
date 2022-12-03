f = open("2-input.txt", "r")
input = f.read().splitlines() #read lines to list
readcount = 0 #count lines read
#total = [] #Array to hold sums
total = 0 #temp var to calculate elf total cal
secondtotal = 0
player1 = input[readcount][0]
player2 = input[readcount][2]

while readcount < len(input) :
    
    player1 = input[readcount][0]
    player2 = input[readcount][2]
    print(input[readcount])
    
    if(player2 == "X") :
        #print("1 point for rock")
        total += 1
        
    if(player2 == "Y") :
        #print("2 point for paper")
        total += 2    
    
    if(player2 == "Z") :
        #print("3 point for scissor")
        total += 3
    
    if((player1 == "A" and player2 == "X") or (player1 == "B" and player2 == "Y") or (player1 == "C" and player2 == "Z")) :
        #print("3 point for draw")
        total += 3
        
    elif((player1 == "A" and player2 == "Y") or (player1 == "B" and player2 == "Z") or (player1 == "C" and player2 == "X")):
        #print("6 point for win")
        total += 6
    else:
        #looose
        #print("0 point for loose")
        total += 0
    
    #print(total)
    
    if(player2 == "Z") :
        #need to win
        secondtotal += 6
        if(player1 == "A") :
            #player choose rock, I chose paper
            secondtotal += 2
        elif(player1 == "B") :
            #player choose paper, I chose scissor
            secondtotal += 3
        elif(player1 == "C") :
            #player choose scissor, I chose rock
            secondtotal += 1
        #print("1 point for rock")
        
        
    if(player2 == "Y") :
        #need draw
        secondtotal += 3
        if(player1 == "A") :
            #player choose rock, I chose rock
            secondtotal += 1
        elif(player1 == "B") :
            #player choose paper, I chose paper
            secondtotal += 2
        elif(player1 == "C") :
            #player choose scissor, I chose scissor
            secondtotal += 3
    
    if(player2 == "X") :
        #need loose
        secondtotal += 0
        if(player1 == "A") :
            #player choose rock, I chose scissor
            secondtotal += 3
        elif(player1 == "B") :
            #player choose paper, I chose rock
            secondtotal += 1
        elif(player1 == "C") :
            #player choose scissor, I chose paper
            secondtotal += 2
    
    
    readcount += 1 #increment line to read
    
print(total)
print(secondtotal)
