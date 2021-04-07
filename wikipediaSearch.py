import wikipedia as w
import pyttsx3
import tkinter as t
from tkinter import messagebox
from googlesearch import search
import webbrowser
root = t.Tk()
root.minsize(700,500)
def submit():
 name = entry1.get() # to get user name
 password = entry2.get() # to get user password
 print(name)
 print(password)
 if name == "nauyanika" and password == "thapa": # to check password is correct or not
  messagebox.showinfo('information',"login Successful") # for dialoge box
  login = t.Toplevel(root) # for login page
  login.minsize(800,750) # to set width and height
  login.title("Wikipedia Assistant System") # to set title
  #bg = t.PhotoImage(file = "mmmut.png") # to insert mmmut pic
  #l = t.Label(login,image=bg) # insert pic to login page
  #l.place(x=300,y=11) # to place image at x=300 and y=11
  # to set label in login page
  t.Label(login,text="Search your Topic",font=("Timesbold",15)).place(x=315,y=260)

  # to get search item
  e1=t.Entry(login,textvariable=t.StringVar())
  e1.place(x=325,y=300) # to place entry at x=325 and y=300

  def search1(): # search function
   item=e1.get() #to get search item
   w.set_lang('en') # set language in wikipedia
   result = w.summary(item,7) # get result from wikipedia
   data1['text']=""
   data1['text']=result # diplay result in empty label

  def hindi_search(): # search in hindi function
   item=e1.get() # to get search item
   w.set_lang('hi') # set language in wikipedia
   result = w.summary(item,5) # get result from wikipedia
   data1['text']=""
   data1['text']=result # display result in empty label

  def search_on_google(): # search on google function
   def callback(event): # search on web browser using link
    # web browser function
    webbrowser.open_new(event.widget.cget("text"))
   item = e1.get() # get search in item
   count = 10
   googlescreen = t.Toplevel(login) # google link page
   googlescreen.minsize(1080,500) # google page set height and width
   googlescreen.title("Website link") # set title for google link page
   # create label in google link page
   t.Label(googlescreen,text="Top 20 Links",font="Times 32").place(x=400,y=25)
   for j in search(item):
     link1 = t.Label(googlescreen, text=j, fg="blue", cursor="hand2")
     link1.place(x=1,y=50+count)
     link1.bind("<Button-1>",callback)
     count=count+20
   googlescreen.mainloop()
  def speak(): # speak function
   engine = pyttsx3.init() #initialize speak function in engine variable
   rate = engine.getProperty('rate') # getting details of current speaking rate
   print(rate) #printing current voice rate
   engine.setProperty('rate', 125)
   item=e1.get()
   w.set_lang("en")
   result = w.summary(item,3)
   engine.say(result)
   engine.runAndWait()
  data1 = t.Label(login,wraplength=700,fg="blue") # empty label
  data1.place(x=20,y=400) # set empty label in place x=20 and y=400
  # create button in login page
  b3 = t.Button(login,text="search in english",fg="blue",command=search1)
  b3.place(x=130,y=330) # set button in place x=130 and y=330
  #create button in login page
  b4 = t.Button(login,text="Search in hindi",fg="blue",command=hindi_search)
  b4.place(x=280,y=330) # set button in place x=280 and y=330
  #create button in login page
  b5 = t.Button(login,text="Search on google",fg="blue",command=search_on_google)
  b5.place(x=420,y=330) # set button in place x=420 and y=330
  #create button in login page
  b6 = t.Button(login,text="Search and Speak",fg="blue",command=speak)
  b6.place(x=580,y=330) # set button in place x=580,y=330
  login.mainloop() # main loop for login page
 else:
     # dialoge box for login failed
  messagebox.showerror('login failed',"Wrong Credential")

name_var = t.StringVar() # create variable type for user name
pass_var = t.StringVar() # create variable type for user password
#bg = t.PhotoImage(file = "wikipedia.png") # insert image of wikipedia
#l = t.Label(root,image=bg) # set wikipedia image in root page
#l.place(x=200,y=20) # set image in place x=200 and y=20
# create label in root
l0 = t.Label(root,text="Welcome to Wikipedia Assistant System. \n Please provide your credential to login",font=('Times bold',15))
l0.place(x=140,y=280) # set label in place x=140 and y=280
# create label in root
l1 = t.Label(root,text="User Name",font=('Times',18))
l1.place(x=250,y=380) # set label in place x=250 and y=380
# create entry for user name
entry1 = t.Entry(root,textvariable=name_var)
entry1.place(x=370,y=380) # set entry in place x=370 and y=380
# create label for password
l2 = t.Label(root,text="Password",font=('Times',18))
l2.place(x=250,y=420) # set label in place x=250 and y=420
# create entry for password which show *
entry2 = t.Entry(root,textvariable=pass_var,show='*')
entry2.place(x=370,y=420) # set entry in place x=370 and y=420
# create submit button
b1 = t.Button(root,text="Submit",command=submit)
b1.place(x=400,y=450) # set button in place x=400 and y=450
root.title("Wikipedia Assistant") # set title for root page
root.mainloop() # main loop for root page