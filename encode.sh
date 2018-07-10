#!/bin/sh 
mencoder mf://frame*.png -mf fps=2 -ovc lavc -lavcopts vcodec=mpeg4:mbd=2:trell -oac copy -o output.avi
