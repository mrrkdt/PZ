# Задание предполагает, что у студента есть проект с практическими работами (№ 2-13),
# оформленный согласно требованиям. Все задания выполняются с использованием модуля OS:
# • Перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена
#  вложенных подкаталогов выводить не нужно.
# • Перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
#  test1. В папку test переместить два файла из П36, а в папку test1 - один файл из П37.
# • Файл из П37 переименовать в test.txt. Вывести в консоль информацию о размере
#  файлов в папке test.
# • Перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
#  консоль. Использовать функцию basename 0 (os.path.basename().
# • Перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в
#  привязанной к нему программе. Использовать функцию os.startfile).
# • Удалить файл test.txt.

import os

root = os.path.abspath('../')


def get_paths():
    return {
        "PZ6": os.path.join(root, 'PZ_6'),
        "PZ7": os.path.join(root, 'PZ_7', 'pz_7.py'),
        "PZ11": os.path.join(root, 'PZ_11'),
        "test": os.path.join(root, 'test'),
        "test1": os.path.join(root, 'test', 'test1'),
        "test_file": os.path.join(root, 'test', 'test1', 'test.txt'),
        "reports": os.path.join(root, 'reports'),
        "report_pdf": 'PZ_7_report.pdf'
    }


def change_directory(path):
    if not os.path.exists(path):
        print(f"Каталог {path} не найден")
        return False
    os.chdir(path)
    return True


def copy_file(source, destination):
    if not os.path.exists(source):
        print(f"Файл {source} не найден")
        return
    with open(source, 'rb') as f_src, open(destination, 'wb') as f_dst:
        f_dst.write(f_src.read())


def list_files_in_directory(path):
    if not os.path.exists(path):
        print(f"Каталог {path} не найден")
        return []
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]


def create_directory(path):
    os.makedirs(path, exist_ok=True)


def print_file_sizes(directory):
    if not os.path.exists(directory):
        print(f"Каталог {directory} не найден")
        return
    for file_s in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file_s)):
            print(f"Размер файла {file_s}: {os.path.getsize(os.path.join(directory, file_s))} байт")


os.chdir(root)

paths = get_paths()
files_in_pz11 = list_files_in_directory(paths['PZ11'])

print("Файлы в каталоге PZ_11:", files_in_pz11)

create_directory(paths['test1'])

file_to_copy = 'pz_6.py'

src = os.path.join(paths['PZ6'], file_to_copy)
dst = os.path.join(paths['test'], file_to_copy)
copy_file(src, dst)

copy_file(paths['PZ7'], paths['test_file'])

print_file_sizes(paths['test'])

if files_in_pz11:
    shortest_filename = min(files_in_pz11, key=len)
    print("Файл с самым коротким именем:", os.path.basename(shortest_filename))

if change_directory(paths['reports']) and os.path.exists(paths['report_pdf']):
    os.startfile(paths['report_pdf'])
else:
    print(f"PDF файл {paths['report_pdf']} не найден")

if os.path.exists(paths['test_file']):
    os.remove(paths['test_file'])
    print(f"Файл test.txt успешно удален")
else:
    print(f"Файл test.txt не найден")
