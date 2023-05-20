from tkinter import *
from tkinter import messagebox as msgbox
from PIL import ImageTk, Image
import webbrowser
import time

root = Tk()
root.title('Elementopeia')

#Geomtry Difining
width_value= root.winfo_screenwidth()
height_value= root.winfo_screenheight()
#root.geometry("%dx%d+0+0"%(width_value,height_value))
root.geometry('1366x768')

#Dictionary of Elements
elements_dict = {
	'Hydrogen' : ('h',3,1),
	'Helium ' : ('he', 3,18),
	'Lithium' :('li', 4,1) ,
	'Berrylium' : ('be', 4,2),
	'Boron' : ('b', 4,13) ,
	'Carbon' :('c', 4,14),
	'Nitrogen' : ('n', 4,15),
	'Oxygen' : ('o', 4,16),
	'Fluorine' : ('f', 4,17),
	'Neon' : ('ne', 4,18),
	'Sodium': ('na', 5, 1),
    'Magnesium': ('mg', 5, 2),
    'Aluminium': ('al', 5, 13),
    'Silicon': ('si', 5, 14),
    'Phosphorus': ('p', 5, 15),
    'Sulphur': ('s', 5, 16),
    'Chlorine': ('cl', 5, 17),
    'Argon': ('ar', 5, 18),
    'Potassium': ('k', 6, 1),
    'Calcium': ('ca', 6, 2),
    'Scandium': ('sc', 6,3),
    'Titanium': ('ti', 6, 4),
    'Vanadium': ('v', 6, 5),
    'Chromium': ('cr', 6, 6),
    'Manganese': ('mn', 6, 7),
    'Iron': ('fe',6, 8),
    'Cobalt': ('co', 6, 9),
    'Nickel': ('ni', 6, 10),
    'Copper': ('cu', 6, 11),
    'Zinc': ('zn', 6, 12),
    'Gallium': ('ga', 6, 13),
    'Germanium': ('ge', 6, 14),
    'Arsenic': ('as', 6, 15),
    'Selenium': ('se', 6, 16),
    'Bromine': ('br', 6, 17),
    'Krypton': ('kr', 6, 18),
    'Rubidium': ('rb', 7, 1),
    'Strontium': ('sr', 7, 2),
    'Yttrium': ('yt', 7, 3),
    'Zirconium': ('zr', 7, 4),
    'Niobium': ('nb', 7, 5),
    'Molybdenum': ('mo', 7, 6),
    'Technetium': ('tc', 7, 7),
    'Ruthenium': ('ru', 7, 8),
    'Rhodium': ('rh', 7, 9),
    'Palladium': ('pd', 7, 10),
    'Silver': ('ag', 7, 11),
    'Cadmium': ('cd', 7, 12),
    'Indium': ('in', 7, 13),
    'Tin': ('sn', 7, 14),
    'Antimony': ('sb', 7, 15),
    'Tellurium': ('te', 7, 16),
    'Iodine': ('i', 7, 17),
    'Xenon': ('xe', 7, 18),
    'Cesium': ('cs', 8, 1),
    'Barium': ('ba', 8, 2),
    'Hafnium': ('hf', 8, 4),
    'Tantalum': ('ta', 8, 5),
    'Tungsten': ('w', 8, 6),
    'Rhenium': ('re', 8, 7),
    'Osmium': ('os', 8, 8),
    'Iridium': ('ir', 8, 9),
    'Platinum': ('pt', 8, 10),
    'Gold': ('au', 8, 11),
    'Mercury': ('hg', 8, 12),
    'Thalium': ('tl', 8, 13),
    'Lead': ('pb', 8, 14),
    'Bismuth': ('bi', 8, 15),
    'Polonium': ('po', 8, 16),
    'Astatine': ('at', 8, 17),
	'Radon': ('rn', 8, 18),	
	'Francium': ('fr', 9, 1),
	'Radium': ('ra', 9, 2),
	'Rutherfordium': ('rf', 9, 4),
	'Dubnium': ('db', 9, 5),
	'Seaborgium': ('sg', 9, 6),
	'Bohrium': ('bh', 9, 7),
	'Hasslum': ('hs', 9, 8),
	'Meltnerium': ('mt', 9, 9),
	'Darmstadtium': ('ds', 9, 10),
	'Roentegenium': ('rg', 9, 11),
	'Copernicium': ('cn', 9, 12),
	'Nihonium': ('nh', 9, 13),
	'Flerovlum': ('fl', 9, 14),
	'Moscovium': ('mc', 9, 15),
	'Livermorium': ('lv', 9, 16),
	'Tennessine': ('ts', 9, 17),
	'Oganesson': ('og', 9, 18),

	'Lanthanum' : ('la', 11, 3),
	'Cerium' : ('ce', 11, 4),
	'Praseodynium' : ('pr', 11, 5),
	'Neodynium' : ('nd', 11, 6),
	'Promethium' : ('pm', 11, 7),
	'Samarium' : ('sm', 11, 8),
	'Europhium' : ('eu', 11, 9),
	'Gadolinium' : ('gd', 11, 10),
	'Terbium' : ('tb', 11, 11),
	'Dysprosium' : ('dy', 11, 12),
	'Holmium' : ('ho', 11, 13),
	'Erbium' : ('er', 11, 14),
	'Thulium' : ('tm', 11, 15),
	'Ytterbium' : ('yb', 11, 16),
	'Lutetium' : ('lu', 11, 17),
	'Actinium' : ('ac', 12, 3),
	'Thorium' : ('th', 12, 4),
	'Protactinium' : ('pa', 12, 5),
	'Uranium' : ('u', 12, 6),
	'Neptunium' : ('np', 12, 7),
	'Plutonium' : ('pu', 12, 8),
	'Americium' : ('am', 12, 9),
	'Curium' : ('cm', 12, 10),
	'Berkelium' : ('bk', 12, 11),
	'Californium' : ('cf', 12, 12),
	'Einsteinium' : ('es', 12, 13),
	'Fermium' : ('fm', 12, 14),
	'Mendelevium' : ('md', 12, 15),
	'Nobelium' : ('no', 12, 16),
	'Lawrencium' : ('lr', 12, 17)

}

global elements

elements = list(elements_dict.keys())
for i in range(len(elements)):
	elements[i] = elements[i].lower()

#Images of Elements
big_images = {}
small_images = {}
for i in elements_dict :
	if i == 'Lanthnoids' or i == 'Actinoids':
		continue
	big_images[i] = Image.open('Images/' + elements_dict[i][0] + '.png')
	small_images[i] = ImageTk.PhotoImage(Image.open('Images/' + elements_dict[i][0] + '.png').resize((67,60), Image.ANTIALIAS))
#Defining functions for element buttons

new = 0

def wiki(elem_name):
	webbrowser.open('https://en.wikipedia.org/wiki/' + str(elem_name),new=new)

def elementopia(elem_name):
	pass

def popup_noresults(search_term): 
	response = msgbox.showinfo('No Results', 'Sorry, The element you seacrhed for (' + search_term + ') does not exist')
	if response != None:
		search_txt.delete(0, 'end')

def enable_but (elem_name):
	for i in elements_buttons:
		elements_buttons[i].config(state = 'active')
		new_win.destroy()

def onclick(elem_name, elem_pic):
	global new_win
	new_win = Toplevel()
	new_win.title(elem_name)
	
	#Once a button is pressed, it gets disabled
	elements_buttons[elem_name].config(state = DISABLED)
	
	#Button reanbles when the window is closed	
	new_win.bind("<Destroy>", lambda event: enable_but(elem_name))

	elem_pic = ImageTk.PhotoImage(elem_pic)
	#Defining the element picture labels and buttons
	pic_label = Label(new_win, image = elem_pic)
	elem_but1 = Button(new_win, text = 'Go to Elementopeia of:\n' + str(elem_name), command = lambda : elementopia(elem_name))
	elem_but2 = Button(new_win, text = 'Go to wiki of:\n'+ str(elem_name), command = lambda : wiki(elem_name))

	#Placing the new labels and buttons on the new window
	pic_label.grid(row = 0, column = 0,  columnspan = 2)
	elem_but1.grid(row = 1, column = 0, ipadx = 5, ipady = 3, padx = 3, pady = 3)
	elem_but2.grid(row = 1, column = 1, ipadx = 5, ipady = 3, padx = 3, pady = 3)

	new_win.mainloop()

def blink(i):
    elements_buttons[i].config(bg='green', bd = 7)
    elements_buttons[i].after(4000, lambda: elements_buttons[i].config(bg='white', bd = 1))

def search(self):
	global keyword
	global elements
	keyword = search_txt.get()
	keyword = keyword.lower().strip()
	for i in elements_buttons:	
		if keyword == i.lower():
			blink(i)
	if keyword not in elements:
		popup_noresults(keyword)
	search_txt.delete(0, END)


def search2():
	global keyword
	global elements
	keyword = search_txt.get()
	Keyword = keyword.lower()
	for i in elements_buttons:	
		if Keyword == i.lower():
			blink(i)
	if keyword not in elements:
		popup_noresults(keyword)
	search_txt.delete(0, END)	

def remove_int_text(self):
	search_txt.delete(0, END)
	search_txt['fg'] = 'black'

#Making and placing labels for groups and periods
for i in range(1,19):
	Label(root, text = i).grid(row = 1, column = i)

for i in range(1,8):
	Label(root, text = i).grid(row = i+2, column = 0, padx = 10)

#Creating Search Button
global search_txt

search_txt = Entry(root, width = 30, font=("Arial",8), fg = 'grey')
search_txt.insert(0, 'Search for elements')
search_txt.bind('<Button-1>', remove_int_text)
search_txt.bind('<Return>', search)

search_but = Button(root, text = 'Search', command = search2)

search_txt.grid(row = 0, column = 0, columnspan =18, ipady = 3, padx = 12, pady = 10)
search_but.grid(row = 0, column = 3, padx = 10, columnspan = 20, ipady = 1)


#Defining Buttons and placing buttons

elements_buttons = {}
for i in elements_dict:
	elements_buttons[i] = Button(root, image = small_images[i], command=lambda i=i: onclick(i, big_images[i]))
	elements_buttons[i].grid(row = elements_dict[i][1], column = elements_dict[i][2])


root.mainloop()

