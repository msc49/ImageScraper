from bs4 import BeautifulSoup
import requests
import io
import time 
from PIL import Image
from selenium import webdriver

class ImageScraper():

  def __init__(self, image_url):
    self.image_url = image_url #url of images

    self.path = "/Users/Shahzaib/Desktop/images/chromedriver" # where we will store image

    wd = webdriver.Chrome(self.path)



  def download_image(self, image_name):

    try: 
    
      wd = webdriver.Chrome(self.path)
      image_url_content = requests.get(self.image_url).content  #contents for the image url
      image_file = io.BytesIO(image_url_content) # convert image content to memory as binary data
      image = Image.open(image_file) #converts binary data to PIL image
      file_path = self.path + image_name

      with open(file_path, "wb") as file:
        image.save(file, "JPEG")

    except:
      print('FAILURE- DOWNLOAD IMAGE METHOD DOES DOES NOT WORK')



  def scroll(wd):
    '''
    scrolls down the page
    '''
    wd.execute("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(0.5)



  

t= ImageScraper("https://icatcare.org/app/uploads/2018/07/Thinking-of-getting-a-cat.png")
t.download_image('cat')