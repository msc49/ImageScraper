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
      image_pil = Image.open(image_file) #converts binary data to PIL image
      file_path = self.path + image_name

      with open(file_path, "wb") as file:
        image_pil.save(file, "JPEG")

    except:
      print('FAILURE- DOWNLOAD IMAGE METHOD DOES DOES NOT WORK')



  def scroll(self, wd):
    '''
    scrolls down the page
    '''
    wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.5)


  def get_google_image(self, maximum_images):
    wd = webdriver.Chrome(self.path)
    self.scroll(wd)
    wd.get(self.google_url)

    images_urls = set()
    skips = 0

    while len(images_urls) < maximum_images:
      self.scroll(wd)

      image_thumbnails = wd.find_element(By.CLASS_NAME, "Q4LuWd") #if you use inspect, you'll see each google image has that class name

      for img in image_thumbnails[len(images_urls)+  skips:maximum_images]:
        try:
          img.click()
          img.sleep(1)

        except:
          continue


        images = wd.find_elements(By.CLASS_NAME, "n3VNCb")
        for image in images:
          if image.get_attribute('src') in images_urls:
            max_images += 1
            skips += 1
            break


          if image.get_attribute('src') and 'http' in image.get_attribute('src'):
            images_urls.add(image.get_attribute('src'))
            print(f"Found {len(images_urls)}")


    return images_urls

    for i, url in enumerate(images_urls):
      download_image(str(i) + ".jpg")

    wd.quit()






  
t= ImageScraper("https://www.google.com/search?q=cats&tbm=isch&ved=2ahUKEwjErt2phZP2AhW18rsIHUD-AwsQ2-cCegQIABAA&oq=cats&gs_lcp=CgNpbWcQAzIECAAQQzIHCAAQsQMQQzIECAAQQzIKCAAQsQMQgwEQQzIECAAQQzIECAAQQzIHCAAQsQMQQzIECAAQQzIICAAQgAQQsQMyCAgAEIAEELEDOgUIABCABDoLCAAQgAQQsQMQgwFQwwdYqQtg5wxoAHAAeACAAUqIAbMCkgEBNZgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=y7IUYoSdNbXl7_UPwPyPWA&bih=821&biw=1440")
t.get_google_image(5)