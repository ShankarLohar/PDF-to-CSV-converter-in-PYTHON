# PDF-to-CSV-converter-in-PYTHON
This is a simple project to convert a pdf into a csv in python. It's more for learning than useful.

Project Name : PDFtoCSV Converter

Installations required: pdftotext and csv Python Modules through pip

About the project: The project is a simple python program that reads a pdf as text through a python library called pdftotext and then a csv file is created with the text content extracted.

How does it work?
When the program is run then the user is asked to provide the pdf file location of the pdf file which is then saved as a csv file to the same location and with the same name as a csv file with a success message. Else if anything went wrong the program throws an exception as provided.

The main Logic: The text from the pdf that is provided is extracted with the function of the pdftotext module and then stored as an object. which is then typecasted as a list that consists of a single element of string type(that is the extracted text of the pdf) with the spaces and new line characters.
The list element is then further split into a group of string element with the breakpoint of newline characters.
Then finally the list of strings is written on the csv file created; one character at a time to manage spaces and newlines.

Limitations of the project: As reading the pdf file and converting to CSV's can be very content specific to the pdf. There might be chances that the piece of code written will not be readable in most cases. For example, A pdf consisting of pictures and unusual formats of writings. 
