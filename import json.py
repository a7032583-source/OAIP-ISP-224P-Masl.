import json

table1Authors = [
    {"ID": 1, "Name": "Федор", "Surname": "Михайлович", "SecondName": "Достоевский"},
    {"ID": 2, "Name": "Александр", "Surname": "Сергеевич", "SecondName": "Пушкин"},
    {"ID": 3, "Name": "Федор", "Surname": "Михайлович", "SecondName": "Достоевский"}
]
table2Books = [
    {"ID": 1, "Name": "Преступление и наказание", "Author(s)": "Ф.М.Достоеквский", "Date": "1866"},
    {"ID": 1, "Name": "Сон смешного человека", "Author(s)": "Ф.М.Достоеквский", "Date": "1872"},
    {"ID": 1, "Name": "Преступление и наказание", "Author(s)": "Ф.М.Достоеквский", "Date": "1866"},
]
table3Readers = [
    {"ID": 1, "Name": "Федор", "Surname": "Михайлович", "SecondName": "Достоевский"},
    {"ID": 2, "Name": "Александр", "Surname": "Сергеевич", "SecondName": "Пушкин"},
    {"ID": 3, "Name": "Федор", "Surname": "Михайлович", "SecondName": "Достоевский"}
]


with open("Authors.json", "w",encoding="utf-8") as f:
    json.dump(table1Authors, f, ensure_ascii=False, indent=1)
with open("Books.json", "w",encoding="utf-8") as f:
    json.dump(table2Books, f, ensure_ascii=False, indent=1)
with open("Readers.json", "w",encoding="utf-8") as f:
    json.dump(table1Authors, f, ensure_ascii=False, indent=1)