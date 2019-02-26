import pikepdf
import pdfx
import re
import os

pdf = pikepdf.open('atul.pdf')
pdf.save('output.pdf')

pdf2 = pdfx.PDFx('output.pdf')
text = pdf2.get_text()

m3 = re.findall('(?<=Course)([\S\s]*?)(?=Description|Term GPA)', text)

for i in range(len(m3)):
    print('******* TERM:')
    data = m3[i].split()
    course_names = data[:len(data)//2]
    course_codes = data[len(data)//2:]
    courses = []
    for j in range(len(data)//2):
        courses.append('{}{}'.format(course_names[j], course_codes[j]))
    print(courses)

os.remove('output.pdf')