from pikepdf import Pdf
import pdfx
import re
import os

def extract_courses_from_transcript(userId, pdf_file):
    file_name = '{}.pdf'.format(userId)

    pdf_file.save(file_name)

    pdf = Pdf.open(file_name)
    pdf.save(file_name)

    pdf2 = pdfx.PDFx(file_name)
    text = pdf2.get_text()

    course_matches = re.findall('(?<=Course)([\S\s]*?)(?=Description|Term GPA)', text)

    all_courses = []

    for i in range(len(course_matches)):
        data = course_matches[i].split()
        course_names = data[:len(data)//2]
        course_codes = data[len(data)//2:]
        courses = []
        for j in range(len(data)//2):
            courses.append('{}{}'.format(course_names[j], course_codes[j]))
        all_courses.extend(courses)
    
    os.remove(file_name)

    return all_courses
