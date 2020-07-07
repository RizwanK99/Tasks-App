import tkinter as tk
import tkinter.font as tk_font
from tkinter import messagebox

title, category, time_req, due_date, description = [], [], [], [], []


def add_task():
    t_title = ent_title.get()
    t_cat = ent_cat.get()
    t_time = ent_time.get()
    t_des = ent_des.get()
    t_due = ent_due.get()

    if t_title == "" or t_cat == "" or t_time == "" or t_des == "":
        messagebox.showinfo(title="Error", message="One or more fields are left blank. You only can leave \"Due Date\" blank.")

    else:
        if t_due == "":
            t_due = "N/A"

        title.append(t_title)
        category.append(t_cat)
        time_req.append(t_time)
        due_date.append(t_due)
        description.append(t_des)
        ent_title.delete(0, tk.END)
        ent_cat.delete(0, tk.END)
        ent_time.delete(0, tk.END)
        ent_due.delete(0, tk.END)
        ent_des.delete(0, tk.END)
        info = open("Tasks.txt", "a")
        info.write("\n" + t_title + ", " + t_cat + ", " + t_time + ", " + t_due + ", " + t_des)
        info.close()
        show()


def edit_task():
    t_title = ent_title.get()
    t_cat = ent_cat.get()
    t_time = ent_time.get()
    t_des = ent_des.get()
    t_due = ent_due.get()

    show()


def delete():
    t_title = ent_title.get()
    t_cat = ent_cat.get()
    t_time = ent_time.get()
    t_des = ent_des.get()
    t_due = ent_due.get()
    ent_title.delete(0, tk.END)
    ent_cat.delete(0, tk.END)
    ent_time.delete(0, tk.END)
    ent_due.delete(0, tk.END)
    ent_des.delete(0, tk.END)
    leng = len(title)
    x = 0
    found = False
    for x in range(leng):
        if t_title.casefold() == title[x].casefold() and t_cat.casefold() == category[x].casefold():

            a_file = open("Tasks.txt", "r")
            lines = a_file.readlines()
            a_file.close()

            new_file = open("Tasks.txt", "w")
            first = 1
            for line in lines:
                line = line.strip("\n")
                to_del = title[x] + ", " + category[x] + ", " + time_req[x] + ", " + due_date[x] + ", " + description[x]
                if line != to_del:
                    if first == 1:
                        new_file.write(line)
                        first = 0
                    else:
                        new_file.write("\n" + line)
            new_file.close()

            title.remove(title[x])
            category.remove(category[x])
            time_req.remove(time_req[x])
            due_date.remove(due_date[x])
            description.remove(description[x])
            show()
            found = True
            break
    if not found:
        messagebox.showinfo(title="Error", message="Could not delete, task not found.")


def sort_by_name():
    global title, category, time_req, due_date, description
    combined = zip(title, category, time_req, due_date, description)
    sorted_pairs = sorted(combined)
    tuples = zip(*sorted_pairs)
    n_title, n_category, n_time_req, n_due_date, n_description = [list(x) for x in tuples]
    title, category, time_req, due_date, description = n_title, n_category, n_time_req, n_due_date, n_description
    show()


def sort_by_date():
    global title, category, time_req, due_date, description
    combined = zip(due_date, title, category, time_req, description)
    sorted_pairs = sorted(combined)
    tuples = zip(*sorted_pairs)
    n_due_date, n_title, n_category, n_time_req, n_description = [list(x) for x in tuples]
    title, category, time_req, due_date, description = n_title, n_category, n_time_req, n_due_date, n_description
    show()


def filter_by_cat():
    leng = len(title)

    txt_edit.delete("1.0", tk.END)
    dash = '-' * 200
    txt_edit.insert(tk.END, dash + "\n")
    txt_edit.insert(tk.END, '{:<20}{:<20}{:<30s}{:<30s}{:<10s}{:<1s}'.format("Title", "Category", "Time", "Due Date", "Description", "\n"))
    txt_edit.insert(tk.END, dash + "\n")
    for x in range(leng):
        if category[x].casefold() == ent_cat.get().casefold():
            txt_edit.insert(tk.END, '{:<30s}{:<30s}{:<30s}{:<30s}{:<10s}{:<1s}'.format(title[x], category[x], time_req[x], due_date[x], description[x], "\n"))


def show():
    leng = len(title)

    # TO PUT THE TEXT IN THE TEXT BOX (GOING TO REMOVE UNLESS I CAN FIGURE OUT COLUMNS)

    txt_edit.delete("1.0", tk.END)
    dash = '-' * 200
    txt_edit.insert(tk.END, dash + "\n")
    txt_edit.insert(tk.END, '{:<20}{:<20}{:<30s}{:<30s}{:<10s}{:<1s}'.format("Title", "Category", "Time", "Due Date", "Description", "\n"))
    txt_edit.insert(tk.END, dash + "\n")
    for x in range(leng):
        txt_edit.insert(tk.END, '{:<30s}{:<30s}{:<30s}{:<30s}{:<10s}{:<1s}'.format(title[x], category[x], time_req[x], due_date[x], description[x], "\n"))

    # TO USE THE TABLE FORMATTING

    for widget in display.winfo_children():
        widget.destroy()

    label = tk.Label(display, text="Title", padx=5, pady=5, font=14)
    label.grid(row=0, column=0, padx=5, pady=5)
    label = tk.Label(display, text="Category", padx=5, pady=5, font=14)
    label.grid(row=0, column=1, padx=5, pady=5)
    label = tk.Label(display, text="Time Required", padx=5, pady=5, font=14)
    label.grid(row=0, column=2, padx=5, pady=5)
    label = tk.Label(display, text="Due Date", padx=5, pady=5, font=14)
    label.grid(row=0, column=3, padx=5, pady=5)
    label = tk.Label(display, text="Description", padx=5, pady=5, font=14)
    label.grid(row=0, column=4, padx=5, pady=5)

    for row in range(leng):
        for col in range(5):
            if col == 0:
                label = tk.Label(display, text=title[row], padx=5, pady=5)
            elif col == 1:
                label = tk.Label(display, text=category[row], padx=5, pady=5)
            elif col == 2:
                label = tk.Label(display, text=time_req[row], padx=5, pady=5)
            elif col == 3:
                label = tk.Label(display, text=due_date[row], padx=5, pady=5)
            elif col == 4:
                label = tk.Label(display, text=description[row], padx=5, pady=5)
            label.grid(row=row+1, column=col, padx=5, pady=5)


def read_file():
    info = open("Tasks.txt", "r")
    line = info.readline()
    items = 0

    while line != "":
        bits = line.split(", ")
        title.append(bits[0])
        category.append(bits[1])
        time_req.append(bits[2])
        due_date.append(bits[3])
        description.append(bits[4])
        description[items] = description[items].rstrip("\n")
        items = items + 1
        line = info.readline()

    info.close()
    return items


def print_file(i):
    dash = '-' * 75
    print(dash)
    print('{:<15s}{:<15s}{:<15s}{:<15s}{:<15s}'.format("Title", "Category", "Time", "Due Date", "Description"))
    print(dash)

    for x in range(i):
        print('{:<15s}{:<15s}{:<15s}{:<15s}{:<15s}'.format(title[x], category[x], time_req[x], due_date[x], description[x]))


total = read_file()

window = tk.Tk()
window.title("Rizwan's Tasks")
window.geometry("1280x720")

frame1 = tk.Frame(master=window, width=256, bg="#594F4F")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

fontStyle = tk_font.Font(family="Lucida Grande", size=20)
lbl_menu = tk.Label(frame1, text="Options", bg="#45ADA8", font=fontStyle, fg="#FFFFFF")
lbl_menu.pack(padx=5, pady=5)

a_d = tk.Frame(frame1, bg="#45ADA8")
a_d.pack(padx=5, pady=5)

btn_add = tk.Button(a_d, text="Add", command=add_task, bg="#9DE0AD")
btn_add.grid(column=0, row=0, padx=5, pady=5)

btn_del = tk.Button(a_d, text="Delete", command=delete, bg="#9DE0AD")
btn_del.grid(column=1, row=0, padx=5, pady=5)

btn_edit = tk.Button(frame1, text="Edit", command=edit_task, bg="#9DE0AD")
btn_edit.pack(padx=5, pady=5)

btn_sort_date = tk.Button(frame1, text="Sort by Date", command=sort_by_date,  bg="#9DE0AD")
btn_sort_date.pack(padx=5, pady=5)

btn_sort_name = tk.Button(frame1, text="Sort by Name", command=sort_by_name,  bg="#9DE0AD")
btn_sort_name.pack(padx=5, pady=5)

btn_filter_cat = tk.Button(frame1, text="Filter by Category", command=filter_by_cat,  bg="#9DE0AD")
btn_filter_cat.pack(padx=5, pady=5)

menu = tk.Frame(frame1, bg="#45ADA8")
menu.pack(padx=5, pady=5)

lbl_title = tk.Label(menu, text="Title", bg="#E5FCC2")
lbl_title.grid(row=0, column=0, padx=5, pady=5)

lbl_cat = tk.Label(menu, text="Category", bg="#E5FCC2")
lbl_cat.grid(row=1, column=0, padx=5, pady=5)

lbl_time = tk.Label(menu, text="Time", bg="#E5FCC2")
lbl_time.grid(row=2, column=0, padx=5, pady=5)

lbl_due = tk.Label(menu, text="Due Date", bg="#E5FCC2")
lbl_due.grid(row=3, column=0, padx=5, pady=5)

lbl_des = tk.Label(menu, text="Description", bg="#E5FCC2")
lbl_des.grid(row=4, column=0, padx=5, pady=5)

ent_title = tk.Entry(menu)
ent_title.grid(row=0, column=1, padx=5, pady=5)

ent_cat = tk.Entry(menu)
ent_cat.grid(row=1, column=1, padx=5, pady=5)

ent_time = tk.Entry(menu)
ent_time.grid(row=2, column=1, padx=5, pady=5)

ent_due = tk.Entry(menu)
ent_due.grid(row=3, column=1, padx=5, pady=5)

ent_des = tk.Entry(menu)
ent_des.grid(row=4, column=1, padx=5, pady=5)

frame2 = tk.Frame(master=window, width=1024, bg="#9DE0AD")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

lbl_title = tk.Label(frame2, text="Welcome, Rizwan", fg="white",  bg="#594F4F", width=100, font=fontStyle)
lbl_title.pack(padx=5, pady=5)

display = tk.Frame(frame2, width=1024, bg="orange")
display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

f_txt = tk_font.Font(family="Lucida Grande", size=11)
txt_edit = tk.Text(frame2, width=150, font=f_txt)
txt_edit.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

show()

window.mainloop()
