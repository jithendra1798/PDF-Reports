# Importing pandas
import pandas as pd

# This function converts the excel sheet to a dictionary
def dictionary_data(file_name):
	# Reading excel file to dataframe
	data_file = pd.read_excel (file_name)

	# Writing dataframe object to csv file
	data_file.to_csv("Dummy Data.csv", index = None, header=True)

	f = open("Dummy Data.csv",'r')

	# Reading first empty row
	reader = f.readline()

	# Reading the Titles row and putting them in a list
	titles = f.readline().strip().split(',')    # Stripping extra whitespaces and splitting into a list
	titles = [title.strip() for title in titles]    # Stripping extra whitespaces in title names

	# Creating a dictionay for storing the data in an organised manner
	data = {}

	#Reading the complete data into the dictionary
	reader = f.readline().strip()
	while reader!="":
		student_data = reader.split(',')
		cand_no = student_data[0]	# Candidate number
		data[cand_no]={}  # Creating a dictionay for each student
		data[cand_no]['Bio data']={}    # Creating dictionary for bio-data
		data[cand_no]['Exam data']={}   # Creating dictionary for Exam-data
		i=1     # iterator over data
		# Entering Bio data and creating lists for questions and answers
		while i<len(titles):
		    if i<=12 :
		        data[cand_no]['Bio data'][titles[i]] = student_data[i]
		    elif i==len(titles)-1:
		        data[cand_no]['Exam data'][titles[i]] = student_data[i]
		    else:
		        data[cand_no]['Exam data'][titles[i]] = []
		    i+=1
        # Entering Exam data in the corresponding lists of the same student
		while (student_data[0] == cand_no):
		    for i in range(13,len(titles)-1):
		        data[cand_no]['Exam data'][titles[i]].append(student_data[i])
		    reader = f.readline().strip()   # Reading data of same student for marks in different question
		    if reader!="":
		        student_data = reader.split(',')
		    else:
		        break
	f.close() # Closing the file
	#Removing the dummy data file 
	import os
	if os.path.exists("Dummy Data.csv"):
	    os.remove("Dummy Data.csv")

	return data

