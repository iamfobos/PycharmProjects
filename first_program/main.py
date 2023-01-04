HELP = ''' 
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя)
show - напечатать все добавленые задачи.'''

tasks = {


}

run = True

while run:
    command = input('Введите команду: ')
    if command == 'help':
        print(HELP)
    elif command == 'show':
        print(tasks)
    elif command == 'add':
        date = input('Введите дату задачи: ')
        task = input('Введите название задачи: ')
        if date in tasks:
            tasks[date].append(task)
        else:
            tasks[date] = []
            tasks[date].append(task)
        print('Задача', task,'добавлена на дату', date,':')
    else:
        print('Неизвестная команда!')
        break
print('До свидания!')
