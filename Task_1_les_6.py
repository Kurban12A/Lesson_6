# C:\Users\Курбан\Desktop\Курс Level UP\Lesson_6\text.txt
with open(input('Введите путь к файлу: '), "r", encoding="utf-8") as file:
    try:
        files = max([elem.rstrip() for elem in file.read().split()], key=len)
        if files:
            print(f'word - {files}, len = {len(files)}')
    except ValueError:
        print('Not Found')

