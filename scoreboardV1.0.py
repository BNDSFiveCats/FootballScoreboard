import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import threading
import time

# 初始化比分和时间
team1_score = 0
team2_score = 0
current_time = 0
is_running = False
team1_name = "Team 1"
team2_name = "Team 2"

# 创建更新比分和时间的函数
def update_display():
    team1_label.config(text=f"{team1_name}")
    score_label.config(text=f"{team1_score} : {team2_score}")
    team2_label.config(text=f"{team2_name}")

def update_timer_label():
    minutes = current_time // 60
    seconds = current_time % 60
    timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
    if is_running:
        root.after(1000, update_timer_label)

# 创建加分函数
def add_score(team):
    global team1_score, team2_score
    if team == 1:
        team1_score += 1
    elif team == 2:
        team2_score += 1
    update_display()

# 创建计时函数
def start_stop_timer():
    global is_running
    if is_running:
        is_running = False
        start_stop_button.config(text="Start")
    else:
        is_running = True
        start_stop_button.config(text="Pause")
        update_timer()

# 更新计时器
def update_timer():
    global current_time
    if is_running:
        current_time += 1
        update_timer_label()
        root.after(1000, update_timer)
    else:
        start_stop_button.config(text="Start")

# 创建设置时间函数
def set_time():
    global current_time
    new_time = int(entry.get())
    current_time = new_time
    entry.delete(0, tk.END)
    update_display()

# 创建函数以在窗口内输入队伍名称
def enter_team_names():
    global team1_name, team2_name
    team1_name = team1_name_entry.get()
    team2_name = team2_name_entry.get()
    update_display()

# 创建主窗口
root = tk.Tk()
root.title("Football Scoreboard")

# 使用ttk样式
style = ttk.Style()
style.configure("TButton", padding=5, font=("Helvetica", 12))
style.configure("TLabel", font=("Helvetica", 14))

# 创建比分和时间窗口
score_window = tk.Toplevel(root)
score_window.title("Score and Timer")

# 背景图片
desired_size = (150, 30) 
score_size = (60, 30) 
team1_image = Image.open("team1.png")
team1_image = team1_image.resize(desired_size, Image.Resampling.NEAREST)
team1_photo = ImageTk.PhotoImage(team1_image)
score_image = Image.open("score.png")
score_image = score_image.resize(score_size, Image.Resampling.NEAREST)
score_photo = ImageTk.PhotoImage(score_image)
team2_image = Image.open("team2.png")
team2_image = team2_image.resize(desired_size, Image.Resampling.NEAREST)
team2_photo = ImageTk.PhotoImage(team2_image)
timer_image = Image.open("timer.png")
timer_image = timer_image.resize(score_size, Image.Resampling.NEAREST)
timer_photo = ImageTk.PhotoImage(timer_image)

# 创建比分和时间标签
team1_label = ttk.Label(score_window, text=f"{team1_name}",image=team1_photo, compound="center")
score_label = ttk.Label(score_window, text=f"0 : 0", image=score_photo, compound="center")
team2_label = ttk.Label(score_window, text=f"{team2_name}", image=team2_photo, compound="center")
timer_label = ttk.Label(score_window, text="00:00", image=timer_photo, compound="center")
team1_label.grid(row=0, column=0)
score_label.grid(row=0, column=1)
team2_label.grid(row=0, column=2)
timer_label.grid(row=0, column=3)#, columnspan=2

# 修改特定Label的字体颜色
team1_label.config(foreground="black")
team2_label.config(foreground="black")

# 创建按钮和输入框
start_stop_button = ttk.Button(root, text="Start", command=start_stop_timer)
add_team1_button = ttk.Button(root, text=f"{team1_name} +1", command=lambda: add_score(1))
add_team2_button = ttk.Button(root, text=f"{team2_name} +1", command=lambda: add_score(2))
set_time_button = ttk.Button(root, text="Set Time", command=set_time)
entry = ttk.Entry(root)
team1_name_label = ttk.Label(root, text=f"{team1_name}:", style="TLabel")
team2_name_label = ttk.Label(root, text=f"{team2_name}:", style="TLabel")

# 显示按钮和输入框
start_stop_button.grid(row=2, column=0, columnspan=2)
add_team1_button.grid(row=3, column=0)
add_team2_button.grid(row=3, column=1)
entry.grid(row=4, column=0, columnspan=2)
set_time_button.grid(row=5, column=0, columnspan=2)
team1_name_label.grid(row=6, column=0)
team2_name_label.grid(row=6, column=1)

# 创建输入队伍名称的文本框和确认按钮
team1_name_entry = ttk.Entry(root)
team2_name_entry = ttk.Entry(root)
update_team_names_button = ttk.Button(root, text="Update Team Names", command=enter_team_names)
team1_name_entry.grid(row=7, column=0)
team2_name_entry.grid(row=7, column=1)
update_team_names_button.grid(row=8, column=0, columnspan=2)

# 启动程序
root.mainloop()
