#!/usr/bin/env python3

import requests, os
from collections import OrderedDict
import json

def main():
 # get the files from source directory
 text_files = os.listdir("/data/feedback")

 # process the text files one by one
 for text_file in text_files:
  # initialize the dictionary to store feedback data inside
  dictionary = OrderedDict()

  # read the contents of the file, and insert them into the dictionary
  with open("/data/feedback/" + text_file, "r") as file:
   dictionary['title'] = file.readline().strip("\n")
   dictionary['name'] = file.readline().strip("\n")
   dictionary['date'] = file.readline().strip("\n")
   dictionary['feedback'] = ''.join([ line.strip("\n") for line in file.readlines()])

  # make the request to the website
  upload_request = requests.post("http://34.133.161.90/feedback/", json=dictionary)

  # check status code
  if not upload_request.status_code == 201:
   print("Error uploading /data/feedback/" + os.path.basename(text_file) + " :: status code:$

if __name__ == "__main__":
 main()
