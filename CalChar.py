import tkinter as tk

# Def The Fun
def counting():
	# OutPut Delete
    output.delete(0.0,"end")
    # Input
    i=inputing.get(0.0,"end")
    # Results
    sp=result.get()
    # Define loops 
    c=0
    if sp==1:
        for k in i:
            if k=="\n":
                continue
            c=c+1
    elif sp==2:
        for k in i:
            if k==" " or k=="\n":
                continue
            c=c+1

    output.insert(tk.INSERT,c)
root=tk.Tk()
# Title
root.title("Count Characters")
# Size
root.geometry("300x250")

label=tk.Label(root,text="Input your Text")

#Input
inputing=tk.Text(root,width=30,height=5,font=(15),wrap="word")
result=tk.IntVar()

# Define Options
r1=tk.Radiobutton(root,text="with spaces",value=1,variable=result)
r2=tk.Radiobutton(root,text="without spaces",value=2,variable=result)

# counting Button
button=tk.Button(root,text="Show Results",command=counting)

label2=tk.Label(root,text="Result")

# Output size
output=tk.Text(root,width=10,height=1,font=(15),wrap="word")

label.pack()
inputing.pack()
r1.pack()
r2.pack()
label2.pack()
output.pack()
button.pack()

root.mainloop()