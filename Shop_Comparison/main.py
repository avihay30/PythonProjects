import subprocess
import tkinter as tk


def run_rami_levi_script():
    subprocess.call('start /wait python rami_levi.py', shell=True)


def run_victory_script():
    subprocess.call('start /wait python victory.py', shell=True)


def run_shufersal_script():
    subprocess.call('start /wait python shufersal.py', shell=True)


def run_all_shops_script():
    subprocess.call('start /wait python all_shops.py', shell=True)



HEIGHT = 500
WIDTH = 500

root = tk.Tk()
root.resizable(False, False)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

root.title("השוואת סופרים")
# photo_icon = PhotoImage(file='images\cart-icon-clipart-4.png')
# root.iconphoto(False, 'images\cart-icon-clipart-4.png')
root.iconbitmap(r'images\cart-icon-clipart-4.ico')

background_image = tk.PhotoImage(file=r'images\cart-icon-clipart-4.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#424242', bd=5)
frame2 = tk.Frame(root, bg='#424242', bd=5)
frame3 = tk.Frame(root, bg='#424242', bd=5)
frame4 = tk.Frame(root, bg='#424242', bd=5)
frame.place(relx=0.80, rely=0.20, relwidth=0.17, relheight=0.1, anchor='n')
frame2.place(relx=0.60, rely=0.20, relwidth=0.17, relheight=0.1, anchor='n')
frame3.place(relx=0.40, rely=0.20, relwidth=0.17, relheight=0.1, anchor='n')
frame4.place(relx=0.58, rely=0.82, relwidth=0.35, relheight=0.1, anchor='n')

button = tk.Button(frame, text="שופרסל", font=40, command=lambda: run_shufersal_script())
button.place(relheight=1, relwidth=1)

button1 = tk.Button(frame2, text="רמי לוי", font=40, command=lambda: run_rami_levi_script())
button1.place(relheight=1, relwidth=1)

button2 = tk.Button(frame3, text="ויקטורי", font=40, command=lambda: run_victory_script())
button2.place(relheight=1, relwidth=1)

button3 = tk.Button(frame4, text="הרץ הכל", font=40, command=lambda: run_all_shops_script())
button3.place(relheight=1, relwidth=1)

root.mainloop()
