from tkinter import *
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


#Images of Elements

#General Code for the images
#img_  = Image.open(r'Images\ .png')
# _img = ImageTk.PhotoImage(img_ .resize((67,67), Image.ANTIALIAS)

img_h = Image.open(r'Images\h.png')
h_img = ImageTk.PhotoImage(img_h.resize((67,67), Image.ANTIALIAS))

img_he = Image.open(r'Images\he.png')
he_img = ImageTk.PhotoImage(img_he.resize((67,67), Image.ANTIALIAS))

img_li = Image.open(r'Images\li.png')
li_img = ImageTk.PhotoImage(img_li.resize((67,67), Image.ANTIALIAS))

img_be = Image.open(r'Images\be.png')
be_img = ImageTk.PhotoImage(img_be.resize((67,67), Image.ANTIALIAS))

img_b = Image.open(r'Images\b.png')
b_img = ImageTk.PhotoImage(img_b.resize((67,67), Image.ANTIALIAS))

img_c = Image.open(r'Images\c.png')
c_img = ImageTk.PhotoImage(img_c.resize((67,67), Image.ANTIALIAS))

img_n = Image.open(r'Images\n.png')
n_img = ImageTk.PhotoImage(img_n.resize((67,67), Image.ANTIALIAS))

img_o = Image.open(r'Images\o.png')
o_img = ImageTk.PhotoImage(img_o.resize((67,67), Image.ANTIALIAS))

img_f = Image.open(r'Images\f.png')
f_img = ImageTk.PhotoImage(img_f.resize((67,67), Image.ANTIALIAS))

img_ne = Image.open(r'Images\ne.png')
ne_img = ImageTk.PhotoImage(img_ne.resize((67,67), Image.ANTIALIAS))

img_na = Image.open(r'Images\na.png')
na_img = ImageTk.PhotoImage(img_na.resize((67,67), Image.ANTIALIAS))

img_mg = Image.open(r'Images\mg.png')
mg_img = ImageTk.PhotoImage(img_mg.resize((67,67), Image.ANTIALIAS))

img_al = Image.open(r'Images\al.png')
al_img = ImageTk.PhotoImage(img_al.resize((67,67), Image.ANTIALIAS))

img_si = Image.open(r'Images\si.png')
si_img = ImageTk.PhotoImage(img_si.resize((67,67), Image.ANTIALIAS))

img_p = Image.open(r'Images\p.png')
p_img = ImageTk.PhotoImage(img_p.resize((67,67), Image.ANTIALIAS))

img_s = Image.open(r'Images\s.png')
s_img = ImageTk.PhotoImage(img_s.resize((67,67), Image.ANTIALIAS))

#img_cl = Image.open(r'Images\cl.png')
#cl_img = ImageTk.PhotoImage(img_cl.resize((67,67), Image.ANTIALIAS))

img_ar = Image.open(r'Images\ar.png')
ar_img = ImageTk.PhotoImage(img_ar.resize((67,67), Image.ANTIALIAS))

img_k = Image.open(r'Images\k.png')
k_img = ImageTk.PhotoImage(img_k.resize((67,67), Image.ANTIALIAS))

img_ca = Image.open(r'Images\ca.png')
ca_img = ImageTk.PhotoImage(img_ca.resize((67,67), Image.ANTIALIAS))

img_sc = Image.open(r'Images\sc.png')
sc_img = ImageTk.PhotoImage(img_sc.resize((67,67), Image.ANTIALIAS))

img_ti = Image.open(r'Images\ti.png')
ti_img = ImageTk.PhotoImage(img_ti.resize((67,67), Image.ANTIALIAS))

img_v = Image.open(r'Images\v.png')
v_img = ImageTk.PhotoImage(img_v.resize((67,67), Image.ANTIALIAS))

img_cr = Image.open(r'Images\cr.png')
cr_img = ImageTk.PhotoImage(img_cr.resize((67,67), Image.ANTIALIAS))

img_mn = Image.open(r'Images\mn.png')
mn_img = ImageTk.PhotoImage(img_mn.resize((67,67), Image.ANTIALIAS))

img_fe = Image.open(r'Images\fe.png')
fe_img = ImageTk.PhotoImage(img_fe.resize((67,67), Image.ANTIALIAS))

img_co = Image.open(r'Images\co.png')
co_img = ImageTk.PhotoImage(img_co.resize((67,67), Image.ANTIALIAS))

img_ni = Image.open(r'Images\ni.png')
ni_img = ImageTk.PhotoImage(img_ni.resize((67,67), Image.ANTIALIAS))

img_cu = Image.open(r'Images\cu.png')
cu_img = ImageTk.PhotoImage(img_cu.resize((67,67), Image.ANTIALIAS))

img_zn = Image.open(r'Images\zn.png')
zn_img = ImageTk.PhotoImage(img_zn.resize((67,67), Image.ANTIALIAS))

img_ga = Image.open(r'Images\ga.png')
ga_img = ImageTk.PhotoImage(img_ga.resize((67,67), Image.ANTIALIAS))

img_ge = Image.open(r'Images\ge.png')
ge_img = ImageTk.PhotoImage(img_ge.resize((67,67), Image.ANTIALIAS))

img_as = Image.open(r'Images\as.png')
as_img = ImageTk.PhotoImage(img_as.resize((67,67), Image.ANTIALIAS))

img_se = Image.open(r'Images\se.png')
se_img = ImageTk.PhotoImage(img_se.resize((67,67), Image.ANTIALIAS))

img_br = Image.open(r'Images\br.png')
br_img = ImageTk.PhotoImage(img_br.resize((67,67), Image.ANTIALIAS))

img_kr = Image.open(r'Images\kr.png')
kr_img = ImageTk.PhotoImage(img_kr.resize((67,67), Image.ANTIALIAS))

img_rb = Image.open(r'Images\rb.png')
rb_img = ImageTk.PhotoImage(img_rb.resize((67,67), Image.ANTIALIAS))


#Defining functions for element buttons

new = 0

def wiki(elem_name):
	webbrowser.open('https://en.wikipedia.org/wiki/' + str(elem_name),new=new)

def elementopia(elem_name):
	pass

def enable_but (elem_name):
	for i in elems:
		elems[i].config(state = 'active')
		new_win.destroy()

def onclick(elem_name, elem_pic):
	global new_win
	new_win = Toplevel()
	new_win.title(elem_name)
	
	#Once a button is pressed, it gets disabled
	elems[elem_name].config(state = DISABLED)
	
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

def search(self):
	global keyword
	global elements
	keyword = search_txt.get()
	keyword = keyword.lower()
	for i in elems:	
		if keyword == i.lower():
			elems[i].config(bg = 'green')
			#elems[i].invoke()
		search_txt.delete(0, END)

def search2():
	global keyword
	global elements
	keyword = search_txt.get()
	keyword = keyword.lower()
	for i in elems:	
		if keyword == i.lower():
			elems[i].config(bd = 10)
			#elems[i].invoke()
		search_txt.delete(0, END)

def remove_int_text(self):
	search_txt.delete(0, END)
	search_txt['fg'] = 'black'

#Making labels for groups and periods
group1 = Label(root, text = '1')
group2 = Label(root, text = '2')
group3 = Label(root, text = '3')
group4 = Label(root, text = '4')
group5 = Label(root, text = '5')
group6 = Label(root, text = '6')
group7 = Label(root, text = '7')
group8 = Label(root, text = '8')
group9 = Label(root, text = '9')
group10 = Label(root, text = '10')
group11 = Label(root, text = '11')
group12 = Label(root, text = '12')
group13 = Label(root, text = '13')
group14 = Label(root, text = '14')
group15 = Label(root, text = '15')
group16 = Label(root, text = '16')
group17 = Label(root, text = '17')
group18 = Label(root, text = '18')

period1 = Label(root, text = '1')
period2 = Label(root, text = '2')
period3 = Label(root, text = '3')
period4 = Label(root, text = '4')
period5 = Label(root, text = '5')
period6 = Label(root, text = '6')
period7 = Label(root, text = '7')

#Creating Search Button
global search_txt

search_txt = Entry(root, width = 30, font=("Arial",8), fg = 'grey')
search_txt.insert(0, 'Search for elements')
search_txt.bind('<Button-1>', remove_int_text)
search_txt.bind('<Return>', search)

search_but = Button(root, text = 'Search', command = search2)

search_txt.grid(row = 0, column = 0, columnspan =18, ipady = 3, padx = 12, pady = 10)
search_but.grid(row = 0, column = 3, padx = 10, columnspan = 20, ipady = 1)


#Defining Buttons
but_h = Button(root, image = h_img, command = lambda : onclick('Hydrogen', img_h))
but_he = Button(root, image = he_img, command = lambda : onclick('Helium', img_he))
but_li = Button(root, image = li_img, command = lambda : onclick('Lithium', img_li))
but_be = Button(root, image = be_img, command = lambda : onclick('Berrylium', img_be))
but_b = Button(root, image = b_img, command = lambda : onclick('Boron', img_b))
but_c = Button(root, image = c_img, command = lambda : onclick('Carbon', img_c))
but_n = Button(root, image = n_img, command = lambda : onclick('Nitrogen', img_n))
but_o = Button(root, image = o_img, command = lambda : onclick('Oxygen', img_o))
but_f = Button(root, image = f_img, command = lambda : onclick('Fluorine', img_f))
but_ne = Button(root, image = ne_img, command = lambda : onclick('Neon', img_ne))
but_na = Button(root, image = na_img, command = lambda : onclick('Sodium', img_na))
but_mg = Button(root, image = mg_img, command = lambda : onclick('Magnesium', img_mg))
but_al = Button(root, image = al_img, command = lambda : onclick('Aluminium', img_al))
but_si = Button(root, image = si_img, command = lambda : onclick('Silicon', img_si))
but_p = Button(root, image = p_img, command = lambda : onclick('Phosphorous', img_p))
but_s = Button(root, image = s_img, command = lambda : onclick('Sulphur', img_s))
#but_cl = Button(root, image = cl_img, command = lambda : onclick('Chlorine', img_cl))
but_ar = Button(root, image = ar_img, command = lambda : onclick('Argon', img_ar))
but_k = Button(root, image = k_img, command = lambda : onclick('Potassium', img_k))
but_ca = Button(root, image = ca_img, command = lambda : onclick('Calcium', img_ca))
but_sc = Button(root, image = sc_img, command = lambda : onclick('Scandium', img_sc))
but_ti = Button(root, image = ti_img, command = lambda : onclick('Titanium', img_ti))
but_v = Button(root, image = v_img, command = lambda : onclick('Vanadium', img_v))
but_cr = Button(root, image = cr_img, command = lambda : onclick('Chromium', img_cr))
but_mn = Button(root, image = mn_img, command = lambda : onclick('Manganese', img_mn))
but_fe = Button(root, image = fe_img, command = lambda : onclick('Iron', img_fe))
but_co = Button(root, image = co_img, command = lambda : onclick('Cobalt', img_co))
but_ni = Button(root, image = ni_img, command = lambda : onclick('Nickel', img_ni))
but_cu = Button(root, image = cu_img, command = lambda : onclick('Copper', img_cu))
but_zn = Button(root, image = zn_img, command = lambda : onclick('Zinc', img_zn))
but_ga = Button(root, image = ga_img, command = lambda : onclick('Gallium', img_ga))
but_ge = Button(root, image = ge_img, command = lambda : onclick('Germanium', img_ge))
but_as = Button(root, image = as_img, command = lambda : onclick('Arsenic', img_as))
but_se = Button(root, image = se_img, command = lambda : onclick('Selenium', img_se))
but_br = Button(root, image = br_img, command = lambda : onclick('Bromine', img_br))
but_kr = Button(root, image = kr_img, command = lambda : onclick('Krypton', img_kr))
#but_rb = Button(root, image = rb_img, command = lambda : onclick())
#but_sr = Button(root, image = sr_img, command = lambda : onclick())
#but_y = Button(root, image = y_img, command = lambda : onclick())


#Dictionary of elements
elems =  {
	'Hydrogen' : but_h,
	'Helium' : but_he,
	'Lithium' : but_li,
	'Berrylium' : but_be,
	'Boron' : but_b,
	'Carbon' : but_c,
	'Oxygen' : but_o,
	'Nitrogen' : but_n,
	'Fluorine' : but_f,
	'Neon' : but_ne,
	'Sodium': but_na,
    'Magnesium': but_mg, 
    'Aluminium': but_al,
    'Silicon': but_si,
    'Phosphorous': but_p,
    'Sulphur': but_s,
    #'Chlorine':but_cl,
    'Argon': but_ar,
    'Potassium': but_k,
    'Calcium': but_ca,
    'Scandium': but_sc,
    'Titanium': but_ti,
    'Vanadium': but_v,
    'Chromium': but_cr,
    'Manganese': but_mn,
    'Iron': but_fe,
    'Cobalt': but_co,
    'Nickel': but_ni,
    'Copper': but_cu,
    'Zinc': but_zn,
    'Gallium': but_ga,
    'Germanium': but_ge,
    'Arsenic': but_as,
    'Selenium': but_se,
    'Bromine': but_br,
    'Krypton': but_kr}


#Placing groups and labels
group1.grid(row = 1, column = 1)
group2.grid(row = 1, column = 2)
group3.grid(row = 1, column = 3)
group4.grid(row = 1, column = 4)
group5.grid(row = 1, column = 5)
group6.grid(row = 1, column = 6)
group7.grid(row = 1, column = 7)
group8.grid(row = 1, column = 8)
group9.grid(row = 1, column = 9)
group10.grid(row = 1, column = 10)
group11.grid(row = 1, column = 11)
group12.grid(row = 1, column = 12)
group13.grid(row = 1, column = 13)
group14.grid(row = 1, column = 14)
group15.grid(row = 1, column = 15)
group16.grid(row = 1, column = 16)
group17.grid(row = 1, column = 17)
group18.grid(row = 1, column = 18)

period1.grid(row = 3, column = 0, padx = 10)
period2.grid(row = 4, column = 0, padx = 10)
period3.grid(row = 5, column = 0, padx = 10)
period4.grid(row = 6, column = 0, padx = 10)
period5.grid(row = 7, column = 0, padx = 10)
period6.grid(row = 8, column = 0, padx = 10)
period7.grid(row = 9, column = 0, padx = 10)

#Placing buttons
but_h.grid(row = 3, column = 1)

but_he.grid(row = 3, column = 18)

but_li.grid(row = 4, column = 1)

but_be.grid(row = 4, column = 2)

but_b.grid(row = 4, column = 13)

but_c.grid(row = 4, column = 14)

but_n.grid(row = 4, column = 15)

but_o.grid(row = 4, column = 16)

but_f.grid(row = 4, column = 17)

but_ne.grid(row = 4, column = 18)

but_na.grid(row = 5, column = 1)

but_mg.grid(row = 5, column = 2)

but_al.grid(row = 5, column = 13)

but_si.grid(row = 5, column = 14)

but_p.grid(row = 5, column = 15)

but_s.grid(row = 5, column = 16)

#but_cl.grid(row = 5, column = 17)

but_ar.grid(row = 5, column = 18)

but_k.grid(row = 6, column = 1)

but_ca.grid(row = 6, column = 2)

but_sc.grid(row = 6, column = 3)

but_ti.grid(row = 6, column = 4)

but_v.grid(row = 6, column = 5)

but_cr.grid(row = 6, column = 6)

but_mn.grid(row = 6, column = 7)

but_fe.grid(row = 6, column = 8)

but_co.grid(row = 6, column = 9)

but_ni.grid(row = 6, column = 10)

but_cu.grid(row = 6, column = 11)

but_zn.grid(row = 6, column = 12)

but_ga.grid(row = 6, column = 13)

but_ge.grid(row = 6, column = 14)

but_as.grid(row = 6, column = 15)

but_se.grid(row = 6, column = 16)

but_br.grid(row = 6, column = 17)

but_kr.grid(row = 6, column = 18)

root.mainloop()

