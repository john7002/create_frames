#you can check the frame rate by VLC. Go to windows -> media information -> codec details
# Based on Tobi Lehman script https://tobilehman.com/blog/2013/01/20/extract-array-of-frames-from-mp4-using-python-opencv-bindings/
import sys
import argparse
from os import listdir
from os.path import isfile, join

import cv2

def extractImages(folderIn, pathOut,resolution=0):
    videofiles = [f for f in listdir(folderIn) if isfile(join(folderIn, f))]
    count_label = 0
    for v_file in videofiles:
        print("Start extracting frames from {0}{1}".format(folderIn,v_file))
        vidcap = cv2.VideoCapture(join(folderIn,v_file))
        success,image = vidcap.read()
        success = True
        count = 0
        while success:
          vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*resolution))
          success,image = vidcap.read()
          print ('Read a new frame: ', success)
          cv2.imwrite( pathOut + "\picture%d.jpg" % count_label, image) # add picture type as option in next version
          count_label += 1
          count +=1

if __name__=="__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--folderIn", help="directory to video(s)")
    a.add_argument("--pathOut", help="path to images")
    a.add_argument("--ms_resolution",type=int, help="get a frame every x milliseconds. By default generate jpg for every frames")
    args = a.parse_args()

    if args.ms_resolution:
        print("Will genererate a frame every {0} milliseconds".format(args.ms_resolution))


    if (args.ms_resolution==None):
        extractImages(args.folderIn, args.pathOut)
    else:
        extractImages(args.folderIn, args.pathOut, args.ms_resolution)
