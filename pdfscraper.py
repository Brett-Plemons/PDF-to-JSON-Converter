# for PDF reading
import PyPDF2 as pdf2
import textract
# for data preprocessing
import re
from dateutil.parser import parse
# For generating the JSON file array
import json
# This finds and opens the pdf file, reads the data, and extracts the data.
filename = "TestSpec.pdf"
pdfFileObj = open(filename, 'rb')
pdfReader = pdf2.PdfFileReader(pdfFileObj)
text = ""
pageObj = pdfReader.getPage(0)
text += pageObj.extractText()

# checks if extracted data is in string form or picture, if picture textract reads data.
# it then closes the pdf file
if text != "":
    text = text
else:
    text = textract.process(filename, method="tesseract", language="eng")
pdfFileObj.close()

# Converts text to string from byte data for preprocessing
stringedText = str(text)
# Removed escaped lines and replaced them with actual new lines.
formattedText = stringedText.replace('\\n', '\n').lower()
# Slices the long string into a workable piece (only contains useful data)
slice1 = formattedText[(formattedText.index("sheet") + 10): (formattedText.index("secondary") - 2)]
clean = re.sub('\n', " ", slice1)
clean2 = re.sub(' +', ' ', clean)
print(clean2)

# Creating the PrimerData dictionary
with open("PrimerData.json",'w') as file:
    primerDataSlice = clean[clean.index("molecular"):]
    primerData = re.split(":", primerDataSlice)
    print(primerData)
    primerKeys = primerData[0::2]
    primerValues = primerData[1::2]
    primerDict = {"Primer Data": dict(zip(primerKeys,primerValues))}
    # Generatring the JSON array "Primer Data"
    primerJSON = json.dumps(primerDict, ensure_ascii=False)
    file.write(primerJSON)

# Grabbing the date (this has just the date, so json will have to add date.)
date = re.findall('(\d{2}[\/\- ](\d{2}|january|jan|february|feb|march|mar|april|apr|may|may|june|jun|july|jul|august|aug|september|sep|october|oct|november|nov|december|dec)[\/\- ]\d{2,4})', clean2)
