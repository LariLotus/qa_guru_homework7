from pypdf import PdfReader
import os

# TODO оформить в тест, добавить ассерты и использовать универсальный путь

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
RESOURCES_PATH = os.path.join(PROJECT_ROOT_PATH, '../resources')


def test_pdf():
    pdf_path = os.path.join(RESOURCES_PATH, "docs-pytest-org-en-latest.pdf")
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        number_of_pages = len(reader.pages)
        page = reader.pages[0]
        text = page.extract_text()
        print(page)
        print(number_of_pages)
        print(text)
        assert number_of_pages == 412
        assert text == 'pytest Documentation\nRelease 0.1\nholger krekel, trainer and consultant, ' \
                       'https://merlinux.eu/\nJul 14, 2022 '
