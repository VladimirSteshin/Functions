from Functions_work import directories, documents


def program(command=(input('Введите команду: ').lower())):
    if command == 'p':
        return doc_people()
    elif command == 's':
        return doc_shelf()
    elif command == 'l':
        return doc_list()
    elif command == 'a':
        return doc_add()
    elif command == 'd':
        return doc_delete()
    elif command == 'm':
        return doc_move()
    elif command == 'as':
        return doc_add_shelf()
    else:
        print('Неверная команда! Введите команду ещё раз: ')
        return program()