from bs4 import BeautifulSoup
import requests

class ImageScraper():

  def __init__(self, image_url):
    self.image_url = image_url #url of images

    self.path = "/Users/Shahzaib/Desktop/images" # where we will store image


