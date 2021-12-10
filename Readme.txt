
System Operation and Control Guide
----------------------------------
#---------------------------------------------
# Project ID: Face Mask Detector
# Author: ---
# Date: December /021
#---------------------------------------------

Boot the Raspberry Pi module, launch the terminal(by CTRL+ALT+T) and perform
the following:

1). Change the operation directory to project directory using the following
    command and hit ENTER

  	cd  face-mask-detector-project

2). Execute the model training code using the command

	   python3 train.py

    - This command invokes the model training functionalities to start
      fetching trining datasets into the code function handlers
    - The process will take some time to accomplish the process depending on number 
      of images.
    - Upon successful completion, the algorithm will be ready to recognize based on the 
      test objective
