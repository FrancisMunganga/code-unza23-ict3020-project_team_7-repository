# Isaac Shapi started coding here 
# import the libraries 

from flask import Flask, request
from bs4 import BeautifulSoup
import requests
import csv
# Isaac Shapi ended here 


# # Jane Yowela started editing here 
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


# Francis Munganga started editing here 
        # Find metadata
        meta = soup.find_all('meta')

        # Define CSV file
        filename = "metadata.csv"
        csv_writer = csv.writer(open(filename, 'w'))
#Francis Munganga ended here 



#Isaac Shapi started editing here 

 for tag in meta:
            if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() in ['author', 'publication', 'title', 'doi', 'date', 'description']:
                name = tag.attrs['name'].lower()
                value = tag.attrs['content']
#Shapi ended here 



#Jane started here

                csv_writer.writerow([name, value]) 
        return "Metadata has been saved to {}".format(filename)

    return '''
# Jane ended here