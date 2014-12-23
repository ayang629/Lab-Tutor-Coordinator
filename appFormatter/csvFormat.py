'''
Created on Dec 21, 2014

@author: Andrew Yang
'''
from collections import namedtuple

Student = namedtuple('Student', 'name email id gpa classes firstTime responses')

'''
removeDuplicates - Parameter(s):  list, each element is a dictionary containing one applicant's information
                   Return value:  copy of the input list, with duplicates removed
'''
def removeDuplicates(applicantList):
    return [dict(t) for t in set([tuple(d.items()) for d in applicantList])]

'''
getIneligibleInformation - Parameter(s):  list, each element is a dictionary containing an ineligible applicant's information
                           Return value:  list of strings, each string is a student's ID number
'''
def getIneligibleIDs(ineligibles):
    return [applicant['Student ID Number'] for applicant in ineligibles]


def getIneligibleMessages(applicantList):
    messages = []
    for applicant in applicantList:
        switch = False
        message = "{} '{}' {}\nEmail: ({}@uci.edu)\n".format(applicant["First Name"], applicant["Preferred Name"], 
                                                   applicant["Last Name"], applicant["UCnetID"])
        if applicant["Are you available to attend ICS 193?"] == "No" and applicant["Have you tutored with us before?"] == "No":
            message += "First time tutor that cannot attend ICS 193"
            switch = True
        if float(applicant['ICS GPA']) < 2.5 or float(applicant['Overall GPA']) < 2.5:
            if switch == True:
                message += "\nGPA does not meet requirement"
            else:
                message += "GPA does not meet requirement"
        message += '\n'
        messages.append(message)
    return messages
            

def getEligibleFirstTimers(applicantList):
    return [applicant for applicant in applicantList if applicant.firstTime == True]


def getEligibleReturnees(applicantList):
    return [applicant for applicant in applicantList if applicant.firstTime == False]

#namedtuple('Student', 'name email id gpa classes firstTime responses')
def buildFirstTimeStudentString(student):
    result = "{}\nEmail: {}\n Student ID: {}\n{}".format(student.name, student.email, student.id, student.gpa)
    
#     for key,value in sorted(student.classes):
#         result += 
    
    
    
    
    
    
    
    
    
    