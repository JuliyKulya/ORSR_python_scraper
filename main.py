from bs4 import BeautifulSoup
import requests
from parsing import Parsing
from pymongo import MongoClient

"""Open home page"""
url = "https://www.orsr.sk/hladaj_zmeny.asp"
response = requests.get(url)
html_content = response.content.decode('windows-1250')

#Search button links "Aktuálny"
soup = BeautifulSoup(html_content, "html.parser")
buttons = soup.find_all('a', class_='link', string='Aktuálny')

#Writing all references to the list
list_of_links = []
for button in buttons:
    links_id = button['href']
    each_url = f"https://www.orsr.sk/{links_id}"
    add_link_to_list = list_of_links.append(each_url)


"""Creating the database"""

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
if 'mycollection' in db.list_collection_names():
    db['mycollection'].drop()
collection = db['mycollection']
print("Database created")
print("Download started...")
for link in list_of_links:
    #Downloading and writing data to the database
    pars = Parsing(link).parsing_method()
    pars_windows_1250 = {k: [v[0].encode('utf-8').decode('utf-8')] for k, v in pars.items()}
    collection.insert_one(pars_windows_1250)
    print(pars_windows_1250)
print("Data has been downloaded")




