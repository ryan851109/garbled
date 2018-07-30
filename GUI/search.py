import tkinter as tk
from tkinter import messagebox
import compare_bit_function
import n_bit_counter_function
import key_convert_number_function
import hashlib

window = tk.Tk()
window.title('Encrypt Search')
window.resizable(False, False)
window.geometry('350x300')
#window.iconbitmap('D:\Icon.png')

def isDigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def search_function():
    window.focus_set()
    if search_input1.get() != '請輸入' and search_input2.get() != '請輸入' and search_input3.get() != '請輸入' and search_input4.get() != '請輸入' and search_input5.get() != '請輸入' and isDigit(seed_input.get()):
        search_result.delete(0,'end')
        check_button.config(state="disabled")
        cancel_button.config(state="disabled")
        search_input1.config(state="disabled")
        search_input2.config(state="disabled")
        search_input3.config(state="disabled")
        search_input4.config(state="disabled")
        search_input5.config(state="disabled")
        seed_input.config(state="disabled")
        feature_hash = ''
        for content in [search_input1.get(),search_input2.get(),search_input3.get(),search_input4.get(),search_input5.get()]:
            hash_value = hashlib.md5()
            hash_value.update(content.encode('utf-8'))
            feature_hash = feature_hash + (bin(int(hash_value.hexdigest()[-1],16))[-2:]).replace('b','0')
        message,succeed = compare_bit_function.compare(feature_hash,seed_input.get())
        if succeed is False :
            search_result.insert('end',message)
            check_button.config(state="normal")
            cancel_button.config(state="normal")
            search_input1.config(state="normal")
            search_input2.config(state="normal")
            search_input3.config(state="normal")
            search_input4.config(state="normal")
            search_input5.config(state="normal")
            seed_input.config(state="normal")
            return
        n_bit_counter_function.counter(seed_input.get())
        result = key_convert_number_function.key_convert()
        for result_position in range(len(result)) :
            search_result.insert('end',result[result_position])
        check_button.config(state="normal")
        cancel_button.config(state="normal")
        search_input1.config(state="normal")
        search_input2.config(state="normal")
        search_input3.config(state="normal")
        search_input4.config(state="normal")
        search_input5.config(state="normal")
        seed_input.config(state="normal")
        """
        state_label_2.config(text="開始轉換")
        message,succeed = produce_feature_table_function.produce(message,seed_input.get())
        if succeed is True :
            state_label_2.config(text=message)
            check_button.config(state="normal")
            cancel_button.config(state="normal")
            file_input.config(state="normal")
            seed_input.config(state="normal")
            return
        """
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

search_label1 = tk.Label(window, 
    text='檔案特徵1 :　',    # 标签的文字
    font=('Arial bold', 12),     # 字体和字体大小
    width=15, height=1  # 标签长宽
    )
search_label1.place(x=16, y=8)

search_label2 = tk.Label(window, 
    text='檔案特徵2 :　',    # 标签的文字
    font=('Arial bold', 12),     # 字体和字体大小
    width=15, height=1  # 标签长宽
    )
search_label2.place(x=16, y=30)

search_label3 = tk.Label(window, 
    text='檔案特徵3 :　',    # 标签的文字
    font=('Arial bold', 12),     # 字体和字体大小
    width=15, height=1  # 标签长宽
    )
search_label3.place(x=16, y=53)

search_label4 = tk.Label(window, 
    text='檔案特徵4 :　',    # 标签的文字
    font=('Arial bold', 12),     # 字体和字体大小
    width=15, height=1  # 标签长宽
    )
search_label4.place(x=16, y=75)

search_label5 = tk.Label(window, 
    text='檔案特徵5 :　',    # 标签的文字
    font=('Arial bold', 12),     # 字体和字体大小
    width=15, height=1  # 标签长宽
    )
search_label5.place(x=16, y=100)

seed_label = tk.Label(window, 
    text='seed :　',    # 标签的文字
    font=('Arial bold', 12),     # 字体和字体大小
    width=15, height=2  # 标签长宽
    )
seed_label.place(x=35, y=130)

state_label = tk.Label(window, 
    text='結果 :　',    # 标签的文字
    font=('Arial bold', 12),     # 字体和字体大小
    width=15, height=2  # 标签长宽
    )
state_label.place(x=38, y=170)

search_result_sb_y = tk.Scrollbar(window)
search_result_sb_y.pack(side=tk.RIGHT,fill=tk.Y)
search_result_sb_x = tk.Scrollbar(window, orient=tk.HORIZONTAL)
search_result_sb_x.pack(side=tk.BOTTOM,fill=tk.X)
search_result = tk.Listbox(window,width=25,height=3,yscrollcommand= search_result_sb_y.set,xscrollcommand= search_result_sb_x.set,highlightthickness = 0)
search_result.place(x=130, y=180)
search_result_sb_y.config(command=search_result.yview)
search_result_sb_x.config(command=search_result.xview)
#for i in ['1','2','3','4','5','6','7','8','9','10','11','12','13']:
    #search_result.insert('end',i)

hint = ''

search_input1 = tk.Entry(window)
search_input1.bind("<FocusIn>",hide_hint)
search_input1.bind("<FocusOut>",show_hint)
search_input1.insert(0,'請輸入')
search_input1.place(x=130, y=11)

search_input2 = tk.Entry(window)
search_input2.bind("<FocusIn>",hide_hint)
search_input2.bind("<FocusOut>",show_hint)
search_input2.insert(0,'請輸入')
search_input2.place(x=130, y=34)

search_input3 = tk.Entry(window)
search_input3.bind("<FocusIn>",hide_hint)
search_input3.bind("<FocusOut>",show_hint)
search_input3.insert(0,'請輸入')
search_input3.place(x=130, y=57)

search_input4 = tk.Entry(window)
search_input4.bind("<FocusIn>",hide_hint)
search_input4.bind("<FocusOut>",show_hint)
search_input4.insert(0,'請輸入')
search_input4.place(x=130, y=80)

search_input5 = tk.Entry(window)
search_input5.bind("<FocusIn>",hide_hint)
search_input5.bind("<FocusOut>",show_hint)
search_input5.insert(0,'請輸入')
search_input5.place(x=130, y=103)

seed_input = tk.Entry(window)
seed_input.bind("<FocusIn>",hide_hint)
seed_input.bind("<FocusOut>",show_hint)
seed_input.insert(0,'請輸入')
seed_input.place(x=130, y=143)

check_button = tk.Button(window,text="確認",width=7,height=1,command=search_function)
check_button.place(x=100, y=250)

cancel_button = tk.Button(window,text="取消",width=7,height=1,command=cancel_function)
cancel_button.place(x=200, y=250)

window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()