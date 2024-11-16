import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import requests
from PIL import ImageTk, Image

# Initialize the main application window
root = tk.Tk()
root.geometry('600x500')
root.title("Currency Converter")
root.iconbitmap('D:\\Project\\icon.ico')

# Load and display the image
try:
    image = Image.open('D:\\Project\\currency.png')
    zoom = 0.5
    pixels_x, pixels_y = tuple([int(zoom * x) for x in image.size])
    img = ImageTk.PhotoImage(image.resize((pixels_x, pixels_y)))
    panel = tk.Label(root, image=img)
    panel.place(x=200, y=10)
except FileNotFoundError:
    messagebox.showerror("File Error", "Image file not found. Please check the file path.")

# Function to fetch and display conversion rates
def show_data():
    amount = E1.get()
    from_currency = c1.get()
    to_currency = c2.get()
    url = f"https://v6.exchangerate-api.com/v6/f915557257aa5b1c351d14b0/latest/{from_currency}"  # Replace YOUR_API_KEY with your actual key

    try:
        if not amount:
            raise ValueError("Please enter the amount.")
        if not from_currency or not to_currency:
            raise ValueError("Please select both currencies.")

        # Fetch exchange rates
        data = requests.get(url).json()
        if data.get('result') != 'success':
            raise Exception("Failed to fetch exchange rates.")
        
        conversion_rates = data['conversion_rates']
        if to_currency not in conversion_rates:
            raise ValueError("Invalid target currency.")
        
        # Perform conversion
        amount = float(amount)
        converted_amount = round(amount * conversion_rates[to_currency], 2)

        # Display results
        E2.delete(0, 'end')
        E2.insert(0, converted_amount)
        text.delete(1.0, 'end')
        text.insert('end', f'{amount} {from_currency} = {converted_amount} {to_currency}\n\n')
        text.insert('end', f'Last Updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to clear inputs and outputs
def clear():
    E1.delete(0, 'end')
    E2.delete(0, 'end')
    text.delete(1.0, 'end')
    c1.set('USD')
    c2.set('')

# Add labels, entry fields, and dropdown menus
tk.Label(root, text="Currency Converter", font=('Verdana', 14, 'bold')).place(x=150, y=80)

tk.Label(root, text="Amount:", font=('Roboto', 10, 'bold')).place(x=20, y=120)
E1 = tk.Entry(root, width=20, font=('Roboto', 10))
E1.place(x=20, y=150)

tk.Label(root, text="From Currency:", font=('Roboto', 10, 'bold')).place(x=20, y=180)
c1 = ttk.Combobox(root, width=20, state='readonly', font=('Verdana', 10))
c1['values'] = ('USD', 'EUR', 'INR', 'GBP', 'JPY')  # Populate with supported currencies
c1.set('USD')  # Default value
c1.place(x=20, y=210)

tk.Label(root, text="To Currency:", font=('Roboto', 10, 'bold')).place(x=300, y=120)
c2 = ttk.Combobox(root, width=20, state='readonly', font=('Verdana', 10))
c2['values'] = ('USD', 'EUR', 'INR', 'GBP', 'JPY')  # Populate with supported currencies
c2.place(x=300, y=150)

E2 = tk.Entry(root, width=20, font=('Arial', 10), state='readonly')
E2.place(x=20, y=260)

text = tk.Text(root, width=57, height=7, font=('Verdana', 10))
text.place(x=20, y=300)

# Add buttons
tk.Button(root, text="Convert", command=show_data, font=('Verdana', 10, 'bold'), bg='green', fg='white').place(x=20, y=450)
tk.Button(root, text="Clear", command=clear, font=('Verdana', 10, 'bold'), bg='red', fg='white').place(x=100, y=450)

# Start the application
root.mainloop()
