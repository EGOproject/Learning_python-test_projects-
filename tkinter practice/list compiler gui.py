import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class ListMakerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("List Maker GUI")
        self.master.geometry("900x400")
        self.master.resizable(False, False)

        self.list_name = ""
        self.items = []
        self.deleted_items = []

        self.create_widgets()

    def create_widgets(self):
        # Part One: New Entries and Edits
        part_one_frame = tk.Frame(self.master)
        part_one_frame.pack(side=tk.LEFT, padx=10, fill=tk.Y)

        self.refresh_button = tk.Button(part_one_frame, text="Refresh", command=self.refresh_app)
        self.refresh_button.pack(fill=tk.X)

        self.label_name = tk.Label(part_one_frame, text="List Name:")
        self.label_name.pack()
        self.entry_name = tk.Entry(part_one_frame)
        self.entry_name.pack()

        self.label_new_item = tk.Label(part_one_frame, text="New Item:")
        self.label_new_item.pack()
        self.entry_new_item = tk.Entry(part_one_frame)
        self.entry_new_item.pack()

        self.add_button = tk.Button(part_one_frame, text="Add", command=self.add_item)
        self.add_button.pack()

        # Part Two: Preview and Show Deleted Items
        part_two_frame = tk.Frame(self.master)
        part_two_frame.pack(side=tk.LEFT, padx=5, fill=tk.BOTH, expand=True)

        left_frame = tk.Frame(part_two_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.preview_label = tk.Label(left_frame, text="Preview:")
        self.preview_label.pack()

        self.active_listbox = tk.Listbox(left_frame, selectmode=tk.SINGLE, height=5)
        self.active_listbox.pack(pady=5)

        self.edit_label = tk.Label(left_frame, text="Edit:")
        self.edit_label.pack()
        self.entry_edit = tk.Entry(left_frame)
        self.entry_edit.pack()

        edit_button_frame = tk.Frame(left_frame)
        edit_button_frame.pack()

        self.edit_button = tk.Button(edit_button_frame, text="Edit", command=self.edit_item)
        self.edit_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(edit_button_frame, text="Delete", command=self.delete_item)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.recover_button = tk.Button(edit_button_frame, text="Recover", command=self.recover_item)
        self.recover_button.pack(side=tk.LEFT, padx=5)

        right_frame = tk.Frame(part_two_frame)
        right_frame.pack(side=tk.LEFT, padx=5, fill=tk.BOTH, expand=True)

        self.deleted_preview_label = tk.Label(right_frame, text="Deleted Items:")
        self.deleted_preview_label.pack()

        self.deleted_listbox = tk.Listbox(right_frame, selectmode=tk.SINGLE, height=5)
        self.deleted_listbox.pack(pady=5)

        # Part Three: Final Preview
        part_three_frame = tk.Frame(self.master)
        part_three_frame.pack(side=tk.LEFT, padx=5, fill=tk.BOTH, expand=True)

        self.final_preview_label = tk.Label(part_three_frame, text="Final Preview:")
        self.final_preview_label.pack()

        self.final_preview_text = tk.Text(part_three_frame, height=15, width=25)
        self.final_preview_text.pack(fill=tk.BOTH, expand=True)

        self.save_button = tk.Button(part_three_frame, text="Save As", command=self.save_list)
        self.save_button.pack(fill=tk.X)

    def refresh_app(self):
        self.entry_name.delete(0, tk.END)
        self.entry_new_item.delete(0, tk.END)
        self.entry_edit.delete(0, tk.END)
        self.list_name = ""
        self.items.clear()
        self.deleted_items.clear()
        self.update_preview()

    def add_item(self):
        new_item = self.entry_new_item.get()
        if new_item:
            self.items.append(new_item)
            self.update_preview()
            self.entry_new_item.delete(0, tk.END)

    def edit_item(self):
        selected_index = self.active_listbox.curselection()
        if selected_index:
            new_item = self.entry_edit.get()
            if new_item:
                self.items[selected_index[0]] = new_item
                self.update_preview()
                self.entry_edit.delete(0, tk.END)

    def delete_item(self):
        selected_index = self.active_listbox.curselection()
        if selected_index:
            deleted_item = self.items.pop(selected_index[0])
            self.deleted_items.append(deleted_item)
            self.update_preview()

    def recover_item(self):
        selected_index = self.deleted_listbox.curselection()
        if selected_index:
            recovered_item = self.deleted_items.pop(selected_index[0])
            self.items.append(recovered_item)
            self.update_preview()

    def update_preview(self):
        self.active_listbox.delete(0, tk.END)
        for item in self.items:
            self.active_listbox.insert(tk.END, item)

        self.deleted_listbox.delete(0, tk.END)
        for item in self.deleted_items:
            self.deleted_listbox.insert(tk.END, item)

        final_preview_text = f"{self.list_name}\n"
        for item in self.items:
            final_preview_text += f"- {item}\n"
        self.final_preview_text.config(state=tk.NORMAL)
        self.final_preview_text.delete("1.0", tk.END)
        self.final_preview_text.insert(tk.END, final_preview_text)
        self.final_preview_text.config(state=tk.DISABLED)

        self.list_name = self.entry_name.get().upper()

    def save_list(self):
        filename = filedialog.asksaveasfilename(defaultextension=".txt", initialfile=self.list_name)
        if filename:
            with open(filename, "w") as file:
                file.write(f"{self.list_name}\n")
                for item in self.items:
                    file.write(f"- {item}\n")
            messagebox.showinfo("Save", f"List saved as {filename}")

def main():
    root = tk.Tk()
    app = ListMakerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
