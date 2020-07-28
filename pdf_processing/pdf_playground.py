import PyPDF2

with open('11.3 dummy.pdf.pdf','rb') as dummy:
    reader = PyPDF2.PdfFileReader(dummy)
    page = reader.getPage(0)
    rotated_page = page.rotateClockwise(90)
    with open('rotated_dummy.pdf' ,'wb') as rotated:
        writer = PyPDF2.PdfFileWriter()
        writer.addPage(rotated_page)
        writer.write(rotated)
