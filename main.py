from bs4 import BeautifulSoup
import requests
import io
from selenium import webdriver

class ImageScraper():

  def __init__(self, image_url):
    self.image_url = image_url #url of images

    self.path = "/Users/Shahzaib/Desktop/images/chromedriver.exe" # where we will store image

    wd = webdriver.Chrome(self.path)



  def download_image(self,path, url, image_name):
    image = requests.get(self.url).content


