import cv2 as cv
import pylab as pl

image=cv.imread('tree.jpg')
#pl.figure()
#pl.imshow(image)
#pl.show()
cv.namedWindow("import image",cv.WINDOW_AUTOSIZE)
cv.imshow("import image",image)
cv.waitKey(0)
cv.destroyAllWindows()
