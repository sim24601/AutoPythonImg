#!/usr/bin/env python3

import os
import requests
import reports
import emails


class fruit:
    def __init__(self, name, weight, description, image_name):
        self._name = name
        self._weight = weight
        self._description = description
        self._image_name = image_name

    def formatDict(self):
        formDict = {"name": self._name,
                    "weight": self._weight,
                    "description": self._description,
                    "image_name": self._image_name}
        return(formDict)

    def formatLine(self):
        formLine = "name: " + self._name + \
            "<br/>weight: " + str(self._weight) + " lbs<br/>"
        return(formLine)


def main():
    path = "./supplier-data/descriptions/"
    fruit_list = []
    for infile in os.scandir(path):
        with open(infile.path, 'r') as txtFile:
            item = [line.rstrip() for line in txtFile]
            obj = fruit(item[0], int(item[1].strip(" lbs")),
                        item[2], infile.name.replace(".txt", ".jpeg"))
            response = requests.post(
                "http://[linux-instance-external-IP]/fruits/",
                json=obj.formatDict())
            response.request.url
            print("{}" .format(response.text))
            if response.ok:
                print("Update successful : {}".format(response.status_code))
    del obj, item, response, infile


if __name__ == "__main__":
    main()
