import cv2
import numpy as np

cv2.namedWindow( "settings" )

def nothing(*arg): pass

cap = cv2.VideoCapture(0)
cv2.createTrackbar('h1', 'settings', 0, 255, nothing)
cv2.createTrackbar('s1', 'settings', 0, 255, nothing)
cv2.createTrackbar('v1', 'settings', 0, 255, nothing)
cv2.createTrackbar('h2', 'settings', 255, 255, nothing)
cv2.createTrackbar('s2', 'settings', 255, 255, nothing)
cv2.createTrackbar('v2', 'settings', 255, 255, nothing)
cv2.createTrackbar('b1', 'settings', 0, 255, nothing)
cv2.createTrackbar('g1', 'settings', 0, 255, nothing)
cv2.createTrackbar('r1', 'settings', 0, 255, nothing)
cv2.createTrackbar('b2', 'settings', 255, 255, nothing)
cv2.createTrackbar('g2', 'settings', 255, 255, nothing)
cv2.createTrackbar('r2', 'settings', 255, 255, nothing)
cv2.createTrackbar('mask', 'settings', 0, 2, nothing)
cv2.createTrackbar('HSV/BGR', 'settings', 0, 1, nothing)
cv2.createTrackbar('HSV/BGR(res)', 'settings', 0, 2, nothing)

while True:
    flag, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )

    h1 = cv2.getTrackbarPos('h1', 'settings')
    s1 = cv2.getTrackbarPos('s1', 'settings')
    v1 = cv2.getTrackbarPos('v1', 'settings')
    h2 = cv2.getTrackbarPos('h2', 'settings')
    s2 = cv2.getTrackbarPos('s2', 'settings')
    v2 = cv2.getTrackbarPos('v2', 'settings')
    b1 = cv2.getTrackbarPos('b1', 'settings')
    g1 = cv2.getTrackbarPos('g1', 'settings') 
    r1 = cv2.getTrackbarPos('r1', 'settings')
    b2 = cv2.getTrackbarPos('b2', 'settings')
    g2 = cv2.getTrackbarPos('g2', 'settings')
    r2 = cv2.getTrackbarPos('r2', 'settings')
    mask_type = cv2.getTrackbarPos('mask', 'settings')
    color_type = cv2.getTrackbarPos('HSV/BGR', 'settings')
    res_type = cv2.getTrackbarPos('HSV/BGR(res)', 'settings')

    bgr = cv2.inRange(img, (b1, g1, r1), (b2, g2, r2))
    thresh = cv2.inRange(hsv, (h1, s1, v1), (h2, s2, v2))
    mask = cv2.bitwise_and(thresh, thresh, mask=bgr)
    mask_bgr = cv2.bitwise_and(img, img, mask=bgr)
    mask_duo = cv2.bitwise_and(img, img, mask=mask)
    mask_tresh = cv2.bitwise_and(img, img, mask=thresh)

    if res_type == 0:
        cv2.imshow('bgr_res', bgr)
        cv2.destroyWindow('hsv_res')
        cv2.destroyWindow('duo_res')
    elif res_type == 1:
        cv2.imshow('hsv_res', thresh)
        cv2.destroyWindow('bgr_res')
        cv2.destroyWindow('duo_res')
    else: 
        cv2.imshow('duo_res', thresh)
        cv2.destroyWindow('bgr_res')
        cv2.destroyWindow('hsv_res')

    if color_type == 0:
        cv2.imshow('bgr', img)
        cv2.destroyWindow('hsv')
    else:
        cv2.imshow('hsv', hsv)
        cv2.destroyWindow('bgr')

    if mask_type == 0:
        cv2.imshow('mask_bgr', mask_bgr)
        cv2.destroyWindow('mask_tresh')
        cv2.destroyWindow('mask_duo')
    elif mask_type == 1:
        cv2.imshow('mask_tresh', mask_tresh)
        cv2.destroyWindow('mask_bgr')
        cv2.destroyWindow('mask_duo')
    else:
        cv2.imshow('mask_duo', mask_duo)
        cv2.destroyWindow('mask_tresh')
        cv2.destroyWindow('mask_bgr')

    ch = cv2.waitKey(1)
    if ch == 27: break

cap.release()
cv2.destroyAllWindows() 
