import tkinter as tk
from tkinter import ttk

import random

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play():
    player_choice = player_var.get()
    computer_choice = get_computer_choice()
    
    result = determine_winner(player_choice, computer_choice)
    result_label.config(text=f"Computer chose {computer_choice}. {result}")

# Create the main window
window = tk.Tk()
window.title("Soham's Rock-Paper-Scissors Game")  # Modified title

# Add some Tkinter styling
style = ttk.Style()

# Configure the window background color
window.configure(bg="#FFD3D3")  # Light red background color

# Configure the window border
window.attributes('-alpha', 0.95)  # Opacity for a light border effect

# Configure button font and border
style.configure("TButton", font=("Arial", 12), borderwidth=2, relief="solid")  # Button font, border, and relief

# Configure label font, border, and background
style.configure("TLabel", font=("Arial", 14, "bold"), borderwidth=2, relief="solid", background="#FFD3D3")  # Label font, border, and background

# Create a label for user instructions
instructions_label = ttk.Label(window, text="Choose Rock, Paper, or Scissors:", style="TLabel")
instructions_label.pack()

# Create a variable to store the player's choice
player_var = tk.StringVar()

# Create radio buttons for player's choices
rock_button = ttk.Radiobutton(window, text="Rock", variable=player_var, value="Rock", style="TButton")
rock_button.pack()

paper_button = ttk.Radiobutton(window, text="Paper", variable=player_var, value="Paper", style="TButton")
paper_button.pack()

scissors_button = ttk.Radiobutton(window, text="Scissors", variable=player_var, value="Scissors", style="TButton")
scissors_button.pack()

# Create a button to play the game
play_button = ttk.Button(window, text="Play", command=play, style="TButton")
play_button.pack()

# Create a label to display the result
result_label = ttk.Label(window, text="", style="TLabel")
result_label.pack()

# Start the Tkinter event loop
window.mainloop()
