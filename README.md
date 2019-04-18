# Using Python to take information from .pdf and .txt and input into a database/ create .json
**Name:** Brett Plemons 
<br/>
**Semester:** Spring 2019
<br/>
**Project Area:** Data Mining

## Objective
To simplify the task of data entry, and increase lab organiziation by reducing the amount of spec sheets stored.

## Outcomes
Collect a user input on first use, or when called again, to select a directory or use a default (user/name/downloads/ or /home/name/Downloads). Then collect all IDT .pdfs from that directory and convert the useful information into usable .json files.

## Rationale
A large issue in a lot of labs is clutter, and finding data when you need it. Another issue for a lot of people, myself in cluded, is data entry. It is tedious, mundane, and just boring. So, I wanted to develop an app that would be able to be implemented into any lab, big or small, and be able to take .pdf files for Primer Spec sheets from IDT and create .json files that can be used as is, or can be implemented into a new or existing database.

## Diagram
<img src="https://github.com/KaynRyu/semesterProject/blob/master/semesterprojectdiagram.JPG"/>

This provides a simplified systematic process of taking data from input and illustrate the process of how the app will organize data.

## Setup
To get started with this program find the [Getting Started](https://github.com/KaynRyu/semesterProject/wiki/Getting-Started) or in the Wiki.
</br>
If you would like to follow a step-by-step walkthrough of this project you can find that [here](https://github.com/KaynRyu/semesterProject/blob/master/WalkthroughIDTtoJSON.ipynb)

## References
For this project I have already used a lot of resources, and these are the ones that ultimately I used in the creation of my script.

[Python 3.7 Documentation](https://www.programiz.com/python-programming/methods/string/index). It is not the official [Python.org](python.org) but it is a bit easier to navigate.
<br>
[PyPi: PyPDF2 Documentation](https://pypi.org/project/PyPDF2/)
<br>
[Regular Expression Module](https://docs.python.org/3/library/re.html)
<br>
Regular expressions was probably the most used, and most helpful module I used in this project. It may even be my absolute favorite module in python right now for anything dealing with text as it is so versatile. I would suggest learning it for any project like at [Regex101](https://regex101.com/r/mH2mnK/2)
<br>
For scanned PDFs I had to use Google's OCR in a Python Wrapper IO called [Textract](https://textract.readthedocs.io/en/stable/)
<br>
[Copter Labs: What is JSON](https://www.copterlabs.com/json-what-it-is-how-it-works-how-to-use-it/)
<br>
For converting the collected data into .JSON files as arrays for database implementation I obviously used the [JSON Module](https://docs.python.org/3/library/json.html)
<br>
The [Stackoverflow](www.stackoverflow.com) and [AskUbuntu](www.askubuntu.com) communities were life savers with debugging, package implementation, and install issues.
</br>
This program requires Tesseract OCR which you can download from [Google](https://github.com/tesseract-ocr/tesseract)
