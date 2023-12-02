import os
import time
import promptlib  #pip install promptlib
import PyPDF2  #pip install PyPDF2
import os.path, time

SILENCE = True


def f_print(*list_str):
    if not SILENCE:
        print(*list_str)


def get_pdf_data(pdf_file_path):
    pdf_file = open(pdf_file_path, "rb")
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    f_print("nb of pages = ", number_of_pages)
    page = read_pdf.getPage(0)
    page_content = page.extractText()
    f_print('\n------first page content---------')
    f_print(page_content)
    pdf_file.close()
    f_print('----------------------------------')
    return {"nb_pages": number_of_pages, "raw_txt": page_content}


def get_file_size_in_kilobytes(file_path):
    """ Get size of file at given path in bytes"""
    size = os.path.getsize(file_path) / 100
    return size


def norm_path(path):
    return os.path.normpath(path).replace('\\', '/')


def get_path_from_user():
    prompter = promptlib.Files()
    dir = prompter.dir()
    print(dir, '\n', dir)
    return dir


def read_folder(folder):
    L = []
    for files in os.listdir(folder):
        path = folder + "\\" + files
        if not os.path.isdir(path):
            L.append(path)
    return L


def get_basic_file_data(filepath):

    data = {}

    #filepath
    filepath = norm_path(filepath)
    data["filepath"] = filepath

    #taille en kb
    data["kb_size"] = get_file_size_in_kilobytes(filepath)

    #filename an extension
    filename, extension = os.path.splitext(filepath)
    data["filename"] = filename.split("/")[-1]
    data["extension"] = extension[1:]

    #timestamp
    last_modification_date = time.ctime(os.path.getmtime(filepath))
    creation_date = time.ctime(os.path.getctime(filepath))
    data["last_modification_date"] = last_modification_date
    data["creation_date"] = creation_date

    return data
