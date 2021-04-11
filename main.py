import tkinter as tk
import search

# Window Object
window = tk.Tk()

# Button to search for the files
search_button = tk.Button(window, text='Search Files',
                          fg='black', height=2, width=10, padx=2, pady=2)
search_button.place(x=100, y=50)

# Entry to write name of file to be search
file_to_search = tk.Entry(window)
file_to_search.insert(0, 'Enter the file name without an extension')
file_to_search.place(x=200, y=56, height=30, width=300)

# Calling the Empty file_to_search entry after clicking on it
file_to_search.bind('<Button-1>', lambda event,
                    file_to_search=file_to_search: search.makeEntryEmpty(file_to_search))

# Calling the start_search method after clicking on Search File Button
search_button.bind('<Button-1>', lambda event, file_to_search=file_to_search,
                   window=window: search.start_search(file_to_search, window))

# Window Related
window.title('File Search App')
window.geometry('700x700+500+200')
window.mainloop()
