import pyautogui
from fastai.vision import *
import cv2
import torch
import time
import warnings
warnings.filterwarnings('ignore')

# counter = 0

cap = cv2.VideoCapture(0)
learn = load_learner(os.getcwd())

while True:
    a = time.time_ns()
    ret, frame = cap.read()
    t = torch.tensor(np.ascontiguousarray(np.flip(frame, 2)).transpose(2,0,1)).float()/255
    img = Image(t)
    preds = learn.predict(img)
    # print(preds)
    # font = cv2.FONT_HERSHEY_SIMPLEX 
    predicted_class_probability = preds[2][learn.data.classes.index(str(preds[0]))].item()
    if predicted_class_probability>0.95:
        prediction = str(preds[0])
        if prediction == "next":
            pyautogui.scroll(-60)
        elif (prediction == "previous") and (predicted_class_probability>0.99):
            pyautogui.scroll(60)
        else:
            pass

    # The commented out code is to track the Predictions and FPS in on a webcam video output.
    # In normal usage a webcam video output is not required.

    #     cv2.putText(frame, str(preds[0]),(50, 50), font, 1,(0, 255, 255), 2, cv2.LINE_4)
    
    # if counter:
    #     b = time.time_ns()
    #     try:
    #         fps = round(1/((b-a)/ (10 ** 9)),1)
    #     except:
    #         fps = "Unlimited"
    #     finally:q
    #         cv2.putText(frame, str(fps),(250, 50), font, 1,(0, 255, 255), 2, cv2.LINE_4)
    # cv2.imshow("Test", frame)
    # counter = 1
    
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
