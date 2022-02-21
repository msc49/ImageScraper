from bs4 import BeautifulSoup
import requests
import io
from PIL import Image
from selenium import webdriver

class ImageScraper():

  def __init__(self, image_url):
    self.image_url = image_url #url of images

    self.path = "/Users/Shahzaib/Desktop/images/chromedriver.exe" # where we will store image

    wd = webdriver.Chrome(self.path)



  def download_image(self,path, url, image_name):
    image_url_content = requests.get(self.url).content  #contents for the image url

    image_file = io.BytesIO(image_url_content) # convert image content to memory

    image = image.open(image_file)

    file_path = path + image_name

    with open(file_path, "wb") as file:
      image.save(file, "JPEG")
