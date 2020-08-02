# Texture-Synthesis

A Texture Synthesis implementation using the non-parametric method

Authors:
Spencer McMurray
Mohan Vashist
## How To Use

Install requirements via `pip install -r requirements.txt`

Place the textures you'd like to synthesize in the /textures folder, then run main.py

You may need to alter NEW_IMG_SIZE &/ WIN_SIZES in data.py to get the results desired,
however making these values larger will increase the time it takes to complete by a lot.

Additionally, try to keep the texture sizes small, as larger textures will increase the time
cost as well.

Feel free to modify the values in data.py, if you wish to disable to show progress or saving images, those flags are located in main.py

Note:
 1) We can confirm this script works with Python 3.8.3, cannot confirm success for other versions of Python
 2) We can confirm the desired results for the current window sizes given in data.py, we encourage testing and manipulating the windows sizes, however, going below a window size of 3 may cause the program to crash.

## A Few Results

![grid](https://i.imgur.com/hvVb10u.png)

![text](https://i.imgur.com/FILAa4h.png)

![text](https://i.imgur.com/dqZnq52.png)

## Credit

The algorithm used was created by [A.A. Efros and T.K. Leung](https://people.eecs.berkeley.edu/~efros/research/NPS/alg.html).
