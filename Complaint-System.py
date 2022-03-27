from tkinter import*
root=Tk()
root.geometry("500x300")


Label(root, text="Register Your Complaint Here", font="arial 15 bold"). grid(row=0, column=3)
name= Label(root,text='Name')
acntno= Label(root,text='Account Number')
phno= Label(root,text='Phone Number')
cd= Label(root,text='Complaint Details')
dp= Label(root,text='Department')

name.grid(row=1, column=2)
acntno.grid(row=2, column=2)
phno.grid(row=3, column=2)
cd.grid(row=4, column=2)
dp.grid(row=5, column=2)

namevalue= StringVar
acntnovalue=StringVar
phnovalue= IntVar
cdvalue= StringVar
dpvalue= StringVar
checkvalue=IntVar

nameentry= Entry(root, textvariable= namevalue)
acntnoentry= Entry(root, textvariable= acntnovalue)
phnoentry= Entry(root, textvariable= phnovalue)
cdentry= Entry(root, textvariable= cdvalue)
dpentry= Entry(root, textvariable= dpvalue)

nameentry.grid(row=1, column=3)
acntnoentry.grid(row=2, column=3)
phnoentry.grid(row=3, column=3)
cdentry.grid(row=4, column=3)
dpentry.grid(row=5, column=3)





root.mainloop()