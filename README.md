# CBIR

This is the fourth version of a SIFT (Scale Invariant Feature Transform) implementation using CUDA for GPUs from NVidia. The first version is from 2007 and GPUs have evolved since then. This version is slightly more precise and considerably faster than the previous versions and has been optimized for Kepler and later generations of GPUs.

On a GTX 1060 GPU the code takes about 1.2 ms on a 1280x960 pixel image and 1.7 ms on a 1920x1080 pixel image. There is also code for brute-force matching of features that takes about 2.2 ms for two sets of around 1900 SIFT features each.

The code relies on CMake for compilation and OpenCV for image containers. OpenCV can however be quite easily changed to something else. The code can be relatively hard to read, given the way things have been parallelized for maximum speed.

The code is free to use for non-commercial applications. If you use the code for research, please cite to the following paper.

M. Bj&ouml;rkman, N. Bergstr&ouml;m and D. Kragic, "Detecting, segmenting and tracking unknown objects using multi-label MRF inference", CVIU, 118, pp. 111-127, January 2014. [ScienceDirect](http://www.sciencedirect.com/science/article/pii/S107731421300194X)

## New version for Pascal (2018-10-26)



