## Go to https://polisci.wustl.edu/people/88/all OR https://polisci.wustl.edu/people/list/88/all
## Go to the page for each of the professors.
## Create a .csv file with the following information for each professor:
##  -Specialization 
##    Example from Deniz's page: https://polisci.wustl.edu/people/deniz-aksoy
##    Professor Aksoy’s research is motivated by an interest in comparative political institutions and political violence. 
##  -Name
##  -Title
##  -E-mail
##  -Web page
	

from bs4 import BeautifulSoup
import urllib.request
import re
import csv
import unicodedata
import os

os.chdir('C:\\Users\\miame\\Documents\\GitHub\\python_summer2022\\Day4\\Lab')

with open('lab04_solution.csv', 'w', encoding="utf-8") as f: # added encoding arg for some extra characters in some cards
  w = csv.DictWriter(f, fieldnames = ("name", "title", "email", "website", "specialization"))
  w.writeheader()
  web_address='https://polisci.wustl.edu/people/88/'
  web_page = urllib.request.urlopen(web_address)
  all_html = BeautifulSoup(web_page.read())
  #all_ppl = all_html.find_all("article")
  all_faculty = all_html.find_all('a', {'class': 'card'})
  counter = 0
  for i in all_faculty:
    counter += 1
    print("Working on " + str(counter) + " of " + str(len(all_faculty)))
    prof = {} ## empty dictionary to fill in
    extension = i.attrs['href']
    # name
    prof["name"] = unicodedata.normalize('NFKD', i.article.h3.get_text())
    # title
    prof['title'] = i.article.find('div', {'class': 'dept'}).get_text()
    # navigate to prof's page
    try:
      prof_page = urllib.request.urlopen('https://polisci.wustl.edu%s' % extension)
    except urllib.error.URLError: 
      prof['email'] = 'NA'
      prof['website'] = extension
      prof['specialization'] = 'NA'
      w.writerow(prof)
      continue
    print("Navigated to page")
    prof_html = BeautifulSoup(prof_page.read())
    ## email
    try: # not all profs have contact info
        email_div = prof_html.find("div", {"class" : "faculty-contact flex"})
        prof["email"] = email_div.a.get_text()
    except:
        prof["email"] = "NA"
    print("Done with email")
    ## website
    website_ul = prof_html.find("ul", {"class" : "links"})
    try: # not all profs have a website
      prof["website"] = website_ul.a.attrs["href"]
    except AttributeError:
      prof["website"] = "NA"
    print("Done with website")
    ## specialization
    spec = prof_html.find("div", {"class" : "post-excerpt"})
    prof["specialization"] = unicodedata.normalize('NFKD', spec.get_text())
    print("Done with specialization")
    ## write observation to csv
    w.writerow(prof)
print("All done!")

