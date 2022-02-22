# Image Scraper

Automation that allows you to download any number of google images from the url you provide

## Prerequisite

make sure you have the following installed:

- Selenium
```
pip install selenium
```
- Pillow
```
pip install Pillow
```
- requests
```
pip install requests
```

You will also need to download chromedriver and add it to the path you want the images to be downloaded to. You can download chromedriver from the following link:
https://chromedriver.chromium.org/home


## Changes

Go the main.py file and change the self.path to the path you want the images to download it. Also make sure chromedriver is in that same path

## How to Run

Once you have done all the above, go the main.py file and at the bottom of the file,
create an instance of the class (and have a google image link for it) and call the get_google_image() method.

For instance,

imagescraper = ImageScraper("https://www.google.com/search?q=cats&tbm=isch&ved=2ahUKEwjErt2phZP2AhW18rsIHUD-AwsQ2-cCegQIABAA&oq=cats&gs_lcp=CgNpbWcQAzIECAAQQzIHCAAQsQMQQzIECAAQQzIKCAAQsQMQgwEQQzIECAAQQzIECAAQQzIHCAAQsQMQQzIECAAQQzIICAAQgAQQsQMyCAgAEIAEELEDOgUIABCABDoLCAAQgAQQsQMQgwFQwwdYqQtg5wxoAHAAeACAAUqIAbMCkgEBNZgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=y7IUYoSdNbXl7_UPwPyPWA&bih=821&biw=1440") 

imagescraper.get_google_image(5)