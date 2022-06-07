import csv
import os

import requests
from tkinter import *
import matplotlib.pyplot as plt

#test
#extragere date
filesize = os.path.getsize("Proiectlp2.txt")
if filesize == 0:
    URL = "https://data.primariatm.ro/dataset/8dd25f96-0e3f-4624-8565-a8d2183d27ce/resource/bb0189fd-2d87-4db1-a6cd-9ef2c71d7450/download/cai-aeriene-transport-aerian.csv"
    with requests.Session() as s:
           download = s.get(URL)
           decoded_content = download.content.decode('utf-8')
           cr = csv.reader(decoded_content.splitlines(), delimiter=',')
           matrix_data = list(cr)
    #salvare date in fisier
    file_string = ""
    python_file = open("Proiectlp2.txt", "w", encoding='utf')
    for i in range(len(matrix_data)):
        for j in range(len(matrix_data[0])):
            matrix_data[i][j] = matrix_data[i][j].replace(',', '.')
            matrix_data[i][j] = matrix_data[i][j].replace('.', '')
            file_string = file_string + matrix_data[i][j]
            file_string = file_string + ","
        file_string = file_string + "\n"
    python_file.write(file_string)
    python_file.close()
else:
    with open('Proiectlp2.txt', encoding='utf') as f:
        lines = f.readlines()
        matrix_data = [[" " for _ in range(3)] for _ in range(len(lines))]
        for i in range(len(lines)):
            data = lines[i].split(",")
            for j in range(len(data)-1):
                matrix_data[i][j] = data[j]

#initialize tkinter
root=Tk()
menu = Menu(root)
root.config(menu=menu)
root.title("Căi Aeriene,Transport Aerian")

filemenu = Menu(menu)
menu.add_cascade(label='Indicator', menu=filemenu)
#afisare Miscari aeronave
def afisare1():
    root = Tk()
    menu = Menu(root)
    root.config(menu=menu)
    root.title("Miscari aeronave")
    for i in range(1):
        for j in range(3):
           entry = Entry(root, width=40, bg='green', fg='white', font=('Times New Roman', 8, ''))
           entry.grid(row=i, column=j)
           entry.insert(END, matrix_data[i][j])
    for i in range(29,43):
        for j in range(len(matrix_data[0])):
            entry = Entry(root, width=40, bg='white', fg='black', font=('Times New Roman', 8, ''))
            entry.grid(row=i, column=j)
            if j==1:
               entry.insert(END, matrix_data[i][j][:4])
            else:
               entry.insert(END, matrix_data[i][j])
    root.mainloop()
#afisare Numar total de marfuri transport aerian
def afisare2():
    root = Tk()
    menu = Menu(root)
    root.config(menu=menu)
    root.title("Numar total de marfuri transport aerian")
    for i in range(1):
        for j in range(3):
           entry = Entry(root, width=40, bg='green', fg='white', font=('Times New Roman', 8, ''))
           entry.grid(row=i, column=j)
           entry.insert(END, matrix_data[i][j])
    for i in range(15,29):
        for j in range(len(matrix_data[0])):
            entry = Entry(root, width=40, bg='white', fg='black', font=('Times New Roman', 8, ''))
            entry.grid(row=i, column=j)
            if j==1:
               entry.insert(END, matrix_data[i][j][:4])
            else:
               entry.insert(END, matrix_data[i][j])
    root.mainloop()
#afisare Numar pasageri
def afisare3():
    root = Tk()
    menu = Menu(root)
    root.config(menu=menu)
    root.title("Numar pasageri")
    for i in range(1):
        for j in range(3):
           entry = Entry(root, width=40, bg='green', fg='white', font=('Times New Roman', 8, ''))
           entry.grid(row=i, column=j)
           entry.insert(END, matrix_data[i][j])
    for i in range(1,15):
        for j in range(len(matrix_data[0])):
            entry = Entry(root, width=40, bg='white', fg='black', font=('Times New Roman', 8, ''))
            entry.grid(row=i, column=j)
            if j==1:
               entry.insert(END, matrix_data[i][j][:4])
            else:
               entry.insert(END, matrix_data[i][j])
    root.mainloop()
filemenu.add_command(label='Miscari aereonave',command=afisare1)
filemenu.add_command(label='Numar total de marfuri transport aerian',command=afisare2)
filemenu.add_command(label='Numar pasageri',command=afisare3)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
# Afisare Grafic Numar pasageri
def graph1():


    # x axis values
    x= [float(matrix_data[1][2]), float(matrix_data[2][2]), float(matrix_data[3][2]), float(matrix_data[4][2]), float(matrix_data[5][2]),float(matrix_data[6][2]),float(matrix_data[7][2]),float(matrix_data[8][2]),
        float(matrix_data[9][2]), float(matrix_data[10][2]), float(matrix_data[11][2]), float(matrix_data[12][2]), float(matrix_data[13][2]),float(matrix_data[14][2])]
    # corresponding y axis values
    y = [float(matrix_data[1][1][:4]), float(matrix_data[2][1][:4]), float(matrix_data[3][1][:4]), float(matrix_data[4][1][:4]), float(matrix_data[5][1][:4]),float(matrix_data[6][1][:4]),
        float(matrix_data[7][1][:4]), float(matrix_data[8][1][:4]), float(matrix_data[9][1][:4]), float(matrix_data[10][1][:4]), float(matrix_data[11][1][:4]), float(matrix_data[12][1][:4]),
         float(matrix_data[13][1][:4]), float(matrix_data[14][1][:4])]


    # plotting the points
    plt.plot(y, x, color='green', linestyle='dashed', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=12)

    # naming the x axis
    plt.xlabel('Ani')
    # naming the y axis
    plt.ylabel('Valoare')

    # giving a title to my graph
    plt.title('Numar pasageri')

    # function to show the plot
    plt.show()
# afisare grafic miscari aeronave
def graph2():


    # x-coordinates of left sides of bars
    x = [float(matrix_data[29][2]), float(matrix_data[30][2]), float(matrix_data[31][2]), float(matrix_data[32][2]), float(matrix_data[33][2]), float(matrix_data[34][2]), float(matrix_data[35][2]),
         float(matrix_data[36][2]), float(matrix_data[37][2]), float(matrix_data[38][2]), float(matrix_data[39][2]), float(matrix_data[40][2]), float(matrix_data[41][2]), float(matrix_data[42][2])]
    # heights of bars
    y =[float(matrix_data[29][1][:4]), float(matrix_data[30][1][:4]), float(matrix_data[31][1][:4]), float(matrix_data[32][1][:4]), float(matrix_data[33][1][:4]), float(matrix_data[34][1][:4]),
        float(matrix_data[35][1][:4]), float(matrix_data[36][1][:4]), float(matrix_data[37][1][:4]), float(matrix_data[38][1][:4]), float(matrix_data[39][1][:4]), float(matrix_data[40][1][:4]),
        float(matrix_data[41][1][:4]), float(matrix_data[42][1][:4])]

    # plotting a bar chart
    plt.plot(y, x, color='green', linestyle='dashed', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=12)

    # naming the x-axis
    plt.xlabel('Ani')
    # naming the y-axis
    plt.ylabel('Valoare')
    # plot title
    plt.title('Miscari aeronave')

    # function to show the plot
    plt.show()
# afisare grafic numar total marfuri transport aerian
def graph3():

    # x axis values
    x = [float(matrix_data[15][2]), float(matrix_data[16][2]), float(matrix_data[17][2]), float(matrix_data[18][2]),
         float(matrix_data[19][2]), float(matrix_data[20][2]), float(matrix_data[21][2]), float(matrix_data[22][2]),
         float(matrix_data[23][2]), float(matrix_data[24][2]), float(matrix_data[25][2]), float(matrix_data[26][2]),
         float(matrix_data[27][2]), float(matrix_data[28][2])]
    # corresponding y axis values
    y = [float(matrix_data[15][1][:4]), float(matrix_data[16][1][:4]), float(matrix_data[17][1][:4]),
         float(matrix_data[18][1][:4]), float(matrix_data[19][1][:4]), float(matrix_data[20][1][:4]),
         float(matrix_data[21][1][:4]), float(matrix_data[22][1][:4]), float(matrix_data[23][1][:4]),
         float(matrix_data[24][1][:4]), float(matrix_data[25][1][:4]), float(matrix_data[26][1][:4]),
         float(matrix_data[27][1][:4]), float(matrix_data[28][1][:4])]

    # plotting the points
    plt.plot(y, x, color='green', linestyle='dashed', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=12)

    # naming the x axis
    plt.xlabel('Ani')
    # naming the y axis
    plt.ylabel('Valoare')

    # giving a title to my graph
    plt.title('Numar pasageri')

    # function to show the plot
    plt.show()

data = Menu(menu)
menu.add_cascade(label="Grafic",menu=data)
data.add_command(label="Afisare grafic Numar pasageri",command=graph1)
data.add_command(label="Afisare grafic Miscari aeronave",command=graph2)
data.add_command(label="Afisare grafic numar total marfuri transport aerian",command=graph3)

def media1():
    #interfata tkinker afisare medie
    from tkinter import ttk
    #def callback():
        #l2.configure(text=cmb.get())

    window = Tk()
    window.title('Media valori')
    window.geometry('300x200')
    nr1="Numar pasageri"
    nr2="Numar total marfuri transport aerian"
    nr3="Miscari aeronave"
    course = [nr1,nr2,nr3]

    l1 = Label(window, text="Alege un indicator")
    l1.grid(column=0, row=0)
    cmb = ttk.Combobox(window, values=course, width=30)
    cmb.grid(column=0, row=1)
    cmb.current(0)
    #numar pasageri
    def media_p():
        s = 0
        for i in range(1, 16):
            s = s + int(matrix_data[i][2])
        return float(s/14)
    #numar total marfuri
    def media_m():
        s = 0
        for i in range(15, 29):
            s = s + int(matrix_data[i][2])
        return float(s / 14)
    #miscari aeronave
    def media_a():
        s = 0
        for i in range(29, 43):
            s = s + int(matrix_data[i][2])
        return float(s / 14)

    def med():
         l2 = Label(window, text="                                        ")
         l2.grid(column=0, row=3)

         if cmb.get() == nr1:
                l2 = Label(window,text=(media_p()))
                l2.grid(column=0, row=3)
         if cmb.get() == nr2:
                l2 = Label(window, text=(media_m()))
                l2.grid(column=0, row=3)
         if cmb.get() == nr3:
                l2 = Label(window, text=(media_a()))
                l2.grid(column=0, row=3)

    btn = Button(window, text="Afiseaza media valorilor",command=med)
    btn.grid(column=0, row=2)

    window.mainloop()

media = Menu(menu)
menu.add_cascade(label="Media valorilor",menu=media)
media.add_command(label="Afisare media valorilor in functie de indicator",command=media1)
#show data in a table  && replace , with . and replace . with " "
for i in range(len(matrix_data)):
    for j in range(len(matrix_data[0])):
        matrix_data[i][j] = matrix_data[i][j].replace(',', '.')
        matrix_data[i][j] = matrix_data[i][j].replace('.', '')
        if i == 0:
            entry = Entry(root, width=40, bg='green', fg='white', font=('Times New Roman', 8, 'bold'))
        else:
            entry = Entry(root, width=40, bg='white', fg='black', font=('Times New Roman', 8, ''))
        entry.grid(row=i, column=j)
        entry.insert(END, matrix_data[i][j])
root.mainloop()
