#!/usr/bin/env python3

# This script would run well as a cron job or in task scheduler if you want automated checking of prices
# remove the following two lines if you don't need logging
import logging
logging.basicConfig(filename='russ_alerts.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO, datefmt='%d/%m/%Y %H:%M:%S')
import requests
from bs4 import BeautifulSoup
import yagmail
# below is a simple custom function to send an email using yagmail
from emailer import emailer
# user agent may need updating periodically to avoid being detected as automated by Amazon
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0' }

def offer_spotter(url, condition):
    """
    generic function to identify when text on a website meets a condition - useful if you're looking for availability for bookings for a certain period from a site,
    or a specifically named sale going live. Takes a url and text to search for as argument
    """
    # get details for site - change to the website you want
    r = requests.get(url)
    subject = "Your website search"
    if not r:
        # send if error loading pages
        emailer(subject, f"Looks like one of pages hasn't loaded properly - the link {url} isn't loading")
    elif condition in r.text:
        emailer(subject, f"The text {condition} has been found in {url}. Hotfoot it over there!")
        return "condition met!"
    return "condition not met"

def amazon(item, target_price, url):
    """ Sends an email when an item on amazon is seen to be a certain price. Takes a string as the name of the item,
    an int or float as the price to trigger an alert, and a string as the url to apply the funtion to. """
    subject = "Amazon price alert" # for the emailer function
    # need to add header so amaxon doesn't identify this as an automated function
    r=requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    try:
        # this is a convoluted way of finding the price for the item in the amazon page, and parsing the price as a float
        price_block = list(soup.find('span', {'class': 'a-price a-text-price a-size-medium apexPriceToPay'}))
        price = (float(list(i[1:] for i in price_block[0])[0]))
    # If the item is out of stock or another error occurs the outcome is recorded as an error
    except TypeError:
        return "Error finding price"
    if price <= target_price:
        # emails nominated accounts if price meets a certain threshold
        emailer(subject, f"price alert for {item}: price is now £{price}")
    return price

def main():
    # Some sample functions
    offer = offer_spotter("www.argos.co.uk", "Summer sale")
    boots_price = amazon("Chelsea boots", 50, "https://www.amazon.co.uk/Timberland-Stormbuck-Pull-Chelsea-Burnished/dp/B00BF0OJPQ/ref=sr_1_5?crid=2MPKRA456Q88T&dchild=1&keywords=chelsea%2Bboots%2Bfor%2Bmen&qid=1618345229&sprefix=chelsea%2Caps%2C303&sr=8-5&th=1&psc=1")
    # logging function logs results of script to a .txt file in current directory
    logging.info(f"""\nOffer checker result is {offer}
        Amazon - {boots_price=}""")

if __name__ == "__main__":
    main()