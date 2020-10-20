# Aneye

# Face detection and Body detection module for python.

## Use aneye module by creating a python file outside the cloned aneye folder , then import aneye module.

## Create pull request to dev branch.

## Two Methods are used to detect and display faces:

 ### video()
 ### picture()
 
## Syntax:

### video(filename="<filename>",method=<0/1>,body=<0/1>,scale=<1-10>,title="")
 
### picture(filename="<filename>",method=<0/1>,body=<0/1>,scale=<1-10>,title="")

## Properties in Methods:

### filename : It is the name of your selected file.There is default file in both.
### method : It is the capability of detection 0 is default value 0 uses the Trained model,1 uses an external library called face_recognition.
### body : It tells the program to detect or don't detect body.Default is 0/False.
### scale : It tells the program whether you want to scale more number means more decreased window.Default is 1 
  
  

## example 1:

### import aneye
### aneye.picture()
  
  
## example 2:

### import aneye
### aneye.picture(filename="aneye/pictures/biden.jpg",method=1,body=1,scale=2,title="Sample")
 
 
## example 3:

### import aneye
### aneye.video()
  
  
## example 4:

### import aneye
### aneye.picture(filename="<file>",method=1,body=1,scale=2,title="Sample")
 
  
