# Importing all the required libraries

from invoice2data import extract_data
from invoice2data.extract.loader import read_templates
from invoice2data.input import pdftotext
import pandas as pd

# Importing custom template
templates = read_templates('./template/')

#print(templates)

# Extract data from PDF
result = extract_data('./data/pnlsheet.pdf', templates = templates, input_module = pdftotext)

# Store the extracted data to a Data-frame
df = pd.DataFrame(data = result)

# Export Data-frame to a csv file
df.to_csv('./data/invoice2data_simple.csv')


''' 
You can use any desired library to extract data from pdftotext, pdftotext, pdfminer, tesseract. It is optional
and by default pdftotext will be used if not specified.

The custom template named temp.yml is placed in the templates. You can remove the templates parameter in
extract_data(). Default templates will be used

'''