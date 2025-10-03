from tasks import add_task
from storage import load_task

def main():
    tasks = load_task()

    while True:
        print("Add task")

        choice = input("Choose an option: ").strip()

        if (choice == '1'):
            add_task(tasks)

if __name__ == "__main__":
    main()
