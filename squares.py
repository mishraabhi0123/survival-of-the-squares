import numpy as np 
import time
import matplotlib.pyplot as plt
plt.ion()

def iterate(grid):
  grid = np.pad(grid, 1, 'constant', constant_values = [0])
  col, row = grid.shape
  for i in range(1,row-1):
    for j in range(1, col-1):
      roi = grid[i-1:i+2,j-1:j+2]
      total = np.sum(roi) - grid[i,j]
      if total == 3 or total == 2:
        grid[i,j] = 1.1
      elif total > 3:
        grid[i,j] = 0
      elif total < 2:
        grid[i,j] = 0
  return grid[1:-1, 1:-1]



GRID_SIZE = (50, 50)
GRID = np.random.random(GRID_SIZE) > 0.5

while True:
  GRID = iterate(GRID)
  print(GRID)
  plt.imshow(GRID, cmap = 'gray')
  plt.show()
  plt.pause(0.01)
  plt.cla()
  GRID = GRID == 1.1
  print(GRID)
  # break

# plt.ioff()