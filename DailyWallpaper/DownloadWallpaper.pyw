import os
import time
import requests
import ctypes

# Define the URL for the XML data
url_xml = 'https://www.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1&mkt=en-US'

# Fetch the XML data
response = requests.get(url_xml)
xml_content = response.text

# Parse the XML to extract the image URL
image_url = xml_content.split('<url>')[1].split('</url>')[0]
image_url = 'https://bing.com' + image_url.replace('_1920x1080', '_UHD').replace('/th?id=', '/th?id=')

# Define the file paths for saving the wallpaper
file_path_jpg = os.path.join(os.environ['TEMP'], 'wallpaper.jpg')
file_path_png = os.path.join(os.environ['TEMP'], 'wallpaper.png')


# Download the image and save it as wallpaper.jpg
response = requests.get(image_url)
with open(file_path_jpg, 'wb') as f:
    f.write(response.content)

# Set wallpaper using SystemParametersInfo
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, file_path_jpg, 3)
