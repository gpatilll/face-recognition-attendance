# import cv2
# import numpy as np

# cap = cv2.VideoCapture(1) 
# ret, frame = cap.read()
# print(ret)
# print(frame)
# def take_photo():
#     cap = cv2.VideoCapture(1)
#     ret, frame = cap. read()
#     cv2. imwrite('webcamphoto.jpg',frame)
#     cap.release()
# take_photo()






#     #print(height)
#     #cv2.imshow("Cropped Image", crop_img)
#     #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# cv2.imshow('frame',frame)
# if cv2.waitKey(1) & 0xFF == ord('q'):
#     break   

# cap.release()
# cv2.destroyAllWindows()
# # import cv2
# # import numpy as np
# # import face_recognition
# # import os
# # from datetime import datetime

# # path = 'ImagesAttendance'
# # images = []
# # classNames = []
# # myList = os.listdir(path)
# # print(myList)
# # for cl in myList:
# #     curImg = cv2.imread(f'{path}/{cl}')
# #     images.append(curImg)
# #     classNames.append(os.path.splitext(cl)[0])
# # print(classNames)

# # def findEncodings(images):
# #     encodeList = []
# #     for img in images:
# #         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# #         encode = face_recognition.face_encodings(img)[0]
# #         encodeList.append(encode)
# #     return encodeList

# # def markAttendance(name):
# #     with open('attend.csv', 'r+') as f:
# #         myDataList = f.readlines()
# #         nameList = []
# #         for line in myDataList:
# #             entry = line.split(',')
# #             nameList.append(entry[0])
# #         if name not in nameList:
# #             now = datetime.now()
# #             dtString = now.strftime('%H:%M:%S')
# #             f.writelines(f'n{name},{dtString}')

# # encodeListKnown = findEncodings(images)
# # print('Encoding Complete')

# # # Replace with your DroidCam IP and port
# # droidcam_ip = '192.168.1.6'
# # droidcam_port = '4747'

# # cap = cv2.VideoCapture(f'http://{droidcam_ip}:{droidcam_port}/video')
# # while True:
# #     ret, img = cap.read()
# #     if not ret:
# #         print("Failed to capture frame from DroidCam.")
# #         break

# #     imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
# #     imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

# #     facesCurFrame = face_recognition.face_locations(imgS)
# #     encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

# #     for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
# #         matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
# #         faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
# #         matchIndex = np.argmin(faceDis)

# #         if matches[matchIndex]:
# #             name = classNames[matchIndex].upper()
# #             y1, x2, y2, x1 = faceLoc
# #             y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
# #             cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
# #             cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
# #             cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
# #             markAttendance(name)

# #     cv2.imshow('DroidCam', img)

# #     if cv2.waitKey(1) & 0xFF == 27:  # Press Esc to exit
# #         break

# # cap.release()
# # cv2.destroyAllWindows()# Python program to check 
# # whether the camera is opened 
# # or not 


import numpy as np 
import cv2 


cap = cv2.VideoCapture(1) 
while(cap.isOpened()): 
	
	while True: 
		
		ret, img = cap.read() 
		cv2.imshow('img', img) 
		if cv2.waitKey(30) & 0xff == ord('q'): 
			break
			
	cap.release() 
	cv2.destroyAllWindows() 
else: 
	print("Alert ! Camera disconnected") 
