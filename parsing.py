import requests
from bs4 import BeautifulSoup
import re

class Parsing:

    def __init__(self, url):
        self.url = url

    def parsing_method(self):
        # Construct the full URL
        url = f"{self.url}"
        response = requests.get(url)
        #get content from webpage
        convert_html_to_text = response.content.decode('windows-1250')

        # Parse the webpage content with BeautifulSoup
        soup = BeautifulSoup(convert_html_to_text, 'lxml')

        # Find all direct children tables in the HTML body
        tables_from_the_body = list(soup.body.find_all("table", recursive=False))
        data = {}

        # Loop through tables (from 3rd) and extract data
        # The first two are skipped because we don't need that data
        for n in range(2, len(tables_from_the_body)):
            current_table = tables_from_the_body[n].text

            # Clean the text by removing extra whitespace
            text_without_whitespace = re.sub(r'\s+', ' ', current_table).strip()

            # Split the text into key-value pairs
            parts = text_without_whitespace.split(':', 1)
            parts[1] = parts[1].strip()

            # Add the data to the dictionary
            data[parts[0]] = [parts[1]]

        return data
