# Isaac Shapi started coding here 
# import the libraries 

from flask import Flask, request
from bs4 import BeautifulSoup
import requests
import csv
# Isaac Shapi ended here 


# # Jane Yowela started here 
# Using flask to create the app

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def scrape():
# Jane Yowela ended here 

# Noel Simpemba started editing here 
    if request.method == 'POST':
        url = request.form['url']
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
# Noel Simpemba ended here 