# The Plan:
# Step 1: Get User Input (all of the files to be checked)
# Step 2: Create a list of all the CSV files in that folder
# Step 3: Create a list for all of the accepted and rejected voters
# Step 3.5: Add every person in the first CSV file to the accepted list
# Step 4: Open the next file and read each person (depends on Zoom formatting)
# Question 1: Is this person in the rejects list?
#   If so, throw them out. Else, continue
# Question 2: Is this person in the accepted list?
#   If so, do nothing.
# Question 4: Did any names appear in accepted but not the file?
#   If so, move them to rejects
# Step 5: Once out of people, close the file
# Question 3: Are there any more files left in the file list?
#   If so, go back to Step 4. Else, contiune
# Step 6: Create a CSV file (or open a provided CSV file and write to that)
# Step 7: Write every person into the accepted list in the way Helios likes
# Step 8: Close the output file and end the script

import csv

#Step 3:
Accpets = []
Rejects = []
IDNumber = 0    #yes, I know giving out ID numbers that increment up isn't secure, but I can make sure the same number doesn't happen twice and shutup abbouttit this
                #is a processing system for a club election chiiiiiiiiiiiiiill
nameIndex = 0   #The index of the names in a Zoom attendence sheet
emailIndex = 1  #The index of the emails in a Zoom attendence sheet
maxMisses - 0   #How many meetings can be missed before a club member is rejected from voting

#Step 1 and 2:
ready = false
fileNames = [input("Enter names of the attendence files, then enter nothing to contiune")]
while(false == false):
    newName = input()
    if(newName == ""): ready = true
    else: fileNames.append(newName)

#Step 3.5
with open(fileNames[0], "r", newline='') as csvfile:    #opens the needed file      needs newline='' to interact with the csvWriter correctly
    csvReader = csv.reader(csvfile)                     #creates reader object      might need dialect='excel'
    for row in csvReader: Accepts.append(VoterID(row[nameIndex], row[emailIndex])) #creates new VoterID objects from file data
fileNames.pop(0)    #remove the first file, which will be used as

#Step 4 and Question 3
for file in fileNames:
    #Step 5 and Question 1 and 2
    successful = process(file)  #success checking might not be needed
    if not successful: print("Error: File " + file + " could not be process successfully\n")

#Step 6 and 7
with open(attendenceOutput.csv, "x", newline='') as csvfile:    #creates a new file                         needs newline='' to interact with the csvWriter correctly
    csvWriter = csv.writer(csvfile)                             #creates writer object                      might need dialect='excel'
    for voter in Accepts: csvWriter.writerow(voter.getRow())    #writes to the file using writer object     do I need to cast voter as VoterID?

#Step 8
sys.exit(0)

#---------------------------------------------------------

def process(fileName):
    VotersInFile = []
    
    #Get all potential voters from the file
    with open(fileName, "r", newline='') as csvfile:    #opens the needed file      needs newline='' to interact with the csvWriter correctly
        csvReader = csv.reader(csvfile)                 #creates reader object      might need dialect='excel'
        for row in csvReader: VotersInFile.append(VoterID(row[nameIndex], row[emailIndex])) #creates new VoterID objects from file data

    #We now have all the new voters. Time to compare lists
        
    #First Comparison: Remove potential voters that have already been rejected
    for voter in VotersInFile:
        if voter in Rejects:
            VotersInFile.remove(voter)
            Rejects.append(voter)

    #Second Comparison: Add 1 miss to every Accept not in VotersInFile
    for voter in Accepts:
        if voter in VotersInFile: VotersInFile.remove(voter)
        else: ++voter.misses

    #Third Comparison: Add everyone from VotersInFile to Accept and give them 1 miss
    for voter in VotersInFile:
        ++voter.misses
        Accepts.append(voter)

    #Fourth Comparison: Move everyone in Accepts with too many misses to Rejects
    for voter in Accepts:
        if voter.misses > maxMisses:
            Accepts.remove(voter)
            Rejects.append(voter)

    #This should make sure that only voters with less than maxMisses are in Accepts

#---------------------------------------------------------

class VoterID:
    def __init__(self, name, email):
        self.ID = IDNumber
        ++IDNumber
        self.name = name
        self.email = email
        self.misses = 0

    def __eq__(self, other):
        if not isinstance(other, VoterID):
            return NotImplemented
        
        return self.ID == other.ID and self.name == other.name and self.email == other.email

    #returns ID, name, and email in an iterable list for CSV writing
    def getRow(self):
        return [ID, name, email]
