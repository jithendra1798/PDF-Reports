def create_string(L,space):
    S=''
    for Q in L:
        if Q=='' or Q==' ':
            Q='NA'
        if Q=='Correct':
            Q='C'
        if Q=='Incorrect':
            Q='IC'
        if Q=='Unattempted':
            Q='NA'
        S=f'{S} {Q:{space}}'
    return [S]
# Creates strings of data to be printed on PDF
def pdf_data(data):
    pdf_text=[]
    pdf_text.append(f"Report Card of {data['Bio data']['First Name']} in Round : {data['Bio data']['Round']}") #0. Title of Reportcard
    pdf_text.append([f"First Name"]+[f"{data['Bio data']['First Name']}"])  #1. Full name of student
    pdf_text.append([f"Last Name"]+[f"{data['Bio data']['Last Name']}"])  #2. Full name of student
    pdf_text.append([f"Full Name"]+[f"{data['Bio data']['Full Name']}"])  #3. Full name of student
    pdf_text.append([f"Registration Number"]+[f"{data['Bio data']['Registration Number']}"])    #4. Student Reg.No
    pdf_text.append([f"Grade"]+[f"{data['Bio data']['Grade']}"]) #5. Student grade
    pdf_text.append([f"Gender"]+[f"{data['Bio data']['Gender']}"])   #6. Gender
    pdf_text.append([f"Name of School"]+[f"{data['Bio data']['Name of School']}"])  #7. School Name of Student
    pdf_text.append([f"Date of Birth"]+[f"{data['Bio data']['Date of Birth'][:10]}"]) #8. DOB
    pdf_text.append([f"City of Residence"]+[f"{data['Bio data']['City of Residence']}"]) #9. City
    pdf_text.append([f"Country of Residence"]+[f"{data['Bio data']['Country of Residence']}"])   #10. Country
    # Test details
    pdf_text.append([f"Date and time of test : "]+[f"{data['Bio data']['Date and time of test']}"]) #11. Data & Time of test
    pdf_text.append(['Question No.    :']+create_string(data['Exam data']['Question No.'],4))    #12. Questions
    pdf_text.append(['What you marked :']+create_string(data['Exam data']['What you marked'],4))  #13. Answered
    pdf_text.append(['Correct Answer  :']+create_string(data['Exam data']['Correct Answer'],4)) #14. Correct answer
    pdf_text.append(['Outcome(C/IC/NA):']+create_string(data['Exam data']['Outcome (Correct/Incorrect/Not Attempted)'],4))#15. Outcome
    pdf_text.append(['Score if correct:']+create_string(data['Exam data']['Score if correct'],4)) #16. Max score
    pdf_text.append(['Your score      :']+create_string(data['Exam data']['Your score'],4)) #17. Your score
    # Finding total marks
    Marks=0
    for i in data['Exam data']['Your score']:
        Marks+=int(i)
    pdf_text.append(['Total Marks : ']+[f'{Marks}/100'])

    pdf_text.append(f"Final result : {data['Exam data']['Final result']}")
    return pdf_text

