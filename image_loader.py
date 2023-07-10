#!/usr/bin/python3

from color_detection import detect_color, train_model
import imageio.v3 as iio
import numpy as np

def import_image():
  img = iio.imread('data/4_pixels.png')
  print (img.shape)

  img_arr = np.asarray(img)

  color_model = train_model()
  #NOTE: Obviously don't use a double for loop, try list comprehension?
  #TODO: Add frequency dict for "Broad Color" for next stage.
  for x in range(img_arr.shape[0]):
    for y in range(img_arr.shape[1]):
      #NOTE: Detect color is literally one line, might not be needed...
      print(detect_color(color_model, img_arr[x][y]))

if __name__ == '__main__':
  import_image()
