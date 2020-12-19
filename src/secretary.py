docs = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

dirs = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': ['']
}


def name_from_number(documents):
    number = input('Enter document number: ')
    if not is_document(documents, number):
        return '\nDocument not found\n', None, None
    for document in documents:
        if document['number'] == number:
            return f'\nDocument owner: {document["name"]}\n', None, None


def shelf_from_number(documents, directories):
    number = input('Enter document number: ')
    if not is_document(documents, number):
        return '\nDocument not found\n', None, None
    for shelf in directories:
        if number in directories[shelf]:
            return f'\nDocument "{number}" is on shelf number: {shelf}\n', None, None
    else:
        return '\nDocument not found\n', None, None


# требуемое по заданию форматирование закомментил. Так ведь симпатичнее?
def all_documents_list(documents):
    if not documents:
        return f'\nDocuments list is EMPTY\n', None, None
    all_documents = ''
    for document in documents:
        # all_documents += f'{document["type"]} "{document["number"]}" "{document["name"]}"\n'
        all_documents += f'{document["type"]:10}| {document["number"]:12}| {document["name"]}\n'
    if all_documents:
        return f'\nDocuments list:\n{all_documents.rstrip()}\n', None, None


def add_document(documents, directories):
    type_ = input('Enter new document type: ')
    number = input('Enter new document number: ')
    name = input('Enter person name: ')
    shelf = input('Input new document shelf: ')
    if not is_shelf(directories, shelf):
        return '\nWrong shelf number\n', None, None
    documents.append({"type": type_, "number": number, "name": name})
    directories[shelf].append(number)
    return f'\nDocument "{number}" added to shelf "{shelf}"\n', documents, directories


def delete_document(documents, directories):
    number = input('Enter document number: ')
    if not is_document(documents, number):
        return '\nDocument not found\n', None, None
    for document in documents:
        if document['number'] == number:
            documents.remove(document)
            for shelf in directories:
                if number in directories[shelf]:
                    directories[shelf].remove(number)
            return f'\nDocument "{number}"" deleted\n', documents, directories


def move_document(documents, directories):
    number = input('Enter document number: ')
    if not is_document(documents, number):
        return '\nDocument not found\n', None, None
    target_shelf = input('Enter target shelf number: ')
    if not is_shelf(directories, target_shelf):
        return '\nTarget shelf not found\n', None, None
    for shelf in directories:
        if number in directories[shelf]:
            directories[shelf].remove(number)
            directories[target_shelf].append(number)
            return f'\nDocument "{number}"" moved\n', None, directories


def add_shelf(directories):
    new_shelf = input('Enter new shelf number: ')
    if is_shelf(directories, new_shelf):
        return '\nShelf already exists\n', None, None
    directories[new_shelf] = []
    return f'\nShelf "{new_shelf}" added\n', None, directories


def is_shelf(directories, shelf):
    if shelf in directories:
        return True
    return False


def is_document(documents, number):
    for document in documents:
        if document['number'] == number:
            return True
    return False


def help_():
    return '\np – person name from document number\n' \
           's – shelf from document number\n' \
           'l – all documents list\n' \
           'a – add new document\n' \
           'd - delete document\n' \
           'm - move document between shelves\n' \
           'as - add new shelf\n' \
           '? - this list\n' \
           'q - quit\n',\
           None, None


def main(documents, directories):
    """
    Function name and parameters are get from menu dictionary

    All functions return unified set of arguments:
    message string, changed_documents or None, changed_directories or None

    (Waiting for OOP)
    """
    menu = {
        'p': (name_from_number, documents),
        's': (shelf_from_number, documents, directories),
        'l': (all_documents_list, documents),
        'a': (add_document, documents, directories),
        'd': (delete_document, documents, directories),
        'm': (move_document, documents, directories),
        'as': (add_shelf, directories),
        '?': (help_,)
    }
    print('Available commands:')
    command = '?'
    while command != 'q':
        if command in menu:
            message, documents_new, directories_new = menu[command][0](*menu[command][1:])
            print(message)
            if documents_new:
                documents = documents_new
            if directories_new:
                directories = directories_new
        else:
            print('\nWrong command ("?" for help)\n')
        command = input('Input command: ')


if __name__ == '__main__':
    main(docs, dirs)
