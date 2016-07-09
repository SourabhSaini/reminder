import os, re
import gi, time, notify2
import tkinter as tk
from tkinter import *
from gi.repository import Gtk, GLib
gi.require_version('AppIndicator3', '0.1')
gi.require_version('AppIndicator3', '0.1')
try: 
       from gi.repository import AppIndicator3 as AppIndicator  
except:  
       from gi.repository import AppIndicator

class Reminder():

	def __init__(self):
         self.ind = AppIndicator.Indicator.new("indicator-reminder","appointment-soon",AppIndicator.IndicatorCategory.APPLICATION_STATUS)
                          
         self.ind.set_icon_theme_path( os.getenv( "HOME" ) )

        # need to set this for indicator to be shown
         self.ind.set_status (AppIndicator.IndicatorStatus.ACTIVE)

        # have to give indicator a menu
         self.menu = Gtk.Menu()

        # you can use this menu item for experimenting
         item = Gtk.MenuItem()
         item.set_label("Add Reminder")
         item.connect("activate", lambda w: self.remNew(error=""))
         item.show()
         self.menu.append(item)

         self.menu.show()
         self.ind.set_menu(self.menu)
		
	def remAdd(self,hour,mins,title,note):
		
		if '#' in title:
			error = 'Invalid Character in "#" Title'
			window.destroy()
			self.remNew(error)
		elif '#' in note:
			error = 'Invalid Character "#" in Note'
			window.destroy()
			self.remNew(error)
		if title == "":
			error = 'Title can not be empty'
			window.destroy()
			self.remNew(error)
		elif note == "":
			error = 'Note can not be empty'
			window.destroy()
			self.remNew(error)
		elif int(hour) < 0 or int(hour) > 23:
			error = 'Invalid Hour'
			window.destroy()
			self.remNew(error)
		elif int(mins) < 0 or int(mins) > 59:
			error = 'Invalid Minutes'
			window.destroy()
			self.remNew(error)
		else:
			remFile = open('reminder','a')
			remFile.write(hour+':'+mins+'#'+title+'#'+note+'\n')
			remFile.close()
		
			window.destroy()
		
	def remNew(self,error):
		window=tk.Tk()
		window.title("Reminder")
		window.maxsize(width=200,height=120)
		window.minsize(width=200,height=120)
		
		title_lab = Label(window, text="TITLE")
		title_lab.place(x=2,y=2)
		title = Entry(window, bd = 1, width = 19)
		title.place(x=40,y=2)
		
		note_lab = Label(window, text="NOTE")
		note_lab.place(x=2,y=25)
		note = Entry(window, bd = 1, width = 19)
		note.place(x=40,y=25)
		
		time_lab = Label(window, text="TIME")
		time_lab.place(x=2,y=50)
		hour = Spinbox(window, from_ = 0, to = 23, width = 2)
		hour.place(x=80,y=50)
		dots = Label(window, text=":")
		dots.place(x=118,y=50)
		mins = Spinbox(window, from_ = 0, to = 59, width = 2)
		mins.place(x=130,y=50)
		
		error_lab = Label(window, text=error, fg='red', font=("Helvetica", 9))
		error_lab.place(x=2,y=71)

		add = tk.Button(text="ADD", fg="black",command=lambda: rem.remAdd(hour.get(),mins.get(),title.get(),note.get()))
		add.place(x=75,y=90)
		
		global window
		window.mainloop()
	
	def Main(self):
		
		Gtk.main()


if __name__ == "__main__":
	rem = Reminder()
	rem.Main()
	
