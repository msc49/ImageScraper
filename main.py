from selenium.webdriver.common.by import By
import requests
import io
import time 
from PIL import Image
from selenium import webdriver

class ImageScraper():

  def __init__(self, google_url):
    
    self.google_url = google_url #url of images

    self.path = "/Users/Shahzaib/Desktop/images/chromedriver" # where we will store image

    wd = webdriver.Chrome(self.path)



  def download_image(self, image_name):

    try: 
    
      wd = webdriver.Chrome(self.path)
      image_url_content = requests.get(self.image_url).content  #contents for the image url CHANGEEEE
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


  def get_google_image(self, maximum_images):
    wd = webdriver.Chrome(self.path)
    self.scroll(wd)
    wd.get(self.google_url)

    images_urls = set()

    while len(images_urls) < maximum_images:
      self.scroll(wd)







  

t= ImageScraper("https://icatcare.org/app/uploads/2018/07/Thinking-of-getting-a-cat.png")
t.download_image('cat')