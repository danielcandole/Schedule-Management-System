import tkinter as tk

def create_text_grid_widgets(root):
    """
    Example of grid layout using text widgets
    """

    # Examples of other sticky options:
    # sticky="n"   -> top of the cell
    # sticky="s"   -> bottom of the cell
    # sticky="e"   -> right side
    # sticky="w"   -> left side
    # sticky="ne"  -> top-right corner
    # sticky="nw"  -> top-left corner
    # sticky="se"  -> bottom-right corner
    # sticky="sw"  -> bottom-left corner
    # sticky="ns"  -> stretch vertically
    # sticky="ew"  -> stretch horizontally
    # sticky="nsew"-> stretch both vertically and horizontally

    # 1. Label
    lbl1 = tk.Label(root, text="Label 1", bg="lightblue", font=("Arial", 12))
    lbl1.grid(
        row=0, column=0, 
        padx=5, pady=5, 
        sticky="nsew",  # stretch in all directions (north, south, east, west)
        columnspan=1, rowspan=1, 
        ipadx=10, ipady=5  # internal padding
    )

    # 2. Label spanning 2 columns
    lbl2 = tk.Label(root, text="Label 2 (span 2 columns)", bg="lightgreen")
    lbl2.grid(
        row=0, column=1, 
        columnspan=2, rowspan=1, 
        padx=5, pady=5, 
        sticky="ew",  # stretch horizontally (east-west) only
        ipadx=5, ipady=5
    )

    # 3. Button
    btn1 = tk.Button(root, text="Button 1", bg="lightyellow")
    btn1.grid(
        row=1, column=0, 
        padx=5, pady=5, 
        sticky="ns",  # stretch vertically (north-south) only
        columnspan=1, rowspan=1, 
        ipadx=10, ipady=5
    )

    # 4. Entry
    entry1 = tk.Entry(root, font=("Arial", 12))
    entry1.grid(
        row=1, column=1, 
        padx=5, pady=5, 
        sticky="ew",  # stretch horizontally
        columnspan=2, rowspan=1, 
        ipadx=50, ipady=5
    )

    # 5. Text widget
    txt1 = tk.Text(root, height=5, width=30)
    txt1.grid(
        row=2, column=0, 
        padx=5, pady=5, 
        sticky="nsew",  # stretch in all directions
        columnspan=3, rowspan=1, 
        ipadx=5, ipady=5
    )

    # 6. Another Button at bottom-right
    btn2 = tk.Button(root, text="Submit", bg="lightcoral")
    btn2.grid(
        row=3, column=0, 
        padx=5, pady=5, 
        sticky="",  
        columnspan=1, rowspan=1, 
        ipadx=10, ipady=5
    )

    # Make columns and rows expandable
    for i in range(3):
        root.columnconfigure(i, weight=1)
    for i in range(4):
        root.rowconfigure(i, weight=1)