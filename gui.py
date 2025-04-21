from tkinter import *
from tkinter import ttk

def create_main_window():

    root = Tk()
    root.title("Dumar")
    root.geometry("800x600")  # Initial size
    root.minsize(600, 400) # Min size of the windos

    # Ovo je malo zbunjujuce ali sam eksperimentalnim metodom utvrdio da ako se ovo ne stavi, on ga ne rasiri lepo
    # jer prakticno funkcionise kao CSS flexbox :D
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Mainframe - gde se stavljaju svi widgeti, tako je po docs-u praksa
    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    
    for i in range(5):
        mainframe.columnconfigure(i, weight=1)
        mainframe.rowconfigure(i, weight=1)

    # Grid layout test
    for row in range(5):
        for col in range(5):
            print("")
            #ttk.Label(mainframe, text=f"{row},{col}", relief="solid").grid(row=row, column=col, padx=5, pady=5)

    # Widgets section

    # Text 
    text = ttk.Label(mainframe, text="Dumar")
    text.grid(row=0, column= 2)

    # URL paste bar
    youtube_URL = StringVar()
    youtube_URL_entry = ttk.Entry(mainframe, width=100, textvariable=youtube_URL)
    youtube_URL_entry.grid(row=1, column=1, columnspan=3)

    # To the spotify button
    ttk.Button(mainframe, text="Spotify").grid(row=2, column=1)

    # To the deezer button
    ttk.Button(mainframe, text="Deezer").grid(row=2, column=3)

    return root