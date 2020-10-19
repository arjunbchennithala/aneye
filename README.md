# aneye
Face detection and Body detection module for python.

use the module /src/aneye.py

Two Methods are used to detect and display faces

##video()
##picture()
video(filename="<filename>",method=<0/1>,body=<0/1>)
picture(filename="<filename>",method=<0/1>,body=<0/1>)

Properties in Methods:
  filename : It is the name of your selected file.There is default file in both.
  method : It is the capability of detection 0 is default value 0 uses the Trained model,1 uses an external library called face_recognition.
  body : It tells the program to detect or don't detect body.Default is 0/False.

example 1:
  import aneye
  aneye.picture()
  
 example 2:
 import aneye
 aneye.picture(filename="../pictures/biden.jpg",method=1,body=1)
 
  
