#  aneye.py
#  				Date and Time : 20.10.2020 03:10:28
#				 Author Name : Arjun B Chennithala 
#	Author GitHub profile : https://github.com/arjunbchennithala
#
#
#  Copyright 2020 Arjun B Chennithala <arjunbchennithala@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
#!/usr/bin/python3


#Importing libraries
import cv2  
import face_recognition as fr 

#Importing Trained models for detecting face and body
face_cascade = cv2.CascadeClassifier("../cascade/face_cascade.xml")
body_cascade = cv2.CascadeClassifier("../cascade/fullbody_cascade.xml")

#Text properties configuration
font = cv2.FONT_HERSHEY_SIMPLEX 
fontScale = 1
color = (0,255,0)
color2 = (0,255,200)
thickness = 2
org = (50,50)
org2 = (50,80)

#Method video definition
def video(filename="../video/short_hamilton_clip.mp4",method=0,body=0):
	
	faces = 0
	bodies = 0
	cap = cv2.VideoCapture(filename) 
	
	while True:
		ret,frame = cap.read() #Extracting each frames
		
		if ret:
			gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #Converting to Grayscale image for good detection.
			
			if method == 0:
				faces = face_cascade.detectMultiScale(gray,1.189,8) #Comparing with trained models for detecting face
				if body:
					bodies = body_cascade.detectMultiScale(gray,1.5,2)
					
				if len(faces) > 0:
					for (x,y,w,h) in faces:
						cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)	
						
				if body:
					for (x1,y1,w1,h1) in bodies:
						cv2.rectangle(frame,(x1,y1),(x1+w1,y1+h1),(0,255,200),2)	
				
			elif method == 1:
				if body:
					bodies = body_cascade.detectMultiScale(gray,1.5,2)
					
				faces = fr.face_locations(frame)
				if faces:
					for i in faces:
						y1 = i[0]
						x2 = i[1]
						y2 = i[2]
						x1 = i[3]
						
						#Drawing rectangles around the found faces
						cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2) 
				
				if body:
					for (x1,y1,w1,h1) in bodies:
						
						#Drawing rectangles around the foud bodies
						cv2.rectangle(frame,(x1,y1),(x1+w1,y1+h1),(0,255,200),2) 
				
			#Writing text above the frame
			word = "Faces detected : "+str(len(faces))
			cv2.putText(frame,word, org, font, fontScale, color, thickness, cv2.LINE_AA)
			
			if body:
				word = "Bodies detected : "+str(len(bodies))
				cv2.putText(frame,word, org2, font, fontScale, color2, thickness, cv2.LINE_AA)
			
			cv2.imshow("Frames",frame) #Displaying the result
			if cv2.waitKey(30) & 0xFF == ord('q'):
				break
		else:
			break
			
			

#Definition of picture Method
def picture(filename="../pictures/kit_with_rose.jpg",method=0,body=0):
	faces = 0
	bodies = 0
	img = cv2.imread(filename,1)
		
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	if method == 0:
		faces = face_cascade.detectMultiScale(gray,1.189,8)
		if body:
			bodies = body_cascade.detectMultiScale(gray,1.5,2)
		if len(faces) > 0:
			for (x,y,w,h) in faces:
				cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
				
		if body:
			for (x1,y1,w1,h1) in bodies:
				cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(0,255,200),2)	
		
				
	elif method == 1:
		
		faces = fr.face_locations(img)
		
		if body:
			bodies = body_cascade.detectMultiScale(gray,1.5,2)
			
		if faces:
			for i in faces:
				y1 = i[0]
				x2 = i[1]
				y2 = i[2]
				x1 = i[3]
				cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
				
		if body:
			for (x1,y1,w1,h1) in bodies:
				cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(0,255,200),2)
		
		
	if len(faces) > 0:
		word = "Faces detected : "+str(len(faces))
		print(word)
		cv2.putText(img,word, org, font, fontScale, color, thickness, cv2.LINE_AA)
		
	if body:
		word = "Bodies detected : "+str(len(bodies))
		print(word)
		cv2.putText(img,word, org2, font, fontScale, color2, thickness, cv2.LINE_AA)
		
	resize = cv2.resize(img,(int(img.shape[1]/1.5),int(img.shape[0]/1.5)))
	
					
	cv2.imshow("Image",resize)
	cv2.waitKey(0)
	
cv2.destroyAllWindows()
