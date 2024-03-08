import json
import datetime

comands = ['add', 'edit', 'delete', 'show', 'save']
date = datetime.datetime.now
notions = {date: {"nameNotin": "NameNotion", "Body Notion": "Text Notion"}}



def choose_action(notions):
    while True:
        user_choice = input('1 - Добавить заметку\n\
2 - Изменить заметку\n3 - Удалить заметку\n4 - Просмотреть все заметки\n0 - Выйти из приложения\n')
        print()
        if user_choice == '1':
            addNotion(notions)
            print("Заметка успено сохранена ")
        elif user_choice == '2':
            changeNotions(notions)
            print("Изменения успешно сохранены ")
        elif user_choice == '3':
            delete(notions)
            print("Заметка успешно удалена!")
        elif user_choice == '4':
            show(notions)
        elif user_choice == '0':
            print('До свидания!')
            break
        else:
            print('Неправильно выбрана команда!')
            print()
            continue

def writeNewInfo():
    date = input('Ввдеите дату заметки(в формате yyyy.mm.dd): ')
    nameNotion= input('Введите имя заметки: ')
    bodyNotion = input('Введите текст заметки: ')
    return date, nameNotion, bodyNotion

def addNotion(file_name):
    info = ' '.join(writeNewInfo())
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{info}\n')

def readFile(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = ['Дата: ', ' Имя заметки: ', ' Текст заметки: ']
    notionText = []
    for line in lines:
        line = line.strip().split()
        notionText.append(dict(zip(headers, line)))
    return notionText
                
def show(file_name):
    newListNotion = sorted(readFile(file_name), key=lambda x: x['Дата: '])
    printNotion(newListNotion)
    print()
    return newListNotion

def printNotion(notionList: list):
    for notion in notionList:
        for key, value in notion.items():
            print(f'{key}: {value}', end='')
        print()


def readFileList(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        notionsList = []
        for line in file.readlines():
            notionsList.append(line.split())
    return notionsList


def delete(file_name):
    notionsList = readFileList(file_name)
    notionsChange = searchToModify(notionsList)
    notionsList.remove(notionsChange)
    with open(file_name, 'w', encoding='utf-8') as file:
        for notions in notionsList:
            line = ' '.join(notions) + '\n'
            file.write(line)


def searchToModify(notionsList: list):
    search_field, search_value = search_parameters()
    search_result = []
    for notions in notionsList:
        if notions[int(search_field) - 1] == search_value:
            search_result.append(notions)
    if len(search_result) == 1:
        return search_result[0]
    elif len(search_result) > 1:
        print('Найдено несколько заметок')
        for i in range(len(search_result)):
            print(f'{i + 1} - {search_result[i]}')
        num_count = int(input('Выберите заметку, которую хотите изменить: '))
        return search_result[num_count - 1]
    else:
        print('Заметка не найден')
    print()


def search_parameters():
    print('По какому полю выполнить поиск?')
    search_field = input('1 - по дате\n2 - по имени заметки\n')
    print()
    search_value = None
    if search_field == '1':
        search_value = input('Введите дату для поиска(в формате yyyy.mm.dd): ')
        print()
    elif search_field == '2':
        search_value = input('Введите имя заметки для поиска: ')
        print()
    return search_field, search_value



def changeNotions(file_name):
    notionsList = readFileList(file_name)
    notionsChange = searchToModify(notionsList)
    notionsList.remove(notionsChange)
    print('Какое поле вы хотите изменить?')
    field = input('1 - Имя заметки\n2 - Текст заметки\n')
    if field == '1':
        notionsChange[1] = input('Введите имя заметки: ')
    elif field == '2':
        notionsChange[2] = input('Введите текст заметки: ')
    notionsList.append(notionsChange)
    with open(file_name, 'w', encoding='utf-8') as file:
        for notions in notionsList:
            line = ' '.join(notions) + '\n'
            file.write(line)


if __name__ == '__main__':
    file = 'Notion.json'
    choose_action(file)
