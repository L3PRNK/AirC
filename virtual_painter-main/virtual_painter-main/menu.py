import tkinter as tk
from tkinter import PhotoImage
import os

def execute_file(file_path):
    os.system(f"python {file_path}")

def option1_clicked():
    execute_file("file.py")

def option2_clicked():
    execute_file("app.py")

def option3_clicked():
    execute_file("file3.py")

def main():
    root = tk.Tk()
    root.title("OpenCVLAB")

    root.geometry("1200x700")  # Set window size

    # Load background image
    bg_image = PhotoImage(file="bg2.png")

    # Function to create buttons with consistent styling
    def create_button(text, command):
        button = tk.Button(root, text=text, command=command, width=20, height=2, bg="black", fg="white", font=("Helvetica", 14))
        return button

    # Create buttons
    option1_button = create_button("Air Canvas", option1_clicked)
    option2_button = create_button("Streaming", option2_clicked)
    option3_button = create_button("Guesture Recognation", option3_clicked)

    # Place buttons in the middle
    option1_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    option2_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    option3_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    # Add background image
    background_label = tk.Label(root, image=bg_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Bring buttons to front
    option1_button.lift()
    option2_button.lift()
    option3_button.lift()

    root.mainloop()

if __name__ == "__main__":
    main()
