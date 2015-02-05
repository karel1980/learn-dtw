import glob
import sys
import os
import cv2
import numpy as np

from gesturetool import GestureTool

class PatternWriter():
    def __init__(self, pattern):
        self.pattern = pattern

    def handle(self, points):
        sampledir = os.path.join("samples", self.pattern)
        files = glob.glob(os.path.join(sampledir, "*.points"))
        
        if not os.path.exists(sampledir):
            os.makedirs(sampledir)

        i = 0
        name = os.path.join(sampledir,"%d.points"%(i))
        while name in files:
            i += 1 
            name = os.path.join(sampledir,"%d.points"%(i))

        nparr = np.array(points)
        np.savetxt(name, nparr)
        print "saved",name

if __name__ == "__main__":
    recorder = GestureTool(PatternWriter(sys.argv[1]))
    recorder.start()
