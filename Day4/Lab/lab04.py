## Go to https://polisci.wustl.edu/people/88/all OR https://polisci.wustl.edu/people/list/88/all
## Go to the page for each of the professors.
## Create a .csv file with the following information for each professor:
## 	-Specialization 
##  	Example from Deniz's page: https://polisci.wustl.edu/people/deniz-aksoy
##		Professor Aksoy’s research is motivated by an interest in comparative political institutions and political violence. 
## 	-Name
## 	-Title
## 	-E-mail
## 	-Web page
	
from bs4 import BeautifulSoup
import urllib.request
import csv 

with open('wustl_polisci_faculty.csv', 'w') as f:
  w = csv.DictWriter(f, fieldnames = ("Name", "Title", "E-mail", "Web Page", "Specialization"))
  w.writeheader()
  web_address = 'https://polisci.wustl.edu/people/88/all'
  web_page = web_page = urllib.request.urlopen(web_address)
  soup = BeautifulSoup(web_page.read())
  faculty = soup.find_all('a', {'class' : "card"})
  for i in faculty:
      try:
          faculty_info = {}
          faculty_info['Name'] = ' '.join(faculty[i].find('h3').text.split('\xa0'))
          faculty_info['Title'] = faculty[i].find('div', {'class' : 'dept'}).text
          inner_page_url = 'https://polisci.wustl.edu' + faculty[i]['href']
          inner_page = urllib.request.urlopen(inner_page_url)
          inner_soup = BeautifulSoup(inner_page.read())
          faculty_info['E-mail'] = inner_soup.find('ul', {'class' : 'detail contact'}).find('a').text
          faculty_info['Web Page'] = faculty_info['Web Page'] = inner_soup.find('ul', {'class' : 'links'}).find('a')['href']
          faculty_info['Specialization'] = inner_soup.find('div', {'class' : 'post-excerpt'}).text
      except:
          faculty_info['E-mail'] = 'NA'
      w.writerow(faculty_info)

