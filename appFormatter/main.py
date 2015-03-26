'''
Created on Dec 21, 2014

    main.py: Run this file to get your results. Directions are as follows
    
        1.) Download spreadsheet from tutor apps tab in .csv format
        2.) (optional, highly recommended) Rename .csv file to something short and recognizable
        3.) Put .csv file inside the 'inputFiles' folder inside the same directory this file is in
        4.) Put the name of your .csv file (include the .csv part) inside the first two lines of this main method below
        5.) Run the file
        6.) When prompted, input a short tag (this will help differentiate outputs from another if you wish)
        7.) If all goes well, the resulting files should show up in the 'outputFiles' folder directory inside the same directory this file is in
    
    IMPORTANT NOTES: This script is ridiculously specialized and hacky right now. Any noticeable changes to the tutor application
                     WILL LIKELY cause this program to crash. Be careful. I've heavily commented each function so finding errors 
                     shouldn't be too difficult.
@author: Andrew Yang
'''

import csvDataHandling
import csvFormat
import csvIO

if __name__ == '__main__':
    #Enter the name of the CSV file you want to process. Do not add any specific path changes.
    rawDataDict = csvIO.readCSVFileToDict('test.csv')# <------ CHANGE FILE NAME HERE
    rawDataList = csvIO.readCSVFileToList('test.csv')# <------ AND HERE
    print("Successfully read input file into raw data...")
    
    outputFileTag = "test" #<------CHANGE FILE NAME HERE (No need to append the .csv part)
    
    #Gather and join ineligible tutors
    allIneligibles = csvDataHandling.findGPAIneligible(rawDataDict)  #Start with GPA ineligible tutors
    allIneligibles.extend(csvDataHandling.findAttendanceIneligible(rawDataDict)) #Add ICS 193 attendance ineligible tutors
    
    allIneligibles = csvFormat.removeDuplicates(allIneligibles) #Final list of ineligible tutors (with duplicates removed)
    ineligibleIDs = csvFormat.getIneligibleIDs(allIneligibles) #Get student ID list of ineligible tutors
    
    eligiblesDict = csvDataHandling.findEligibleDict(rawDataDict, ineligibleIDs) #Use that list right above to find your eligible tutors
    eligiblesList = csvDataHandling.findEligibleList(rawDataList, ineligibleIDs) #The list form of the same information above. 
    
    allEligibles = csvDataHandling.buildStudentList(eligiblesDict, eligiblesList) #This is where you get your list of student namedtuples
    eligibleFirstTimers = csvFormat.getEligibleFirstTimers(allEligibles) #Isolate first time applicants
    eligibleReturnees = csvFormat.getEligibleReturnees(allEligibles) #Isolate returning applicants
    
    #Gathering the list of formatted strings to write to output files
    writeIneligibles = csvFormat.getIneligibleMessages(allIneligibles) #ineligibles 
    writeEligibleReturnees = [csvFormat.buildReturningStudentString(student) for student in eligibleReturnees] #returnees
    writeEligibleFirstTimers = [csvFormat.buildFirstTimeStudentString(student) for student in eligibleFirstTimers] #first timers
    writeLogistics = csvFormat.buildLogistics(eligiblesList, len(rawDataList), len(eligibleFirstTimers), len(eligibleReturnees), len(ineligibleIDs))
    
    
    #process of writing the three output files: ineligible students, first time candidates and returning tutors
    csvIO.writeToOutputFile(outputFileTag+'_Ineligible_Tutors.txt', writeIneligibles, "These are ineligible students")
    print("Successfully wrote ineligible students to '{}' in outputFiles folder".format(outputFileTag+'_Ineligible_Tutors.txt'))
    
    csvIO.writeToOutputFile(outputFileTag+'_Returning_Tutors.txt', writeEligibleReturnees, "These are returning tutors")
    print("Successfully wrote returning tutors to '{}' in outputFiles folder".format(outputFileTag+'_Returning_Tutors.txt'))
    
    csvIO.writeToOutputFile(outputFileTag+'_Candidate_Tutors.txt', writeEligibleFirstTimers, "These are first-time candidates")
    print("Successfully wrote first time candidates to '{}' in outputFiles folder".format(outputFileTag+'_Candidate_Tutors.txt'))
    
    csvIO.writeLogistics(outputFileTag+'_Logistics.txt', writeLogistics)
    print("Successfully wrote logistical details to {} in outputFiles folder".format(outputFileTag+'_Logistics.txt'))
    

