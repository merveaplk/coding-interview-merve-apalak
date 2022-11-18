# BSP-ML Coding Interview
## Biomedical signal processing and machine learning coding interview
### Department of Biomedical Informatics, Emory University

Please answer the following questions and push your codes and documentation to the same repository by the due date and time.

---
1. **File handling**

Write a script (in Python, MATLAB, or Linux Shell) to read the creation date and [MD5 hash](https://en.wikipedia.org/wiki/Md5sum) of the `.mat` records of the `A00` *training* dataset of the [PhysioNet/Computing in Cardiology Challenge 2017](https://physionet.org/content/challenge-2017/1.0.0/). Generate a CSV file with the following columns:
- #1: The .mat file path and name relative to the root folder of the data. Example: `./training/A00/A00001.mat`
- #2: The MD5 hash of the data file (in HEX). Example: `c5edcf9aeb1c20ec632853edabe59ac1`
- #3: File size in bytes. Example: `18024`
- #4: File creation date in `YYYYMMDDhhmmss` format. Example `201701101421`
- #5: File Modification date in `YYYYMMDD` format.
- #6: The sampling frequency of the `.mat` file, which can be found from the corresponding header files (same base file name but with `.hea` extension) according to the [WFDB header file format](https://www.physionet.org/physiotools/wag/header-5.htm).

---
2. **Random variables**

2a. Sample $n$ = 1000 elements, with replacement, uniformly at random from the set $X$ = {0, 1} of size $m =\|X\|=$ 2. Record your samples in a vector $Y$ of length $n$.
     
2b. Implement a function $f(Y)$ that counts the number of occurrences of each $x \in X$ in Y. Record the counts in a vector $Z$ of length $m$. While $n$ = 1000, $X$ = {0, 1}, and $m$ = 2, implement your function for an arbitrary number $n$ of samples from an arbitrary set $X$ of size $m$, e.g., if one of the elements of $Y$ were “2” or “a”, then your function should count them as well. 
     
2c. Evaluate the statistical significance of the number of 0s and 1s in $Y$ under the null hypothesis that they were sampled uniformly at random with replacement. You can use your code from 1a and 1b. Which statistical significance test did you use?
     
2d. Repeat steps 2a-2c for a total of $r$ = 1000 times. Record the $p$-values from your statistical significance test in a vector $W$ of length $r$.
     
2e. How are the values of $W$ distributed? Why? Can you quantify your answer or use another statistical test to show it?

---
3. **File handling**

There are 1377 JPEG images of scallions/onions growing over a 24 hour time period in either the following folder or `tar.gz` file. The filenames are given by the MD5 checksums of the image files, so the files (or at least the filenames) aren’t ordered chronologically:
https://drive.google.com/drive/folders/14HhFab1s4Q5nMI2uPWWF5r5UC4ofbs4L?usp=sharing
https://drive.google.com/file/d/1qndW3o4C22JRNoY0X5Kt6onB3gPQy8Qi/view?usp=sharing

For the following tasks, you don’t need to use a command-line tool to download the image files or upload the video, and you can use your favorite file browser to test the files, but please use the command line for the main tasks.

3a. Rename the image files to replace their filenames with the creation or modification dates of the images so that the earliest image has the first filename (as sorted by `ls` command), the second earliest image has the second filename, etc. What command did you use?

3b. Create a GIF, APNG, or video with ImageMagick and/or another tool that shows the scallions/onions growing. What command did you use? Please to share a link to the video.

3c. Do the renamed image files have the same MD5 checksums, creation dates, and modification dates as the original image files? Why or why not?

3d. Do the creation and modification dates affect the MD5 checksums of the image files? Why or why not?

3e. Does the `tar.gz` file of the renamed image files have the same MD5 checksum as the `tar.gz` file of the original image  files? Why or why not?

3f. Any other comments or observations?

---
4. **Time-series analysis**

4a. We are given a data file containing ECG or EEG time-series; but the sampling frequency of the data $f_s$ is not provided (or we would like to confirm it). Can we find practically find $f_s$ by analyzing the data? Write a code to test your idea on any of the `A00` dataset records.

4b. In an ECG application, we are given more than 1 million *raw samples* (before any preprocessing) recorded from an analog-to-digital (ADC) converter. Assuming that the ECG has used the full dynamic range of the ADC (i.e., the ECG was not too small in amplitude and it used all the ADC bits), how can we find the number of bits of the ADC and its quantization level size by analyzing the samples? Write a function to test your idea on any of the `A00` dataset records. 
*Hint: If your function is more than 5-15 lines of code in MATLAB/Python, you're probably doing it in an inefficient way!*

4c. Design and implement a notch filter to reject the powerline noise from a given signal recorded. The signal may be recorded in any country.

---
5. **Electrocardiogram R-peak detection**

5a. Write a MATLAB or Python code to extract the ECG R-peaks of the `A00` *training* dataset from the [PhysioNet/Computing in Cardiology Challenge 2017](https://physionet.org/content/challenge-2017/1.0.0/). For all records, the first channel available in each record can be used for R-peak detection. You may develop your own R-peak detector, or use any of the R-peak detectors available in the [Open-Source Electrophysiological Toolbox](https://github.com/alphanumericslab/OSET), or [Clifford's Lab Cardiovascular Signal Toolbox](https://github.com/cliffordlab/PhysioNet-Cardiovascular-Signal-Toolbox.git). The R-peak indexes should be stored as `CSV` files with the base file name as the corresponding `.mat` files.

5b. Write a function to calculate the instantaneous heart-rate time series $hr_n$ and the smoothed heart-rate time-series $HR_n$ in beats per minute (bpm), where $n$ is the beat index. The smoothing algorithm is as follows: calculate the running median of the RR intervals $M_n = \text{MEDIAN}(hr_{n-w+1}, \ldots, hr_n)$, where $w$ is the sliding window length (input of the function). Next, calculate $$HR_n=\left\\{\eqalign{hr_n&\text{ if } |hr_n-M_n|\leq\delta\\\M_n&\text{ otherwise }}\right.$$ where $\delta$ is the smooting threshold (input of the function). Write a script to test the function with parameters $w=$ 5 beats and $\delta=$ 15 bpm, on an arbitrary record from the `A00` dataset.

5c. Write a script to: i) plot the heart rate time series in bpm vs time in seconds; ii) plot the histogram of the RR-intervals in seconds; iii) plot the histogram of the beat-wise heart rates in bpm. The script should take the per-subject `CSV` files from 5a as input.

---
6. **Baseline wander removal**

A very effective filter for removing the baseline wander noise from biomedical signals (especially the ECG) is a running median filter followed by a moving average filter. given a discrete time-series $x_n$, the first stage of the filter calculates $M_n=\text{MEDIAN}(x_{n-w_1+1},\ldots,x_n)$ and the second stage calculates the baseline estimate $b_n = \text{MEAN}(M_{n-w_2+1}, \ldots, M_n)$, where $w_1$ and $w_2$ are the median filter and the moving average window lengths, respectively.

6a. Is this filter causal?

6b. Is the filter time-invarient?

6c. Is the filter linear?

6d. Implement the filter as a function in MATLAB/Python and test it on a sample ECG record of the `A00` dataset. Choose $w_1$ and $w_2$ to best remove the baseline and plot the raw ECG and the baseline estimate to demonstrate the performance. 


