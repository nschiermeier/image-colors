#!/usr/bin/python3

import imageio.v3 as iio
import numpy as np
import sys

def import_image(image_path, debug=False):
  img = iio.imread(image_path)

  if debug:
    print (f"Image path: {image_path}\nImage Size: {img.shape}\n")


  img_arr = np.asarray(img)
  return img_arr

if __name__ == '__main__':

  if len(sys.argv) != 2:
    print("Provide image path to debug")
    sys.exit(1)
  import_image(sys.argv[1], True)

