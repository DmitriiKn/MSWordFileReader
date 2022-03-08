import docx2txt


def reader(path):
    return docx2txt.process(path)


def test():
    my_text = reader("G:\\Мой диск\\ДИССЕРТАЦИЯ\\Педагогика\\пр10_11\\ЛЕКЦИЯ 11. СРЕДСТВА ОБУЧЕНИЯ.docx")
    print(my_text)

