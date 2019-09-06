# pdf-image-data-parsing

There is so much data into the `pdfs` that we store but for other purposes like training the machine learning model we can not use that data directly from `pdfs`. This is relly one of the issue when we have to work with financial data as most of the companies works with `pdfs` to store their P&L, tax returns, general meeting notes and much more. Even the brouchers of the companies are into `pdfs`. In order to study more about the companies we need some way to extract this data efficiently and precisely. Here we would like to show our research and work around how to get the data from `pdfs`. 

There are some libraries already created open sourced for doing such extractions. Let's see in depth some of them. 

### 1. PDFToText: 

If the pdf is not made out of images this library is one of the best to use. It is really easy to use and can cnvert the pdf data into simple raw text very precisely. Let's see some samples of this.
![samples_pdf](images/sample_pdf.PNG)
    
![sample_csv](images/sample_csv.PNG)


In the above two pictures, the first one is the image of the pdf file and the second one is of the `csv` file that is generated from by the `pdftotext` library. The example taken is to show the capability of the library to extract the tables and data at the same time in meaningful day. 
    
    Requirments to use `pdftotext` are:
     1. OS - Linux
     2. Python >= 3.0
    Here is the package link on pypi https://pypi.org/project/pdftotext/. 
