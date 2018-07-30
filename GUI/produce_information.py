import tkinter as tk
from tkinter import messagebox
import data
import produce_feature_table_function
import time

window = tk.Tk()
window.title('Encrypt Search')
window.resizable(False, False)
window.geometry('350x200')
#window.iconbitmap('D:\Icon.png')

def isDigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def produce_function():
    window.focus_set()
    if file_input.get() != "請輸入檔案名字" and isDigit(seed_input.get()):
        check_button.config(state="disabled")
        cancel_button.config(state="disabled")
        file_input.config(state="disabled")
        seed_input.config(state="disabled")
        state_label_2.config(text="開始轉換")
        start = time.time()
        message,succeed = data.convert_data(file_input.get())
        if succeed is False :
            state_label_2.config(text=message)
            check_button.config(state="normal")
            cancel_button.config(state="normal")
            file_input.config(state="normal")
            seed_input.config(state="normal")
            end = time.time()
            print("執行時間 : " + str(end - start))
            return
        message,succeed = produce_feature_table_function.produce(message,seed_input.get())
        state_label_2.config(text=message)
        check_button.config(state="normal")
        cancel_button.config(state="normal")
        file_input.config(state="normal")
        seed_input.config(state="normal")
        end = time.time()
        print("執行時間 : " + str(end - start))
        return
    else :
        messagebox.showinfo(title='Warning', message='請填完所有空格或格式錯誤')
	
def cancel_function():
    window.destroy()
	
def on_closing():
    window.focus_set()
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()

def hide_hint(event):
    global hint
    hint = event.widget.get()
    event.widget.delete(0,'end')

def show_hint(event):
    if event.widget.get() == '' :
        event.widget.insert(0,hint) 

name_label = tk.Label(window, 
    text='檔案名稱 :　',    # 标签的文字
    font=('Arial bold', 12),     # 字体和字体大小
    width=15, height=2  # 标签长宽
    )
name_label.place(x=20, y=10)

seed_label = tk.Label(window, 
    text='seed :　',    # 标签的文字
    font=('Arial bold', 12),     # 字体和字体大小
    width=15, height=2  # 标签长宽
    )
seed_label.place(x=35, y=50)

state_label = tk.Label(window, 
    text='狀態 :　',    # 标签的文字
    font=('Arial bold', 12),     # 字体和字体大小
    width=15, height=2  # 标签长宽
    )
state_label.place(x=38, y=90)

state_label_2 = tk.Label(window, 
    text='Inital',    # 标签的文字
    font=('Arial bold', 12),     # 字体和字体大小
    width=15, height=2  # 标签长宽
    )
state_label_2.place(x=130, y=90)

hint = ''

file_input = tk.Entry(window)
file_input.bind("<FocusIn>",hide_hint)
file_input.bind("<FocusOut>",show_hint)
file_input.insert(0,'請輸入檔案名字')
file_input.place(x=130, y=23)

seed_input = tk.Entry(window)
seed_input.bind("<FocusIn>",hide_hint)
seed_input.bind("<FocusOut>",show_hint)
seed_input.insert(0,'請輸入檔案seed')
seed_input.place(x=130, y=63)

check_button = tk.Button(window,text="確認",width=7,height=1,command=produce_function)
check_button.place(x=100, y=150)

cancel_button = tk.Button(window,text="取消",width=7,height=1,command=cancel_function)
cancel_button.place(x=200, y=150)

window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()
