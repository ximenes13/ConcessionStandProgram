# 🍕 Snack Menu App (Python + Tkinter)

This project is an interactive desktop snack-ordering application built with Python and Tkinter.
Users can browse a variety of snacks, add items to their cart, adjust quantities, switch themes, and view an automatically updated order total — all within a clean modern interface.

---

## 🚀 Features
🍟 Snack menu with prices and emoji-labeled buttons <br>
🛒 Add items to cart instantly with a single click <br>
🔼 Increase or decrease item quantities directly in the cart <br>
❌ Remove selected items or clear the entire cart <br>
💶 Automatic total price calculation with formatting <br>
📜 Scrollable cart using a styled Treeview widget <br>
🎨 Light & Dark theme switching with custom colors <br>
📢 Error handling when trying to modify items without selection <br>
🪟 Modern, clean layout using ttk styles and custom theming <br>
🛠️ Easy to extend with more menu items or theme packs <br>

---

## 🎨 Theme System

- 🌤️ Light Theme: Bright, soft, and clean colors for a daytime look — great for visibility and contrast in lit environments. <br>
- 🌙 Dark Theme: Deep blues and charcoal tones for a modern look — ideal for low-light use and reduced eye strain. <br>

Both themes dynamically restyle buttons, frames, labels, backgrounds, and the cart’s Treeview to ensure a consistent visual experience.

---

## 🖥️ Technologies Used

- Python 3.x
- Tkinter (GUI interface using ttk widgets)
- PyCharm or VS Code (recommended IDEs)

---

## 📂 Project Structure

- **main.py**: Main application script. Handles layout, logic, and theme styling.
    - 🖼️ Builds GUI layout (menu buttons, cart display, total bar, theme bar) <br>
    - 🔁 Refreshes Treeview to update quantities and price <br>
    - 🧠 Handles cart logic: add, increment, decrement, remove <br>
    - 🔦 Includes two built-in themes (Light & Dark) <br>
    - ❌ Shows messageboxes for invalid user actions <br>
    - 🧹 Clears cart with confirmation dialogs <br>
    - 📏 Styles all widgets (buttons, frames, Treeview, labels) using ttk <br>

---

## 🛠️ Setup

### Step 1: Clone the Repository

To get started, clone this repository to your local machine using the following command:

`git clone https://github.com/your-username/SnackMenu.git`

### Step 2: Dependencies

Make sure you have Python 3.x installed. You can check your version with:

`python3 --version`

### Step 3: Run the project

Once you've installed the dependencies, you can run the main Python script to generate and interact with the snack menu app.

`python3 main.py`

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve the project, feel free to:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to your branch (`git push origin feature-name`).
5. Submit a pull request.

If you find bugs or have feature requests, please [open an issue](https://github.com/ximenes13/SnackMenu/issues).







