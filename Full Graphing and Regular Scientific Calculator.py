import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import tkinter.messagebox
from scipy.optimize import fsolve

# Function to handle trigonometric and scientific notations
def trigs(fom):
    fom = fom.replace("^", "**")
    fom = fom.replace("sin", "np.sin")
    fom = fom.replace("cos", "np.cos")
    fom = fom.replace("tan", "np.tan")
    fom = fom.replace("pi", "np.pi")
    fom = fom.replace("e", "np.e")
    fom = fom.replace("sqrt", "np.sqrt")
    fom = fom.replace("log", "np.log")
    fom = fom.replace("ln", "np.log")
    fom = fom.replace("exp", "np.exp")
    return fom

class GraphingAndScientificCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Graphing and Scientific Calculator")

        # Create a menu bar
        self.menu_bar = tk.Menu(master)
        master.config(menu=self.menu_bar)

        # Create Help menu
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="How to Use", command=self.show_help)

        # Create frames for content
        self.main_frame = tk.Frame(master)
        self.main_frame.pack(side=tk.LEFT, padx=20, pady=20)

        self.sidebar_frame = tk.Frame(master)
        self.sidebar_frame.pack(side=tk.RIGHT, padx=20, pady=20)

        # Frame for Scientific Calculator
        self.calc_frame = tk.Frame(master)
        self.calc_frame.pack(side=tk.LEFT, padx=20, pady=20)

        # ** Graphing Calculator Components ** #
        # Input for equation
        self.equation_label = tk.Label(self.main_frame, text="Enter Equation (y = f(x)):", font=("Arial", 24))
        self.equation_label.pack(pady=10)
        self.equation_entry = tk.Entry(self.main_frame, font=("Arial", 20), width=20)
        self.equation_entry.pack(pady=10)

        # Plot button
        self.plot_button = tk.Button(self.main_frame, text="Plot", command=self.plot_graph, font=("Arial", 20), height=3, width=12)
        self.plot_button.pack(pady=20)

        # Figure and canvas for the plot
        self.fig = plt.figure(figsize=(12, 9))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.main_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

        # Input for finding x or y
        self.x_value_label = tk.Label(self.sidebar_frame, text="Enter x Value:", font=("Arial", 18))
        self.x_value_label.pack(pady=10)
        self.x_value_entry = tk.Entry(self.sidebar_frame, font=("Arial", 16), width=10)
        self.x_value_entry.pack(pady=10)
        self.find_y_button = tk.Button(self.sidebar_frame, text="Find y", font=("Arial", 16), command=self.find_y_value, height=2, width=10)
        self.find_y_button.pack(pady=10)

        self.y_value_label = tk.Label(self.sidebar_frame, text="Enter y Value:", font=("Arial", 18))
        self.y_value_label.pack(pady=10)
        self.y_value_entry = tk.Entry(self.sidebar_frame, font=("Arial", 16), width=10)
        self.y_value_entry.pack(pady=10)
        self.find_x_button = tk.Button(self.sidebar_frame, text="Find x", font=("Arial", 16), command=self.find_x_value, height=2, width=10)
        self.find_x_button.pack(pady=10)

        # Bind "Enter" key to plot_graph method
        self.master.bind("<Return>", self.enter_pressed)

        # ** Scientific Calculator Components ** #
        # Entry for the calculator
        self.calc_entry = tk.Entry(self.calc_frame, font=("Arial", 24), width=15)
        self.calc_entry.grid(row=0, column=0, columnspan=4, pady=10)

        # Buttons for the calculator
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('sqrt', 5, 3),
            ('log', 6, 0), ('ln', 6, 1), ('exp', 6, 2), ('pi', 6, 3)
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(self.calc_frame, text=text, font=("Arial", 18), width=5, height=2, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)

    def show_help(self):
        help_text = (
            "How to Use:\n\n"
            "Graphing Calculator:\n"
            "1. Enter an equation in the form y = f(x) in the input field.\n"
            "2. Click 'Plot' or press Enter to plot the graph of the equation.\n"
            "3. To find the value of y for a specific x, use 'Find y'.\n"
            "4. To find the value of x for a specific y, use 'Find x'.\n\n"
            "Scientific Calculator:\n"
            "1. Use the number buttons and operators (+, -, *, /) for calculations.\n"
            "2. Use functions like sin, cos, tan, sqrt, log, ln, and exp for scientific calculations.\n"
            "3. Use the 'C' button to clear the entry, and '=' to calculate the result."
        )
        tk.messagebox.showinfo("Help", help_text)

    def plot_graph(self):
        try:
            equation = self.equation_entry.get()
            equation = trigs(equation)
            x = np.linspace(-10, 10, 1000)
            y = eval(equation)
            self.fig.clear()
            plt.plot(x, y)
            plt.grid(True)
            self.canvas.draw()

        except Exception as e:
            tk.messagebox.showerror("Error", f"Invalid equation: {e}")

    def find_y_value(self):
        try:
            equation = self.equation_entry.get()
            equation = trigs(equation)
            x_value = float(self.x_value_entry.get())
            y_value = eval(equation.replace("x", str(x_value)))
            tk.messagebox.showinfo("Result", f"For x = {x_value}, y = {y_value}")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Invalid input: {e}")

    def find_x_value(self):
        try:
            equation = self.equation_entry.get()
            equation = trigs(equation)
            y_value = float(self.y_value_entry.get())
            def equation_function(x):
                return eval(equation.replace("x", str(x))) - y_value
            x_solution = fsolve(equation_function, 0)[0]
            tk.messagebox.showinfo("Result", f"For y = {y_value}, x = {x_solution}")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Invalid input: {e}")

    def enter_pressed(self, event):
        self.plot_graph()

    def on_button_click(self, button_text):
        entry = self.calc_entry.get()
        
        if button_text == "=":
            try:
                entry = trigs(entry)  # Convert trigonometric and scientific functions
                result = eval(entry)
                self.calc_entry.delete(0, tk.END)
                self.calc_entry.insert(tk.END, str(result))
            except Exception as e:
                self.calc_entry.delete(0, tk.END)
                self.calc_entry.insert(tk.END, "Error")
        
        elif button_text == "C":
            self.calc_entry.delete(0, tk.END)
        
        else:
            self.calc_entry.insert(tk.END, button_text)

root = tk.Tk()
calculator = GraphingAndScientificCalculator(root)
root.mainloop()
