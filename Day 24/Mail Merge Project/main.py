#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

from os import sys, path

with open(path.join(sys.path[0],"Input/Letters/starting_letter.txt"), "r") as f:
    lines = []
    for line in f.readlines():
        lines.append(line)

with open(path.join(sys.path[0],"Input/Names/invited_names.txt"), "r") as fl:
    names = []
    for name in fl.readlines():
        names.append(name.strip('\n'))

for n in names:
    file_name = "/Users/abhisheksabnivis/Desktop/100daysofcode/Day 24/Mail Merge Project/Output/ReadyToSend/letter_for_" + str(n) + ".txt"
    with open(file_name, "w") as file:
        for ln in lines:
            file.writelines(ln.replace("[name]",n,1))