import json
#========== ketabkhane baraye rastchin kardane horof==========
import arabic_reshaper
from bidi.algorithm import get_display
import os

TASK_FILE = "tasks.json"

# ============= bargozari task ha
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return []

# ======== zakhire tasks
def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

# ======== rastchin kardane matn
def rtl_text(text):
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)

# ======== namayeshe tasks
def display_tasks(tasks):
    if not tasks:
        print(rtl_text("📋 وظیفه‌ای ثبت نشده است."))
        return
    print(rtl_text("📋 وظایف شما:"))
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {rtl_text(task['title'])} [{status}]")

# ======== menuo asliy
def main():
    tasks = load_tasks()

    while True:
        print("\n" + rtl_text("منوی منشی:"))
        print(rtl_text("1. اضافه کردن وظیفه جدید"))
        print(rtl_text("2. نمایش وظایف"))
        print(rtl_text("3. علامت زدن انجام شده"))
        print(rtl_text("4. یادآوری امروز"))
        print(rtl_text("q. خروج"))
        choice = input(">> ").lower()

        if choice == "1":
            title = input(rtl_text("عنوان وظیفه: "))
            tasks.append({"title": title, "done": False})
            save_tasks(tasks)
            print(rtl_text("✅ وظیفه اضافه شد."))

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            display_tasks(tasks)
            idx = int(input(rtl_text("شماره وظیفه‌ای که انجام شده: "))) - 1
            if 0 <= idx < len(tasks):
                tasks[idx]["done"] = True
                save_tasks(tasks)
                print(rtl_text("✅ علامت زده شد."))
            else:
                print(rtl_text("⚠️ شماره نامعتبر است."))

        elif choice == "4":
            print(rtl_text("🎯 یادآوری امروز:"))
            for task in tasks:
                if not task["done"]:
                    print(f"- {rtl_text(task['title'])}")

        elif choice == "q":
            print(rtl_text("👋 خداحافظ!"))
            break

        else:
            print(rtl_text("⚠️ انتخاب نامعتبر است."))

if __name__ == "__main__":
    main()
