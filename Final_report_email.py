#!/usr/bin/env python3

import os
import datetime
import reports
import emails


def main():
    path = "./supplier-data/descriptions/"
    fruit_list = []
    for infile in os.scandir(path):
        with open(infile.path, 'r') as txtFile:
            item = [line.rstrip() for line in txtFile]
            fruit_list.append("name: " + item[0]
                              + "<br/>weight: " + item[1] + "<br/>")

    summary = "<br/>".join(map(str, fruit_list))
    reports.generate("/tmp/processed.pdf",
                     "Processed Update on "+datetime.datetime().today, summary)
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate(
        sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send(message)
