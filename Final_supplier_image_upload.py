#!/usr/bin/env python3
import requests
import os

url = "http://IP-ADDRESS/upload/"
path = "./supplier-data/images/"
for infile in os.scandir(path):
    if infile.name.lower().endswith('.jpeg'):
        with open(infile.path, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
