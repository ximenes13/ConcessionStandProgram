import tkinter as tk

# ---------------- Menu Data ----------------
menu = {
    "🍕 Pizza": 3.00,
    "🥨 Nachos": 4.50,
    "🍿 Popcorn": 5.00,
    "🍟 Fries": 2.50,
    "🥔 Chips": 1.00,
    "🥨 Pretzel": 3.50,
    "🥤 Soda": 3.00,
    "🍋 Lemonade": 4.25,
    "💧 Water": 2.99
}

cart = []
buttons_list = []

# ---------------- Theme Data ----------------
themes = {
    "Light": {
        "bg": "#e3f6fd",
        "frame_bg": "#f8f9fa",
        "cart_bg": "#fffbe7",
        "fg": "#22223b",
        "button_bg": "#caf0f8",
        "button_fg": "#253655"
    },
    "Dark": {
        "bg": "#253655",
        "frame_bg": "#32475b",
        "cart_bg": "#22223b",
        "fg": "#e0eafc",
        "button_bg": "#448aff",
        "button_fg": "#f8f9fa"
    }
}
current_theme = "Light"

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
    cart_list.configure(bg=theme["cart_bg"], fg=theme["fg"], selectbackground=theme["button_bg"])
    cart_scroll.configure(bg=theme["cart_bg"], troughcolor=theme["frame_bg"])
    total_label.configure(bg=theme["frame_bg"], fg=theme["fg"])
    clear_btn.configure(bg=theme["button_bg"], fg=theme["button_fg"],
                        activebackground=theme["bg"], activeforeground=theme["button_fg"])
    menu_label.configure(bg=theme["frame_bg"], fg=theme["fg"])
    order_label.configure(bg=theme["frame_bg"], fg=theme["fg"])
    for btn in buttons_list:
        btn.config(bg=theme["button_bg"], fg=theme["button_fg"],
                   activebackground=theme["bg"], activeforeground=theme["button_fg"],
                   highlightbackground=theme["bg"])
    dark_btn.config(bg=theme["button_bg"], fg=theme["button_fg"],
                    activebackground=theme["bg"], activeforeground=theme["button_fg"])
    light_btn.config(bg=theme["button_bg"], fg=theme["button_fg"],
                     activebackground=theme["bg"], activeforeground=theme["button_fg"])

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("🍕 Snack Menu")
root.geometry("1000x890")
root.resizable(False, False)
root.configure(bg=themes[current_theme]["bg"])

# --- Menu Frame ---
menu_frame = tk.LabelFrame(root, text="", padx=22, pady=16, font=("Segoe UI", 12, "bold"),
                          bg=themes[current_theme]["frame_bg"],
                          highlightbackground="#cff4fc", highlightthickness=2, bd=0)
menu_frame.pack(padx=24, pady=20, fill="both")

menu_label = tk.Label(menu_frame, text="Menu", font=("Segoe UI", 21, "bold"),
                      bg=themes[current_theme]["frame_bg"], fg=themes[current_theme]["fg"],
                      anchor="center", justify="center")
menu_label.grid(row=0, column=0, columnspan=2, pady=(0, 12), sticky="ew")

menu_frame.grid_columnconfigure(0, weight=1)
menu_frame.grid_columnconfigure(1, weight=1)


# --- Create menu buttons in two columns ---
for idx, (item, price) in enumerate(menu.items()):
    btn = tk.Button(menu_frame, text=f"{item} - {price:.2f}€", width=25,
                    font=("Segoe UI", 13, "bold"),
                    command=lambda i=item: add_to_cart(i),
                    bg=themes[current_theme]["button_bg"],
                    fg=themes[current_theme]["button_fg"],
                    bd=0,
                    relief='ridge',
                    highlightbackground="#cff4fc",
                    highlightthickness=1)
    row = idx // 2 + 1  # +1 because menu_label is in row 0
    col = idx % 2
    btn.grid(row=row, column=col, padx=12, pady=6, sticky="ew")
    buttons_list.append(btn)

# --- Cart Frame ---
cart_frame = tk.LabelFrame(root, text="", padx=22, pady=16, font=("Segoe UI", 12, "bold"),
                          bg=themes[current_theme]["frame_bg"],
                          highlightbackground="#ffeebf", highlightthickness=2, bd=0)
cart_frame.pack(padx=24, pady=2, fill="both")

order_label = tk.Label(cart_frame, text="Your Order", font=("Segoe UI", 18, "bold"),
                       bg=themes[current_theme]["frame_bg"], fg=themes[current_theme]["fg"])
order_label.pack(pady=(0, 8))

# -- Listbox with Scrollbar --
listbox_frame = tk.Frame(cart_frame, bg=themes[current_theme]["frame_bg"])
listbox_frame.pack()

cart_list = tk.Listbox(listbox_frame, width=28, height=8, font=("Segoe UI", 13),
                       bg=themes[current_theme]["cart_bg"], fg=themes[current_theme]["fg"],
                       bd=0, highlightthickness=1, highlightbackground="#ffeebf")
cart_list.pack(side=tk.LEFT, fill=tk.BOTH)

cart_scroll = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=cart_list.yview)
cart_list.config(yscrollcommand=cart_scroll.set)
cart_scroll.pack(side=tk.RIGHT, fill=tk.Y)

total_label = tk.Label(cart_frame, text="Total: 0.00€", font=("Segoe UI", 15, "bold"),
                       bg=themes[current_theme]["frame_bg"], fg=themes[current_theme]["fg"])
total_label.pack(pady=8)

clear_btn = tk.Button(cart_frame, text="Clear Cart", font=("Segoe UI", 12, "bold"),
                      command=clear_cart,
                      bg=themes[current_theme]["button_bg"],
                      fg=themes[current_theme]["button_fg"],
                      bd=0, highlightbackground="#ffeebf")
clear_btn.pack(pady=5)

# --- Theme Buttons Frame ---
theme_frame = tk.Frame(root, bg=themes[current_theme]["bg"])
theme_frame.pack(pady=16, fill="x")

light_btn = tk.Button(theme_frame, text="🌤 Light Theme", font=("Segoe UI", 12, "bold"),
                      command=lambda: apply_theme("Light"),
                      bg=themes["Light"]["button_bg"], fg=themes["Light"]["button_fg"],
                      bd=0, highlightbackground=themes["Light"]["bg"])
light_btn.pack(side=tk.LEFT, padx=(60,12), pady=4)

dark_btn = tk.Button(theme_frame, text="🌙 Dark Theme", font=("Segoe UI", 12, "bold"),
                     command=lambda: apply_theme("Dark"),
                     bg=themes["Dark"]["button_bg"], fg=themes["Dark"]["button_fg"],
                     bd=0, highlightbackground=themes["Dark"]["bg"])
dark_btn.pack(side=tk.LEFT, padx=12, pady=4)

apply_theme("Light")

# ---------------- Run App ----------------
root.mainloop()
