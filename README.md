# Statementt-data-parsing

There is so much data into the `pdfs` that we store but for other purposes like training the machine learning model we can not use that data directly from `pdfs`. This is really one of the issue when we have to work with financial data as most of the companies works with `pdfs` to store their P&L, tax returns, general meeting notes and much more. Even the broachers of the companies are into `pdfs`. In order to study more about the companies we need some way to extract this data efficiently and precisely. Here we would like to show our research and work around how to get the data from `pdfs`. 

There are some libraries already created, open sourced for doing such extractions. Let's see in depth some of them. 

### 1. PDFToText: 

If the pdf is not made out of images this library is one of the best to use. It is really easy to use and can convert the pdf data into simple raw text very precisely. Let's see some samples of this.
![samples_pdf](images/sample_pdf.PNG)
    
![sample_csv](images/sample_csv.PNG)


In the above two pictures, the first one is the image of the pdf file and the second one is of the `csv` file that is generated from by the `pdftotext` library. The example taken is to show the capability of the library to extract the tables and data at the same time in meaningful way. After that anyone can apply regular extractions to get the most out of the data from the csv file. We have added some files in `data` folder as examples. 

You can use the sample code that we have used from `code` folder. Do following to use that

1. Change the name of the `pdf` file path at the line 5 from `./data/sample_file.pdf` to your desired file path.
2. Change the name of the output file at the line line 16 from `./data/sample_csv.csv` to your desired file path. 
3. Run file `pdftotext_sample.py` from the terminal using `python pdftotext_sample.py` command.
    
    Requirements to use `pdftotext` are:
     1. OS - Linux
     2. Python >= 3.0
    Here is the package link on pypi https://pypi.org/project/pdftotext/.

### Tesseract

PDF2Text can extract data from `text PDF`, where as it will fail for extracting data from `image PDF`. In real world scenario one can get any kind of PDFs, so one needs to use `Optical character recognition` (OCR) libraries which are meant for this. Tesseract is one of the best example of it. Let us understand it with these samples:

![tesseract Example](images/tesseract_sample_result.PNG)

In the above picture we can see how information is extracted. The lest most is the a receipt and the left most is the output which one gets after applying tesseract onto it.

    Requirements to use `tesseract` are:
     1.  1. OS - Linux, Mac OSX and Windows
     2. Python 2.7 or 3.5+
    Here is the package link on pypi https://pypi.org/project/pytesseract/

### Invoice2Data

Invoice2Data library can used not just only to extract data from PDF but also get information from that extracted data. Both the above libraries can be used for their specific usage, where as `Invoice2Data` provides ability to extract data with any of the above mentioned (and also more) libraries. It extracts the data from the PDF and then using the templates one can get the desired information out of it. Below is shown a sample of how it works:

![AWS PDF](images/AmazonWebService_PDF_Image.jpg)

![Invoice2Data CSV](images/invoice2data_csv_result.PNG)


The first image is the PDF of AWS receipt, and the second is the extracted information in form of CSV data. For more information on how to use Invoice2Data and how templates work, review it's [GitHub repository](https://github.com/invoice-x/invoice2data)

    
    Requirements to use `invoice2data` are:
     1. OS - Linux
     2. Python >= 3.0
    Here is the package link on pypi https://pypi.org/project/invoice2data/0.0.1/

### Pdfminer.six

Pdfminer.six is a community maintained fork of the original PDFMiner. It is a tool for extracting information from PDF documents. It focuses on getting and analyzing text data. Pdfminer.six extracts the text from a page directly from the sourcecode of the PDF. It can also be used to get the exact location, font or color of the text.

It is build in a modular way such that each component of pdfminer.six can be replaced easily. You can implement your own interpreter or rendering device to use the power of pdfminer.six for other purposes that text analysis.

![SAMPLE PDF](images/pdf-sample-page-001.jpg)

Result:

Adobe Acrobat PDF Files <br />
Adobe® Portable Document Format (PDF) is a universal file format that preserves all <br />
of the fonts, formatting, colours and graphics  of any  source document,  regardless of <br />
the application and platform used to create it. <br />
Adobe PDF is an ideal format for electronic document distribution as it overcomes the <br />
problems commonly encountered with electronic file sharing. <br />
•  Anyone, anywhere can open a PDF file. All you need is the free Adobe Acrobat <br />
Reader.  Recipients  of  other  file  formats  sometimes  can't  open  files  because  they <br />
don't have the applications used to create the documents. <br />
•  PDF files always print correctly on any printing device. <br />
•  PDF  files  always  display  exactly  as  created,  regardless  of  fonts,  software,  and <br />
operating systems. Fonts, and graphics are not lost due to platform, software, and <br />
version incompatibilities. <br />
•  The  free  Acrobat  Reader  is  easy  to  download  and  can  be  freely  distributed  by <br />
anyone. <br />
•  Compact  PDF  files  are  smaller  than  their  source  files  and  download  a <br />
page at a time for fast display on the Web. <br />


    Requirements to use `pdfminer.six` are:
     1. Python >= 3.4
    
    Insall:
     1. pip install pdfminer.six
 
 ### Fetching information from KYC document using pytessereact:
 
 Pytessereact is trained on different languages.If the document has different languages then we need to train the pytessereact and if image is not clear or visible then we need to use some image processing techniques like thresholding,opening,border detection.
 
 Here we have fetched data from UK sample licence using this library.
 
 ![LICENCE IMAGE](images/Uk_licence.jpg)
         
Result:

DRIVING LICENCE <br />
1, MORGAN <br/>
2, SARAH <br/>
MEREDYTH <br/>
3. 11.03.1976 UNITED KINGDOM <br/>
4a. 19.01.2013 4c. DVLA <br/>
4b. 18.01.2023 <br/>
5. MORGA753116SM9lJ 35 <br/>
8. 122 BURNS CRESCENT <br/>
EDINBURGH <br/>
EH1 9GP. <br/>
9. AM/A/B1/B/f/kK/I/n/p/q <br/>
DVLA INTERNAL USE <br/>

