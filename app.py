import tkinter as tk
from tkinter import ttk
from turtledemo.clock import setup


class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.style = ttk.Style()

        self.setup_style()
        self.setup_window()
        self.create_widgets()

    def setup_style(self):
        self.style.theme_use('default')
        #self.style.configure("TFrame", background="#2c3e50")

    def setup_window(self):
        """Configure the main window"""
        self.root.title("Optimise Your Life")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

    def create_widgets(self):
        """Create and layout all widgets"""
        # Main frame with padding
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill="both", expand=True)

        # Title
        title_label = ttk.Label(
            main_frame,
            text="Optimise Your Life",
            font=('Segoe UI', 16, 'bold')
        )
        title_label.pack(pady=(0, 20))

        # Input section
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=(0, 15))

        ttk.Label(input_frame, text="Enter your name:").pack(anchor=tk.W)
        self.name_entry = ttk.Entry(input_frame, font=('Segoe UI', 10))
        self.name_entry.pack(fill=tk.X, pady=(5, 0))

        # Button
        self.greet_btn = ttk.Button(
            main_frame,
            text="Say Hello",
            command=self.greet_user,
            style='Accent.TButton'
        )
        self.greet_btn.pack(pady=(0, 15))

        # Output label
        self.output_label = ttk.Label(
            main_frame,
            text="",
            font=('Segoe UI', 12),
            foreground='#2E7D32'
        )
        self.output_label.pack()

    def greet_user(self):
        """Handle button click"""
        name = self.name_entry.get().strip()
        if name:
            self.output_label.config(text=f"Hello, {name}! 👋")
        else:
            self.output_label.config(text="Please enter your name first!")

    def run(self):
        """Start the application"""
        self.root.mainloop()
