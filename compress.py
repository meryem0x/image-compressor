#!/usr/bin/python3
import os
import concurrent.futures
from PIL import Image
from multiprocessing import cpu_count

img_names = os.listdir()

def process_image(imgs):
  try:
    img_name = imgs
    img = Image.open(img_name)
    img.thumbnail((1020,573))
    img.save(f"compress/{img_name}")
    print(f"{img_name} okay")
  except:
    print("OOPSS!")

with concurrent.futures.ProcessPoolExecutor(max_workers=cpu_count() - 1) as executor:
  executor.map(process_image, img_names)

