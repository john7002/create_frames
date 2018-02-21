#you can check the frame rate by VLC. Go to windows -> media information -> codec details

import sys
import argparse

import cv2
print(cv2.__version__)

def extractImages(pathIn, pathOut,resolution=0):
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
      vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*resolution))
      success,image = vidcap.read()
      print ('Read a new frame: ', success)
      cv2.imwrite( pathOut + "\\frame%d.jpg" % count, image) # add picture type as option in next version
      count += 1

if __name__=="__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video")
    a.add_argument("--pathOut", help="path to images")
    a.add_argument("--ms_resolution",type=int, help="get a frame every x milliseconds. By default generate jpg for every frames")
    args = a.parse_args()

    if args.ms_resolution:
        print("Will genererate a frame every {0} milliseconds".format(args.ms_resolution))
    print(args)
    if (args.ms_resolution==None):
        extractImages(args.pathIn, args.pathOut)
    else:
        extractImages(args.pathIn, args.pathOut, args.ms_resolution)
