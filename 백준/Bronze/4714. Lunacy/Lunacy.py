import sys

while(True):
  N = float(sys.stdin.readline())
  if N == -1.0:
    break
  else:
    print('Objects weighing', "%.2f" % N, 'on Earth will weigh', "%.2f" % (N*0.167), 'on the moon.')
