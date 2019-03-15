# Using Python to take information from .pdf and .txt and input into a database/ create .json
**Name:** Brett Plemons 
<br/>
**Semester:** Spring 2019
<br/>
**Project Area:** Molecular Biology

## Objective
To write a python script that extract data from .pdf and .txt from IDT oligo spec sheets and organize it into a easy to read, and access format.

## Outcomes
This script should create a hassle-less way to extract data and create easy to use formats such as .json, and update SQL data bases.

## Rationale
The most tedious part of upkeeping a database and inventory is data input. Whether that be a collection of .json files or a structured database like those maintained with SQL. Python, however, can be used as a tool to reduce the tedium of data entry by automating this process.

My lab, like many other labs, is constantly receiving new primers specific to each project, as well as sequence data, and other chemicals for molecular experiments. My goal is to provide a hassle-less method of taking data sent to our lab by IDT, Sigma, GeneWiz, and created by our labmates and inputting it into a SQL Database.

This will also give my lab the ability to inventory, and check inventory for products, as well as check primers for projects to avoid replicates.

One of my major goals is to design a progrma that can help to bridge the gap in smaller labs to those of larger labs. So, whether you are using an established SQL database or want to step ahead and convert to JSON. 

## Diagram
<img src="https://github.com/KaynRyu/semesterProject/blob/master/semesterprojectdiagram.JPG"/>

This provides a simplified systematic process of taking data from input and illustrate the process of how the script will organize data.

## References
For this project I have already used a lot of resources, and expect to need to use many more.

[Copter Labs: What is JSON](https://www.copterlabs.com/json-what-it-is-how-it-works-how-to-use-it/)
<br>
Extraction Method 1:
<br>
[Using Python to extract data from PDF](https://www.zevross.com/blog/2014/04/09/extracting-tabular-data-from-a-pdf-an-example-using-python-and-regular-expressions/)
<br>
[Pypi: PDFMiner Documentation](https://pypi.org/project/pdfminer.six/)
<br>
Extraction Method 2:
<br>
[Extracting data from PDFs using Python](https://qxf2.com/blog/extracting-data-from-pdfs-python/)
<br>
[PyPi: PyPDF2 Documentation](https://pypi.org/project/PyPDF2/)
