# Semester Project Update #2

## Goal and Rationale
The Rationale of this project is to simplify and automate the mundane task of data entry. Using Python I am
designing a script that will take .pdf files (because of the roadblocks I've had, tabular and scanned), and
convert them into well organized .json files. These files can then be implemented into a pre-existing or newly
created database, such as MongoDB or PostGreSQL, with ease. This will allow this data to be easily retrieved,
checked and make inventory of product in a lab a cinch. 

## Basic Illustration of how the this works:

<img src = "https://github.com/KaynRyu/semesterProject/blob/master/semesterprojectdiagram.JPG"/>

## Current roadblocks and progress
There seem to be more roadblocks than there is progress at this point. **However**, progress is being made.
The biggest roadblock was when I found out that most of the .pdf's that we recieve in our lab are just scanned
images converted into a .pdf. This means there is no tabular data that I can simply extract from the metadata.
Instead, I have decided to use Google's OCR (Optical Character Recognition) Tesseract to check the image for recognizable words, this requires
a conversion back to a .jpg so that most of pythons wrappers for Tesseract can read the image. This will extract
a string of data in a list, which can then be split by the spaces and the JSON dictionary can be created.
