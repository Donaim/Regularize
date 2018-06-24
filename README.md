
# Regularize

Goal of this application is to see if random data can be regularized with code

# Use
First you need python >= 3.5 and pygame

Run `main.py`  
Two windows will pop up: one with target data and one with text editor  
Try to enter this code in text editor:

    reg=[]
    for x in range(15):
	    reg.append( [1] * 15 )

And save text file (no need to close)  
Prograw will compile the code and you will see that right part of target data window canged color  
That is because `reg` variable got initialized with ones  
Try to change one of its values to 0  
You 'win' if right image will be the same as left one  
You can (and should) create functions and even classes - everything that will make you code shorter  
The shorter your code is the better  
'Size' of code is measured by tokens and displayed on console after each commit  

You can change image size by writing `change_size 10 10` in console (progress will be reset)  


