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


# Noel started here
        <html>
            <body style="text-align: center;">
                <p style="line-height: 2.0;">Welcome to Web Scraper! This tool allows you to scrape metadata such as "Author, Publication, Title, DOI, Date, Description" from digital libraries and save these metadata as a CSV file. Simply enter the URL of the website you want to scrape in the form below and click "Scrape". Please note that the effectiveness of the scraper may vary depending on the structure of the website. Always ensure that you have permission to scrape a website before doing so.</p>

                <br>
                <hr>
                <br>

                <p>Enter the URL of the website you want to scrape metadata from in the form below:</p>
# Noel ended here


# Francis began here
                <form method="POST">
                    URL: <input type="text" name="url"><br>
                    <br>
                    <input type="submit" value="Scrape"><br>
                </form>
            </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)

