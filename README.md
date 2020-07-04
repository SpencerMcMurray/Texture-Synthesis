# Texture-Synthesis
A Texture Synthesis implementation using the non-parametric method

## Using the program
To run the texture synthesis, put all the textures you want to use in the /textures folder and make sure that they aren't too large, otherwise it will take a very long time (64x64 textures run in a reasonable amount of time).

Next you need to go into the data.py file and change the NEW_IMG_SIZE variable to be the desired size of the synthesized images. You can also choose to tune the WIN_SIZES variable to get more accurate results.

Finally run main.py and the program will start. It will keep you updated with frequent prints to tell you what stage the program is on.

## Credit
The algorithm used was created by [A.A. Efros and T.K. Leung](https://people.eecs.berkeley.edu/~efros/research/NPS/alg.html).
