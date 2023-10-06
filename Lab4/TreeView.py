from tkinter import ttk
import tkinter as tk

window = tk.Tk()
window.resizable(width = 1, height = 1)

treev = ttk.Treeview(window, selectmode ='browse')

treev.pack(side ='right')

verscrlbar = ttk.Scrollbar(window,
						orient ="vertical",
						command = treev.yview)

verscrlbar.pack(side ='right', fill ='x')

treev.configure(xscrollcommand = verscrlbar.set)

treev["columns"] = ("1", "2", "3")

treev['show'] = 'headings'

treev.column("1", width = 90, anchor ='c')
treev.column("2", width = 90, anchor ='se')
treev.column("3", width = 90, anchor ='se')

treev.heading("1", text ="Tên")
treev.heading("2", text ="Giới tính")
treev.heading("3", text ="Tuổi")


treev.insert("", 'end', text ="L1",
			values =("Dark", "Dark", "20"))
treev.insert("", 'end', text ="L2",
			values =("Lmao", "Lmao", "20"))
treev.insert("", 'end', text ="L3",
			values =("Bruh", "Bruh", "20"))

window.mainloop()
