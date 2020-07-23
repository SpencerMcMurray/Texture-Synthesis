# Texture-Synthesis

A Texture Synthesis implementation using the non-parametric method

## How To Use

Install requirements via `pip install -r requirements.txt`

Place the textures you'd like to synthesize in the /textures folder, then run main.py

You may need to alter NEW_IMG_SIZE &/ WIN_SIZES in data.py to get the results desired,
however making these values larger will increase the time it takes to complete by a lot.

Additionally, try to keep the texture sizes small, as larger textures will increase the time
cost as well.

## A Few Results

![grid](https://i.imgur.com/hvVb10u.png)

![text](https://i.imgur.com/FILAa4h.png)

## Credit

The algorithm used was created by [A.A. Efros and T.K. Leung](https://people.eecs.berkeley.edu/~efros/research/NPS/alg.html).
