'''
Created on Dec 21, 2014

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

def writeIneligiblesToOutputFile(fileName, information):
    os.chdir('outputFiles')
    try:
        writeFile = open(fileName, 'w')
        writeFile.write("========================================\nThe following are ineligible tutors\n========================================\n")
        for line in information:
            writeFile.write(line)
            writeFile.write("\n=============================\n")
    finally:
        writeFile.close()
    