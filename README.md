# Parallel Programming with Google Maps Services

* [Introduction](#Introduction)
* [Running](#Running)

## Introduction
Being an undergraduate researcher (UNO '19), this is how I started on experimenting on using processes, threads and a combinaton of both to get google map directions with Python clients. Due to issues with npm, only the sequential approach was possible with javascript as documented in folder 'npmMaps'

## Running
The programs in folders hybrid, threads and processes have the respective python files that mimic corresponding parallel behaviour. The command line would like you to use  
  
`python <program_name.py> <no. of processe/threads>`  
   
And, do not forget to put your Google API Key in there!

## Miscellaneous goal
These programs were also used to get the distances and durations between stops for public transit for systems MTA (NY), TheBus (Honolulu) & RTA (New Orleans), and compare their performances among them. Thata data is on the the '.txt' files in terms of miles and minutes.