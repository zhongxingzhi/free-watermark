from pyPdf import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
input1 = PdfFileReader(file("doc/document.pdf", "rb"))

# print the title of document1.pdf
print "title = %s" % (input1.getDocumentInfo().title)

for i in range(0, input1.getNumPages()):
    page = input1.getPage(i)
    watermark = PdfFileReader(file("doc/watermark.pdf", "rb"))
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

# print how many pages input1 has:
print "document.pdf has %s pages." % input1.getNumPages()

# finally, write "output" to document-output.pdf
outputStream = file("document-output.pdf", "wb")
output.write(outputStream)
outputStream.close()
