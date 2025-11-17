import tkinter as tk

# ---------------- Menu Data ----------------
menu = {
    "Pizza": 3.00,
    "Nachos": 4.50,
    "Popcorn": 5.00,
    "Fries": 2.50,
    "Chips": 1.00,
    "Pretzel": 3.50,
    "Soda": 3.00,
    "Lemonade": 4.25,
    "Water": 2.99
}

cart = []
buttons_list = []

# ---------------- Functions ----------------
def add_to_cart(item):
    cart.append(item)
    update_cart()

def update_cart():
    cart_list.delete(0, tk.END)
    total = 0
    for item in cart:
        cart_list.insert(tk.END, f"{item} - {menu[item]:.2f}€")
        total += menu[item]
    total_label.config(text=f"Total: {total:.2f}€")

def clear_cart():
    cart.clear()
    update_cart()

def apply_theme(theme_name):
    global current_theme
    current_theme = theme_name
    theme = themes[theme_name]

    root.configure(bg=theme["bg"])
    menu_frame.configure(bg=theme["frame_bg"])
    cart_frame.configure(bg=theme["frame_bg"])
    cart_list.configure(bg=theme["cart_bg"], fg=theme["fg"])
    total_label.configure(bg=theme["frame_bg"], fg=theme["fg"])
    clear_btn.configure(bg=theme["button_bg"], fg=theme["button_fg"])
    for btn in buttons_list:
        btn.config(bg=theme["button_bg"], fg=theme["button_fg"],
                   activebackground=theme["button_bg"],
                   activeforeground=theme["button_fg"])
    dark_btn.config(bg=theme["button_bg"], fg=theme["button_fg"])
    light_btn.config(bg=theme["button_bg"], fg=theme["button_fg"])

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("🍕 Snack Menu")
root.geometry("600x650")
root.resizable(False, False)

# --- Menu Frame ---
menu_frame = tk.LabelFrame(root, text="Menu", padx=10, pady=10, font=("Arial", 12, "bold"))
menu_frame.pack(padx=10, pady=10, fill="both")

for item, price in menu.items():
    btn = tk.Button(menu_frame, text=f"{item} - {price:.2f}€", width=20,
                    command=lambda i=item: add_to_cart(i))
    btn.pack(pady=3)
    buttons_list.append(btn)

# --- Cart Frame ---
cart_frame = tk.LabelFrame(root, text="Your Order", padx=10, pady=10, font=("Arial", 12, "bold"))
cart_frame.pack(padx=10, pady=10, fill="both")

cart_list = tk.Listbox(cart_frame, width=30, height=8)
cart_list.pack(pady=5)

total_label = tk.Label(cart_frame, text="Total: 0.00€", font=("Arial", 12, "bold"))
total_label.pack(pady=5)

clear_btn = tk.Button(cart_frame, text="Clear Cart", command=clear_cart)
clear_btn.pack(pady=5)

# --- Theme Buttons Frame ---
theme_frame = tk.Frame(root)
theme_frame.pack(pady=10, fill="x")

# ---------------- Run App ----------------
root.mainloop()
