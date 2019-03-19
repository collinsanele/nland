import webbrowser
import requests
from bs4 import BeautifulSoup
import time
from flask import Flask


app = Flask(__name__)
url = "https://nairaland.com"

@app.route('/')
def index():
	with requests.Session() as s:
		r = s.get(url).content
		soup = BeautifulSoup(r, 'html.parser')
		td = soup.findAll('td', {'featured w'})
		raw_links = [item.findAll('a') for item in td]
		for item in raw_links:
			for link in item:
				try:
					webbrowser.open(link['href'])
					time.sleep(64)
				except:
					print('Invalid link')
					pass

if __name__ == "__main__":
	app.run()				
	
	






