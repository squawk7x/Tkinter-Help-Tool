
#!/usr/bin/env python
import io
import re
import sys
from tkinter import *
from tkinter import ttk, font
from tkinter import messagebox, filedialog, colorchooser
from tkinter.scrolledtext import ScrolledText
import inspect


def filter_list(_list=None, pattern=None):
	sorted_filtered_list = sorted(set([val for val in _list
	                                   if re.search(pattern, val)]).difference(
		{'children', 'master'}))
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
		self.rb_winfo = None
		self.layout_var = None
		self.rb_off = None
		self.rb_place = None
		self.rb_pack = None
		self.rb_grid = None
		self.layout_frm = None
		self.w_frm = None
		self.caption_label = None
		self.definition_label = None
		self.cbox1 = None
		self.cbox2 = None
		self.toggleButton = None
		self.showButton = None
		self.widget1 = None
		self.widget2 = None
		self.help_text = None
		self.definition_var = StringVar()
		self.cbox1_var = StringVar()
		self.cbox2_var = StringVar()
		self.configure(height=800, width=550, padx=2, pady=2)
		self.grid(sticky='nesw')
		self.createWidgets()

	def toggle(self):
		temp1 = self.cbox1_var.get()
		temp2 = self.cbox2_var.get()
		self.cbox2_var.set(temp1)
		self.cbox1_var.set(temp2)
		self.showButton.invoke()

	def show_help_on_widget(self):

		for w in self.w_frm.winfo_children():
			w.destroy()

		if self.cbox1_var.get() in {'Misc', 'Pack', 'Place',
		                            'Grid', 'object'}:
			self.widget1 = eval(F"{self.cbox1_var.get()}()")
		elif self.cbox1_var.get() in {'BaseWidget'}:
			self.widget1 = eval(
				F"{self.cbox1_var.get()}(self.w_frm, 'toplevel')")
		elif self.cbox1_var.get() in {'ttk.Widget', 'Widget'}:
			self.widget1 = eval(F"{self.cbox1_var.get()}(self.w_frm, None)")
		elif self.cbox1_var.get() in {'messagebox'}:
			self.widget1 = eval(F"{self.cbox1_var.get()}")
		# messagebox.showinfo('Tkinter Help Tool', 'Version 1.0')
		elif self.cbox1_var.get() in {'filedialog'}:
			self.widget1 = eval(F"{self.cbox1_var.get()}")
		# filedialog.askdirectory()
		elif self.cbox1_var.get() in {'colorchooser'}:
			self.widget1 = eval(F"{self.cbox1_var.get()}")
		# colorchooser.askcolor()
		elif self.cbox1_var.get() in self.cbox1['values']:
			self.widget1 = eval(F"{self.cbox1_var.get()}(self.w_frm)")
			if issubclass(self.widget1.__class__, Widget):
				self.widget1.pack(fill='x')
		else:
			self.widget1 = eval(F"{self.cbox1_var.get()}()")

		self.definition_var.set(F"w = {self.cbox1_var.get()}" + str(
			inspect.signature(self.widget1.__init__)))

		if self.cbox2_var.get() in {'Misc', 'Pack', 'Place',
		                            'Grid', 'object'}:
			self.widget2 = eval(F"{self.cbox2_var.get()}()")
		elif self.cbox2_var.get() in {'messagebox', 'filedialog',
		                              'colorchooser'}:
			self.widget2 = eval(F"{self.cbox2_var.get()}")
		elif self.cbox2_var.get() in {'BaseWidget'}:
			self.widget2 = eval(
				F"{self.cbox2_var.get()}(self.w_frm, 'toplevel')")
		elif self.cbox2_var.get() in {'ttk.Widget', 'Widget'}:
			self.widget2 = eval(F"{self.cbox2_var.get()}(self.w_frm, None)")
		elif self.cbox2_var.get() in self.cbox2['values']:
			self.widget2 = eval(F"{self.cbox2_var.get()}(self.w_frm)")

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

		if pattern := self.layout_var.get():
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

		self.help_text.configure(state=NORMAL)
		header = f'Unique Methods of {self.cbox1_var.get()} vs. {self.cbox2_var.get()}:\n\n'
		self.help_text.replace(0.1, 'end',
		                       header + str(unique_methods) + '\n\n')
		if issubclass(self.widget1.__class__, BaseWidget):
			self.help_text.insert('end', + 79 * '_' + '\n' + inspect.getsource(
				self.widget1.__init__))
		self.help_text.insert('end', screen_txt)
		self.help_text.configure(state=DISABLED)
		sys.stdout = old_stdout

	def createWidgets(self):
		top = self.winfo_toplevel()
		self.caption_label = ttk.Label(self, textvariable=self.cbox1_var,
		                               anchor='center',
		                               style='Caption.TLabel')
		self.definition_label = Label(self, textvariable=self.definition_var,
		                              bg='#e0e0e0', relief='ridge')
		self.cbox1 = ttk.Combobox(self, textvariable=self.cbox1_var)
		self.cbox2 = ttk.Combobox(self, textvariable=self.cbox2_var)

		self.cbox1['values'] = (('ttk.Button', 'ttk.Radiobutton',
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
		                         'Radiobutton', 'Entry',
		                         'Frame', 'Label',
		                         'LabelFrame',
		                         'Menubutton',
		                         'PanedWindow',
		                         'Radiobutton', 'Scale',
		                         'Scrollbar',
		                         'Spinbox',
		                         'Text') +
		                        ('Widget', 'BaseWidget', 'Misc') +
		                        ('Pack', 'Place', 'Grid') +
		                        ('messagebox', 'filedialog', 'colorchooser') +
		                        ('object',))

		self.cbox2['values'] = self.cbox1['values']
		self.cbox1_var.set('ttk.Button')
		self.cbox2_var.set('Widget')
		self.help_text = ScrolledText(self, bg='#ffffdd', wrap='word',
		                              font=font.Font(size=10), height=45)
		self.toggleButton = ttk.Button(self, text='⇆', command=self.toggle)
		self.showButton = ttk.Button(self,

		                             text='↖ Unique Methods compared to ↗',
		                             command=self.show_help_on_widget)

		self.w_frm = ttk.Labelframe(self, text='Widget', labelanchor='n',
		                            width=120, height=40)
		self.w_frm.propagate(False)
		self.w_frm.grid(column=0, row=5, sticky='ns')
		self.layout_var = StringVar()
		self.layout_frm = ttk.Labelframe(self,
		                                 text='Method Filter', labelanchor='n')
		self.rb_off = ttk.Radiobutton(self.layout_frm, text='off',
		                              variable=self.layout_var, value='',
		                              command=self.show_help_on_widget)
		self.rb_winfo = ttk.Radiobutton(self.layout_frm, text='winfo',
		                                variable=self.layout_var,
		                                value='^winfo',
		                                command=self.show_help_on_widget)
		self.rb_grid = ttk.Radiobutton(self.layout_frm, text='grid',
		                               variable=self.layout_var, value='^grid',
		                               command=self.show_help_on_widget)
		self.rb_pack = ttk.Radiobutton(self.layout_frm, text='pack',
		                               variable=self.layout_var, value='^pack',
		                               command=self.show_help_on_widget)
		self.rb_place = ttk.Radiobutton(self.layout_frm, text='place',
		                                variable=self.layout_var,
		                                value='^place',
		                                command=self.show_help_on_widget)

		self.caption_label.grid(column=0, row=0, sticky='ew',
		                        columnspan=3)
		self.definition_label.grid(column=0, row=2, sticky='ew', columnspan=3)
		self.cbox1.grid(column=0, row=3, sticky='n')
		self.toggleButton.grid(column=1, row=3, sticky='n')
		self.cbox2.grid(column=2, row=3, sticky='n')
		self.showButton.grid(column=1, row=5, padx=5, pady=10, sticky='ns')
		self.layout_frm.grid(column=2, row=5, sticky='ns')
		self.rb_off.invoke()
		self.rb_off.grid(column=0, row=1)
		self.rb_winfo.grid(column=2, row=1)
		self.rb_grid.grid(column=1, row=0)
		self.rb_pack.grid(column=1, row=1)
		self.rb_place.grid(column=1, row=2)
		self.help_text.grid(column=0, row=10, columnspan=3, sticky='nesw')

		for w in self.winfo_children():
			w.grid_configure(padx=3, pady=3)

		top.rowconfigure(0, weight=1)
		top.columnconfigure(0, weight=1)
		self.columnconfigure('all', weight=1)
		self.rowconfigure('all', weight=0)
		self.rowconfigure(10, weight=3)

		self.cbox1.bind("<<ComboboxSelected>>",
		                lambda e: self.showButton.invoke())
		self.cbox2.bind("<<ComboboxSelected>>",
		                lambda e: self.showButton.invoke())


app = Application()
app.master.title('Tkinter Help Tool')
app.mainloop()
