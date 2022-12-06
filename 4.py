# Read lines from the file
with open('4-input.txt', 'r') as f:
    lines = f.readlines()

# Initialize counter
counter = 0
counteroverlap = 0
# Parse pairs of numbers from each line
for line in lines:
    pairs = line.split(',')
    
    numbers = pairs[0].split('-')
    start = int(numbers[0])
    end = int(numbers[1])

# Get start and end values of the other pair
    other_numbers = pairs[1].split('-')
    other_start = int(other_numbers[0])
    other_end = int(other_numbers[1])

# Check if one range fully covers the other
    if (start <= other_start and end >= other_end) or (start >= other_start and end <= other_end):
        counter += 1
        
    if start <= other_end and end >= other_start:
        counteroverlap += 1

# Print the final value of the counter
print(counter)
print(counteroverlap)