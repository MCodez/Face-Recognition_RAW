# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 12:18:52 2017

@author: LALIT ARORA
"""

from PIL import Image 
import cv2,os
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'dataSet'


def getImageswithId(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    IDs=[]
    for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert('L')
        faceNp=np.array(faceImg,'uint8')
        ID=int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)
        IDs.append(ID)
        cv2.imshow("Training.",faceNp)
        cv2.waitKey(10)
    return np.array(IDs),faces

Ids,faces=getImageswithId(path)
recognizer.train(faces,Ids)
recognizer.write('trainer/trainingData.yml')
cv2.destroyAllWindows()