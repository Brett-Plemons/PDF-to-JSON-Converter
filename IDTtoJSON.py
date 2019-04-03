# for PDF reading
import PyPDF2 as pdf2
import textract
# for data preprocessing
import re
from dateutil.parser import parse
import math
from Bio.SeqUtils import molecular_weight as mw
from Bio.SeqUtils import MeltingTemp as mt
from Bio.Alphabet import generic_dna
from Bio.Seq import Seq
from datetime import date
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
formattedText = stringedText.replace('\\n', '\n')
# Slices the long string into a workable piece (only contains useful data)
slice1 = formattedText[(formattedText.index("SHEET") + 10): (formattedText.index("Secondary") - 2)]
clean = re.sub('\n', " ", slice1)
clean2 = re.sub(' +', ' ', clean)

# Collect the sequence name
name = clean2[clean2.index("Sequence") + 11: clean2.index("Sequence") + 19]
# Collecting Shipment info
ordered = input("Who placed this order? ")
received = input("Who is receiving this order? ")
dateOrder = re.findall(
    r'(\d{2}[\/\- ](\d{2}|January|Jan|February|Feb|March|Mar|April|Apr|May|May|June|Jun|July|Jul|August|Aug|September|Sep|October|Oct|November|Nov|December|Dec)[\/\- ]\d{2,4})',
    clean2)
dateReceived = date.today()
refNo = clean2[clean2.index("ref.No. ")+8: clean2.index("ref.No.")+17]
orderNo = clean2[clean2.index("Order No.")+ 10: clean2.index("Order No.") + 18]
# Finding and grabbing the sequence data. Storing it and then finding the
# GC content and melting temp or TM
bases = int(clean2[clean2.index("bases") - 3:clean2.index("bases") - 1])
seqList = [line for line in clean2 if re.match(r'^[AGCT]+$', line)]
sequence = "".join(i for i in seqList[:bases])


def gcContent(sequence):
    count = 0
    for i in sequence:
        if i == 'G' or i == 'C':
            count += 1
        else:
            count = count
    return round((count / bases) * 100, 1)


gc = gcContent(sequence)
tm = mt.Tm_GC(sequence, Na=50)
moleWeight = round(mw(Seq(sequence, generic_dna)), 2)
dilWeight = float(clean2[clean2.index("ug/OD260:") +
                         10: clean2.index("ug/OD260:") + 14])
dilution = dilWeight * 10
primerDict = {"Primer Data":{
                           "Sequence": sequence,
                           "Bases": bases,
                           "TM (50mM NaCl)": tm,
                           "% GC content": gc,
                           "Molecular weight": moleWeight,
                           "ug/0D260": dilWeight,
                           "Dilution volume (uL)": dilution
               },
               "Shipment Info": {
                           "Ref. No.": refNo,
                           "Order No.": orderNo,
                           "Ordered by": ordered,
                           "Date of Order": dateOrder,
                           "Received By": received,
                           "Date Received": str(dateReceived.strftime("%d-%b-%Y"))
               }}
# Generatring the JSON array "Primer Data"
with open("".join(name) + ".json", 'w') as file:
    primerJSON = json.dumps(primerDict, ensure_ascii=False)
    file.write(primerJSON)
