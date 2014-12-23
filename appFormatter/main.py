'''
Created on Dec 21, 2014

@author: Andrew Yang
'''

import csvDataHandling
import csvFormat
import csvIO

if __name__ == '__main__':
    #Enter the name of the CSV file you want to process. Do not add any specific path changes.
    rawDataDict = csvIO.readCSVFileToDict('test.csv')# <------ Change file here
    rawDataList = csvIO.readCSVFileToList('test.csv')# <------ and here
    print("Successfully read input file into raw data...")
    
    outputFileTag = input("Enter your desired output file tag (Warning - Entering a name that already exists will overwrite the file!): ")
    
    #Gather and join ineligible tutors
    allIneligibles = csvDataHandling.findGPAIneligible(rawDataDict)  #Start with GPA ineligible tutors
    allIneligibles.extend(csvDataHandling.findAttendanceIneligible(rawDataDict)) #Add ICS 193 attendance ineligible tutors
    
    allIneligibles = csvFormat.removeDuplicates(allIneligibles) #Final list of ineligible tutors (with duplicates removed)
    ineligibleIDs = csvFormat.getIneligibleIDs(allIneligibles)
    writeIneligibles = csvFormat.getIneligibleMessages(allIneligibles) #List of strings to write to file
    
    eligiblesDict = csvDataHandling.findEligibleDict(rawDataDict, ineligibleIDs)
    eligiblesList = csvDataHandling.findEligibleList(rawDataList, ineligibleIDs)
    allEligibles = csvDataHandling.buildStudentList(eligiblesDict, eligiblesList) 
    
    writeEligibleFirstTimers = csvFormat.getEligibleFirstTimers(allEligibles)
    writeEligibleReturnees = csvFormat.getEligibleReturnees(allEligibles)
    
    csvIO.writeIneligiblesToOutputFile(outputFileTag+'_Ineligible_Tutors.txt', writeIneligibles)
    print("Successfully wrote ineligible tutors to '{}' in outputFiles folder".format(outputFileTag+'_Ineligible_Tutors.txt'))
    

