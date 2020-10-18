import tkinter as tk
import webbrowser

hadva_lecture = 'חדו"א - הרצאה'
hadva_practice = 'חדו"א - תרגול'
algebra_lecture = 'אלגברה - הרצאה'
algebra_practice = 'אלגברה - תרגול'
computer_science_lecture = 'מל"מ - הרצאה'
computer_science_practice = 'מל"מ - תרגול'
computer_science_lab = 'מל"מ - מעבדה'
mahrachot_lecture = 'מערכות ספרתיות - הרצאה'
mahrachot_practice = 'מערכות ספרתיות - תרגול'
engineering_skills = 'מיומניות הנדסיות'
cinema = 'חינוך לקיימות דרך קולנוע'

day_font = 'Helvetica 9 underline bold'
filedict = {}
with open("urls.text") as myfile:
    for line in myfile:
        name, var = line.partition("=")[::2]
        filedict[name.strip()] = str(var.strip())

links = list(filedict.values())


def openweb(url):
    webbrowser.open_new(url)


app = tk.Tk()
f = tk.Frame(app)
app.title("לוח שעות")
background_image = tk.PhotoImage(file=r'white.png')
background_label = tk.Label(app, image=background_image)
background_label.place(relwidth=1, relheight=1)

app.wm_attributes("-transparentcolor", "white")

title = tk.Label(app, text="לוח שעות", font='Helvetica 13 bold underline')
title.grid(row=0, column=2, sticky='E')

dayName = tk.Label(app, text="ראשון", font=day_font)
dayName.grid(row=1, column=5, padx=50)


dayName = tk.Label(app, text="שני", font=day_font)
dayName.grid(row=1, column=4, padx=50)
c2_first = tk.Button(app, text=hadva_lecture, command=lambda: openweb(links[0]))
c2_first.grid(row=2, column=4)
c2_second = tk.Button(app, text=computer_science_lab, command=lambda: openweb(links[1]))
c2_second.grid(row=3, column=4)
c2_third = tk.Button(app, text=computer_science_practice, command=lambda: openweb(links[2]))
c2_third.grid(row=4, column=4)

dayName = tk.Label(app, text="שלישי", font=day_font)
dayName.grid(row=1, column=3, padx=50)
c3_first = tk.Button(app, text=computer_science_lecture, command=lambda: openweb(links[3]))
c3_first.grid(row=2, column=3)

dayName = tk.Label(app, text="רביעי", font=day_font)
dayName.grid(row=1, column=2, padx=50)
c4_first = tk.Button(app, text=hadva_lecture, command=lambda: openweb(links[4]))
c4_first.grid(row=2, column=2, pady=10)
c4_second = tk.Button(app, text=hadva_practice, command=lambda: openweb(links[5]))
c4_second.grid(row=3, column=2, pady=10)
c4_third = tk.Button(app, text=engineering_skills, command=lambda: openweb(links[6]))
c4_third.grid(row=4, column=2, pady=10)
c4_forth = tk.Button(app, text=mahrachot_practice, command=lambda: openweb(links[7]))
c4_forth.grid(row=5, column=2, pady=10)
c4_fifth = tk.Button(app, text=cinema, command=lambda: openweb(links[8]))
c4_fifth.grid(row=6, column=2, pady=10)

dayName = tk.Label(app, text="חמישי", font=day_font)
dayName.grid(row=1, column=1, padx=50)
c5_first = tk.Button(app, text=algebra_lecture, command=lambda: openweb(links[9]))
c5_first.grid(row=2, column=1)
c5_second = tk.Button(app, text=algebra_practice, command=lambda: openweb(links[10]))
c5_second.grid(row=3, column=1)
c5_third = tk.Button(app, text=mahrachot_lecture, command=lambda: openweb(links[11]))
c5_third.grid(row=4, column=1)

dayName = tk.Label(app, text="שישי", font=day_font)
dayName.grid(row=1, column=0, padx=50)
# c6_first = tk.Button(app, text="One")
# c6_first.grid(row=2, column=0)

app.mainloop()
