import cv2
import os

cam = cv2.VideoCapture(0)

# cv2.namedWindow("test")

classes = ["next","previous","background"]

for image_class in classes:

    img_counter = 0
    while_start = 1

    while while_start:
        
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow(image_class, frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            cv2.destroyWindow(image_class)
            while_start = 0
        elif k%256 == 32:
            # SPACE pressed
            img_name = "opencv_frame__{}.png".format(img_counter)
            path = os.getcwd()
            path = os.path.join(path,image_class)
            if not os.path.isdir(path):
                os.mkdir(path)
            cv2.imwrite(os.path.join(path ,img_name), frame)
            print("{} written!".format(img_name))
            print("Path : " + str(os.path.join(path ,img_name)))
            img_counter += 1

cam.release()

cv2.destroyAllWindows()