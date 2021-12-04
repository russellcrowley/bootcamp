#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import os
def image_downloader(search_term=None, pics=None):
""" Gets a specified amount of images from imgur matching a search term, and saves them to the current directory.
Takes strings for search term and amount of pictures of arguments, or prompts for them if not provided. """
    if search_term == None:
        search_term = input("Enter your search term: ")
    if pics == None:
        pics = int(input("How many pictures do you want? "))
    # Get pages results and a list of image urls
    r = requests.get(f"https://imgur.com/search?q={search_term}")
    soup = BeautifulSoup(r.text, "html.parser")
    images = []
    for link in soup.find_all("img"):
        image = (link.get('src'))
        # Remove 'b' from thumbnail link to get high quality image
        if image.startswith("//i.imgur.com/"):
            images.append(f"https:{image[0:-5]}.jpg")
        else:
            pass
    # Make directory named after search term
    os.mkdir(search_term)
    # Don't index beyond amount of images
    if len(images) < pics:
        pics = len(images)
    # Get image and save in directory

    for i in range(pics):
        print(f"Saving {images[i]}...")
        image_file = open(os.path.join(search_term, os.path.basename(images[i])), 'wb')
        image = requests.get(images[i])
        for chunk in image.iter_content(100000):
            image_file.write(chunk)
        image_file.close()
    print(f"All done! Saved {pics} images in a {search_term} folder in your current directory.")

if __name__ == "__main__":
    image_downloader()
