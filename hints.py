options = {
	"class": "The widget class name.\n"
	         "This may be specified when the widget is created, but cannot "
	         "be changed later.",
	"command": "A function to be called when the widget is asking for, "
	           "for example when a button is pushed.",
	"compound": "If you provide both image and text options, the compound "
	            "option specifies the position of the image relative to the "
	            "text. The value may be tk.TOP (image above text), tk.BOTTOM "
	            "(image below text), tk.LEFT (image to the left of the text), "
	            "or tk.RIGHT (image to the right of the text)."
	            "When you provide both image and text options but don't "
	            "specify a compound option, the image will appear and the "
	            "text will not be displayed.",
	"cursor": "The cursor that will appear when the mouse is over the widget.",
	"image": "To display a graphic image on the widget, set this option to an "
	         "image object.",
	"style": "The style to be used in rendering this widget.",
	"takefocus": "By default, a ttk.widget will be included in focus "
	             "traversal. To remove the widget from focus traversal, "
	             "use takefocus=False or takefocus=0."
	             "Normally, keyboard focus does visit buttons and a space "
	             "character acts as the same as a mouse click, “pushing” the "
	             "button. You can set the takefocus option to zero to prevent "
	             "focus from visiting the widget. If you set this option to "
	             "1, focus will always visit this widget. Set it to '' to get "
	             "the default behavior. ",
	"text": "The text to appear on the widget, as a string. Use newlines ("
	        "'\\n') to display multiple lines of text. ",
	"textvariable": "If you need to change the label on a widget during "
	                "execution, create a StringVar to manage the "
	                "current value, and set this option to that control "
	                "variable. Whenever the control variable's value changes, "
	                "the widgets's annotation will automatically change "
	                "as well. "
	                "For the entry widget in order to be able to retrieve the "
	                "current text from your entry widget, you must set this "
	                "option to an instance of the StringVar class; You "
	                "can retrieve the text using v.get(), or set it using "
	                "v.set(), where v is the associated control variable. ",
	"underline": "Default is -1, meaning that no character of the text on the "
	             "button will be underlined. Set this option to the "
	             "index of a character in the text (counting from zero) to "
	             "underline that character. For example, underline=1"
	             "would underline the second character of the button's text.",

	"validate": "You can use this option to set up the widget so that its "
	            "contents are checked by a validation function at certain "
	            "times.",
	"validatecommand": "A callback that validates the text of the widget.",
	"variable": "The control variable that tracks the current state of the "
	            "widget; For checkbutton this variable is an IntVar, "
	            "and 0 means cleared and 1 means set, but see the offvalue "
	            "and onvalue options above.",
	"width": "If the label is text, this option specifies the absolute width "
	         "of the text area on the widget, as a number of characters. the "
	         "actual width is that number multiplied by the average width of "
	         "a character in the current font. For image labels, this option "
	         "is ignored. The option may also be configured in a style. The "
	         "horizontal dimension of the new frame will be ignored "
	         "unless you also call .grid_propagate(0) on the frame; ",

	"activebackground": "Background color when the widget is under the cursor. "
	                    "Use a style map to control the background option.",
	"activeforeground": "Foreground color when the widget is under the cursor. "
	                    "Use a style map to control the foreground option.",

	"activestyle": "This option specifies the appearance of the active line. "
	               "It may have any of these values:"
	               "'underline'  The active line is underlined. This is the "
	               "default option."
	               "'dotbox' The active line is enclosed in a dotted line on "
	               "all four sides."
	               "'none' The active line is given no special appearance. ",
	"anchor": "If the widget inhabits a space larger than it needs, "
	          "this option specifies where the widget will sit in that "
	          "space. The default is anchor=tk.CENTER. "
	          "For example, if you use  anchor=NW, the widget will be placed "
	          "in the upper left corner of the space."
	          "When the widget displays an image but no text, this option is "
	          "ignored.",
	"background": "Normal background color. For the bitmap option, this "
	              "specifies the color displayed for 0-bits in the bitmap. "
	              "Configure the background option using a style.",
	"bg": "Normal background color. For the bitmap option, this "
	      "specifies the color displayed for 0-bits in the bitmap. "
	      "Configure the background option using a style.",
	"bitmap": "Name of one of the standard bitmaps to display on the widget ("
	          "instead of text). To display a monochrome image on a button, "
	          "set this option to a bitmap.",
	"borderwidth": "The size of the border around the widget. Default is two "
	               "pixels. Configure the borderwidth option using a style. ",
	"bd": "The size of the border around the widget. Default is two "
	      "pixels. Configure the borderwidth option using a style. ",
	"closeenough": "A float that specifies how close the mouse must be to an "
	               "item to be considered inside it. Default is 1.0. ",
	"confine": "If true (the default), the canvas cannot be scrolled outside of "
	           "the scrollregion (see below). ",
	"default": "tk.NORMAL is the default; use tk.DISABLED if the widget is to "
	           "be initially disabled (grayed out, unresponsive to mouse "
	           "clicks).",
	"disabledbackground": "The background color to be displayed when the "
	                      "widget is in the tk.DISABLED state. Use a style "
	                      "map for the foreground option.",
	"disabledforeground": "The foreground color to be displayed when the "
	                      "widget is in the tk.DISABLED state."
	                      "Use a style map for the foreground option.",
	"exportselection": "By default, if you select text within an Entry widget, "
	                   "it is automatically exported to the clipboard. To avoid "
	                   "this exportation, use exportselection=0. ",
	"font": "Text font to be used for the widget's label. Configure this "
	        "option using a style.",
	"fg": "Normal foreground (text) color. Configure this option using a "
	      "style. For the bitmap option, this specifies the color displayed "
	      "for 1-bits in the bitmap. ",
	"foreground": "Normal foreground (text) color. Configure this option "
	              "using a style. For the bitmap option, this specifies the "
	              "color displayed for 1-bits in the bitmap. ",
	"height": "Height of the widget in text lines (for textual widgets) or "
	          "pixels (for images). The vertical dimension of the new frame. "
	          "This will be ignored unless you also call .grid_propagate(0) "
	          "on the frame; Number of lines (not pixels!) shown in the "
	          "listbox. Default is 10. ",
	"highlightbackground": "To control the color of the focus highlight when "
	                       "the widget does not have focus, use a style map "
	                       "to control the highlightcolor option.",
	"highlightcolor": "The color of the focus highlight when the widget "
	                  "has the focus. You may specify the default focus "
	                  "highlight color by setting this option in a style. You "
	                  "may also control the focus highlight color using a "
	                  "style map.",
	"highlightthickness": "Thickness of the focus highlight. Configure this "
	                      "option using a style. This option may not work in "
	                      "all themes.",
	"indicatoron": "Normally a checkbutton displays as its indicator a box "
	               "that shows whether the checkbutton is set or not. You can "
	               "get this behavior by setting indicatoron=1. However, "
	               "if you set indicatoron=0, the indicator disappears, "
	               "and the entire widget becomes a push-push button that "
	               "looks raised when it is cleared and sunken when it is "
	               "set. You may want to increase the borderwidth value to "
	               "make it easier to see the state of such a control. ",

	"insertbackground": "By default, the insertion cursor (which shows the "
	                    "point within the text where new keyboard input will "
	                    "be inserted) is black. To get a different color of "
	                    "insertion cursor, set insertbackground to any color;",
	"insertborderwidth": "By default, the insertion cursor is a simple "
	                     "rectangle. You can get the cursor with the tk.RAISED "
	                     "relief effect by setting insertborderwidth to the "
	                     "dimension of the 3-d border. If you do, make sure "
	                     "that the insertwidth option is at least twice that "
	                     "value. ",
	"insertofftime": "Similar to insertofftime, this option specifies how much "
	                 "time the cursor spends on per blink. Default is 600 ("
	                 "milliseconds). ",
	"insertwidth": "By default, the insertion cursor is 2 pixels wide. You can "
	               "adjust this by setting insertwidth to any dimension. ",
	"justify": "How to show multiple text lines: tk.LEFT to left-justify each "
	           "line; tk.CENTER to center them; or tk.RIGHT to right-justify."
	           "If the text contains newline ('\n') characters, the text will"
	           "occupy multiple lines on the widget. The justify option "
	           "controls how each line is positioned horizontally. Configure "
	           "this option using a style.",
	"labelanchor": "Use this option to specify the position of the label on "
	               "the widget's border. The default position is 'nw', "
	               "which places the label at the left end of the top border. ",
	"labelwidget": "Instead of a text label, you can use any widget as the "
	               "label by passing that widget as the value of this option. "
	               "If you supply both labelwidget and text options, the text "
	               "option is ignored. ",
	"listvariable": "A StringVar that is connected to the complete list of "
	                "values in the listbox. If you call the .get() method of "
	                "the listvariable, you will get back a string of the form "
	                "('v0', 'v1', ...), where each vi is the contents of one "
	                "line of the listbox. To change the entire set of lines in "
	                "the listbox at once, call .set(s) on the listvariable, "
	                "where s is a string containing the line values with "
	                "spaces between them. For example, if listCon is a "
	                "StringVar associated with a listbox's listvariable "
	                "option, this call would set the listbox to contain three "
	                "lines:  listCon.set('ant bee cicada')"
	                "This call would return the string ('ant', 'bee', "
	                "'cicada'):  listCon.get()",
	"offrelief": "By default, checkbuttons use the tk.RAISED relief style when "
	             "the button is off (cleared); use this option to specify a "
	             "different relief style to be displayed when the button is "
	             "off.",
	"offvalue": "Normally, a checkbutton's associated control variable will be "
	            "set to 0 when it is cleared (off). You can supply an alternate "
	            "value for the off state by setting offvalue to that value.",
	"onvalue": "Normally, a checkbutton's associated control variable will be "
	           "set to 1 when it is set (on). You can supply an alternate "
	           "value for the on state by setting onvalue to that value."
	           "value for the off state by setting offvalue to that value.",
	"overrelief": "The relief style to be used while the mouse is over the "
	              "widget; default relief is tk.RAISED.Use a style map to "
	              "control the relief option. Default is 1 pixel. ",
	"padx": "Additional padding left and right of the text.",
	"pady": "Additional padding above and below the text.",
	"readonlybackground": "The background color to be displayed when the "
	                      "widget's state option is 'readonly'. ",

	"relief": "Specifies the relief type for the widget. With the default "
	          "value, relief=tk.FLAT, the widget does not stand out from "
	          "its background. You may set this option to any of the other "
	          "styles, or use  relief=tk.SOLID, which gives you a solid black "
	          "frame around it. Other options are tk.RIDGE and tk.SUNKEN."
	          "Configure this option using a style.",
	"repeatdelay": "See repeatinterval, below.",
	"repeatinterval": "Normally, a button fires only once when the user "
	                  "releases the mouse button. If you want the button to "
	                  "fire at regular intervals as long as the mouse button "
	                  "is held down, set this option to a number of "
	                  "milliseconds to be used between repeats, and set the "
	                  "repeatdelay to the number of milliseconds to wait "
	                  "before starting to repeat. For example, if you specify "
	                  "“repeatdelay=500, repeatinterval=100” the button will "
	                  "fire after half a second, and every tenth of a second "
	                  "thereafter, until the user releases the mouse button."
	                  "If the user does not hold the mouse button down at "
	                  "least repeatdelay milliseconds, the button will fire "
	                  "normally.",

	"scrollregion": "A tuple (w, n, e, s) that defines over how large an area "
	                "the canvas can be scrolled, where w is the left side, "
	                "n the top, e the right side, and s the bottom. ",

	"selectcolor": "The color of the checkbutton when it is set. Default is "
	               "selectcolor='red'.",
	"selectbackground": "The background color to use displaying selected items. ",
	"selectborderwidth": "The width of the border to use around selected "
	                     "items. The default is one pixel.  ",
	"selectforeground": "The foreground color to use displaying selected items. ",
	"selectimage": "TIf you set this option to an image, that image will appear "
	               "in the checkbutton when it is set.",
	"selectmode": "Determines how many items can be selected, and how mouse "
	              "drags affect the selection: "
	              "tk.BROWSE: Normally, you can only select one line out of a "
	              "listbox. If you click on an item and then drag to a "
	              "different line, the selection will follow the mouse. This "
	              "is the default. "
	              "tk.SINGLE: You can only select one line, and you can't drag "
	              "the mouse—wherever you click button 1, that line is "
	              "selected. "
	              "tk.MULTIPLE: You can select any number of lines at once. "
	              "Clicking on any line toggles whether or not it is "
	              "selected. "
	              "tk.EXTENDED: You can select any adjacent group of lines at "
	              "once by clicking on the first line and dragging to the last "
	              "line. ",
	"show": "Normally, the characters that the user types appear in the entry. "
	        "To make a “password” entry that echoes each character as an "
	        "asterisk, set show='*'. ",
	"state": "Different widgets have different default values for this option. "
	         "Possible values are: tk.ACTIVE, tk.NORMAL tk.DISABLED."
	         "Use this option to disable the Entry "
	         "widget so that the user can't type anything into it. Use "
	         "state=tk.DISABLED to disable the widget, state=tk.NORMAL to "
	         "allow user input again. Your program can also find out whether "
	         "the cursor is currently over the widget by interrogating this "
	         "option; it will have the value tk.ACTIVE when the mouse is over "
	         "it. You can also set this option to 'disabled', which is like "
	         "the tk.DISABLED state, but the contents of the widget can still "
	         "be selected or copied. In ttk, there is no option with this "
	         "name. The state mechanism"
	         "has been generalized.",

	"wraplength": "If this value is set to a positive number, the text lines "
	              "will be wrapped to fit within this length. If you use a "
	              "style with this option set to some dimensions, the text "
	              "will be sliced into pieces no longer than that dimension.",

	"xscrollcommand": "If the widget is scrollable, set this option to the .set("
	                  ") method of the horizontal scrollbar. If you expect "
	                  "that users will often enter more text than the "
	                  "onscreen size of the widget, you can link your  "
	                  "widget to a scrollbar.",

	"xscrollincrement": "Normally, canvases can be scrolled horizontally to "
	                    "any position. You can get this behavior by setting "
	                    "xscrollincrement to zero. If you set this option to "
	                    "some positive dimension, the canvas can be "
	                    "positioned only on multiples of that distance, "
	                    "and the value will be used for scrolling by "
	                    "scrolling units, such as when the user clicks on the "
	                    "arrows at the ends of a scrollbar.",
	"yscrollincrement": "Works like incrementalist, but governs vertical "
	                    "movement. ",

	"yscrollcommand": "If the widget is scrollable, this option should be the "
	                  ".set() method of the vertical scrollbar."
}
