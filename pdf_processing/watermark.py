import PyPDF2


def embed_watermark(file, watermark):
    reader = PyPDF2.PdfFileReader(open(file, 'rb'))
    watermark_reader = PyPDF2.PdfFileReader(open(watermark, 'rb'))
    writer = PyPDF2.PdfFileWriter()

    for num in range(reader.getNumPages()):
        page = reader.getPage(num)
        page.mergePage(watermark_reader.getPage(0))
        writer.addPage(page)
    writer.write(open('watermarked.pdf', 'wb'))



embed_watermark('dummy.pdf', 'wtr.pdf')
