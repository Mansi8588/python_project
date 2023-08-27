import cv2
import matplotlib.pyplot as plt
config_file="ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
frozen_model=r"C:\Users\younl\Downloads\frozen_inference_graph (2).pb"
model=cv2.dnn_DetectionModel(frozen_model,config_file)

# putting label file into classLable
classLabels=[]
file_name="coco.name"
with open(file_name,"rt") as name:
    classLabels=name.read().rstrip("\n").split("\n")
 # print(len(classLabels))

model.setInputSize(320,320)
model.setInputScale(1.0/127.5)
model.setInputMean((127.5,127.5,127.5))
model.setInputSwapRB(True)


#cap=cv2.VideoCapture(1)
#img=cv2.imread(cap)
#classIds, confs, bbox = model.detect(img, confThreshold=1)
#print(classIds)

cap=cv2.VideoCapture(0)
if not cap.isOpened():
    cap=cv2.VideoCapture(1)
if not cap.isOpened():
    raise IOError("can not open the video")
font_scale=3
font=cv2.FONT_HERSHEY_PLAIN
while True:
   success,im=cap.read()
   classIds,confs,bbox = model.detect(im,confThreshold=0.5)
   print(classIds,bbox)
   if len(classIds) !=0:
     for classID,confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
         if(classID<=80):
             cv2.rectangle(im,box,(32,67,99),2)
             cv2.putText(im,classLabels[classID-1],(box[0]+10,box[1]+30),font,fontScale=font_scale,color=(225,0,0),thickness=2)
   cv2.imshow("obj",im)
   if cv2.waitKey(2) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

