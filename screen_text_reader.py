import time
import cv2
import mss
import numpy
import pytesseract
import falcon


mon = {'top': 0, 'left': 0, 'width': 1366, 'height': 768}

with mss.mss() as sct:
    while True:
        time.sleep(1)
        im = numpy.asarray(sct.grab(mon))


        text = pytesseract.image_to_string(im)
        falcon.talk(text)



        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

        # One screenshot per second
        time.sleep(10)
