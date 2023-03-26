#!/usr/bin/env python3

import argparse, requests, bs4, json
from datetime import datetime

# Giving the user some options
argParser = argparse.ArgumentParser(
                    prog = 'Nagano Akiya List',
                    description = 'Get a list of Akiyas in Nagano',
                    epilog = 'Have a nice day!')
argParser.add_argument("-minp", "--min_price", help="Minimum price.", default=0)
argParser.add_argument("-maxp", "--max_price", help="Maximum price.", default=0)
argParser.add_argument("-maxa", "--max_age", help="Maximum age.", default=0)
argParser.add_argument("-minl", "--min_land", help="Minimum land size (sqm).", default=0)
argParser.add_argument("-maxl", "--max_land", help="Maximum land size (sqm).", default=0)
argParser.add_argument("-minh", "--min_house", help="Minimum house size (sqm).", default=0)
argParser.add_argument("-maxh", "--max_house", help="Maximum house size (sqm).", default=0)

args = argParser.parse_args()
min_price = str(args.min_price)
max_price = str(args.max_price)
max_age = str(args.max_age)
min_land = str(args.min_land)
max_land = str(args.max_land)
min_house = str(args.min_house)
max_house = str(args.max_house)

# Creating the url to parse from
req_url = 'https://rakuen-akiya.jp/housesearch/feature/?vender_id=&keyword=&bc1=1&kakaku1=' + min_price +'&kakaku2=' + max_price +'&kakaku3=0&kakaku4=0&chiku=' + max_age + '&tochi1=' + min_land +'&tochi2=' + max_land +'&tatemono1=' + min_house + '&tatemono2=' + max_house
prop_list_res = requests.get(req_url)

# Showing status  and requested URL
print(str(prop_list_res.status_code) + " - " + str(req_url))
# res.raise_for_status()
prop_list_soup = bs4.BeautifulSoup(prop_list_res.text, 'html.parser')

# Array for the result URLs
property_urls = []

# Getting all the URLs for the results
for a in prop_list_soup.select('h3 > a'):
    # Gets all property urls
    property_urls.append(a['href'])

# Place for the dict
property_list = []

# Loop for getting property details from the URLs
for p in property_urls:

    prop_res = requests.get('https://rakuen-akiya.jp' + p)
    prop_soup = bs4.BeautifulSoup(prop_res.text, 'html.parser')

    # create dictionary object for this property
    prop_dict = {}

    h1_span = prop_soup.find('span', class_='lbl')
    location_text = h1_span.next_sibling
    prop_dict['location'] = location_text.text

    table = prop_soup.find("table", {"class":"tableStyleC styleC"})
    tds = table.find_all("td")
    values = [td.text for td in tds]
    prop_dict['address'] = values[0]
    prop_dict['name'] = values[1]
    prop_dict['price'] = values[2]
    prop_dict['tax'] = values[3]
    prop_dict['land_size'] = values[4]
    prop_dict['building_size'] = values[5]
    prop_dict['rooms'] = values[6]
    prop_dict['structure'] = values[7]
    prop_dict['floor_plan'] = values[8]
    prop_dict['floors'] = values[9]
    prop_dict['build_year'] = values[10]
    prop_dict['hot_spring'] = values[11]
    prop_dict['sewer'] = values[12]
    prop_dict['school'] = values[13]
    prop_dict['move_in_date'] = values[14]
    prop_dict['prop_name'] = values[15]
    prop_dict['prop_number'] = values[16]
    prop_dict['facility'] = values[17]
    prop_dict['parking'] = values[18]
    prop_dict['transport'] = values[19]
    prop_dict['land_rights'] = values[20]
    prop_dict['other'] = values[21]

    # Some properties got a google maps link
    google_maps = prop_soup.find("a", class_="btn externalLink")
    try:
        prop_dict['google_maps'] = google_maps["href"]
    except:
        prop_dict['google_maps'] = 'N/A'
    

    # Adding data
    property_list.append(prop_dict)

    # Keeping the user updated with what is going on...
    print(f"Added: " + prop_dict['address'] + " (" +  prop_dict['price'] + ")\n")
    
# Get the current date/time for json file
now = datetime.now()
current_date = now.strftime('%d%m%Y_%H:%M')

# write the list of dictionaries to a JSON file
with open('property_list_' + current_date + '.json', 'w', encoding='utf8') as f:
    json.dump(property_list, f, ensure_ascii=False)
