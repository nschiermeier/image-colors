#!/usr/bin/python3

from color_detection import train_model, detect_color
from image_loader import import_image
import argparse

img_arr = import_image()

color_model = train_model()
#TODO: Find a mroe efficient way to do this?
color_list = [detect_color(color_model, img_arr[x][y]) for y in range(img_arr.shape[1]) for x in range(img_arr.shape[0])]


print (color_list)

freq = {}
for color in color_list:
  print(color[0])
  if (color[0] in freq):
    freq[color[0]] += 1
  else:
    freq[color[0]] = 1

print(freq)
