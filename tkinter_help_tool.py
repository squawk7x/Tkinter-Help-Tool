# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""tkinter-help-tool.py: evaluate methods and options on tkinter widgets"""

__author__ = "Andreas Ottburg"
__copyright__ = "GPLv3"
__contact__ = "andreas@ottburg.de"
__credits__ = ["John W. Shipmann"]
__date__ = "2023/05/04"
__maintainer__ = "Andreas Ottburg"
__status__ = "Production"
__version__ = "0.0.2"

import inspect
import io
import re
import sys
from tkinter import *
from tkinter import ttk, font
from tkinter.scrolledtext import ScrolledText

from hints import options
from keysyms import keysyms


def filter_list(_list=None, pattern=None):
	sorted_filtered_list = sorted(set([val for val in _list
	                                   if re.search(pattern, val)]).difference(
		{'children', 'master', 'builtins.object'}))
	return sorted_filtered_list


s = ttk.Style()
s.configure('Caption.TLabel',
            foreground=['#663300'],
            background=['#ffe2a0'],
            font=(font.NORMAL, 16, 'bold'),
            relief='ridge')


class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.top = None
		self.caption_label = None
		self.definition_label = None
		self.cbox1 = None
		self.cbox2 = None
		self.widget1 = None
		self.widget2 = None
		self.toggleButton = None
		self.showButton = None
		self.widget_lf = None
		self.filter_lf = None
		self.rb_off = None
		self.rb_event = None
		self.rb_bind = None
		self.rb_grid = None
		self.rb_pack = None
		self.rb_place = None
		self.rb_tk = None
		self.rb_wm = None
		self.rb_winfo = None
		self.notebook = None
		self.methods_frm = None
		self.methods_text = None
		self.options_frm = None
		self.options_text = None
		self.events_frm = None
		self.sensor_lf = None
		self.mouse_field = None
		self.entry_field = None
		self.events_text = None
		self.definition_var = StringVar()
		self.option_menu_var = StringVar()
		self.option_menu_choices = []
		self.cbox1_var = StringVar()
		self.cbox2_var = StringVar()
		self.method_var = StringVar()
		self.entry_field_var = StringVar()
		self.createWidgets()

	def set_values(self):
		self.cbox1['values'] = (('ttk.Button', 'ttk.Checkbutton',
		                         'ttk.Combobox',
		                         'ttk.Entry',
		                         'ttk.Frame', 'ttk.Label', 'ttk.Labelframe',
		                         'ttk.LabelFrame',
		                         'ttk.Menubutton', 'ttk.Notebook',
		                         'ttk.Panedwindow',
		                         'ttk.PanedWindow',
		                         'ttk.Progressbar', 'ttk.Radiobutton',
		                         'ttk.Scale',
		                         'ttk.Scrollbar',
		                         'ttk.Separator', 'ttk.Sizegrip',
		                         'ttk.Spinbox',
		                         'ttk.Style',
		                         'ttk.Treeview', 'ttk.LabeledScale',
		                         'ttk.Widget') +
		                        ('Button',
		                         'Canvas',
		                         'Checkbutton', 'Entry',
		                         'Frame', 'Label',
		                         'LabelFrame',
		                         'Menu',
		                         'Menubutton',
		                         'OptionMenu',
		                         'PanedWindow',
		                         'Radiobutton', 'Scale',
		                         'Scrollbar',
		                         'Spinbox',
		                         'Text',
		                         'Tk') +
		                        ('Widget', 'BaseWidget', 'Misc') +
		                        ('Pack', 'Place', 'Grid') +
		                        ('messagebox', 'filedialog', 'colorchooser') +
		                        ('object',))
		self.cbox2['values'] = self.cbox1['values']
		self.option_menu_choices = self.cbox1['values']
		self.entry_field_var.set(
			'Keyboard Input here:')

	def toggle(self):
		temp1 = self.cbox1_var.get()
		temp2 = self.cbox2_var.get()
		self.cbox2_var.set(temp1)
		self.cbox1_var.set(temp2)
		self.showButton.invoke()

	def createWidgets(self):

		# Definition
		self.top = self.winfo_toplevel()
		self.notebook = ttk.Notebook(self)

		self.caption_label = ttk.Label(self, textvariable=self.cbox1_var,
		                               anchor='center',
		                               style='Caption.TLabel')
		self.definition_label = Label(self, textvariable=self.definition_var,
		                              bg='#e0e0e0', relief='ridge')

		self.cbox1 = ttk.Combobox(self, textvariable=self.cbox1_var)
		self.cbox2 = ttk.Combobox(self, textvariable=self.cbox2_var)
		self.set_values()
		self.cbox1_var.set('ttk.Button')
		self.cbox2_var.set('object')

		self.widget_lf = ttk.Labelframe(self, text='Widget', labelanchor='n',
		                                width=180, height=40)
		self.widget_lf.propagate(False)
		self.widget_lf.grid(column=0, row=5, sticky='ns')
		self.filter_lf = ttk.Labelframe(self,
		                                text='Method Filter', labelanchor='n')
		self.toggleButton = ttk.Button(self, text='   ⇆   ',
		                               command=self.toggle)
		self.showButton = ttk.Button(self,
		                             text='↖ Unique Methods compared to ↗',
		                             command=self.show_methods)
		self.rb_off = ttk.Radiobutton(self.filter_lf, text='off', width=5,
		                              variable=self.method_var, value='',
		                              command=self.show_methods)
		self.rb_event = ttk.Radiobutton(self.filter_lf, text='event', width=5,
		                                variable=self.method_var,
		                                value='^.*event.*$',
		                                command=self.show_methods)
		self.rb_bind = ttk.Radiobutton(self.filter_lf, text='bind', width=5,
		                               variable=self.method_var,
		                               value='^.*bind.*$',
		                               command=self.show_methods)
		self.rb_grid = ttk.Radiobutton(self.filter_lf, text='grid', width=5,
		                               variable=self.method_var, value='^grid',
		                               command=self.show_methods)
		self.rb_pack = ttk.Radiobutton(self.filter_lf, text='pack', width=5,
		                               variable=self.method_var, value='^pack',
		                               command=self.show_methods)
		self.rb_place = ttk.Radiobutton(self.filter_lf, text='place', width=5,
		                                variable=self.method_var,
		                                value='^place',
		                                command=self.show_methods)
		self.rb_tk = ttk.Radiobutton(self.filter_lf, text='tk_', width=5,
		                             variable=self.method_var,
		                             value='^tk_',
		                             command=self.show_methods)
		self.rb_winfo = ttk.Radiobutton(self.filter_lf, text='winfo_', width=5,
		                                variable=self.method_var,
		                                value='^winfo_',
		                                command=self.show_methods)
		self.rb_wm = ttk.Radiobutton(self.filter_lf, text='wm_', width=5,
		                             variable=self.method_var,
		                             value='^wm_',
		                             command=self.show_methods)
		self.methods_frm = Frame(self.notebook)
		self.options_frm = Frame(self.notebook)
		self.events_frm = Frame(self.notebook)
		self.notebook.add(self.methods_frm, text='Methods')
		self.notebook.add(self.options_frm, text='Options')
		self.notebook.add(self.events_frm, text='Events')

		self.methods_text = ScrolledText(self.methods_frm, bg='#ffffdd',
		                                 fg='#663300',
		                                 wrap='word',
		                                 font=font.Font(size=11), height=60)
		self.options_text = ScrolledText(self.options_frm, bg='#ffffdd',
		                                 fg='#663300',
		                                 wrap='word',
		                                 font=font.Font(size=11), height=60)
		self.sensor_lf = ttk.Labelframe(self.events_frm, text='Sensor field',
		                                labelanchor='n', height=140)
		self.mouse_field = ttk.Label(self.sensor_lf, anchor='n',
		                             relief='ridge',
		                             background='grey', foreground='white',
		                             text='\nmove mouse here '
		                                  '\nand push a button\n',
		                             width=30)
		self.entry_field = ttk.Entry(self.sensor_lf,
		                             textvariable=self.entry_field_var)
		self.events_text = ScrolledText(self.events_frm, bg='#ffffdd',
		                                fg='#663300',
		                                wrap='word',
		                                font=font.Font(size=11), height=60)
		old_stdout = sys.stdout
		sys.stdout = my_stdout = io.StringIO()
		self.events_text.configure(state=NORMAL)
		print(help(Event))
		self.events_text.insert(0.1, f"\n{my_stdout.getvalue()}\n")
		self.events_text.configure(state=DISABLED)
		sys.stdout = old_stdout

		# Layout
		self.grid(sticky='nesw')
		self.caption_label.grid(column=0, row=0, sticky='ew',
		                        columnspan=3)
		self.definition_label.grid(column=0, row=2, sticky='ew', columnspan=3)
		self.cbox1.grid(column=0, row=3, sticky='n')
		self.cbox2.grid(column=2, row=3, sticky='n')
		self.toggleButton.grid(column=1, row=3, sticky='n')
		self.showButton.grid(column=1, row=5, padx=5, pady=10, sticky='ns')
		self.filter_lf.grid(column=2, row=5, sticky='ns')
		self.rb_off.invoke()
		self.rb_off.grid(column=0, row=0)
		self.rb_event.grid(column=0, row=1)
		self.rb_bind.grid(column=0, row=2)
		self.rb_grid.grid(column=1, row=0)
		self.rb_pack.grid(column=1, row=1)
		self.rb_place.grid(column=1, row=2)
		self.rb_tk.grid(column=2, row=0)
		self.rb_winfo.grid(column=2, row=1)
		self.rb_wm.grid(column=2, row=2)
		self.notebook.grid(column=0, row=10, columnspan=3, sticky='nesw')
		self.methods_text.grid(sticky='nesw')
		self.options_text.grid(sticky='nesw')
		self.sensor_lf.pack(side='top', expand=FALSE)
		self.mouse_field.pack(side='top', fill='both', expand=FALSE)
		self.entry_field.pack(side='top', fill='both', expand=FALSE)
		self.events_text.pack(side='top', fill='both', expand=TRUE)

		for w in self.winfo_children():
			w.grid_configure(padx=3, pady=3)

		# Configuration
		self.top.rowconfigure(0, weight=1)
		self.top.columnconfigure(0, weight=1)
		self.configure(height=800, width=550, padx=2, pady=2)
		self.columnconfigure('all', weight=1)
		self.rowconfigure('all', weight=0)
		self.rowconfigure(10, weight=3)
		self.methods_frm.columnconfigure('all', weight=1)
		self.methods_frm.rowconfigure('all', weight=1)
		self.options_frm.columnconfigure('all', weight=1)
		self.options_frm.rowconfigure('all', weight=1)
		self.events_frm.columnconfigure('all', weight=1)
		self.events_frm.rowconfigure('all', weight=1)

		# Bindings
		self.cbox1.bind("<<ComboboxSelected>>",
		                lambda e: self.showButton.invoke())
		self.cbox2.bind("<<ComboboxSelected>>",
		                lambda e: self.showButton.invoke())

		for event_type in ['<KeyPress>', '<KeyRelease>']:
			self.entry_field.bind(event_type, self.log_event)

		for event_type in ['<ButtonPress>', '<ButtonRelease>', '<MouseWheel>',
		                   '<Motion>', '<Enter>', '<Leave>']:
			self.mouse_field.bind(event_type, self.log_event)

		for event_type in ['<Visibility>',
		                   '<Unmap>', '<Map>', '<Expose>', '<FocusIn>',
		                   '<FocusOut>', '<Circulate>', '<Colormap>',
		                   '<Gravity>', '<Reparent>', '<Property>',
		                   '<Destroy>', '<Activate>', '<Deactivate>']:
			self.bind(event_type, self.log_event)

		# self.generate_events()

	def get_widget1(self):

		if self.cbox1_var.get() in {'Tk', 'Menu', 'Misc', 'Pack', 'Place',
		                            'Grid', 'object'}:
			self.widget1 = eval(F"{self.cbox1_var.get()}()")
		elif self.cbox1_var.get() in {'BaseWidget'}:
			self.widget1 = eval(
				F"{self.cbox1_var.get()}(self.widget_lf, 'toplevel')")
		elif self.cbox1_var.get() in {'ttk.Widget', 'Widget'}:
			self.widget1 = eval(
				F"{self.cbox1_var.get()}(self.widget_lf, None)")
		elif self.cbox1_var.get() in {'messagebox'}:
			self.widget1 = eval(F"{self.cbox1_var.get()}")
		# messagebox.showinfo('Tkinter Help Tool', 'Version 1.0')
		elif self.cbox1_var.get() in {'filedialog'}:
			self.widget1 = eval(F"{self.cbox1_var.get()}")
		# filedialog.askdirectory()
		elif self.cbox1_var.get() in {'colorchooser'}:
			self.widget1 = eval(F"{self.cbox1_var.get()}")
		# colorchooser.askcolor()
		elif self.cbox1_var.get() in {'OptionMenu'}:
			self.option_menu_var.set('Select an Option')
			self.widget1 = eval(
				F"OptionMenu(self.widget_lf, "
				F"self.option_menu_var, *{self.option_menu_choices})")
			self.widget1.pack(fill='x')
		elif self.cbox1_var.get() in self.cbox1['values']:
			self.widget1 = eval(F"{self.cbox1_var.get()}(self.widget_lf)")
			if issubclass(self.widget1.__class__, (Scrollbar, ttk.Scrollbar)):
				self.widget1.pack(fill='y')
			elif issubclass(self.widget1.__class__, Widget):
				self.widget1.pack(fill='x')
		else:
			self.widget1 = eval(F"{self.cbox1_var.get()}()")

		self.definition_var.set(F"w = {self.cbox1_var.get()}" + str(
			inspect.signature(self.widget1.__init__)))

	def get_widget2(self):
		if self.cbox2_var.get() in {'Tk', 'Menu', 'Misc', 'Pack', 'Place',
		                            'Grid', 'object'}:
			self.widget2 = eval(F"{self.cbox2_var.get()}()")
		elif self.cbox2_var.get() in {'messagebox', 'filedialog',
		                              'colorchooser'}:
			self.widget2 = eval(F"{self.cbox2_var.get()}")
		elif self.cbox2_var.get() in {'BaseWidget'}:
			self.widget2 = eval(
				F"{self.cbox2_var.get()}(self.widget_lf, 'toplevel')")
		elif self.cbox2_var.get() in {'OptionMenu'}:
			self.option_menu_var.set('Select an Option')
			self.widget2 = eval(
				F"OptionMenu(self.widget_lf, "
				F"self.option_menu_var, *{self.option_menu_choices})")
		elif self.cbox2_var.get() in {'ttk.Widget', 'Widget'}:
			self.widget2 = eval(
				F"{self.cbox2_var.get()}(self.widget_lf, None)")
		elif self.cbox2_var.get() in self.cbox2['values']:
			self.widget2 = eval(F"{self.cbox2_var.get()}(self.widget_lf)")

	def show_methods(self):

		for w in self.widget_lf.winfo_children():
			w.destroy()

		self.get_widget1()
		self.get_widget2()

		if self.widget1 is not None:
			widget1_methods = set(dir(self.widget1))
		else:
			widget1_methods = set()

		if self.widget2 is not None:
			widget2_methods = set(dir(self.widget2))
		else:
			widget2_methods = set()

		unique_methods = filter_list((widget1_methods - widget2_methods),
		                             pattern=r'^[^_?][a-z]')

		if pattern := self.method_var.get():
			unique_methods = filter_list(unique_methods, pattern=pattern)

		old_stdout = sys.stdout
		sys.stdout = my_stdout = io.StringIO()

		if unique_methods:
			for attr in unique_methods:
				print(79 * '_' + '\n')
				eval(f'help(self.widget1.{attr})')
			screen_txt = my_stdout.getvalue()
			print(79 * '_')
		else:
			screen_txt = ''

		self.methods_text.configure(state=NORMAL)
		header = f'Unique Methods of {self.cbox1_var.get()} ' \
		         f'   ⇆    {self.cbox2_var.get()}:\n\n'
		self.methods_text.replace(0.1, 'end',
		                          header + str(unique_methods) + '\n\n')
		if issubclass(self.widget1.__class__, BaseWidget):
			self.methods_text.insert('end',
			                         + 79 * '_' + '\n' + inspect.getsource(
				                         self.widget1.__init__))
		self.methods_text.insert('end', screen_txt)
		self.methods_text.configure(state=DISABLED)
		sys.stdout = old_stdout

		self.show_options()

	def show_options(self):
		widget1_options = set()
		widget2_options = set()

		if issubclass(self.widget1.__class__, BaseWidget) and type(
				self.widget1) not in {Widget, ttk.Widget}:
			widget1_options = set(self.widget1.configure().keys())
			if 'text' in widget1_options:
				self.widget1['text'] = self.cbox1_var.get()
			if 'height' in widget1_options:
				self.widget1['height'] = 50
				self.widget1.propagate(0)

		if issubclass(self.widget2.__class__, BaseWidget) and type(
				self.widget2) not in {Widget, ttk.Widget}:
			widget2_options = set(self.widget2.configure().keys())

		unique_options = sorted(widget1_options - widget2_options)

		old_stdout = sys.stdout
		sys.stdout = my_stdout = io.StringIO()
		self.options_text.configure(state=NORMAL)
		print(f"{self.widget1.__doc__}\n")
		print(f"Unique Options of {self.widget1.__class__} "
		      f"   ⇆    {self.widget2.__class__}\n")
		print(unique_options)
		print(f"\nAll Options on {self.widget1.__class__}\n")
		for option in sorted(widget1_options):
			try:
				print("{:<}".format(option))
				if self.widget1.config()[option][3]:
					print("Default value is:",
					      self.widget1.config()[option][3])
				print("{:<}\n".format(options[option]))
			except KeyError:
				# self.bell()
				print('no hint available\n')
			except IndexError as err:
				# self.bell()
				print('not available\n')
				pass
			else:
				pass

		screen_text = my_stdout.getvalue()
		self.options_text.replace(0.1, 'end', screen_text)

		self.options_text.configure(state=DISABLED)
		sys.stdout = old_stdout

	def log_event(self, event):
		self.events_text.configure(state=NORMAL)
		if (type(event.keycode) is int) and (event.keycode not in {8}):
			self.events_text.insert(0.1,
			                        f"|  STATE MASK: {event.state} == "
			                        f"{hex(event.state)} == "
			                        f"{bin(event.state)}  "
			                        f"|  KEYSYM_NUM: {event.keysym_num}\n"
			                        f"{120 * '-'}\n")
		self.events_text.insert(0.1, f"{event}\n")
		self.events_text.configure(state=DISABLED)

	# def generate_events(self):
	# 	for keysym in keysyms:
	# 		try:
	# 			self.event_generate("<KeyPress>", keysym=keysym)
	# 		except TclError as err:
	# 			print(err)


app = Application()
app.master.title('Tkinter Help Tool')
app.mainloop()
