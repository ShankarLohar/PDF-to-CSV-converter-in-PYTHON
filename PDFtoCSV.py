# 22 Feb 2021
#Shankar Lohar
#Just learnt about how to convert files through python

##imports required
import pdftotext #to convert the pdf to text format
import csv #to make a csv file

myfile = input("Enter the location of your pdf file: ")

## opening PDF file and converting to text with the module pdftotext
with open(myfile, 'rb') as mypdf:
    pdfobject = pdftotext.PDF(mypdf)

# # writing the data to a CSV file and saving to the same location as provided
with open(myfile[:-3]+'csv', 'w') as mycsv:
    writer = csv.writer(mycsv)
    writer.writerows(list(pdfobject)[0].split('\n'))
    print("File Converted! and Saved to the file location given.")