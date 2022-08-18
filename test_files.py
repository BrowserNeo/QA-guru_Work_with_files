import os
import shutil
import zipfile
import csv
from PyPDF2 import PdfReader
from openpyxl import load_workbook


# Добавляем файлы в архив
def test_archive_zip():
    myzip = ZipFile(filename('my_zip.zip'), 'w')
    myzip.write(filename('username.csv'))
    myzip.write(filename('file_example_XLSX_50.xlsx'))
    myzip.write(filename('docs-pytest-org-en-latest.pdf'))
    myzip.close()


# Создаем папку и архив
def test_zip_files():
    os.mkdir('resources'):
    myzip = zipfile.ZipFile('resources\my_zip.zip', w)
    myzip.close()

# Проверка файла
def test_read_zip():
    read_zip = ZipFile(filename('my_zip.zip'), 'r')
    print(read_zip.namelist())
    read_zip.close()


# Разархивируем файл
def test_unzip_files():
    unzip_file = zipfile.ZipFile('resources\my_zip.zip')
    unzip_file.extractall('resources/')
    unzip_file.close()


# Проверка pdf
def test_read_pdf():
    reader = PdfReader('folder/Штирнер, Ницше Этика эгоизма. Нет ничего выше меня.pdf')
    page = reader.pages[1]
    text = page.extract_text()
    assert 'Этика эгоизма' in text
    import xlrd

    book = xlrd.open_workbook('resources/file_example_XLS_10.xls')
    print(f'Количество листов {book.nsheets}')
    print(f'Имена листов {book.sheet_names()}')
    sheet = book.sheet_by_index(0)
    print(f'Количество столбцов {sheet.ncols}')
    print(f'Количество строк {sheet.nrows}')
    print(f'Пересечение строки 9 и столбца 1 = {sheet.cell_value(rowx=9, colx=1)}')
    # печать всех строк по очереди
    for rx in range(sheet.nrows):
        print(sheet.row(rx))




# Проверка файла
def test_check_files():
    for file_info in zip_file.infolist():
        print(file_info.filename, file_info.date_time, file_info.file_size)

    zip_file.close()





# – Запаковать в zip архив несколько разных файлов: pdf, xlsx, csv;
# – Положить его в ресурсы;
# – Реализовать чтение и проверку содержимого каждого файла из архива
#
# Задачка со *
# Написать автотест для скачивания файла из firefox
# с фикстурой удаления файла из временной директории tmp перед каждым тестом

def test_zip_unzipping():
    zip_file = zipfile.ZipFile('../resources/work.zip', 'a')
    zip_file.extractall('../resources/tmp/')
    zip_file.close()


def test_txt_file_check():
    f = open('../resources/tmp/resources/filezipone.txt')
    for row in f:
        assert 'txt in zip file for test' in row
    f.close()


def test_scv_file_check():
    with open('../resources/tmp/resources/username-password-recovery-code.csv') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
    assert 'Recovery code' in str(headers)
    csvfile.close()


def test_pdf_file_check():
    reader = PdfReader('../resources/tmp/resources/docs-pytest-org-en-latest.pdf')
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()

    assert number_of_pages == 412
    assert 'pytest Documentation' in text


def test_delete_dir():
    shutil.rmtree('../resources/tmp/')







# Проверка файлов
def test_check_files():
    for file_info in zip_file.infolist():
        print(file_info.filename, file_info.date_time, file_info.file_size)

    zip_file.close()


# Разархивируем файл
def test_unzip_files():
    zip_file = zipfile.ZipFile('resources\Архив содержимого.zip')
    zip_file.extractall('resources/')
    zip_file.close()


# Проверка pdf
def test_read_pdf():
    reader = PdfReader('folder/Штирнер, Ницше Этика эгоизма. Нет ничего выше меня.pdf')
    page = reader.pages[1]
    text = page.extract_text()
    assert 'Этика эгоизма' in text


# Проверка xlsx
def test_read_xlsx():
    workbook = load_workbook('folder/file_excel.xlsx')
    sheet = workbook.active
    name = sheet.cell(row=2, column=1).value
    assert 'Ivan' == name


# Проверка csv
def test_read_csv_():
    with open('folder/users.csv') as f:
        reader = csv.reader(f)
        headers = next(reader)
    assert 'First_name' in str(headers)


# Удаляем папку
def test_remove_folder():
    shutil.rmtree('resources')