tasks = []

def add_task(task): #Adding tasks to list
    tasks.append({'task': task, 'finished': False})
    print('Task added successfully')

def display_tasks(): #View Tasks
    if len(tasks) > 0:
        for serialno, task in enumerate(tasks, start=1):
            if task['finished']:
                status = '✓'
            else:
                status = 'o'
            print(f'{serialno}: [{status}] {task["task"]}')
    else:
        print('No tasks to display')

def mark_as_finished(task_no):
    if 1 <= task_no <= len(tasks):
        tasks[task_no - 1]['finished'] = True
        print(f"Task {tasks[task_no - 1]['task']} marked as finished ")

    else:
        print('Invalid task number')

print('-----To Do List Application-----')
while True:
    print('''________________________________
1. Add Task
2. View Task
3. Mark task
4. Quit''')
    choice = input('Enter your choice: ')
    if choice == '1':
        task = input('Enter your task: ')
        add_task(task)
    elif choice == '2':
        display_tasks()
    elif choice == '3':
        n = int(input('Enter the task number to mark as finished: '))
        mark_as_finished(n)
    elif choice == '4':
        print('Good Bye')
        break
    else:
        print('Invalid choice. Please try again')


