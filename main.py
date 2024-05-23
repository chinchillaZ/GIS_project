import csv
import os
import pandas as pd


# 三豐1004
def tell_dir_row(dir):
  # region: dir_ranges
  dir_ranges = {
    (0, 11.25): 0, # be carefull, later
    (11.25,33.75) : 1, 
    (33.75,56.25) : 2, 
    (56.25,78.75) : 3, 
    (78.75,101.25) : 4, 
    (101.25,123.75) : 5, 
    (123.75,146.25) : 6, 
    (146.25,168.75) : 7, 
    (168.75,191.25) : 8, 
    (191.25,213.75) : 9, 
    (213.75,236.25) : 10, 
    (236.25,258.75) : 11, 
    (258.75,281.25) : 12, 
    (281.25,303.75) : 13, 
    (303.75,326.25) : 14, 
    (326.25,348.75) : 15,
    (348.75, 360): 0
}
# endregion
  
  #對比dir_ranges
  for dir_ranges, dir_name in dir_ranges.items():
    start, end = dir_ranges
    if start <= float(dir) < end:
        return dir_name
  return -1
  

def tell_speed_col(speed):
# region: speed_ranges
  speed_ranges = {
    (0, 3.3): 0,
    (3.4, 7.9): 1,
    (8, 13.8): 2,
    (13.9, 20.7): 3,
    (20.8, 28.4): 4,
    (28.4, 35): 5,
    (35, 50): 6,
    (50, 52): 7,
    (53, 54): 8,
    (55, 100): 9,
    (100, 120): 10,
    (120, 130): 11
}
# endregion
  
  #對比speed_ranges
  for speed_range, speed_name in speed_ranges.items():
    start, end = speed_range
    if start <= float(speed) < end:
        return speed_name
  return -1



with open('梧棲1005.csv', newline='') as csvfile:
  input_file_name = '梧棲1005.csv'
  # 讀取 CSV 檔案內容
  data = list(csv.reader(csvfile))
  print(data)

result_list = []
zero_matrix = [[0 for _ in range(12)] for _ in range(16)]

for i in range(len(data)):
  # print(data[i][0]) #string type
  x = tell_dir_row(data[i][0])
  y = tell_speed_col(data[i][1])
 
  result_list.append([x, y])
  zero_matrix[x][y] += 1 # save in matrix
print()
print(result_list)
print()
print(zero_matrix)

# pricessing the string 
output_file_name = input_file_name.split(".")[0]
save_name = output_file_name + "_ouput.csv"


# Open the CSV file for writing (overwrite existing file)
with open(save_name, 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)

  # Write each row (sublist) to the CSV file
  for row in zero_matrix:
    writer.writerow(row)

print("save!" + save_name)



