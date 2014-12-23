'''
Created on Dec 21, 2014

@author: Andrew Yang
'''

import csvFormat

'''=======================================
   findAttendanceIneligible - Parameter(s):  List 'rawData', represents dictionaries of applicant information
                              Return type:   List, each element in the list is a dictionary representing a single applicant's information
   ======================================='''
def findAttendanceIneligible(rawData):
    return [applicant for applicant in rawData
            if applicant["Are you available to attend ICS 193?"] == "No" and applicant["Have you tutored with us before?"] == "No"]

  
'''===============================
   findGPAIneligible - Parameter(s):  List 'rawData', represents dictionaries of applicant information
                       Return type:   List, each element in the list is a dictionary representing a single applicant's information
   ==============================='''
def findGPAIneligible(rawData):
    return [applicant for applicant in rawData
            if float(applicant['ICS GPA']) < 2.5 or float(applicant['Overall GPA']) < 2.5]


'''================================
   findEligibleDict -  Parameter(s):  list 'rawData', represents dictionaries of applicant information
                                      list 'ineligibles', represents student ID's (in string form) of ineligible tutors
                       Return type:   copy of input list with ineligible tutors removed
   ================================'''
def findEligibleDict(rawData, ineligibles):
    return [applicant for applicant in rawData
            if applicant["Student ID Number"] not in ineligibles]
    

'''================================
   findEligibleList -  Parameter(s):  list 'rawData', represents lists of applicant information
                                      list 'ineligibles', represents student ID's (in string form) of ineligible tutors
                       Return type:   copy of input list with ineligible tutors removed
   ================================'''
def findEligibleList(rawData, ineligibles):
    return [applicant for applicant in rawData
            if applicant[5] not in ineligibles]


def buildStudentGrades(studentDict, studentList): #EDIT THIS FUNCTION WHEN 45J COMES UP AND/OR APPLICATION FORM CHANGES
    classList = ["ICS31", "ICS32", "ICS33", "ICS45J", "ICS45C", "ICS46"]
    gradeDict = {}
    increment = 0
    for i in range(15,24,4):
        if studentList[i] == "Yes":
            gradeDict[classList[increment]] = [studentList[i+1], studentList[i+2]]
        ++increment
    ++increment #skip past 45J
    for i in range(27,36,8):
        if studentList[i] == "Yes":
            gradeDict[classList[increment]] = [studentList[i+1], studentList[i+2]]
        ++increment
    return gradeDict

            
def determineFirstTime(studentDict):
    return studentDict["Have you tutored with us before?"] == "No"


def getResponses(studentList):
    return [studentList[12], studentList[13], studentList[14]]

    
def buildStudent(studentDict, studentList):
    name = "{} '{}' {}".format(studentDict["First Name"], studentDict["Preferred Name"], studentDict["Last Name"])
    email = "{}@uci.edu".format(studentDict["UCnetID"])
    ID = studentDict["Student ID Number"]
    gpa = "Overall GPA: {}\nICS GPA: {}\n".format(studentDict["Overall GPA"], studentDict["ICS GPA"])
    classes = buildStudentGrades(studentDict, studentList)
    firstTime = determineFirstTime(studentDict)
    if firstTime == True:
        responses = getResponses(studentList)
    else:
        responses = []
    return csvFormat.Student(name, email, ID, gpa, classes, firstTime, responses)


def buildStudentList(eligiblesDict, eligiblesList):
    sortedDict = sorted(eligiblesDict, key = lambda k: k['Last Name'].lower())
    sortedList = sorted(eligiblesList, key = lambda k: k[3].lower()) 
    return [buildStudent(sortedDict[i], sortedList[i]) for i in range(len(sortedList))]
    



