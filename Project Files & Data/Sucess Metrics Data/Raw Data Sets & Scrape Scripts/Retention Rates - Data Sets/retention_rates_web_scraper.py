# Web Scraping Script - Big Data Challenge 2021 - 

import requests
import csv
from bs4 import BeautifulSoup as bs

# Catagory Example (I.e: Parts of the site that want to be scraped. Needs to be edited according to sites):
def extract_item(raw):
    item = raw.text
    item = item.strip()
    item.replace("\"", "")
    return item

def extract_graduation_rates(raw):
    item = raw.text
    item = item.strip()
    item.replace("\"", "")
    return item

def extract_total_credit(base_url, tag):
    url_data_tags = requests.get(base_url+tag)
    soup = bs(url_data_tags.content, 'html.parser')

    tr = soup.find("tr")
    td = tr.find("td")
    description_raw = td.find(id="definition")

    if description_raw:
        description = extract_item(description_raw)
        description = description[description.find('\n'):]
        return description.strip()

    return ""

def extract_core_courses_droupout_rate(raw):
    item = raw.text
    item = item.strip()
    item.replace("\"", "")
    return item

# Webiste Information
base_url = "https://"
soup = bs(base_url.content, 'html.parser')

# These next lines push all the data to the csv file:
filename = "data_all.csv"
csv_writer = csv.writer(open(filename, 'w'), lineterminator='\n')

csv_writer.writerow(["Name", "Tag", "Type", "Units",
                     "Period", "Description", "Historic"])

for tr in soup.find_all("tr"):
    data = []

    body = tr.find_all("td")

    if body:
        name_raw = body[0]
        tag_raw = body[1]
        type_raw = body[2]
        units_raw = body[3]

        # Appends catagories that are to be scraped into a csv:
        data.append(extract_item(name_raw))

        if data:
            print("Inserting data: {} ".format(','.join(data)))
            csv_writer.writerow(data)
