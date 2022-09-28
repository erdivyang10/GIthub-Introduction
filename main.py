import pdfplumber
import pandas as pd

#function to read the number of pages
def number_of_pages(filename):

        with pdfplumber.open(filename) as pdf:
        
                for tables in pdf.pages:
                        print('Pages in PDF files: ',tables)


a = number_of_pages("abc.pdf")

a ==b 
                        