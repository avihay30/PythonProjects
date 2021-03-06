import tkinter as tk
import webbrowser

hedva2_lecture = 'חדו"א 2 - הרצאה'
hedva2_practice = 'חדו"א 2 - תרגול'
introduction_lecture = "מבוא - הרצאה"
introduction_practice = "מבוא - תרגול"
adv_computer_science_lecture = 'מת"מ - הרצאה'
adv_computer_science_lab = 'מת"מ - מעבדה'
discrete_mathematics_lecture = "דיסקרטית - הרצאה"
discrete_mathematics_practice = "דיסקרטית - תרגול"
algebra2_lecture = "מבנים אלגברים - הרצאה"
algebra2_practice = "מבנים אלגברים - תרגול"

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

title = tk.Label(app, text="'לוח שעות - סמסטר ב", font='Helvetica 13 bold underline')
title.grid(row=0, column=2, sticky='E')

dayName = tk.Label(app, text="ראשון", font=day_font)
dayName.grid(row=1, column=5, padx=55)


dayName = tk.Label(app, text="שני", font=day_font)
dayName.grid(row=1, column=4, padx=55)
c2_first = tk.Button(app, text=introduction_practice, command=lambda: openweb(links[0]))
c2_first.grid(row=2, column=4, pady=10)
c2_second = tk.Button(app, text=hedva2_lecture, command=lambda: openweb(links[1]))
c2_second.grid(row=3, column=4, pady=10)
c2_third = tk.Button(app, text=adv_computer_science_lecture, command=lambda: openweb(links[2]))
c2_third.grid(row=4, column=4, pady=10)
c2_forth = tk.Button(app, text=adv_computer_science_lab, command=lambda: openweb(links[3]))
c2_forth.grid(row=5, column=4, pady=10)
c2_fifth = tk.Button(app, text=discrete_mathematics_practice, command=lambda: openweb(links[4]))
c2_fifth.grid(row=6, column=4, pady=10)

dayName = tk.Label(app, text="שלישי", font=day_font)
dayName.grid(row=1, column=3, padx=55)
c3_first = tk.Button(app, text=hedva2_practice, command=lambda: openweb(links[5]))
c3_first.grid(row=2, column=3, pady=10)
c3_second = tk.Button(app, text=hedva2_lecture, command=lambda: openweb(links[6]))
c3_second.grid(row=3, column=3, pady=10)
c3_third = tk.Button(app, text=discrete_mathematics_lecture, command=lambda: openweb(links[7]))
c3_third.grid(row=4, column=3, pady=10)

dayName = tk.Label(app, text="רביעי", font=day_font)
dayName.grid(row=1, column=2, padx=55)
c4_first = tk.Button(app, text=introduction_lecture, command=lambda: openweb(links[8]))
c4_first.grid(row=2, column=2, pady=10)

dayName = tk.Label(app, text="חמישי", font=day_font)
dayName.grid(row=1, column=1, padx=55)
c5_first = tk.Button(app, text=algebra2_lecture, command=lambda: openweb(links[9]))
c5_first.grid(row=2, column=1, pady=10)
c5_second = tk.Button(app, text=algebra2_practice, command=lambda: openweb(links[10]))
c5_second.grid(row=3, column=1, pady=10)

dayName = tk.Label(app, text="שישי", font=day_font)
dayName.grid(row=1, column=0, padx=55)
# c6_first = tk.Button(app, text="One")
# c6_first.grid(row=2, column=0)

app.mainloop()
