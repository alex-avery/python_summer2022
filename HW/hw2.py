# Python Course - Summer 2022
# Homework 2
# Alex Avery

# Assignment reequirements: 

# Go to: https://www.presidency.ucsb.edu/documents/app-categories/presidential/spoken-addresses-and-remarks
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
    web_url =  'https://www.presidency.ucsb.edu/documents/app-categories/presidential/spoken-addresses-and-remarks'
    # first we need to loop through all the pages 
    # there are 253 pages
    counter = 0
    for i in range(107):
        counter += 1
        print("Working on page " + str(counter) + " url")
        address_url = []
        if i == 0: 
            address_url = web_address    
        else: 
            address_url.append() = web_address + "?page=" + str(i)
        address_page = urllib.request.urlopen(address_url) # read the web address of each page with urllib
        soup = BeautifulSoup(address_page.read()) # open each page with soup
    for i in range(0, 60): 
        address = {}
        address_title = soup.findAll('div', {'class' : 'field-title'})
        
        

        

       
         

        
        
        
        
    
    
