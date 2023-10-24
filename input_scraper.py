# Isaac Shapi started here

#Import the libraries 

import requests 
import pandas as pd 
from bs4 import BeautifulSoup

# Isaac Shapi ended here 


# Noel Simpemba started here 

# Define the URL of the digital library website 
# Send an HTTP request and parse the HTML
url = 'https://example.com/digital-library'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Noel Simpemba ended here


# Noel Simpemba started here 

# Find all the <tbody> elements that contain the metadata elements

tbodies = soup.find_all("tbody")

# Create an empty list to store the scraped data

data = []

# Loop through each <tbody> element

for tbody in tbodies:

    # Create an empty dictionary to store the metadata of one item

    item = {}
# Noel Simpemba ended here


# Jane Yowela started here
 # Find all the <tr> elements that contain the metadata name and value
    trs = tbody.find_all("tr")
    # Loop through each <tr> element
    for tr in trs:
        # Find the <th> element that contains the metadata name
        th = tr.find("th")
        # Get the text of the <th> element and strip any whitespace
        name = th.text.strip()
        # Find the <td> element that contains the metadata value
        td = tr.find("td")
# Jane Yowela ended here

# Francis Munganga started here
        # If the metadata name is "Title"
        if name == "Title":
            # Find the <span> element that contains the language of the title metadata
            lang_span = td.find("span", class_="badge grey-badge")
            # Get the text of the <span> element and strip any whitespace
            lang = lang_span.text.strip()
            # Find the <span> element that contains the name of the title metadata
            title_span = td.find("span", class_="col-md-11")
            # Get the text of the <span> element and strip any whitespace
            title = title_span.text.strip()
# Francis Munganga ended here
            


