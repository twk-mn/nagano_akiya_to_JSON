# Nagano Akiya to JSON
Old script to parse properties from a Nagano akiya site to JSON.<br />
Created back when I was learning Python.

### Installation
(This is for linux, shouldn't be hard to find out how to do it on Windows if you google...)

1. Clone the repo and enter the dir
```sh
git clone https://github.com/twk-mn/nagano_akiya_to_JSON.git && cd nagano_akiya_to_JSON
```
2. Install requirements.txt

```sh
pip3 install -r requirements.txt
```

3. Make it executable
```sh
chmod +x nagano_akiya_to_JSON.py
```

4. Show options/help
 ```sh
./nagano_akiya_to_JSON.py -h
```

The file output will be named "property_list_[date]_[time].json"

### Options

 ```sh
  -h, --help            show this help message and exit
  -minp MIN_PRICE, --min_price MIN_PRICE
                        Minimum price.
  -maxp MAX_PRICE, --max_price MAX_PRICE
                        Maximum price.
  -maxa MAX_AGE, --max_age MAX_AGE
                        Maximum age.
  -minl MIN_LAND, --min_land MIN_LAND
                        Minimum land size (sqm).
  -maxl MAX_LAND, --max_land MAX_LAND
                        Maximum land size (sqm).
  -minh MIN_HOUSE, --min_house MIN_HOUSE
                        Minimum house size (sqm).
  -maxh MAX_HOUSE, --max_house MAX_HOUSE
                        Maximum house size (sqm).

```

Don't have any plans to add more features right now... But maybe someday(?)...