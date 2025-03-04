# импортируем модуль os
import os

# Модуль os позволяет пайтон работать с операционной системой.
# Просматривать директории (они же папки), файлы в директориях
# Создавать директории и перемещать файлы
#>
# создаем переменную dir и назначем ей прямой путь до папки требующей сортировки
dir = "D:\Downloads"

#>
# также делаем dir рабочей директорией
os.chdir(dir) 

# и сразу считываем файлы в папке dir
files_in_dir = os.listdir(dir)
#>
# на всякий случай проверим сколько элементов нашлось в dir
print("Files and folders in dir:", len(files_in_dir))

#>
# словарь названий папок и расширений файлов, которые будут в них помещены
folders_extensions = {
    "archives": ["rar", "7z", "zip"],
    "images":["jpg", "jpeg", "png", "gif", "ico", "webp", "JPG"],
    "docs": ["txt", "pdf", "doc", "docx", "xls", "xlx", "xlsx", "ppt", "pptx"],
    "torrents":["torrent"],
    "executables": ["exe", "msi"],
    "python": ["py"],
    "c#": ["cs"],
    "web": ["html", "php"],
    "databases": ["sql", "mdb"],
    "books": ["epub"],
    "music": ["mp3"],
    "others": ["swf", "apk", "menu"],
}
#>
# будьте осторожны - после выполнения этой части скрипта изменения необратимы
# перепроверьте все внимательно перед тем как двигаться дальше

# пробежимся по папкам (archives, images, docs... etc) 
for folder in folders_extensions:
    # проверяем есть ли папка в dir
    if not os.path.exists(folder) and os.path.isdir(folder):
        # создаем папку в папке dir
        os.mkdir(folder.capitalize())
#>
# функция сортировщик
def sort_file(file_in_dir):
    # игнорируем директории работаем только с файлами
    if not os.path.isfile(file_in_dir): return

#>
    # получаем расширение файла
    file_extension = file_in_dir.split(".")[-1]
#>
    for file_type in folders_extensions:
        # находим расширение файла в нашем словаре folders_extensions
        if file_extension in folders_extensions[file_type]:
            print(f"Перемещаю файл {file_in_dir} в папку {file_type}")
#>
            try:
                # перемещаем файл в подпапку
                os.rename(file_in_dir, f"{file_type}/{file_in_dir}")
            except FileExistsError:
                os.rename(file_in_dir, f"{file_type}/copy_{file_in_dir}")
#>
# вызываем функцию сортировщик на каждом файле папки dir
for file in files_in_dir:
    sort_file(file)

#>
# Точки для улучшения:
# - более оптимальный поиск расширения через сет
# - записывать все файлы с которыми столкнулись в журнал работы с файлами 
#   чтобы в будущем можно было посмотреть где был файл и куда был перемещен 
#   эксель таблица хорошо бы подошла - можно и быстрый поиск делать по ней
# - спрашивать путь до рабочей папки у пользователя перед началом работы
#   так можно сортировать любую папку
#   