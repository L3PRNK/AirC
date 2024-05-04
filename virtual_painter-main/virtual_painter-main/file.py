import tkinter as tk
from tkinter import PhotoImage
import os

def start_main_py():
    os.system("python main.py")

def main():
    root = tk.Tk()
    root.title("Menu")
    root.geometry("1200x700")  # Set window size

    # Load background image
    bg_image = PhotoImage(file="BG2.png")

    # Add background image
    background_label = tk.Label(root, image=bg_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Create "Start" button with blue background
    start_button = tk.Button(root, text="Start", command=start_main_py, bg="blue", fg="white", font=("Helvetica", 20), bd=0, highlightthickness=0)
    start_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    start_button.lift()  # Lift the button to the front

    root.mainloop()

if __name__ == "__main__":
    main()
