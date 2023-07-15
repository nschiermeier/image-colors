#!/usr/bin/python3

import imageio.v3 as iio
import numpy as np

#TODO: let users specify location of file
def import_image(debug=False):
  img = iio.imread('data/4_pixels.png')

  path = "lol"
  if debug:
    print (f"Image path: {path}\nImage Size: {img.shape}\n")


  img_arr = np.asarray(img)
  return img_arr

if __name__ == '__main__':
  import_image(True)
