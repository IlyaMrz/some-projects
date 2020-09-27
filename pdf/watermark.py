# combines pdfs, and stamps watermark of first pdf

import PyPDF2
from sys import argv

watermarkpdf = argv[1]
pdfs = argv[2:]

output = PyPDF2.PdfFileWriter()

# pdf wich contains watermark
wmark = PyPDF2.PdfFileReader(open(watermarkpdf, 'rb'))


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('new.pdf')


pdf_combiner(pdfs)

twmrk = PyPDF2.PdfFileReader(open('new.pdf', 'rb'))  # to watermark pdf
watermarkPage = twmrk.getPage(0)


def watermarker(pdfmark, pdf):
    for i in range(pdf.getNumPages()):
        page = pdf.getPage(i)
        page.mergePage(watermarkPage)
        output.addPage(page)
    with open('newpdf.pdf', 'wb') as f:
        output.write(f)


watermarker(watermarkpdf, twmrk)
