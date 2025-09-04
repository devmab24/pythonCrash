picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
]

def show_tree():
  for image in picture:
    for pixel in image:
      if (pixel):
        print('*', end ="")
      else:
        print(' ', end ="")
    print('')

show_tree()
