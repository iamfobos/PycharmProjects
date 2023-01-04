HELP = ''' 
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя)
show - напечатать все добавленые задачи.
exit - завершить использование программой'''

tasks = []

run = True

while run:
    command = input('Введите команду: ')
    if command == 'help':
        print(HELP)
    elif command == 'show':
        print(tasks)
    elif command == 'add':
        task = input('Введите название задачи :')
        tasks.append(task)
        print('Задача добавлена!')
    elif command == 'exit':
        print('Вы вышли из программы!')
        break
    else:
        print('Неизвестная команда!')
        break
print('До свидания!')
