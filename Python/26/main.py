import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.geometry("1024x720")
window.title("Lista proizvoda")

fruit_info = {
    "Apple": "A crisp, sweet fruit often enjoyed fresh or used in pies and juices.",
    "Banana": "A soft, elongated fruit with a creamy texture and naturally sweet flavor.",
    "Cherry": "A small, juicy fruit with a tart-sweet taste and vibrant red color.",
    "Date": "A chewy, caramel-like fruit commonly eaten dried and rich in natural sugars.",
    "Elderberry": "A tiny, dark-purple berry known for its tart flavor and use in syrups and jams."
}

fruit_images = {
    "Apple": "apple.jpeg",
    "Banana": "banana.jpeg"
}

def show_item_info(event):
    selection = listbox.curselection() # current selection - trenutna selekcija
    name = listbox.get(selection)
    product_info.configure(state='normal')

    image = Image.open(fruit_images[name])
    image = image.resize((50, 50))
    photo = ImageTk.PhotoImage(image)

    product_info.delete('1.0', tk.END)
    product_info.insert(tk.END, fruit_info[name])

    image_label.config(image=photo)
    image_label.image = photo

    product_info.configure(state='disabled')

product_list = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

listbox = tk.Listbox(window, height=50)
listbox.pack(side="left", padx=10)

for item in product_list:
    listbox.insert(tk.END, item)

listbox.bind("<<ListboxSelect>>", show_item_info)

product_info = tk.Text(window, width=50, font=("Arial", 14))
product_info.pack(side="left")

image_label = tk.Label(window, bg="white", width=50, height=50)
image_label.pack(side='left', padx=20)


window.mainloop()