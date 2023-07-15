#!/usr/bin/python3

#NOTE: Other possible names: color_stats, stats4colors, image_breakdown, image_color_breakdown, color_breakdown

from collections import OrderedDict
from color_detection import train_model, detect_color
from image_loader import import_image
from matplotlib import pyplot as plt
import argparse
import os
import sys

def validate_args(args):

  if not os.path.exists(args.input):
    print("Input image does not exist! Exiting")
    return 1
  
  valid_extensions = ['.jpg', '.png', '.jpeg'] # add more later?
  ext = os.path.splitext(args.input)[1]
  
  if ext not in valid_extensions:
    print ("Input image type not supported!")
    return 1

  return 0

def get_frequency(image_path):

  img_arr = import_image(image_path)

  color_model = train_model()
  #TODO: Find a more efficient way to do this? (One-step it)

  freq2 = {}
  color_list = [detect_color(color_model, img_arr[x][y]) for y in range(img_arr.shape[1]) for x in range(img_arr.shape[0])]

  freq = {}
  for color in color_list:
    if (color[0] in freq):
      freq[color[0]] += 1
    else:
      freq[color[0]] = 1

  #ENDTODO
  print(freq)

  # create a dictionary that sorts the keys based on their values
  # Taken from GeeksforGeeks: geeksforgeeks.org/python-sort-dictionary-by-values-and-keys/
  res = {val[0] : val[1] for val in sorted(freq.items(), key = lambda x: (-x[1], x[0]))}
  print(res)
  print(len(color_list))
  for item in res:
    #TODO: add color names here too, make it prettier
    print(f'{round(float(res[item]) / float(len(color_list)), 3)*100}%')
  return freq

def show_chart(frequency):
  
  #TODO: make this look better (better colors)
  #      add the percentages(?)
  #      add something that prints where this saved (user_files?)

  fig, ax = plt.subplots()

  piechart, text = plt.pie(frequency.values(), colors=frequency)
  ax.legend(piechart, frequency, loc="best")
  plt.title("Your Image by Colors")
  plt.show()
  fig.savefig("figure.png")

if __name__ == "__main__":
  #TODO: Add optional flag for chart
  parser = argparse.ArgumentParser()

  parser.add_argument("input",
                      help="The input file (image) to see the colors by percentage of"
                     )

  args = parser.parse_args()

  ret_val = validate_args(args)
  if ret_val != 0:
    sys.exit(ret_val)

  new_freq = get_frequency(args.input)
  show_chart(new_freq)

