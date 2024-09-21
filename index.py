import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Payment Form")

# Set the size of the window
root.geometry("400x300")

# Function to handle form submission
def submit_form():
    name = name_entry.get()
    amount = amount_entry.get()
    
    # Check if the fields are filled
    if name and amount:
        try:
            amount = float(amount)  # Convert amount to float
            messagebox.showinfo("Success", f"Payment of ${amount} from {name} received!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

# Labels and Entry Fields
name_label = tk.Label(root, text="Full Name:")
name_label.pack(pady=10)

name_entry = tk.Entry(root)
name_entry.pack(pady=10)

amount_label = tk.Label(root, text="Amount (in USD):")
amount_label.pack(pady=10)

amount_entry = tk.Entry(root)
amount_entry.pack(pady=10)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack(pady=20)

# Run the application
root.mainloop()
