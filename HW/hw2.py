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
    web_address =  'https://www.presidency.ucsb.edu/documents/app-categories/presidential/spoken-addresses-and-remarks'
    web_address_60 = web_address + '?items_per_page=60'
    # first we need to loop through all the pages 
    # there are 253 pages
    counter = 0  
    for i in range(253):
        counter += 1
        print("Working on page " + str(counter) + " url")
        if i == 0: 
            page_url = web_address_60    
        else: 
            page_url = web_address_60 + "?page=" + str(i)
        page = urllib.request.urlopen(page_url) 
        page_soup = BeautifulSoup(page.read()) 
        address_title = soup.find_all('div', {'class' : 'field-title'})
        for i in address_title: 
            address_url = 'https://www.presidency.ucsb.edu' + i.find('a')['href']
            address_page = urllib.request.urlopen(address_url)
            address_soup = BeautifulSoup(address_page.read())
            address = {}
            if address_soup.find('h3', {'class' : 'diet-title'}).text == 'Joseph R. Biden': 
                address["Title"] = address_soup.find('div', {'class' : 'field-ds-doc-title'})
                address["Date"] = address_soup.find('span', {'class' : 'date-display-single'})
                address["Full Text"] = address_soup.find('div', {'class' : 'field-docs-content'})

        

       
         

        
        
        
        
    
    
