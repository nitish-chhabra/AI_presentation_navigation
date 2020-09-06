import pyautogui
import time
import handy
import cv2

cap = cv2.VideoCapture(0)
# hist = handy.capture_histogram(source=0)

while True:
    ret, frame = cap.read()
    
    # detect the hand
    # hand = handy.detect_hand(frame, hist)
    
    # # plot the fingertips
    # for fingertip in hand.fingertips:
    #     cv2.circle(hand.outline, fingertip, 5, (0, 0, 255), -1)

    # cv2.imshow("Handy", hand.outline)
    cv2.imshow("Handy", frame)
    
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

# time.sleep(3)

# # pyautogui.rightClick()
# size = 10
# for i in range(size):
#     # pyautogui.scroll(-1)
#     pyautogui.press('right')
#     time.sleep(0.1)
# # pyautogui.alert('Kaam karle kuch!')
cap.release()
cv2.destroyAllWindows()