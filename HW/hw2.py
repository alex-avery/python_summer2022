# Python Course - Summer 2022
# Homework 2
# Alex Avery

# Assignment reequirements: 

# Go to: https://www.presidency.ucsb.edu/documents/app-categories/presidential/spoken-addressesand-remarks
# Create a csv file with the following information for each spoken address given by President Biden since he became president on 2021-01-20:
    # Date of spoken address
    # Title
    # Full text of address or remarks
    # Citation/footnote (if one exists)
# Remember, be polite and sleep after accessing each individual document page!

# import necessary modules
from bs4 import BeautifulSoup
import urllib.request
import csv 

with open('biden_speeches.csv', 'w') as f:
    w = csv.DictWriter(f, fieldnames = ("Title", "Date", "Full Text", "Citation/Footnote"))
    w.writeheader()
    web_address =  https://www.presidency.ucsb.edu/documents/app-categories/presidential/spoken-addressesand-remarks
    web_page = urllib.request.urlopen(web_address)
    all_html = BeautifulSoup(web_page.read())
    
