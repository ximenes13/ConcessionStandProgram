import tkinter as tk
from tkinter import ttk, messagebox
import platform

MENU = {
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

THEMES = {
    "Light": {
        "bg": "#e3f6fd",
        "panel": "#f8f9fa",
        "cart_bg": "#fffbe7",
        "fg": "#22223b",
        "accent": "#448aff",
        "muted": "#9aa7b3"
    },
    "Dark": {
        "bg": "#253655",
        "panel": "#32475b",
        "cart_bg": "#22223b",
        "fg": "#e0eafc",
        "accent": "#ffd966",
        "muted": "#9aa7b3"
    }
}

class SnackApp(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.style = ttk.Style(master)
        try:
            self.style.theme_use("clam")
        except Exception:
            self.style.theme_use(self.style.theme_names()[0])

        self.current_theme = "Dark"
        self.cart = {}   # item_name -> quantity

        master.title("🍕 Snack Menu")
        master.geometry("970x870")
        master.resizable(False, False)
        master.tk.call('tk', 'scaling', 1.0)

        self.build_styles()
        self.create_widgets()
        self.apply_theme(self.current_theme)

    def build_styles(self):
        self.style.configure("App.TFrame", background=THEMES[self.current_theme]["bg"])
        self.style.configure("Panel.TLabelframe", background=THEMES[self.current_theme]["panel"], borderwidth=2, relief="solid")
        self.style.configure("Panel.TLabelframe.Label", background=THEMES[self.current_theme]["panel"], foreground=THEMES[self.current_theme]["fg"], font=("Segoe UI", 18, "bold"))
        self.style.configure("Heading.TLabel", background=THEMES[self.current_theme]["panel"], foreground=THEMES[self.current_theme]["fg"], font=("Segoe UI", 22, "bold"))
        self.style.configure("TButton", relief="flat", padding=6)
        self.style.configure("Menu.TButton", font=("Segoe UI", 13, "bold"), padding=(12,10))
        self.style.configure("Accent.TButton", font=("Segoe UI", 12, "bold"), padding=(12,8))
        self.style.configure("Total.TLabel", background=THEMES[self.current_theme]["panel"], foreground=THEMES[self.current_theme]["fg"], font=("Segoe UI", 16, "bold"))
        self.style.configure("Secondary.TButton", font=("Segoe UI", 12), padding=(12,8))
        self.style.configure("Cart.Treeview", background=THEMES[self.current_theme]["cart_bg"],
                             fieldbackground=THEMES[self.current_theme]["cart_bg"],
                             foreground=THEMES[self.current_theme]["fg"],
                             rowheight=26,
                             font=("Segoe UI", 12))
        self.style.layout("Cart.Treeview", self.style.layout("Treeview"))

    def create_widgets(self):
        # Outer frame
        self.pack(fill="both", expand=True)
        self["style"] = "App.TFrame"

        # Menu panel
        self.menu_panel = ttk.LabelFrame(self, text="Menu", padding=(20,18), style="Panel.TLabelframe")
        self.menu_panel.pack(padx=20, pady=(20,12), fill="x")

        menu_inner = ttk.Frame(self.menu_panel, style="App.TFrame")
        menu_inner.pack(fill="x", padx=8, pady=(6,2))
        menu_inner.columnconfigure(0, weight=1)
        menu_inner.columnconfigure(1, weight=1)

        self.menu_buttons = []
        items = list(MENU.items())
        for idx, (name, price) in enumerate(items):
            text = f"{name} - {price:.2f}€"
            btn = ttk.Button(menu_inner, text=text, style="Menu.TButton",
                             command=lambda n=name: self.add_to_cart(n))
            btn.grid(row=idx//2, column=idx%2, padx=10, pady=8, sticky="ew")
            btn.bind("<Enter>", lambda e, b=btn: b.state(["active"]))
            btn.bind("<Leave>", lambda e, b=btn: b.state(["!active"]))
            self.menu_buttons.append(btn)

        # Cart panel
        self.cart_panel = ttk.LabelFrame(self, text="Your Order", padding=(20,18), style="Panel.TLabelframe")
        self.cart_panel.pack(padx=20, pady=(12,8), fill="both", expand=True)

        cart_center = ttk.Frame(self.cart_panel, style="App.TFrame")
        cart_center.pack(expand=True)

        self.cart_tree = ttk.Treeview(cart_center, columns=("item", "price"), show="headings", height=8, style="Cart.Treeview")
        self.cart_tree.column("item", anchor="center", width=320)
        self.cart_tree.column("price", anchor="center", width=120)
        self.cart_tree.heading("item", text="Item")
        self.cart_tree.heading("price", text="Price")
        self.cart_tree.grid(row=0, column=0, padx=(50,0), pady=6)

        # Scrollbar
        self.cart_scroll = ttk.Scrollbar(cart_center, orient="vertical", command=self.cart_tree.yview)
        self.cart_tree.configure(yscrollcommand=self.cart_scroll.set)
        self.cart_scroll.grid(row=0, column=1, sticky="ns", padx=(6,20), pady=6)

        # Controls frame, same column, stacked vertically
        controls = ttk.Frame(cart_center, style="App.TFrame")
        controls.grid(row=0, column=2, sticky="n", padx=10, pady=10)

        self.inc_btn = ttk.Button(controls, text="＋", style="Accent.TButton", command=self.increment_selected)
        self.inc_btn.grid(row=0, column=0, pady=(4,6), sticky="ew")
        self.dec_btn = ttk.Button(controls, text="－", style="Accent.TButton", command=self.decrement_selected)
        self.dec_btn.grid(row=1, column=0, pady=(0,6), sticky="ew")
        self.clear_btn = ttk.Button(controls, text="Clear Cart", style="Accent.TButton", command=self.clear_cart)
        self.clear_btn.grid(row=2, column=0, pady=(10,6), sticky="ew")
        self.remove_btn = ttk.Button(controls, text="Remove Selected", style="Accent.TButton", command=self.remove_selected)
        self.remove_btn.grid(row=3, column=0, pady=(0,10), sticky="ew")

        # Total label below cart
        self.total_label = ttk.Label(cart_center, text="Total: 0.00€", style="Total.TLabel")
        self.total_label.grid(row=1, column=0, columnspan=3, pady=(12,6))

        # Theme bar
        theme_bar = ttk.Frame(self, style="App.TFrame")
        theme_bar.pack(fill="x", padx=10, pady=(6,16))
        theme_bar.columnconfigure(0, weight=1)
        theme_bar.columnconfigure(1, weight=1)
        self.light_btn = ttk.Button(theme_bar, text="🌤 Light Theme", style="Accent.TButton", command=lambda: self.apply_theme("Light"))
        self.light_btn.grid(row=0, column=0, sticky="w", padx=(60,0))
        self.dark_btn = ttk.Button(theme_bar, text="🌙 Dark Theme", style="Accent.TButton", command=lambda: self.apply_theme("Dark"))
        self.dark_btn.grid(row=0, column=1, sticky="e", padx=(0,60))

    # --- Cart logic ---
    def add_to_cart(self, item_name):
        if item_name not in self.cart:
            self.cart[item_name] = 1
        else:
            self.cart[item_name] += 1
        self.refresh_cart()

    def refresh_cart(self):
        for row in self.cart_tree.get_children():
            self.cart_tree.delete(row)
        total = 0
        for item, qty in self.cart.items():
            price = MENU[item]
            subtotal = qty * price
            total += subtotal
            self.cart_tree.insert("", "end", values=(f"{item} x{qty}", f"{subtotal:.2f}€"))
        self.total_label.config(text=f"Total: {total:.2f}€")

    def get_selected_item(self):
        sel = self.cart_tree.selection()
        if not sel:
            return None
        vals = self.cart_tree.item(sel[0])["values"]
        if not vals:
            return None
        return vals[0]

    def increment_selected(self):
        item = self.get_selected_item()
        if not item:
            messagebox.showinfo("Selected item", "Please select an item to increase quantity")
            return
        item_name = item.split(" x")[0]
        self.cart[item_name] = self.cart.get(item_name, 0) + 1
        self.refresh_cart()

    def decrement_selected(self):
        item = self.get_selected_item()
        if not item:
            messagebox.showinfo("Selected item", "Please select an item to decrease quantity")
            return
        item_name = item.split(" x")[0]
        if item_name in self.cart:
            if self.cart[item_name] > 1:
                self.cart[item_name] -= 1
            else:
                del self.cart[item_name]
        self.refresh_cart()

    def remove_selected(self):
        sel = self.cart_tree.selection()
        if not sel:
            return
        item_display = self.cart_tree.item(sel[0])["values"][0]
        item_name = item_display.split(" x")[0]
        if item_name in self.cart:
            del self.cart[item_name]
        self.refresh_cart()

    def clear_cart(self):
        if not self.cart:
            return
        if messagebox.askyesno("Clear cart", "Clear all items from the cart?"):
            self.cart.clear()
            self.refresh_cart()

    # --- Theme application ---
    def apply_theme(self, theme_name):
        if theme_name not in THEMES:
            return
        self.current_theme = theme_name
        t = THEMES[theme_name]

        self.master.configure(bg=t["bg"])
        self.style.configure("App.TFrame", background=t["bg"])
        self.style.configure("Panel.TLabelframe", background=t["panel"], bordercolor=t["accent"])
        self.style.configure("Panel.TLabelframe.Label", background=t["panel"], foreground=t["fg"])
        self.style.configure("Heading.TLabel", background=t["panel"], foreground=t["fg"])
        self.style.configure("Menu.TButton",
                             background=t["panel"],
                             foreground=t["fg"],
                             borderwidth=0,
                             focuscolor='none')
        self.style.map("Menu.TButton",
                       background=[("active", t["accent"]), ("!active", t["panel"])],
                       foreground=[("active", t["panel"]), ("!active", t["fg"])])
        self.style.configure("Accent.TButton",
                             background=t["accent"],
                             foreground=t["panel"],
                             font=("Segoe UI", 11, "bold"))
        self.style.map("Accent.TButton",
                       background=[("active", t["panel"]), ("!active", t["accent"])],
                       foreground=[("active", t["accent"]), ("!active", t["panel"])])
        self.style.configure("Cart.Treeview",
                             background=t["cart_bg"],
                             fieldbackground=t["cart_bg"],
                             foreground=t["fg"])
        self.style.configure("Vertical.TScrollbar", troughcolor=t["panel"])
        for widget in (self.menu_panel, self.cart_panel):
            widget.configure(style="Panel.TLabelframe")
        self.total_label.configure(style="Total.TLabel")
        self.refresh_cart()

if __name__ == "__main__":
    root = tk.Tk()
    app = SnackApp(root)
    root.mainloop()
