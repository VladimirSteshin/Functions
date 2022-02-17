from Functions_work import directories, documents


def doc_people(doc_number):
    result = 0
    for ask in documents:
        if doc_number in ask.values():
            result = ask['name']
            return result
    if result == 0:
        return doc_people(input('Неверный номер! Введите номер документа повторно: '))


def doc_shelf(doc_number):
    result = 0
    for key, value in directories.items():
        if doc_number in value:
            result = key
            return f'Номер полки: {result}'
    if result == 0:
        return doc_shelf(input('Неверный номер! Введите номер документа повторно: '))


def doc_list():
    for ask in documents:
        print(f'{ask["type"]} "{ask["number"]}" "{ask["name"]}"')
    return ''


def doc_add(add_shelf, add_type, add_number, add_name):
    if add_shelf in directories.keys():
        documents.append({'type': add_type, 'number': add_number, 'name': add_name})
        for key, value in directories.items():
            if key == add_shelf:
                value.append(add_number)
        return documents, directories
    else:
        print('Неверный номер полки!')
        return doc_add(input('Введите номер полки для хранения: '), input('Введите тип документа: '),
                       input('Введите номер документа: '), input('Введите имя владельца документа: '))


def program(command=(input('Введите команду: ').lower())):
    if command == 'p':
        return doc_people(input('Введите номер документа: '))
    elif command == 's':
        return doc_shelf(input('Введите номер документа: '))
    elif command == 'l':
        return doc_list()
    elif command == 'a':
        return doc_add(input('Введите номер полки для хранения: '), input('Введите тип документа: '),
                       input('Введите номер документа: '), input('Введите имя владельца документа: '))
    # elif command == 'd':
    #     return doc_delete()
    # elif command == 'm':
    #     return doc_move()
    # elif command == 'as':
    #     return doc_add_shelf()
    else:
        return program(command=(input('Неверная команда! Введите команду повторно: ').lower()))


print(program())
