def score_file(filename: str) -> int:
    # Open the file for reading
    with open(filename, 'r') as f:
        # Initialize the score to 0
        score = 0

        # Read all the lines in the file
        lines = f.readlines()

        # For each line in the file
        for line in lines:
            # Cut the line in half
            half1, half2 = line[:len(line) // 2], line[len(line) // 2:]

            # Compare the two halves
            found = False
            for c1 in half1:
                for c2 in half2:
                    # If the characters are the same (case-insensitive)
                    if c1 == c2:
                        # Add the score for the character
                        score += ord(c1.lower()) - ord('a')+1
                        # If the character is upper case, add 26 to the score
                        if c1.isupper():
                            score += 26
                        found = True
                    
                    if found :
                        break
                if found :
                        break
        # Return the total score
        return score
        

score = score_file('3-input.txt')
print(score)

def score_file2(file_name):
  # Open the file in read mode
  with open(file_name, "r") as file:
    # Initialize the score to 0
    score = 0

    # Read the first three lines
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()

    # Keep reading lines until there are no more lines to read
    while line1 and line2 and line3:
      # Iterate over the characters in the lines
      for c in line1:
        if c in line2 and c in line3:
          # If the character is in all three lines, calculate its score
          # If the character is uppercase, add 26 to the score
          score += ord(c) - ord('a') + 1 if c.islower() else ord(c) - ord('A') + 27
          
          # Break out of the loop
          break
      # Read the next three lines
      line1 = file.readline()
      line2 = file.readline()
      line3 = file.readline()

    # Return the final score
    return score
    

file_name = '3-input.txt'
final_score = score_file2(file_name)
print(final_score)