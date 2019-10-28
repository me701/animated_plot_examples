# Animated Plot Examples

This repository contains several example ways to produce animated plots.
Many of these examples have been adapted from [https://matplotlib.org/3.1.1/api/animation_api.html](https://matplotlib.org/3.1.1/api/animation_api.html).

In order to save any of the animations, you need to have ffmpeg or another video codex installed.
If using an anaconda system, use `conda install -c conda-forge ffmpeg` to install the codex.

The following examples explore the two main ways to animate plots, which is via function animation or artist animation.

## 1D_func_animation.py

This script is designed to create a standard 1-D plot animation using function animation.
Function animation provides a function that will update the plot in some way, e.g., changing the data.

## multiline_func_animation.py

This script provides an example of how to control multiple 1-D plots simultaneously.

## spiral.py

This example creates a 2-D plot animated with function animation.

## growing_spiral.py

This example is very similar to spiral, but the output is a bit different.

## 3D_func_animation.py

This example shows a 3-D plot of the current iteration vector that is updated for each iteration.
In other words, this example shows the convergence of a solution to the Poisson equation.
This is animated using function animation.

## 2D_artist_animation.py

This is a 2-D animation using pcolormesh and artist animation.
Artist animation creates all frames first as individual plots, then stitches the frames together.







