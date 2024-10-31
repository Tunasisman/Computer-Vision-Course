import cv2

img = cv2.imread('00-puppy.jpg')

while True:
    cv2.imshow('Puppy', img)

    # If we have waited at least 1 ms and we have pressed the Esc
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()