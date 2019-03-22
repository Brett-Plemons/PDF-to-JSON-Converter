import PyPDF2 as pdf2
import textract

with "TestSpec.pdf" as filename:
    pdfFileObj = open(filename, 'rb')
    pdfReader = pdf2.pdfFileReader(pdfFileObj)
    num_pages = pdfReader.numpages
    count = 0
    text = ""

    while count < num_pages:
        pageObj = pdfReader.getPage(0)
        count += 1
        text += pageObj.extractText()

    if text != "":
        text = text
    else:
        text = textract.process(filename, method="tesseract", language="eng")

def cleanText(x):
    '''
    This function takes the byte data extracted from scanned PDFs, and cleans it of all
    unnessary data.
    Requires re
    Author: Brett Plemons
    Date of writing: 20-Mar-19
    '''
    stringedText = str(x)
    cleanText = stringedText.replace('\n','')
    splitText = re.split(r'\W+', cleanText)
    caseingText = [word.lower() for word in splitText]
    cleanOne = [word for word in caseingText if word != 'n']
    dexStop = cleanOne.index("od260")
    dexStart = cleanOne.index("sheet")
    clean = cleanOne[dexStart + 1:dexStop]
    return clean

cleanText = cleanText(text)
