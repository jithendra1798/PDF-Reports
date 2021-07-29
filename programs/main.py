# Inputting the file name
file_name = "../Dummy Data.xlsx"

# Importing a function which converts excel to dictionary in an organised manner
from excel_to_dictionary import dictionary_data
# Converting excel to dictionary
data = dictionary_data(file_name)

# Importing a function which extracts data to be printed on PDF from the dictionary
from dictionary_to_pdf_text import pdf_data
from pdf_report import scorecard
# Converting dictionay data to a list of strings to be printed on PDF and Extracting PDF's
for key in data:
    pdf_text = pdf_data(data[key])
    scorecard(pdf_text,key)

# Removing __pycache__
import pathlib
[p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]
my_folder = '__pycache__'
import os
if os.path.exists(my_folder):
    os.rmdir(my_folder)







