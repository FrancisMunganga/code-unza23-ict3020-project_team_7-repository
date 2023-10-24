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
