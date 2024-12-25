from components import (
    File,
    Edit,
    Reference,
    New,
    Save,
    Open
)



def show_menu():
    print(Edit().functional())
    print(Edit().aim())
    print(Reference().functional())
    print(Reference().aim())
    file = File()
    file.add_chapter(New())
    file.add_chapter(Save())
    file.add_chapter(Open())
    print(file.functional())
    for key in file.subsections.keys():
        print(key)
    print(file.aim())
show_menu()