from tkinter import *
from tkinter import ttk
import requests
win=Tk()
win.geometry('550x550')
win.config(bg="black")
win.title("Weather App")


head=Label(win, text='How Crazy Is The Weather Now?',
      font='arial 15 bold',bg="black",fg="white") 
head.place(x=130,y=30)

statelist=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
city=StringVar()
select=ttk.Combobox(win,text="Vijayawada",values=statelist,font=('Kozuka Gothic Pro M',10,"normal"),textvariable=city)
select.insert(0,"Vijayawada")
select.place(y=90,height=20,width=250,x=170)


req=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+str(city)+"&appid="+"e2aae2e910118cb474b82b10211a93fc").json()

def cheppey_mowa():
	req=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+(city.get())+"&appid="+"e2aae2e910118cb474b82b10211a93fc").json()
	
	
	
	a1.config(text='City',font='arial 15 bold',bg="#03fc03",fg="black")
	a11.config(text=city.get(),font='arial 24 bold',fg="#03fc03",bg="black")
	
	
	a2.config(text='Weather',font='arial 15 bold',bg="#03fc03",fg="black")
	
	a21.config(text=str(req["weather"][0]["main"]),font='arial 17 bold',fg="#03fc03",bg="black")
	
	
	a3.config(text='Temperature',font='arial 15 bold',bg="#03fc03",fg="black")
	
	a31.config(text=round(int(req["main"]["temp"])-273.15,2),font='arial 17 bold',fg="#03fc03",bg="black")
	
	
	a4.config(text='Pressure',font='arial 15 bold',bg="#03fc03",fg="black")
	
	a41.config(text=str(req["main"]["pressure"]),font='arial 17 bold',fg="#03fc03",bg="black")

	a5.config(text='Humidity',font='arial 15 bold',bg="#03fc03",fg="black")
	a51.config(text=str(req["main"]["humidity"]),font='arial 17 bold',fg="#03fc03",bg="black")

	print(req)			#This is for my compiler
	

a1=Label(win) 
a1.place(x=100,y=150)
a11=Label(win) 
a11.place(x=350,y=150)

a2=Label(win) 
a2.place(x=100,y=200)
a21=Label(win) 
a21.place(x=350,y=200)

a3=Label(win) 
a3.place(x=100,y=250)
a31=Label(win) 
a31.place(x=350,y=250)

a4=Label(win) 
a4.place(x=100,y=300)
a41=Label(win) 
a41.place(x=350,y=300)

a5=Label(win) 
a5.place(x=100,y=350)
a51=Label(win) 
a51.place(x=350,y=350)


reveal=Button(win,text="Reveal daa",font=('Kozuka Gothic Pro M',20,"bold"),bg="#03fc03",fg="black",command=cheppey_mowa)
reveal.place(x=200,y=470,height=30,width=170)



win.mainloop()
