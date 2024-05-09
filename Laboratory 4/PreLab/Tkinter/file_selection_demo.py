import tkinter as tk
from tkinter import filedialog

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        # Display the selected file path in the label
        lFileSelected.config(text="Selected File: " + file_path)

# create the top level window/frame
top = tk.Tk()
F = tk.Frame(top)
F.pack(fill="both")

# Now the frame with text entry
fEntry = tk.Frame(F, border=1)
eHello = tk.Entry(fEntry)
eHello.pack(side="left")
lHistory = tk.Label(fEntry, text="     ", foreground="steelblue")
lHistory.pack(side="bottom", fill="x")
fEntry.pack(side="top")

# File Selection Button
fFileSelection = tk.Frame(F, border=1)
bSelectFile = tk.Button(fFileSelection, text="Select File", command=select_file)
bSelectFile.pack(side="left", padx=5, pady=2)
lFileSelected = tk.Label(fFileSelection, text="Selected File: ")
lFileSelected.pack(side="left", padx=5, pady=2)
fFileSelection.pack(side="top", fill="x")

# Finally the frame with the buttons. 
# We'll sink this one for emphasis
fButtons = tk.Frame(F, relief="sunken", border=1)
bClear = tk.Button(fButtons, text="Clear Text", command=lambda: lHistory.config(text=""))
bClear.pack(side="left", padx=5, pady=2)
bQuit = tk.Button(fButtons, text="Quit", command=F.quit)
bQuit.pack(side="left", padx=5, pady=2)
fButtons.pack(side="top", fill="x")

# Now run the eventloop
F.mainloop()
