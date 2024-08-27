import numpy as np
import cv2 as cv

class Tracker():
    def __init__(self, path_to_haar='haarcascade_frontalface_default.xml'):
        self.haar_file = path_to_haar
        self.cap = cv.VideoCapture(0)
        self.face_cascade = cv.CascadeClassifier(self.haar_file)

    
    def detect_face(self, gray):
       faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)  
       for face in faces:
           (x,y,w,d) = face
           cv.rectangle(gray,(x,y),(x+w, y+d),(255, 255, 255), 2)
    def web_start(self,):
        if not self.cap.isOpened():
            print("Cannot open camera")
            exit()
        while True:
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            # Our operations on the frame come here
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            self.detect_face(gray)
            # Display the resulting frame
            cv.imshow('frame', gray)
            if cv.waitKey(1) == ord('q'):
                break
 
# When everything done, release the capture
        self.cap.release()
        cv.destroyAllWindows()

if __name__ == "__main__":
    tracker = Tracker()
    tracker.web_start()

