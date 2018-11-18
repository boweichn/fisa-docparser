import os
from read_db import retrive_dict
from pprint import pprint
from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject
import re


my_file = './PDFs/blank_PDFs/test_me.pdf'
my_file2 = './PDFs/blank_PDFs/School19-Fact Sheet 2001-02.pdf'
output_file = './PDFs/prepared_fact_sheets/tested_me.pdf'

my_dir = './PDFs/blank_PDFs'

def prep_input(input_dir):
    my_pdf_list = []
    
    for filename in os.listdir(input_dir):
        my_pdf_list.append(filename)
    return my_pdf_list

def field_names_dict(field_names):
    field_name_index = {}

    for keys in field_names.keys():
        if 'NAME OF SCHOOL' in keys: field_name_index[keys]='SCHOOL'
        if 'YEAR FOUNDED' in keys: field_name_index[keys]='FOUNDED'
        if 'NAME OF AUTHORITY' in keys: field_name_index[keys]='AUTHORITY'
        if 'SCHOOL PHONE' in keys: field_name_index[keys]='PHONE'  
        if 'MAILING ADDRESS' in keys: field_name_index[keys]='ADDRESS'  
        if 'SCHOOL FAX' in keys: field_name_index[keys]='FAX'  
        if 'WEBSITE' in keys: field_name_index[keys]='Website'  
        if 'CITY  POSTAL CODE' in keys: field_name_index[keys]='CITY'  
        if 'PRINCIPAL  DEGREE' in keys: field_name_index[keys]='DEGREE'  
        if 'EMAIL' in keys: field_name_index[keys]='Email'  
        if 'a GRADES OFFERED' in keys: field_name_index[keys]='GRADES'  
        if 'Grade 8' in keys: field_name_index[keys]='8'  
        if 'Grade 9' in keys: field_name_index[keys]='9'  
        if 'Grade 10' in keys: field_name_index[keys]='10'  
        if 'Grade 11' in keys: field_name_index[keys]='11'  
        if 'Grade 12' in keys: field_name_index[keys]='12'  
        if 'Grade 17' in keys: field_name_index[keys]='1_7'  
        if 'Halfday K' in keys: field_name_index[keys]='Halfday_k' 
        if 'Fullday K' in keys: field_name_index[keys]='Fullday_k' 
        if 'Ungraded Elem' in keys: field_name_index[keys]='UNE'  
        if 'Ungraded Sec' in keys: field_name_index[keys]='UNS'  
        if 'a SCHOOL CLASSIFICATION GIVEN BY INDEPENDENT SCHOOLS OFFICE' in keys: field_name_index[keys]='FUNDING'  
        if 'd SCHOOL SPECIALTY IF ANY' in keys: field_name_index[keys]='SPECIALTY'  
        if 'a SCHOOL IS MEMBER OF FISA BC' in keys: field_name_index[keys]='FISA'  
        if 'b SCHOOL IS MEMBER OF PROVINCIAL ASSOCIATION' in keys: field_name_index[keys]='ASSOC'  
        if 'c SCHOOL IS MEMBER OF NATIONALINTERNATIONAL ASSOCIATIONS' in keys: field_name_index[keys]='ASSOC2'  
        if 'i PUBLIC SCHOOL DISTRICT' in keys: field_name_index[keys]='SDNUM'  
        if ('NAME_' in keys or keys == 'NAME'): field_name_index[keys]='SD'  
        if 'ii PROVINCIAL ELECTORAL DISTRICT' in keys: field_name_index[keys]='ELECTORAL'  
        if 'if different from above' in keys: field_name_index[keys]='SADDRESS'  
    return field_name_index

def school_num_finder(input_file):
    pdfFileObj = open(input_file, 'rb') 
    pdfReader = PdfFileReader(pdfFileObj)
    
    # creating a page object 
    pageObj = pdfReader.getPage(0) 
    my_file, retrive_dict()
    # extracting text from page 
    my_page_object = pageObj.extractText()
    school_num = my_page_object.split('\n')[-2]

    # closing the pdf file object 
    pdfFileObj.close() 
    return school_num

def set_need_appearances_writer(writer):
    try:
        catalog = writer._root_object
        # get the AcroForm tree and add "/NeedAppearances attribute
        if "/AcroForm" not in catalog:
            writer._root_object.update({
                NameObject("/AcroForm"): IndirectObject(len(writer._objects), 0, writer)})

        need_appearances = NameObject("/NeedAppearances")
        writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)
        return writer

    except Exception as e:
        print('set_need_appearances_writer() catch : ', repr(e))
        return writer

def write_to_pdf(input_file, data_dict):

    school_num = school_num_finder(input_file)
    pprint(school_num)

    output_file_name = "./PDFs/prepared_fact_sheets/"

    inputStream = open(input_file, "rb")
    pdf_reader = PdfFileReader(inputStream, strict=False)
    if "/AcroForm" in pdf_reader.trailer["/Root"]:
        pdf_reader.trailer["/Root"]["/AcroForm"].update(
            {NameObject("/NeedAppearances"): BooleanObject(True)})

    pdf_writer = PdfFileWriter()
    set_need_appearances_writer(pdf_writer)
    if "/AcroForm" in pdf_writer._root_object:
        pdf_writer._root_object["/AcroForm"].update(
            {NameObject("/NeedAppearances"): BooleanObject(True)})

    data = data_dict
    field_names = field_names_dict(pdf_reader.getFields())
    field_dictionary = {}

    for item in data:
        if school_num == item['SCHOOL_NUM']:
            output_file_name += '{}.pdf'.format(item["SCHOOL"])
            for key in item.keys():
                for field in field_names.keys():
                    if key == field_names[field]:
                        field_dictionary[field] = item[key]

    pdf_writer.addPage(pdf_reader.getPage(0))
    pdf_writer.updatePageFormFieldValues(pdf_writer.getPage(0), field_dictionary)

    outputStream = open(output_file_name, "wb")
    pdf_writer.write(outputStream)

    inputStream.close()
    outputStream.close()

def pdf_filler(input_list):
    
    for files in input_list:
        write_to_pdf("./PDFs/blank_PDFs/{}".format(files), retrive_dict())
    
if __name__ == "__main__":
    pdf_filler(prep_input(my_dir))
