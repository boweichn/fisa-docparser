import os
import pdfrw
from read_db import retrive_dict
from pprint import pprint

my_file = './PDFs/test_me.pdf'
output_file = './PDFs/tested_me.pdf'

ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'

field_name_index = {
    'NAME OF SCHOOL': 'SCHOOL',
    'YEAR FOUNDED': 'FOUNDED',
    'NAME OF AUTHORITY': 'AUTHORITY',
    'SCHOOL PHONE': 'PHONE',
    'MAILING ADDRESS': 'ADDRESS',
    'SCHOOL FAX': 'FAX',
    'WEBSITE': 'Website',
    'CITY  POSTAL CODE': 'CITY',
    'PRINCIPAL  DEGREE': 'DEGREE',
    'EMAIL': 'Email',
    'a GRADES OFFERED': 'GRADES',
    'Grade 8': '8',
    'Grade 9': '9',
    'Halfday K': 'Halfday_k',
    'Grade 10': '10',
    'Fullday K': 'Fullday_k',
    'Grade 11': '11',
    'Grade 17': '1_7',
    'Grade 12': '12',
    'Ungraded Elem': 'UNE',
    'Ungraded Sec': 'UNS',
    'a SCHOOL CLASSIFICATION GIVEN BY INDEPENDENT SCHOOLS OFFICE': 'FUNDING',
    'd SCHOOL SPECIALTY IF ANY': 'SPECIALTY',
    'a SCHOOL IS MEMBER OF FISA BC': 'FISA',
    'b SCHOOL IS MEMBER OF PROVINCIAL ASSOCIATION': 'ASSOC',
    'c SCHOOL IS MEMBER OF NATIONALINTERNATIONAL ASSOCIATIONS': 'ASSOC2',
    'i PUBLIC SCHOOL DISTRICT': 'SDNUM',
    'NAME': 'SD',
    'ii PROVINCIAL ELECTORAL DISTRICT': 'ELECTORAL',
    'if different from above': 'SADDRESS'
}

def write_fillable_pdf(input_path, output_path, data_dict):
    whole_db = data_dict

    template_pdf = pdfrw.PdfReader(input_path)
    annotations = template_pdf.pages[0][ANNOT_KEY]
    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                if key in field_name_index.keys():
                    if field_name_index[key] in data_dict[0].keys():
                        annotation.update(
                            pdfrw.PdfDict(V='{}'.format(data_dict[0][field_name_index[key]]))
                        )
    pdfrw.PdfWriter().write(output_file, template_pdf)

if __name__ == "__main__":
    write_fillable_pdf(my_file, output_file, retrive_dict())