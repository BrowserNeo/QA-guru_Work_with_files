import os
import shutil
import zipfile
import csv
from PyPDF2 import PdfReader
from openpyxl import load_workbook

# Создаем папку и архив
os.mkdir('resources'):
myzip = zipfile.ZipFile('resources\my_zip.zip', w)


# Добавляем файлы в архив
def test_archive_zip():
    myzip = ZipFile(filename('my_zip.zip'), 'w')
    myzip.write(filename('username.csv'))
    myzip.write(filename('file_example_XLSX_50.xlsx'))
    myzip.write(filename('docs-pytest-org-en-latest.pdf'))
    myzip.close()

# Проверка файла
def test_read_zip():
    for file_info in myzip.infolist():
        print(file_info.filename, file_info.date_time, file_info.file_size)
    myzip.close()


# Разархивируем файл
def test_unzip_files():
    unzip_file = zipfile.ZipFile('resources\my_zip.zip')
    unzip_file.extractall('resources/')
    unzip_file.close()


