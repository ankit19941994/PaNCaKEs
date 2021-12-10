
System Operation and Control Guide
---------------------------------

After booting the Pi, launch the terminal(by CTRL+ALT+T) and perform
the following:

1). Change the operation to project directory enter the following
    command and hit ENTER

	cd  facial_recognition

2). Start taking sample pictures using the following command and hit ENTER

	python3 headshots_picam.py

    - This command invokes a new window for camera image display 
    - Position your face well before the camera and take the camera shots by 
      pressing the "space key" on the keyboard(every press of the key corresponds to a snapshot).
    - At least 20 to 30 images are essential for training process.
    - The saved images are stored in the project owner directory e.g "Student-X" for this case stored 
      in "dataset" directory.
    - NOTE: 
        - Image storage directory e.g "Student-X" will correspond to image recognition in the next step below.
  	    - Hence ensure to create multiple storage directories for different individuals whose face images
  	      are to be taken.

    - Close this camera window by pressing "ESC" key on the keyboard


3). To train the project algorithm in order to be able to recognize the above saved images run the command 

	python3 train_model.py

    - This will take some time depending on the number of saved images creating a file named "encodings.pickle" 
      containing the criteria for identifying faces.
    - Upon successful completion, the algorithm will be ready to recognize the saved images in comperison with
      the camera capture in recognition process(next step).

4). Finally, use the following command to run the faces recognition process

	python3 recognition.py

    - Like the command in step 2, this invokes the camera in to action ready to capture image faces for recognition.
    - Upon successful face image match with the saved images a relay is energized to innitiate door opening 
    - This is captured in a short notification displayed.
    - Close this camera window by pressing "Q" key on the keyboard
	
