import cv2
import numpy as np

class GestureTool:
    
    def __init__(self, pattern_handler):
        self.current = None
        self.drawing = False
        self.pattern_handler = pattern_handler

    # mouse callback function
    def handle_mouse_callback(self,event,x,y,flags,param):

        if event == cv2.EVENT_LBUTTONDOWN:
            self.current = []
            self.current.append((x,y))

        elif event == cv2.EVENT_MOUSEMOVE:
            if self.current is not None:
                self.current.append((x,y))

        elif event == cv2.EVENT_LBUTTONUP:
            self.pattern_handler.handle(self.current)
            self.current = None

    def start(self):
        # Create a black image, a window and bind the function to window
        img = np.zeros((512,512,3), np.uint8)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image',self.handle_mouse_callback)

        while(1):
            cv2.imshow('image',img)
            if cv2.waitKey(20) & 0xFF == 27:
                break
        cv2.destroyAllWindows()

