#! /usr/bin/env python3

import os
import requests


class review:
    def __init__(self, title, name, date, feedback):
        self._title = title
        self._name = name
        self._date = date
        self._feedback = feedback

    def formatDict(self):
        formDict = {"title": self._title,
                    "name": self._name,
                    "date": self._date,
                    "feedback": self._feedback}
        return(formDict)


def main():
    path = "/data/feedback"
    for infile in os.scandir(path):
        with open(infile.path, 'r') as txtFile:
            item = [line.rstrip() for line in txtFile]
            obj = review(item[0], item[1], item[2], item[3])
            response = requests.post(
                "http://34.134.247.21/feedback/",
                json=obj.formatDict())
            response.request.url
            print("{} : {}" .format(response.status_code, response.text))
            if response.ok:
                print("Update successful : {}".format(response.status_code))
    del obj, item, response, infile

if __name__ == "__main__":
    main()
