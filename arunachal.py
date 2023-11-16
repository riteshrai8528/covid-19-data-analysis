import tkinter as tk
from tkinter import *
from tkinter import Tk
import os
import json
import requests
import pandas as pd
import matplotlib.pyplot as plt

root = Tk()
root.geometry("1440x1440")
root.config(bg="sky blue")
root.title("Arunachal Pradesh")

pic0 = PhotoImage(file='COVID.png')
labelphoto = Label(root, image = pic0, )
labelphoto.pack(pady=30)



pic = PhotoImage(file='STATS 2.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.iconbitmap(r'virus.ico')
    os.system('python arunast.py')
    top.destroy()

btn1 = Button(
    root,
    image=pic,
    border=0,
    command=open


)
btn1.pack(pady=30)

pic1 = PhotoImage(file='GRAPH 2.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.iconbitmap(r'virus.ico')
    os.system('python arungraph.py')
    top.destroy()

btn2 = Button(
    root,
    image=pic1,
    bd = 0,
    command=open
)
btn2.pack(pady=30)

pic3 = PhotoImage(file='HOSPITAL 2.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.iconbitmap(r'virus.ico')
    os.system('python arunachalhospital.py')
    top.destroy()
btn3 = Button(
    root,
    image=pic3,
    bd = 0,
    command=open


)
btn3.pack(pady=30)

pic4 = PhotoImage(file='Useful.png')
def open():
    top = Toplevel()
    top.geometry("1440x1440")
    top.iconbitmap(r'virus.ico')
    os.system('python arunachallinks.py')
    top.destroy()
btn4 = Button(
    root,
    image=pic4,
    bd = 0,
    command=open
)
btn4.pack(pady=30)
btn = Button(root, text="Back", command=root.destroy, ).pack()
root.mainloop()
root.mainloop()

url = "https://api.covid19india.org/state_district_wise.json"


# function to get data from api


def casesData():
    # getting the json data by calling api
    data = ((requests.get(url)).json())
    states = []

    # getting states
    for key in data.items():
        states.append(key[0])

    # getting statewise data

    for state in states:
     if state =='Goa':
        f = (data[state]['districtData'])
        tc = []
        dis = []
        act, con, dea, rec = 0, 0, 0, 0

        # getting districtwise data
        for key in (data[state]['districtData']).items():
            district = key[0]
            dis.append(district)
            active = data[state]['districtData'][district]['active']
            confirmed = data[state]['districtData'][district]['confirmed']
            deaths = data[state]['districtData'][district]['deceased']
            recovered = data[state]['districtData'][district]['recovered']
            if district == 'Unknown':
                active, confirmed, deaths, recovered = 0, 0, 0, 0
            tc.append([active, confirmed, deaths, recovered])
            act = act + active
            con = con + confirmed
            dea = dea + deaths
            rec = rec + recovered
        tc.append([act, con, dea, rec])
        dis.append('Total')
        parameters = ['Active', 'Confirmed', 'Deaths', 'Recovered']

        # creating a dataframe
        df = pd.DataFrame(tc, dis, parameters)
        print('COVID - 19', state, 'District Wise Data')
        print(df)
        df.to_csv('df.csv')




# Driver Code
casesData()