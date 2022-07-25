#!/usr/bin/env python3

from PIL import Image
import sys, os

def perform_changes(image):
 image_name = os.path.basename(image)
 if image_name == ".DS_Store":
  return
 image_path = os.path.expanduser("~") + "/images/" + image_name
 Image.open(image_path).rotate(90).resize((128,128)).convert("RGB").save("/opt/icons/" + image_name + ".jpeg")

def main():
 # get all the files
 images = os.listdir(os.path.expanduser("~")+"/images")
 # for each file perform the needed operations, and return the final file
 for image in images:
  perform_changes(image)

if __name__ == "__main__":
 main()
