from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msgbox
from PIL import ImageTk, Image
import webbrowser
import os

root = Tk()
root.title('Elementopedia')

#Geomtry Difining
width_value= root.winfo_screenwidth()
height_value= root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(width_value,height_value))
#root.geometry('1366x768')

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
global elements_symbols

elements = list(elements_dict.keys())
for i in range(len(elements)):
	elements[i] = elements[i].lower()

elements_symbols = []
for i in elements_dict:
	elements_symbols.append(elements_dict[i][0])
	
#Images of Elements
big_images = {}
small_images = {}
for i in elements_dict :
	if i == 'Lanthnoids' or i == 'Actinoids':
		continue
	big_images[i] = Image.open('Images/' + elements_dict[i][0] + '.png').resize((300,300), Image.ANTIALIAS)
	small_images[i] = ImageTk.PhotoImage(Image.open('Images/' + elements_dict[i][0] + '.png').resize((int(width_value//21),int(height_value//13.24)), Image.ANTIALIAS))

#Images of graphs
alkali_f = {}
alkaline_f = {}
III_A_f = {}
carbon_f = {}
nitrogen_f = {}
oxygen_f = {}
halogens_f = {}
threed_f = {}
lanthanides_f = {}

atomic_radius = {}
boling_point = {}
melting_point = {}
electron_affinity = {}
electronegativity = {}
ionisation = {}
metallic_chr = {}
summary = {}

all_graphs = os.listdir('Graphs')
#print(all_graphs)

for graphs in all_graphs:
	if '3-D' in graphs:
		threed_f[graphs.split('.')[0]] = [ImageTk.PhotoImage(Image.open('Graphs/' + graphs).resize((int(width_value//4),int(height_value//4)), Image.ANTIALIAS)),]
	elif 'alkaline' in graphs:
		alkaline_f[graphs.split('.')[0]] = [ImageTk.PhotoImage(Image.open('Graphs/' + graphs).resize((int(width_value//4),int(height_value//4)), Image.ANTIALIAS)),]
	elif 'alkali' in graphs:
		alkali_f[graphs.split('.')[0]] = [ImageTk.PhotoImage(Image.open('Graphs/' + graphs).resize((int(width_value//4),int(height_value//4)), Image.ANTIALIAS)),]
	elif 'carbon' in graphs:
		carbon_f[graphs.split('.')[0]] = [ImageTk.PhotoImage(Image.open('Graphs/' + graphs).resize((int(width_value//4),int(height_value//4)), Image.ANTIALIAS)),]
	elif 'IIIA' in graphs:
		III_A_f[graphs.split('.')[0]] = [ImageTk.PhotoImage(Image.open('Graphs/' + graphs).resize((int(width_value//4),int(height_value//4)), Image.ANTIALIAS)),]
	elif 'nitrogen' in graphs:
		nitrogen_f[graphs.split('.')[0]] = [ImageTk.PhotoImage(Image.open('Graphs/' + graphs).resize((int(width_value//4),int(height_value//4)), Image.ANTIALIAS)),]
	elif 'oxygen' in graphs:
		oxygen_f[graphs.split('.')[0]] = [ImageTk.PhotoImage(Image.open('Graphs/' + graphs).resize((int(width_value//4),int(height_value//4)), Image.ANTIALIAS)),]
	elif 'halogens' in graphs:
		halogens_f[graphs.split('.')[0]] = [ImageTk.PhotoImage(Image.open('Graphs/' + graphs).resize((int(width_value//4),int(height_value//4)), Image.ANTIALIAS)),]
	elif 'lanthanides' in graphs:
		lanthanides_f[graphs.split('.')[0]] = [ImageTk.PhotoImage(Image.open('Graphs/' + graphs).resize((int(width_value//4),int(height_value//4)), Image.ANTIALIAS)),]
	elif 'atomic_radius' in graphs:
		atomic_radius[graphs.split('.')[0]] = [ImageTk.PhotoImage(Image.open('Graphs/' + graphs).resize((int(width_value//2),int(height_value//2)), Image.ANTIALIAS)),]
	elif 'mp_' in graphs:
		melting_point[graphs.split('.')[0]] = [ImageTk.PhotoImage(Image.open('Graphs/' + graphs).resize((int(width_value//2),int(height_value//2)), Image.ANTIALIAS)),]
	elif 'bp_' in graphs:
		boling_point[graphs.split('.')[0]] = [ImageTk.PhotoImage(Image.open('Graphs/' + graphs).resize((int(width_value//2),int(height_value//2)), Image.ANTIALIAS)),]
	elif 'electron_' in graphs:
		electron_affinity[graphs.split('.')[0]] = [ImageTk.PhotoImage(Image.open('Graphs/' + graphs).resize((int(width_value//2),int(height_value//2)), Image.ANTIALIAS)),]
	elif 'electronegativity_' in graphs:
		electronegativity[graphs.split('.')[0]] = [ImageTk.PhotoImage(Image.open('Graphs/' + graphs).resize((int(width_value//2),int(height_value//2)), Image.ANTIALIAS)),]
	elif 'ionisation_' in graphs:
		ionisation[graphs.split('.')[0]] = [ImageTk.PhotoImage(Image.open('Graphs/' + graphs).resize((int(width_value//2),int(height_value//2)), Image.ANTIALIAS)),]
	elif 'metallic_' in graphs:
		metallic_chr[graphs.split('.')[0]] = [ImageTk.PhotoImage(Image.open('Graphs/' + graphs).resize((int(width_value//2),int(height_value//2)), Image.ANTIALIAS)),]
	elif 'summary' in graphs:
		summary[graphs.split('.')[0]] = [ImageTk.PhotoImage(Image.open('Graphs/' + graphs).resize((int(width_value//2),int(height_value//2)), Image.ANTIALIAS)),]


#print(atomic_radius, melting_point, boling_point, electronegativity, electron_affinity, ionisation, metallic_chr, summary, sep = '\n')

positions = ((0,0), (0,1), (1,0), (1,1), (2,0), (2,1))
#print(alkali_f, alkaline_f, III_A_f, carbon_f, nitrogen_f, oxygen_f, halogens_f, threed_f, lanthanides_f, sep = '\n')
alkali_f = dict(sorted(alkali_f.items()))
alkaline_f = dict(sorted(alkaline_f.items()))
III_A_f = dict(sorted(III_A_f.items()))
carbon_f = dict(sorted(carbon_f.items()))
nitrogen_f = dict(sorted(nitrogen_f.items()))
oxygen_f = dict(sorted(oxygen_f.items()))
halogens_f = dict(sorted(halogens_f.items()))
threed_f = dict(sorted(threed_f.items()))
lanthanides_f = dict(sorted(lanthanides_f.items()))

	
#Defining functions for element buttons

def wiki(elem_name):
	webbrowser.open('https://en.wikipedia.org/wiki/' + str(elem_name),new=0)

def elementopia(elem_name):
	#os.getcwd() gets the python file directory
	os.startfile(os.getcwd() + '/Elementopedia/'+ str(elements_dict[elem_name][0])+'.pdf')

def popup_noresults(search_term): 
	response = msgbox.showinfo('No Results', 'Sorry, The element you seacrhed for (' + search_term + ') does not exist')
	if response != None:
		search_txt.delete(0, 'end')

def enable_but (elem_name):
	for i in elements_buttons:
		elements_buttons[i][0].config(state = 'active')
		new_win.destroy()

def onclick(elem_name, elem_pic):
	global new_win
	new_win = Toplevel()
	new_win.title(elem_name)
	
	#Once a button is pressed, it gets disabled
	elements_buttons[elem_name][0].config(state = DISABLED)
	
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
    elements_buttons[i][0].config(bg='green', bd = 7)
    elements_buttons[i][0].after(4000, lambda: elements_buttons[i][0].config(bg='white', bd = 1))
    search_txt.delete(0, END)

def search(self):
	global keyword
	global elements
	setvalue_r(radio.get())
	keyword = search_txt.get()
	keyword = keyword.lower()
	if keyword.strip() == '' or keyword.strip() == 'search for elements':
		pass
	else:
		for i in elements_buttons:	
			if keyword == i.lower() or keyword == elements_buttons[i][1]:
				if value_r == 'highlight':
					blink(i)
				elif value_r == 'open':
					search_txt.delete(0, END)
					elements_buttons[i][0].invoke()
					
		#if keyword not in elements or keyword not in elements_symbols:
			#popup_noresults(keyword)


def search2():
	global keyword
	global elements
	setvalue_r(radio.get())
	keyword = search_txt.get()
	keyword = keyword.lower()
	if keyword.strip() == '' or keyword.strip() == 'search for elements':
		pass
	else:
		for i in elements_buttons:	
			if keyword == i.lower() or keyword == elements_buttons[i][1]:
				if value_r == 'highlight':
					blink(i)
				elif value_r == 'open':
					search_txt.delete(0, END)
					elements_buttons[i][0].invoke()
		#if keyword not in elements or keyword not in elements_symbols:
			#popup_noresults(keyword)	

def remove_int_text(self):
	search_txt.delete(0, END)
	search_txt['fg'] = 'black'

def setvalue_r(string):
	global value_r
	value_r = str(string)

def find_graph_dic(string):
	if string == drop_options2[1]:
		return alkali_f
	elif string == drop_options2[2]:
		return alkaline_f
	elif string == drop_options2[3]:
		return III_A_f
	elif string == drop_options2[4]:
		return carbon_f
	elif string == drop_options2[5]:
		return nitrogen_f
	elif string == drop_options2[6]:
		return oxygen_f	
	elif string == drop_options2[7]:
		return halogens_f
	elif string == drop_options2[8]:
		return threed_f
	elif string == drop_options2[9]:
		return lanthanides_f	
	elif string == drop_options1[1]:
		return atomic_radius
	elif string == drop_options1[2]:
		return electronegativity
	elif string == drop_options1[3]:
		return electron_affinity
	elif string == drop_options1[4]:
		return boling_point
	elif string == drop_options1[5]:
		return melting_point
	elif string == drop_options1[6]:
		return ionisation
	elif string == drop_options1[7]:
		return metallic_chr
	elif string == drop_options1[8]:
		return summary		
#Making dictionaries to produce 
def create_graph_win(choice):
	if choice == drop_options2[0] or choice == drop_options1[0]:
		pass 
	else:
		global group
		global graph_win
		graph_win = Toplevel()	
		graph_win.title(choice.split()[0:2])
		group = find_graph_dic(choice)
		i = 0
		while i < len(group):
			for images in group:
				if images == images.split('_')[0] + '_radius' or images == images.split('_')[0] + '_Radius':
					Label(graph_win, image = group[images]).grid(row = 0, column = 0)
				else:
					Label(graph_win, image = group[images]).grid(row = positions[i][0], column = positions[i][1])
				i += 1


	graph_win.mainloop()


#Making dropdowns

drop_options1 = [
'Choose a general trend',
'Atomic Radius',
'Electronegativity',
'Electron - Affinity',
'Boiling Point',
'Melting Point',
'ionisation',
'Metallic Character',
'Summary'
]

drop1 = ttk.Combobox(root, value = drop_options1, width = 20)
drop1.current(0)
drop1_but = Button(root, text = 'Go to graph', command = lambda : create_graph_win(drop1.get()))

drop1.grid(row = 2, column = 3, columnspan = 4, ipadx = 7)
drop1_but.grid(row = 2, column = 4, columnspan = 6)

drop_options2 = [
'Select the group of elements to observe trends for',
'Alkali Metals',
 'Alkaline Earth Metals',
 'III-A Elements (Boron Family)',
 'Carbon Family',
  'Nitrogen Family',
   'Oxygen Family',
  'Halogens',
  '3D Elements',
   'Lanthanides'
]

drop2 = ttk.Combobox(root, value = drop_options2, width = 45)
drop2.grid(row = 2, column = 5, columnspan = 10)
drop2.current(0)

drop2_but =  Button(root, text = 'Go to graphs', command = lambda : create_graph_win(drop2.get()))
drop2_but.grid(row = 2, column = 8, columnspan = 10)

#Making and placing labels for groups and periods
#Groups
for i in [1,18]:
	Label(root, text = i).grid(row = 2, column = i)
for i in [2,13,14,15,16,17]:
	Label(root, text = i).grid(row = 3, column = i)
for i in range(3,14):
	Label(root, text = i).grid(row = 5, column = i)

#Periods
for i in range(1,8):
	Label(root, text = str(i) + '   ').grid(row = i+2, column = 0, padx = 15)

#Making labels for showing blocks
Label(root, text ='<' + '—'*3 + 'S-Block' + '—'*3 + '>').grid(row = 1, column = 1, columnspan = 2)	
Label(root, text ='<' + '—'*25 + 'D-Block' + '—'*25 + '>').grid(row = 4, column = 3, columnspan = 10)	
Label(root, text ='<' + '—'*15 + 'P-Block' + '—'*15 + '>').grid(row = 1, column = 13, columnspan = 6)	
Label(root, text = 'Λ\n' +'|\n'*3 + 'F-Block\n' + '|\n' *3 + 'V').grid(row = 11, column = 1, rowspan = 2)
Label(root, text = 'Lanthanides').grid(row = 11, column = 2)
Label(root, text = 'Actinides').grid(row = 12, column = 2)


#Making radio buttons
global radio
radio = StringVar()
radio.set('open')

radio1 = Radiobutton(root, text = 'Highlight searched element', variable = radio, value = 'highlight', command = lambda : setvalue_r(radio.get()))
radio2 = Radiobutton(root, text = 'Open searched element', variable = radio, value = 'open', command = lambda : setvalue_r(radio.get())) 
radio1.grid(row = 0, column = 0, columnspan = 11)
radio2.grid(row = 0, column  = 1, columnspan = 14)

global search_txt

search_txt = Entry(root, width = 30, font=("Arial",8), fg = 'grey')
search_txt.insert(0, 'Search for elements')
search_txt.bind('<Button-1>', remove_int_text)
search_txt.bind('<Return>', search)

search_but = Button(root, text = 'Search', command = search2)

search_txt.grid(row = 0, column = 2, columnspan =18, ipady = 3, padx = 12, pady = 10)
search_but.grid(row = 0, column = 5, padx = 10, columnspan = 20, ipady = 1)


#Defining Buttons and placing buttons

#Making a dictionary of buttons with element
elements_buttons = {}

for i in elements_dict:
	elements_buttons[i] = (Button(root, image = small_images[i], command=lambda i=i: onclick(i, big_images[i])), elements_dict[i][0])
	elements_buttons[i][0].grid(row = elements_dict[i][1], column = elements_dict[i][2])

#Making some empty labels to create space in 10th row
for i in range(19):
	Label(root, text = '     ').grid(row = 10, column =  i, pady = 5)


root.mainloop()

