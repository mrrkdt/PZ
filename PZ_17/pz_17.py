import tkinter as tk
from PZ_9.pz_9 import init_dict, remove_element_from_dict


class DictionaryManager:
    def __init__(self, master):
        self.master = master
        master.title("Dictionary Manager")
        self.dict = {}

        self.label_size = tk.Label(master, text="Enter dictionary size:")
        self.label_size.grid(row=0, column=0)

        self.entry_size = tk.Entry(master)
        self.entry_size.grid(row=0, column=1)

        self.create_button = tk.Button(master, text="Create Dictionary", command=self.create_dictionary)
        self.create_button.grid(row=0, column=2)

        self.label_remove = tk.Label(master, text="Enter elements to remove (space separated):")
        self.label_remove.grid(row=1, column=0)

        self.entry_remove = tk.Entry(master)
        self.entry_remove.grid(row=1, column=1)

        self.remove_button = tk.Button(master, text="Remove Elements", command=self.remove_elements)
        self.remove_button.grid(row=1, column=2)

        self.output_label = tk.Label(master, text="Output:")
        self.output_label.grid(row=2, column=0)

        self.output_text = tk.Text(master, width=70, height=20)
        self.output_text.grid(row=3, column=0, columnspan=3)

    def create_dictionary(self):
        size = int(self.entry_size.get())
        self.output_text.insert(tk.END, f"Creating dictionary of size {size}...\n")

        self.dict = {}

        init_dict(self.dict, size)

        self.output_text.insert(tk.END, f"Created dictionary: {self.dict}\n")

    def remove_elements(self):
        elements = list(map(int, self.entry_remove.get().split()))
        self.output_text.insert(tk.END, f"Removing elements: {elements}\n")

        remove_element_from_dict(self.dict, elements)

        self.output_text.insert(tk.END, f"After removal: {self.dict}\n")


root = tk.Tk()
app = DictionaryManager(root)
root.mainloop()
