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
The main dependencies needed for this code are included in the `requirements.txt`.
However, here are the steps to install the dependencies not included in Anaconda.
</br>
</br>
I will show all steps on any OS
</br>
The first thing you will need is `pip` as `conda-forge` does not have all of the libraries that I have used.
</br>
On Mac:
```
sudo easy_install pip
# Or if using homebrew
brew install python 
^ this will install python3.x as well as the pip installer
```
On Windows:
* Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) to a folder on your computer. Open a command prompt window and navigate to the folder containing get-pip.py. Then run `python get-pip.py`. This will install `pip`.
* Verify a successful installation by opening a command prompt window and navigating to your Python installation's script directory (default is `C:\Python27\Scripts`). Type `pip freeze` from this location to launch the Python interpreter.
* `pip freeze` displays the version number of all modules installed in your Python non-standard library; On a fresh install, pip freeze probably won't have much info to show but we're more interested in any errors that might pop up here than the actual content. However, if you have Anaconda it will include all Anaconda packages.

On Linux:
Debian/Ubuntu:
```
sudo apt-get install python3-pip
```
Arch:
```
sudo pacman -S python-pip
```
CentOS:
```
sudo yum install python3 python3-wheel
```
Fedora:
```
sudo dnf install python3 python3-wheel
```
OpenSUSE:
```
sudo zypper install python3-pip python3-setuptools python3-wheel
```
</br>
Once you have pip installed you will be able to install PyPDF2, textract. 
</br>
All CLI will use the same commands with `pip installer`
```
pip install pypdf2 textract
```
</br>
The last thing is installing Tesseract OCR from Google which on some OS you cannot do from terminal/cmd prompt/powershell.
</br>
For Windows go [here](https://github.com/tesseract-ocr/tesseract/wiki#windows) for install instructions
Ubuntu/Debian:
```
sudo apt-get install tesseract-ocr
sudo apt install libtesseract-dev
```
Homebrew:
```
brew install tesseract
```
MacOS:
```
sudo port install tesseract
```
Fedora:
```
sudo dnf config-manager --add-repo https://download.opensuse.org/repositories/home:Alexander_Pozdnyakov/Fedora_26/home:Alexander_Pozdnyakov.repo
sudo dnf install tesseract
sudo dnf install tesseract-langpack-deu
```
OpenSUSE Tumbleweed:
```
sudo zypper addrepo https://download.opensuse.org/repositories/home:Alexander_Pozdnyakov/openSUSE_Tumbleweed/home:Alexander_Pozdnyakov.repo
sudo zypper refresh
sudo zypper install tesseract-ocr
sudo zypper install tesseract-ocr-traineddata-german
```
OpenSUSE 15.0:
```
sudo zypper addrepo https://download.opensuse.org/repositories/home:Alexander_Pozdnyakov/openSUSE_Leap_15.0/home:Alexander_Pozdnyakov.repo
sudo zypper refresh
sudo zypper install tesseract-ocr
sudo zypper install tesseract-ocr-traineddata-german
```
CentOS:
```
sudo
yum-config-manager --add-repo https://download.opensuse.org/repositories/home:/Alexander_Pozdnyakov/CentOS_7/
sudo rpm --import https://build.opensuse.org/projects/home:Alexander_Pozdnyakov/public_key
yum update
yum install tesseract 
yum install tesseract-langpack-deu
```
If you are using Snap Package manager:
```
sudo snap install --channel=edge tesseract
```
Depending on packages you may or may not have installed you may be missing some dependencies, the most common are `sphinx` you can check [here](https://github.com/tesseract-ocr/tesseract/wiki#windows) for help with any issues.
</br>
With that you should be all set up to run this script.
</br>
How do I run this script?
As long as you have followed the above steps you can simply open terminal/cmd prompt/powershell and run:
```
git clone https://github.com/KaynRyu/semesterProject/
cd ./semesterProject/
python IDTtoJSON.py
```

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
