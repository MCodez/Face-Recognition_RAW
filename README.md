# Face-Recognition_RAW

Face Recognition using LBPH Face Recognizer using OpenCV 3 and Python 3.6

## Procedure: 

### Py files :

1. recog_face - Recognizes face of the person in real time using trainer.
2. SetCreator - Creates data set by taking multiple images of user and ask for Input (name) for every dataset.  
3. trainer - Trains LBPH Face Recognizer using the dataset created by the SetCreator.

### Classifier:

1. haarcascade_frontalface_default - Frontal Face classifier for detecting the frontal face of person while creating dataset.

### Database:

1. pdb.sqlite - Database with one table named "people". 
                TABLE `people` ( `Id` INTEGER PRIMARY KEY AUTOINCREMENT, `Name` TEXT, `Username` TEXT, `Email` TEXT, `Mobile` TEXT )

### Folders:

Create two folders with names-

1. dataSet - All the dataset images will be stored in this folder with appropriate file name.
2. trainer - Trainer file (.yml)  will be generated from the dataset images.

### Sequence of Execution of Files:

SetCreator >> trainer >> recog_face

## Softwares:

1. Python 3.6 
    Dependencies: 
                  Numpy
                  PIL
                  OS
                  OPENCV (cv2)
                  SQLITE3
