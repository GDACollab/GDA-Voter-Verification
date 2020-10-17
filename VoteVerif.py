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

# Okay, Eric is taking over.
# So, what we need is a repository of emails that have attended at least 3 meetings.
# Names should also match, but I'd rather just base it off the emails.
# They should have also stayed for more than just a moment, let's say 15 mins. 
# Step 1: Take in the variables with which we'll be working with
#   This will involve taking in the index numbers where key information is located.
# Step 2: Create the voter registry
# Step 3: Logs every single person in the attendance CSVs
#   Finds discrepancies (emails that were not registered and names that matched, but the emails were wrong)
#   Also marks the specific meeting at which you were fully qualified to vote.
# Step 4: Create a new CSV file
#   This will first contain a list of all registered voters.
#   Followed by a list of all discrepancies.
#   Followed by a list of all attendees that have not yet registered.
# Step 5: Return the new CSV file.

import csv

# Step 1: Take in the variables with which we'll be working with.
fileNames = []

# Here we're asking a bunch of questions such as what are the names of the files, what position can I find the vital information?
nameIndex = int(input("What column are the names in the csv files?"))
emailIndex = int(input("What column are the emails in the csv files?"))
timeIndex = int(input("What column are the timed durations located?"))
weeksOfProcessing = int(input("How many weeks are we processing today?"))
for i in range(weeksOfProcessing):
    newName = input("Please enter week " + str(i+1) + "'s CSV file, or enter nothing to skip.")
    if (newName == ""): continue
    else: filesNames.append(newName)
emailCSV = input("Please enter the csv file containing all registered voters.")
registeredEmailIndex = int(input("What column are the emails for this CSV file?"))
registeredNameIndex = int(input("What column are the names for this CSV file?"))
print("Processing...")

#Step 2: Create the voter registry.
voterRoll = []

# This will go through the entire registered voter roll and create that list.
with open(emailCSV, "r", newline='') as csvfile:
    csvReader = csv.reader(csvfile)
    for row in csvReader: voterRoll.append(VoterID(row[registeredNameIndex],row[registeredEmailIndex], True))

# Step 3: Process the attendance of all registered members
notRegisteredRoll = []
badNameRoll = []
confirmedRoll = []

# We're going through the files one by one and sending them to be processed.
for file in fileNames:
    successful = process(file)  #success checking might not be needed
    if not successful: print("Error: File " + file + " could not be process successfully\n")






#Step 3:
Accepts = []
Rejects = []
#IDNumber = 0    #yes, I know giving out ID numbers that increment up isn't secure, but I can make sure the same number doesn't happen twice and shutup abbouttit this
                #is a processing system for a club election chiiiiiiiiiiiiiill
                # Nah, we really don't need this. 
nameIndex = 0   #The index of the names in a Zoom attendence sheet
emailIndex = 1  #The index of the emails in a Zoom attendence sheet
# maxMisses = 0   #How many meetings can be missed before a club member is rejected from voting

#Step 1 and 2:
ready = False
fileNames = [input("Enter names of the attendence files, then enter nothing to contiune")]
while(ready == False):
    newName = input()
    if(newName == ""): ready = True
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
    fileAccess = []
    

    #Get all the people in attendance with the meeting.
    with open(fileName, "r", newline='') as csvfile:    #opens the needed file      needs newline='' to interact with the csvWriter correctly
        csvReader = csv.reader(csvfile)                 #creates reader object      might need dialect='excel'
        for row in csvReader: fileAccess.append(VoterID(row[nameIndex], row[emailIndex])) #creates new VoterID objects from file data

    # We're checking if this person is on the registered list of 
    for voter in fileAccess:
        if voter in Accepts:



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
        self.name = name
        self.email = email
        self.registered = False
        self.attends = 0
        self.additional_names = []

    def __eq__(self, other):
        if not isinstance(other, VoterID):
            return False
        return self.name == other.name and self.email == other.email

    #returns ID, name, and email in an iterable list for CSV writing
    def getRow(self):
        return [, self.name, self.email]