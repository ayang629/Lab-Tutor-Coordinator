'''
Created on Dec 21, 2014

    csvFormat.py: This module handles more abstract pieces of data. Most functions involve generating simple
                  data structures based off of cleaned up raw data generated from csvDataHandling functions

    Functions Defined:
        Helper:
            condenseFRQ(response)
        Normal:
            removeDuplicates(applicantList)
            getIneligibleIDs(ineligibles)
            getEligibleFirstTimers(applicantList)
            getEligibleReturnees(applicantList)
            getIneligibleMessages(applicantList)
            buildReturningStudentString(student)
            buildFirstTimeStudentString(student)
            
@author: Andrew Yang
'''
    
'''==========================
   condenseFRQ - Parameter(s):  A string representing a student's free response answer
                 Return value:  A formatted string that shortens line length by splitting each line by a sentence (denoted by a '.')
                                (IMPORTANT NOTE: HELPER FUNCTION, NOT USED OUTSIDE OF csvFormat)
   ==========================='''
def condenseFRQ(response):
    responseList = response.split('.')
    result = ""
    for line in responseList:
        result += line + "\n"
    return result


'''================================
   removeDuplicates - Parameter(s):  list, each element is a dictionary containing one applicant's information
                      Return value:  copy of the input list, with duplicates removed
   ================================'''
def removeDuplicates(applicantList):
    return [dict(t) for t in set([tuple(d.items()) for d in applicantList])]


'''================================
   getIneligibleIDs - Parameter(s):  list, each element is a dictionary containing an ineligible applicant's information
                      Return value:  list of strings, each string is a student's ID number
   ================================'''
def getIneligibleIDs(ineligibles):
    return [applicant['Student ID Number'] for applicant in ineligibles]
            
'''======================================
   getEligibleFirstTimers - Parameter(s):  list, each element is a student namedtuple
                            Return value:  Copy of the input list, with returning tutor student namedtuples removed
   ======================================'''
def getEligibleFirstTimers(applicantList):
    return [applicant for applicant in applicantList if applicant.firstTime == True]

'''==========================================
   getEligibleReturneesTimers - Parameter(s):  list, each element is a student namedtuple
                                Return value:  Copy of the input list, with first time candidate student namedtuples removed
   =========================================='''
def getEligibleReturnees(applicantList):
    return [applicant for applicant in applicantList if applicant.firstTime == False]


'''=====================================
   getIneligibleMessages - Parameter(s):  list, each element is a dictionary containing an ineligible applicant's information
                           Return value:  list of strings, each string is the formatted information string to be written to an output file
   ====================================='''
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


'''===========================================
   buildReturningStudentString - Parameter(s):  A Student that should be a returning tutor
                                 Return value:  Formatted information string to be written to an output file
   ==========================================='''
def buildReturningStudentString(student):
    result = "{} ({})\nStudent ID: {}\n{}".format(student.name, student.email, student.id, student.gpa)
    result += "Major: {}\nInterested Classes:\n".format(student.major)
    for key,value in sorted(student.classes.items()):
        result += "\t{} ({})\n".format(key, value[0].replace("\n", ", "))
        if key == "ICS45C" or key == "ICS46":
            timeList = value[1].replace("\n", ", ")
            result += "\t\t{}\n".format(timeList)
        else:
            result += "\t\t{}\n".format(value[1])
    result += "Additional information listed:\n{}\n".format(student.info)
    return result


'''===========================================
   buildFirstTimeStudentString - Parameter(s):  A Student that should be a first time tutor candidate
                                 Return value:  Formatted information string to be written to an output file
                                 (IMPORTANT NOTE: USES HELPER FUNCTION condenseFRQ AND MODULE FUNCTION buildReturningStudentString)
   ==========================================='''      
def buildFirstTimeStudentString(student):
    result = buildReturningStudentString(student)
    result += "\nPrior Experiences?\n{}\nDescribe a moment...\n{}\nHow is a tutor different from a classmate?\n{}\n".format(
               condenseFRQ(student.responses[0]), condenseFRQ(student.responses[1]), condenseFRQ(student.responses[2]))
    return result   
    
