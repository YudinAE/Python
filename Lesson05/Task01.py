"""==================================================================================================================
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
====================================================================================================================="""

# Создание наименование файла
FILENAME = "Create_user_file_input.txt"

if __name__ == "__main__":
    print(f'========== Задание 1. Создать файл и записать в него ввод с клавиатуры ===========')
    with open(FILENAME, 'w+', encoding='utf-8') as user_file:
        user_text = input('Введите текст: ')
        while user_text:
            user_file.writelines(f'{user_text}\n') # Записать последовательность (список) строк в файл
            user_text = input('Введите текст: ')
            if not user_text:
                break
        # устанавливаем текущую позицию указателя чтения/записи в файле file.
        # 0 - означает, что нужно сместить указатель относительно начала файла.
        user_file.seek(0)
        # Читаем, что записалось
        user_text_read = user_file.read()
        print(user_text_read)