from src import secretary as s


class TestSecretary:

    def test_name_from_number_right(self, get_test_documents, get_document, monkeypatch):
        """name_from_number должен вернуть сообщение с верным именем из базы"""
        documents = get_test_documents
        document_number = get_document
        expected_msg = f'\nDocument owner: {documents[0]["name"]}\n'
        monkeypatch.setattr('builtins.input', lambda _: document_number)
        assert s.name_from_number(documents) == (expected_msg, None, None)

    def test_name_from_number_wrong(self, get_test_documents, get_wrong_document, monkeypatch):
        """name_from_number должен вернуть сообщение о том что документ не найден"""
        documents = get_test_documents
        document_number = get_wrong_document
        expected_msg = '\nDocument not found\n'
        monkeypatch.setattr('builtins.input', lambda _: document_number)
        assert s.name_from_number(documents) == (expected_msg, None, None)

    def test_shelf_from_number_right(self, get_test_documents, get_test_directories, get_document, monkeypatch):
        """shelf_from_number должен вернуть сообщение c верным номером полки"""
        documents = get_test_documents
        directories = get_test_directories
        document_number = get_document
        expected_msg = f'\nDocument "{documents[0]["number"]}" is on shelf number: {list(directories.keys())[0]}\n'
        monkeypatch.setattr('builtins.input', lambda _: document_number)
        assert s.shelf_from_number(documents, directories) == (expected_msg, None, None)

    def test_shelf_from_number_wrong(self, get_test_documents, get_test_directories, get_wrong_document, monkeypatch):
        """shelf_from_number должен вернуть сообщение о том что документ не найден"""
        documents = get_test_documents
        directories = get_test_directories
        document_number = get_wrong_document
        expected_msg = '\nDocument not found\n'
        monkeypatch.setattr('builtins.input', lambda _: document_number)
        assert s.shelf_from_number(documents, directories) == (expected_msg, None, None)

    def test_all_documents_list(self, get_test_documents):
        """all_documents_list должен вернуть список всех документов"""
        documents = get_test_documents
        expected_msg = f'\nDocuments list:\n' \
                       f'{documents[0]["type"]:10}| {documents[0]["number"]:12}| {documents[0]["name"]}\n'
        assert s.all_documents_list(documents) == (expected_msg, None, None)

    def test_all_documents_list_empty(self):
        """all_documents_list должен вернуть сообщение что список документов пуст"""
        documents = []
        expected_msg = f'\nDocuments list is EMPTY\n'
        assert s.all_documents_list(documents) == (expected_msg, None, None)

    def test_add_document(self, get_test_documents, get_test_directories, get_new_document, monkeypatch):
        """add_document должен вернуть сообщение о добавлении документа и новые documents и directories"""
        documents = get_test_documents
        directories = get_test_directories
        new_document = get_new_document
        type_, number, name, shelf = new_document
        monkeypatch.setattr('builtins.input', make_multiple_inputs(new_document))
        expected_msg = f'\nDocument "{number}" added to shelf "{shelf}"\n'
        expected_doc = documents.copy()
        expected_doc.append({"type": type_, "number": number, "name": name})
        expected_dir_key = list(directories.keys())[0]
        expected_dir_value = list(directories.values())[0]
        expected_dir_value.append(number)
        expected_dir = {expected_dir_key: expected_dir_value}
        assert s.add_document(documents, directories) == (expected_msg, expected_doc, expected_dir)

    def test_add_document_wrong_shelf(self,
                                      get_test_documents,
                                      get_test_directories,
                                      get_new_document,
                                      get_wrong_shelf,
                                      monkeypatch):
        """add_document должен вернуть сообщение о неверной полке"""
        documents = get_test_documents
        directories = get_test_directories
        new_document = get_new_document
        new_document[3] = get_wrong_shelf
        monkeypatch.setattr('builtins.input', make_multiple_inputs(new_document))
        expected_msg = '\nWrong shelf number\n'
        assert s.add_document(documents, directories) == (expected_msg, None, None)

    def test_delete_document(self, get_test_documents, get_test_directories, get_document, monkeypatch):
        """delete_document должен вернуть сообщение об удалении файла и новые documents и directories"""
        documents = get_test_documents
        directories = get_test_directories
        document_number = get_document
        monkeypatch.setattr('builtins.input', lambda _: document_number)
        expected_msg = f'\nDocument "{document_number}"" deleted\n'
        expected_doc = []
        expected_dir_key = list(directories.keys())[0]
        expected_dir_value = list(directories.values())[0]
        expected_dir_value.remove(document_number)
        expected_dir = {expected_dir_key: expected_dir_value}
        assert s.delete_document(documents, directories) == (expected_msg, expected_doc, expected_dir)

    def test_delete_document_wrong(self, get_test_documents, get_test_directories, get_wrong_document, monkeypatch):
        """delete_document должен вернуть сообщение о неверном файле"""
        documents = get_test_documents
        directories = get_test_directories
        document_number = get_wrong_document
        monkeypatch.setattr('builtins.input', lambda _: document_number)
        expected_msg = '\nDocument not found\n'
        assert s.delete_document(documents, directories) == (expected_msg, None, None)


def make_multiple_inputs(inputs):
    def next_input(_):
        return inputs.pop(0)
    return next_input
