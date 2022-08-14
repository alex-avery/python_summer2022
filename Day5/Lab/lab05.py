import re
import os

os.chdir('/Users/alexcisco/Library/Mobile Documents/com~apple~CloudDocs/Documents/WUSTL/Courses/Python Course/python_summer2022/Day5/Lab')

# open text file of 2008 NH primary Obama speech
with open("obama-nh.txt", "r") as f:
	obama = f.readlines()


## TODO: print lines that do not contain 'the' using what we learned
## (although you ~might~ think you could do something like
## [l for l in obama if "the" not in l]

for line in obama:
    no_the_lines = []
    if len(re.findall(r"the", str(line).lower())) == 0: 
        no_the_lines.append(line)
    print(no_the_lines)


# TODO: print lines that contain a word of any length starting with s and ending with e

for line in obama:
    se_words = []
    pattern = re.compile(r'[s][a-z]*e')
    if len(pattern.findall(line.lower())) >= 1:
        se_words.append(line)
    print(se_words)

## TODO: Print the date input in the following format
## Month: MM
## Day: DD
## Year: YY
date = 'Please enter a date in the following format: 08.18.21'


pattern = re.compile(r'\d{2}') 
date_objects = pattern.findall(date)
Month = date_ojects[0]
Day = date_objects[1]
Year = date_objects[2]
print(f"Month:{Month}\nDay:{Day}\nYear:{Year}")

