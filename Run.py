from exif import Image

# Import Module
import os
  
# Folder Path
path = "E:/Photomanagement/"
  
# Change the directory
os.chdir(path)
  
# Read text File
  
date="2021:11:25 00:00:00"

# iterate through all file
for file in os.listdir():
    
    with open(file, "rb") as photo:
        image = Image(photo)
        image.datetime_original = date
        print(image.datetime_original)
    with open(file, 'wb') as updated_photo:
        updated_photo.write(image.get_file())
    with open(file, "rb") as photo:
        image = Image(photo)
        print(image.datetime_original)
