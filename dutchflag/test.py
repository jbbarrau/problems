from patientfiles import PatientFile, PatientList

files = [PatientFile('High'),\
            PatientFile('Mid'),\
            PatientFile('Low'),\
            PatientFile('High'),\
            PatientFile('High'),\
            PatientFile('Low'),\
            PatientFile('Mid'),\
            PatientFile('Low'),\
            PatientFile('High'),\
            PatientFile('High'),\
            PatientFile('Low'),\
            PatientFile('Mid'),\
            PatientFile('Low'),\
            PatientFile('High'),\
            PatientFile('High'),\
            PatientFile('Low'),\
            PatientFile('Mid'),\
            PatientFile('Low'),\
            PatientFile('High'),\
            PatientFile('High'),\
            PatientFile('Low'),\
        ]
        
        
list = PatientList(files)

list.sort()
