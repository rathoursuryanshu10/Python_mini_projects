from pdf2docx import Converter 
pdf_input='demo.pdf'
docx_output='output.docx'
cv=Converter(pdf_input)
cv.convert(docx_output)
cv.close()
