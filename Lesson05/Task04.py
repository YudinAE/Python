"""=====================================================================================================================
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
====================================================================================================================="""
# Исходный файл
source_file = "Task04_source.txt"
# Преобразованный файл
final_file = "Task04_final.txt"
numerals = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
final_text = []

if __name__ == "__main__":
    print(f'========== Задание 4 ===========')
    try:
        # Поток считывания информации и преобразования
        with open(source_file, "r+", encoding='utf-8') as user_file:
            source_text = user_file.read()
            print(f'Исходный текст:\n{source_text}\n-----------')
            user_file.seek(0)
            for i in user_file:
                # Разделяем строку по первому пробелу
                i = i.split(' ', 1)
                # Заменяем английские числительные на русские
                final_text.append(numerals[i[0]] + '  ' + i[1])
    except IOError as file_n_found:
        print(f'Файл не найден:\n{file_n_found}')
# Поток записи информации в новый файл
with open(final_file, 'w+', encoding='utf-8') as final_file:
    final_file.writelines(final_text)
    final_file.seek(0)
    final_text = final_file.read()
    print(f'Итоговый текст:\n{final_text}')
