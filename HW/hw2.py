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
import time
import random
import os

# directory to store file 
os.chdir('/Users/alexcisco/Library/Mobile Documents/com~apple~CloudDocs/Documents/WUSTL/Courses/Python Course/python_summer2022/HW')

with open('biden_speeches.csv', 'w') as f:
    w = csv.DictWriter(f, fieldnames = ("Title", "Date", "Full Text", "Citation/Footnote"))
    w.writeheader()
    # given web address for assignment
    web_address =  'https://www.presidency.ucsb.edu/documents/app-categories/presidential/spoken-addresses-and-remarks'
    # using 60 items per page to avoid having to loop over the web adress more times
    web_address_60 = web_address + '?items_per_page=60'
    # adding a counter to tell us what page it is currently working on 
    counter = 0  
    # Biden's inagural address is on page 11
    for i in range(11):
        counter += 1
        print("Working on page " + str(counter))
        if i == 0: 
            page_url = web_address_60    
        else: 
            page_url = web_address_60 + "?page=" + str(i)
        page = urllib.request.urlopen(page_url) 
        page_soup = BeautifulSoup(page.read()) 
        address_title = page_soup.find_all('div', {'class' : 'field-title'})
        for i in address_title: 
            # get the unique url for each address
            address_url = 'https://www.presidency.ucsb.edu' + i.find('a')['href']
            address_page = urllib.request.urlopen(address_url)
            address_soup = BeautifulSoup(address_page.read())
            # create empty dictionary 
            address = {}
            #We only want Biden's speeches
            if address_soup.find('h3', {'class' : 'diet-title'}).text == 'Joseph R. Biden': 
                try:
                    address["Title"] = address_soup.find('div', {'class' : 'field-ds-doc-title'}).text
                    address["Date"] = address_soup.find('span', {'class' : 'date-display-single'}).text
                    address["Full Text"] = address_soup.find('div', {'class' : 'field-docs-content'}).text
                    address["Citation/Footnote"] = address_soup.find('div', {'class' : 'field-docs-footnote'}).text
                # some addresses do not have footnotes
                except:
                    address["Citation/Footnote"] = "NA"
                w.writerow(address)
                # add sleep time so we do not accidentaly break the site 
                time.sleep(random.uniform(1,5))
            # skip if not an address given by Biden     
            else: 
                break
                
                
     


       
            
           
        

       
         

        
        
        
        
    
    
