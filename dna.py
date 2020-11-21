from sys import argv, exit
import csv

# Check for CLA
if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit()

# Open the csv file
with open(argv[1], newline='') as csvfile:
    reader = list(csv.reader(csvfile))
    # List of the STRs we are looking for
    strs_list = reader[0][1:]
    rest = list(reader[1:])

# Turn STR list to a dictionary
strs = dict.fromkeys(strs_list, 0)

# Open the Sequence.text
f = open(argv[2], "r")
sequence = f.read()

# Loop over each STR in STRS-LIST, then loop over the sequence to find the max number of times the STR was repeated consecutively, then add that to the Dictionary
for item in strs_list:
    i = 0
    counter = 0
    while i < len(sequence):
        current = sequence[i: i + len(item)]
        if current == item:
            counter += 1
            i += len(item)
            if counter > strs[item]: 
                strs[item] = counter
        else:
            counter = 0
            i += 1


# Find if there is a match by looping over the people in the CSV file, and comparing the results with the sequence.text
match = False
for array in rest:
    match = True
    for j in range(len(strs_list)):
        if int(array[1:][j]) != strs[strs_list[j]]:
            match = False
            break
    if match == True:
        print(array[0:1][0])
        break

if match == False:
    print("No match")
    