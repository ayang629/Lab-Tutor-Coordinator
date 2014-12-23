'''
Created on Dec 21, 2014

    csvDataHandling.py: This module is mostly concerned with handling raw data from input files and creating simple
                        data structures from purely raw input data.
    
    Objects Defined:
        "Student" namedtuple
        
    Functions Defined:
        Helper:
            buildStudentClassInterest(studentDict, studentList)
            buildStudent(studentDict, studentList)
            determineFirstTime(studentDict)
            getResponses(studentList)
        Normal:
            buildStudentList(eligiblesDict, eligiblesList)
            findAttendanceIneligible(rawData)
            findGPAIneligible(rawData)
            findEligibleDict(rawData, ineligibles)
            findEligibleList(rawData, ineligibles)
            
@author: Andrew Yang
'''

from collections import namedtuple

'''==================
   Student namedtuple: The definition of a student namedtuple is defined below. If expanded/condensed, please 
                       keep in mind this structure is used extensively in both this file and in csvDataHandling.py
   =================='''
Student = namedtuple('Student', 'name email id major gpa classes firstTime responses')


'''==========================================
    buildStudentClassInterest -  Parameter(s):  dictionary 'studentDict', represents a single student's information in dictionary form
                                                list 'studentList', represents a single student's information in list form
                                 Return type:   dictionary, keys = string: classes interested in
                                                            values = list: first element is grade details; second element is times available
    (HELPER FUNCTION TO buildStudent)
   =========================================='''
def buildStudentClassInterest(studentDict, studentList): #EDIT THIS FUNCTION WHEN 45J COMES UP AND/OR APPLICATION FORM CHANGES
    classList = ["ICS31", "ICS32", "ICS33", "ICS45J", "ICS45C", "ICS46"]
    gradeDict = {}
    increment = 0
    for i in range(15,24,4):
        if studentList[i] == "Yes":
            gradeDict[classList[increment]] = [studentList[i+1], studentList[i+2]]
        increment += 1
    increment += 1 #skip past 45J
    for i in range(27,36,8):
        if studentList[i] == "Yes":
            gradeDict[classList[increment]] = [studentList[i+1], studentList[i+2]]
        increment += 1
    return gradeDict


'''==========================================
    buildStudent -  Parameter(s):  dictionary 'studentDict', represents a single student's information in dictionary form
                                   list 'studentList', represents a single student's information in list form
                    Return type:   Correctly built Student namedtuple
    (HELPER FUNCTION TO buildStudentList)
   =========================================='''
def buildStudent(studentDict, studentList):
    name = "{} '{}' {}".format(studentDict["First Name"], studentDict["Preferred Name"], studentDict["Last Name"])
    email = "{}@uci.edu".format(studentDict["UCnetID"])
    major = studentDict["Major"]
    ID = studentDict["Student ID Number"]
    gpa = "Overall GPA: {}\nICS GPA: {}\n".format(studentDict["Overall GPA"], studentDict["ICS GPA"])
    classes = buildStudentClassInterest(studentDict, studentList)
    firstTime = determineFirstTime(studentDict)
    if firstTime == True:
        responses = getResponses(studentList)
    else:
        responses = []
    return Student(name, email, ID, major, gpa, classes, firstTime, responses)

'''==========================================
    buildStudent -  Parameter(s):  dictionary 'studentDict', represents a single student's information in dictionary form
                    Return type:   True if student is a first-time applicant, False if student is a returning tutor
    (HELPER FUNCTION TO buildStudentList)
   =========================================='''          
def determineFirstTime(studentDict):
    return studentDict["Have you tutored with us before?"] == "No"


'''==========================================
    getResponses -  Parameter(s):  list 'studentList', represents a single student's information in list form
                    Return type:   list, each element is a string of applicant FRQ responses
    (HELPER FUNCTION TO buildStudentList)
   =========================================='''
def getResponses(studentList):
    return [studentList[12], studentList[13], studentList[14]]
  
'''==========================================
    buildStudentList -  Parameter(s):  dictionary 'studentDict', represents a single student's information in dictionary form
                                       list 'studentList', represents a single student's information in list form
                        Return type:   list, each element is a correctly built Student namedtuple
   =========================================='''
def buildStudentList(eligiblesDict, eligiblesList):
    sortedDict = sorted(eligiblesDict, key = lambda k: k['Last Name'].lower())
    sortedList = sorted(eligiblesList, key = lambda k: k[3].lower()) 
    return [buildStudent(sortedDict[i], sortedList[i]) for i in range(len(sortedList))]


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


