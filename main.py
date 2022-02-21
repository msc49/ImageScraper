from bs4 import BeautifulSoup
import requests
import io
from PIL import Image
from selenium import webdriver

class ImageScraper():

  def __init__(self, image_url):
    self.image_url = image_url #url of images

    self.path = "/Users/Shahzaib/Desktop/images/chromedriver" # where we will store image

    wd = webdriver.Chrome(self.path)



  def download_image(self, image_name):
    wd = webdriver.Chrome(self.path)
    image_url_content = requests.get(self.image_url).content  #contents for the image url

    image_file = io.BytesIO(image_url_content) # convert image content to memory

    image = Image.open(image_file)

    file_path = path + image_name

    with open(file_path, "wb") as file:
      image.save(file, "JPEG")

    print("successful")

  

t= ImageScraper("https://en.wikipedia.org/wiki/Van_cat#/media/File:VAN_CAT.png")
t.download_image('cat_image')