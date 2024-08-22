import cv2 as cv
import numpy as np


def locator(path, dist, min_radius, max_radius, put_text=True):
    img = cv.imread(path)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_blur = cv.GaussianBlur(img_gray, (7, 7), sigmaX=1.5, sigmaY=1.5)
    img_th = cv.adaptiveThreshold(img_blur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 5)
    # cv.imshow("Contours", img_th)
    circles = cv.HoughCircles(img_th, cv.HOUGH_GRADIENT, 1, minDist=dist, param1=100, param2=30,
                              minRadius=min_radius, maxRadius=max_radius)

    centroids = []
    if circles is not None:
        # circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            centroids.append((str(i[0]), str(i[1])))
            text = f"({i[0]},{i[1]})"
            i = np.uint16(np.around(i))
            cv.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 1)
            cv.circle(img, (i[0], i[1]), 1, (0, 0, 255), 2)
            if put_text:
                cv.putText(img, text, (i[0] - 60, i[1] + 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv.LINE_AA)
    # cv.imshow("Detected Circles", img)
    # cv.waitKey(0)
    return centroids
