import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import json
import os

class AdAstraEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Ad Astra Editor")

        self.galaxies = []

        # Create tabs
        self.tab_control = ttk.Notebook(self.root)
        self.create_galaxy_tab()
        self.create_solar_system_tab()
        self.create_planet_tab()

        self.tab_control.pack(expand=1, fill="both")

    def create_galaxy_tab(self):
        galaxy_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(galaxy_tab, text="Galaxies")

        self.galaxy_listbox = tk.Listbox(galaxy_tab, selectmode=tk.SINGLE)
        self.galaxy_listbox.pack(pady=10)

        add_galaxy_button = tk.Button(galaxy_tab, text="Add Galaxy", command=self.add_galaxy)
        add_galaxy_button.pack(pady=5)

        edit_galaxy_button = tk.Button(galaxy_tab, text="Edit Galaxy", command=self.edit_galaxy)
        edit_galaxy_button.pack(pady=5)

        remove_galaxy_button = tk.Button(galaxy_tab, text="Remove Galaxy", command=self.remove_galaxy)
        remove_galaxy_button.pack(pady=5)

        # Fields for Galaxy Properties
        self.galaxy_name_var = tk.StringVar()
        self.galaxy_properties_frame = ttk.LabelFrame(galaxy_tab, text="Galaxy Properties")
        self.galaxy_properties_frame.pack(padx=10, pady=10)

        galaxy_name_label = tk.Label(self.galaxy_properties_frame, text="Name:")
        galaxy_name_label.grid(row=0, column=0, padx=5, pady=5)
        galaxy_name_entry = tk.Entry(self.galaxy_properties_frame, textvariable=self.galaxy_name_var)
        galaxy_name_entry.grid(row=0, column=1, padx=5, pady=5)

    def create_solar_system_tab(self):
        solar_system_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(solar_system_tab, text="Solar Systems")

        # TODO: Add UI elements for Solar Systems

    def create_planet_tab(self):
        planet_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(planet_tab, text="Planets")

        # TODO: Add UI elements for Planets

    def add_galaxy(self):
        galaxy_name = simpledialog.askstring("Enter Galaxy Name", "Galaxy Name:")
        if galaxy_name:
            galaxy_properties = {"name": galaxy_name}
            self.galaxies.append({"properties": galaxy_properties, "solar_systems": []})
            self.update_galaxy_listbox()

    def edit_galaxy(self):
        selected_index = self.galaxy_listbox.curselection()
        if selected_index:
            galaxy_properties = self.galaxies[selected_index[0]]["properties"]
            self.galaxy_name_var.set(galaxy_properties["name"])
            if simpledialog.askokcancel("Edit Galaxy", "Edit Galaxy Properties?"):
                galaxy_name = self.galaxy_name_var.get()
                galaxy_properties["name"] = galaxy_name
                self.update_galaxy_listbox()

    def remove_galaxy(self):
        selected_index = self.galaxy_listbox.curselection()
        if selected_index:
            confirmed = messagebox.askokcancel("Confirmation", "Are you sure you want to remove this galaxy?")
            if confirmed:
                del self.galaxies[selected_index[0]]
                self.update_galaxy_listbox()

    def update_galaxy_listbox(self):
        self.galaxy_listbox.delete(0, tk.END)
        for galaxy in self.galaxies:
            self.galaxy_listbox.insert(tk.END, galaxy["properties"]["name"])

if __name__ == "__main__":
    root = tk.Tk()
    app = AdAstraEditor(root)
    root.mainloop()
