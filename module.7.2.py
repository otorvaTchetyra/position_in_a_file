def custom_write(file_name, strings):
    strings_positions = {}
    
    with open(file_name, 'w', encoding='utf-8') as file:
        for index, string in enumerate(strings):
            byte_position = file.tell()  # Получаем текущую позицию в байтах
            file.write(string + '\n')    # Записываем строку в файл с переносом
            strings_positions[(index + 1, byte_position)] = string  # Сохраняем в словарь

    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
