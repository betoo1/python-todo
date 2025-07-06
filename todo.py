#!/home/betoo/python-projeleri/todo/venv/bin/python

import argparse
from storage import load_tasks, save_tasks

def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "done": False})
    save_tasks(tasks)
    print(f"[+] Görev eklendi: {description}")

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"[-] Görev silindi: {removed['description']}")
    else:
        print("[!] Geçersiz görev numarası.")



def complete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"[✓] Görev tamamlandı: {tasks[index]['description']}")
    else:
        print("[!] Geçersiz görev numarası.")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Henüz görev yok.")
        return

    for idx, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else " "
        print(f"{idx}. [{status}] {task['description']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basit Todo Listesi")
    parser.add_argument("--add", help="Yeni görev ekle")
    parser.add_argument("--list", action="store_true", help="Tüm görevleri listele")
    parser.add_argument("--delete", type=int, help="Görevi sil")
    parser.add_argument("--done", type=int, help="Görevi tamamlandı olarak işaretle")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        list_tasks()
    elif args.done is not None:
        complete_task(args.done - 1) 
    elif args.delete is not None:
        delete_task(args.delete - 1)
    else:
        parser.print_help()
