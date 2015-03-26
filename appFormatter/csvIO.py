'''
Created on Dec 21, 2014

    csvIO.py: This module handles all standard I/O functionality.
    
    Functions inside:
        readCSVFileToDict(fileName)
        readCSVFileToList(fileName)
        writeLogistics(fileName, information)
        writeToOutputFile(fileName, information, kind)

@author: Andrew Yang
'''
import csv
import os


'''================================
   readCSVFileToDict - Parameter(s):  String 'fileName', represents name of CSV file to read
                       Return type:   List, each element in the list is a dictionary representing a single applicant's information
   ================================'''
def readCSVFileToDict(fileName):
    try:
        csvFile = open(os.path.join('inputFiles', fileName))
        reader = csv.DictReader(csvFile)
        dictList = [applicant for applicant in reader]
        return dictList
    except (FileNotFoundError):
        raise Exception("Entered an invalid file name in your call to readCSVFileToDict. Make sure you entered the correct file name.")
    except:
        print("Unknown Error. Debug in readCSVFileToDict function in csvDataHandling.py")


'''================================
   readCSVFileToList - Parameter(s):  String 'fileName', represents name of CSV file to read
                       Return type:   List, each element in the list is a list representing a single applicant's information
                       (Note: This alternative is needed to resolve the non-unique keys issue in the application)
   ================================'''
def readCSVFileToList(fileName):
    try:
        csvFile = open(os.path.join('inputFiles', fileName))
        reader = csv.reader(csvFile)
        next(reader)
        dictList = [applicant for applicant in reader]
        return dictList
    except (FileNotFoundError):
        raise Exception("Entered an invalid file name in your call to readCSVFileToList. Make sure you entered the correct file name.")
    except:
        print("Unknown Error. Debug in readCSVFileToList function in csvDataHandling.py")


'''==============================
   writeLogistics - Parameter(s):  String 'fileName', represents name of CSV file to write
                                   String 'information', represents string of logistical details to write to file
                    Return type:   None, but output files should be created in /outputFiles directory
   =============================='''
def writeLogistics(fileName, information):
    initialDirectory = os.getcwd()
    os.chdir('outputFiles')
    try:
        writeFile = open(fileName, 'w')
        writeFile.write("==========================================================================================\n")
        writeFile.write("If you would like to add more details, refer to the 'buildLogistics' function in csvFormat\n")
        writeFile.write("==========================================================================================\n\n")
        writeFile.write(information)
    finally:
        writeFile.close()
        os.chdir(initialDirectory)


'''================================
   writeToOutputFile - Parameter(s):  String 'fileName', represents name of CSV file to write
                                      list 'information', each element is a formatted string containing tutor 
                                                          information to write directly into file
                                      String 'kind', represents message to be printed on top of the file
                       Return type:   None, but output files should be created in /outputFiles directory
   ================================'''
def writeToOutputFile(fileName, information, kind):
    initialDirectory = os.getcwd()
    os.chdir('outputFiles')
    try:
        writeFile = open(fileName, 'w')
        writeFile.write("========================================\n{}:\n========================================\n".format(kind))
        for line in information:
            writeFile.write(line)
            writeFile.write("\n=============================\n")
    finally:
        writeFile.close()
        os.chdir(initialDirectory)
    
