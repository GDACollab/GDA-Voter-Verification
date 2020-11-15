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
#   This will use the GDA interest meeting as a 
# Step 3: Logs every single person in the attendance CSVs
#   Finds discrepancies (emails that were not registered and names that matched, but the emails were wrong)
#   Also marks the specific meeting at which you were fully qualified to vote.
# Step 4: Create a new CSV file
#   This will first contain a list of all registered voters.
#   Followed by a list of all discrepancies.
#   Followed by a list of all attendees that have not yet registered.
# Step 5: Return the new CSV file.

import csv
#---------------------------------------------------------

# Process is intended to go through a CSV, then output a list of every single person that showed up that meeting.
# It will go row by row, and find the name.
# Once it has done that, it'll start counting up how long each person had been here.
# After counting up everything, it returns a 
def process(fileName):
    # Meeting log is the dictionary that will link each name with a VoterID.
    meetingLog = {}
    confirmedAttendance = []

    # Get all the people in attendance with the meeting.
    # It goes row by row and starts counting how many minutes they were here.
    with open(fileName, "r", newline='') as csvfile:    #opens the needed file      needs newline='' to interact with the csvWriter correctly
        csvReader = csv.reader(csvfile)                 #creates reader object      might need dialect='excel'
        first_skip = True
        for row in csvReader: 
            # Skipping the first row.
            if first_skip:
                first_skip = False
                continue
            # Now we're moving through the rows.
            voterName = row[nameIndex]
            # If we find that the voter is already logged in the voterRoll, we add their time to the total time of the meeting.
            if voterName in meetingLog:
                meetingLog[voterName] += int(row[timeIndex])
            # If they didn't appear already, then we add them to the meeting log.
            else:
                meetingLog.update({ voterName : int(row[timeIndex])})

    # This makes sure every attendee meets the time requirement.
    # Only if they meet the time requirement are they counted for the meeting.
    for voter in meetingLog.keys():
        if meetingLog[voter] >= timeRequirement:
            confirmedAttendance.append(voter)

    return confirmedAttendance

# -----------------------------------------------------------------
# For Testing Purposes Only
#nameIndex = 0
#timeIndex = 4
#weeksOfProcessing = 2
#timeRequirement = 10
#fileNames = ['interest_meeting.csv', 'general_meeting_1.csv']


# Step 1: Take in the variables with which we'll be working with.
fileNames = []

# Here we're asking a bunch of questions such as what are the names of the files, what position can I find the vital information?
nameIndex = int(input("What column are the names in the csv files? (Number)"))
timeIndex = int(input("What column are the timed durations located? (Number)"))
weeksOfProcessing = int(input("How many weeks are we processing today?"))
for i in range(weeksOfProcessing):
    newName = input("Please enter week " + str(i+1) + "'s CSV file, or enter nothing to skip.")
    if (newName == ""): continue
    else: fileNames.append(newName)
timeRequirement = int(input("How many minutes will each member need to be at the meeting to count as a voting member?"))
print("Processing...")


# ------------------------------------------------------------------
# Step 2: Process a batch of the attendees.
# This involves passing a file over to the process function, which will get us a list of people that attended the required number of minutes.
# After that, we add them into the VoterRoll dictionary, which tracks names as well as the number of visits they've made.

voterRoll = {} # Dictionary of voter names as well as what meetings they were able to make.

for aFile in fileNames:
    attendees = process(aFile)
    for person in attendees:
        if person in voterRoll:
            voterRoll[person] += 1
        else:
            voterRoll[person] = 1

# --------------------------------------------------------------------
# Step 3: Process the attendance of all registered members
#notRegisteredRoll = []
#badNameRoll = []
#confirmedRoll = []

# We're going through the files one by one and sending them to be processed.
#for file in fileNames:
#    successful = process(file)  #success checking might not be needed
#    if not successful: print("Error: File " + file + " could not be process successfully\n")


#Step 3:
#Accepts = []
#Rejects = []
#IDNumber = 0    #yes, I know giving out ID numbers that increment up isn't secure, but I can make sure the same number doesn't happen twice and shutup abbouttit this
                #is a processing system for a club election chiiiiiiiiiiiiiill
                # Nah, we really don't need this. 
#nameIndex = 0   #The index of the names in a Zoom attendence sheet
#emailIndex = 1  #The index of the emails in a Zoom attendence sheet
# maxMisses = 0   #How many meetings can be missed before a club member is rejected from voting

#Step 1 and 2:
#ready = False
#fileNames = [input("Enter names of the attendence files, then enter nothing to contiune")]
#while(ready == False):
#    newName = input()
#    if(newName == ""): ready = True
#   else: fileNames.append(newName)

#Step 3.5
#with open(fileNames[0], "r", newline='') as csvfile:    #opens the needed file      needs newline='' to interact with the csvWriter correctly
#    csvReader = csv.reader(csvfile)                     #creates reader object      might need dialect='excel'
#    for row in csvReader: Accepts.append(VoterID(row[nameIndex], row[emailIndex])) #creates new VoterID objects from file data
#fileNames.pop(0)    #remove the first file, which will be used as

#Step 4 and Question 3
#for file in fileNames:
#    #Step 5 and Question 1 and 2
#    successful = process(file)  #success checking might not be needed
#    if not successful: print("Error: File " + file + " could not be process successfully\n")

#Step 6 and 7
with open('attendenceOutput.csv', "x", newline='') as csvfile:    #creates a new file                         needs newline='' to interact with the csvWriter correctly
    csvWriter = csv.writer(csvfile)                             #creates writer object                      might need dialect='excel'
    for voter in voterRoll.keys(): csvWriter.writerow([voter,int(voterRoll[voter])])    #writes to the file using writer object     do I need to cast voter as VoterID?

#Step 8 Quit
quit()



#---------------------------------------------------------
# Voter ID is an object for tracking every single voter that comes through.
class VoterID:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.attends = 0
        self.additional_names = []

    def __eq__(self, other):
        if not isinstance(other, VoterID):
            return False
        return self.name == other.name and self.email == other.email

    #returns ID, name, and email in an iterable list for CSV writing
    #def getRow(self):
    #    return [, self.name, self.email]