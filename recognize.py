import numpy as np

from gesturetool import GestureTool

class GestureRecognizer():
    def __init__(self):
        # TODO: load one of the .points files for each known shape

    def handle(self, points):
        # TODO: compare the received points to each shape, get distance from the known shapes
        # and print closest match

if __name__ == "__main__":
    recorder = GestureTool(GestureRecognizer())
    recorder.start()
