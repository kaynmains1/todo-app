from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, edit, show, complete or exit: ")
    user_action = user_action.strip()


    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)
    elif user_action.startswith("edit"):
        try:
            todos = get_todos()

            number = int(user_action[5:])
            number = number - 1
            new_todo = input("Enter new todo: ") + "\n"
            todos[number] = new_todo

            write_todos(todos)
        except ValueError:
            print("Write a number after 'edit'.")
            continue
        except IndexError:
            print(f"There no todo under this number")
            continue

    elif user_action.startswith("show"):
        todos = get_todos()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item.capitalize()}"
            print(row)
    elif user_action.startswith("complete"):
        try:
            todos = get_todos()

            number = int(user_action[9:])
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            message = f"Todo '{todo_to_remove.capitalize()}' has been removed from the list"
            print(message)

            write_todos(todos)
        except ValueError:
            print("Write a number after 'complete'.")
            continue
        except IndexError:
            print(f"There no todo with this number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")

print("Bye!")