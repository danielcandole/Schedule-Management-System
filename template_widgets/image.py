import tkinter as tk
from PIL import Image, ImageTk

def create_image_widgets(root):
    """
    Image widgets
    """

    # 1. Basic Image Label
    img1 = Image.open("assets/images/py.png").resize((100, 100))
    photo1 = ImageTk.PhotoImage(img1)
    lbl1 = tk.Label(root, image=photo1, bg=root["bg"])
    lbl1.image = photo1  
    lbl1.pack(pady=10)

    # 2. Image Label with text
    img2 = Image.open("assets/images/py.png").resize((50, 50))
    photo2 = ImageTk.PhotoImage(img2)
    lbl2 = tk.Label(
        root, 
        text="Python Logo", 
        image=photo2, 
        compound="top",
        font=("Arial", 12, "bold"),
        bg=root["bg"]
    )
    lbl2.image = photo2
    lbl2.pack(pady=10)

    # 3. Button with image only
    img3 = Image.open("assets/images/py.png").resize((50, 50))
    photo3 = ImageTk.PhotoImage(img3)
    btn1 = tk.Button(root, image=photo3, bg=root["bg"], bd=0, highlightthickness=0)
    btn1.image = photo3
    btn1.pack(pady=10)

    # 4. Button with image and text
    img4 = Image.open("assets/images/py.png").resize((50, 50))
    photo4 = ImageTk.PhotoImage(img4)
    btn2 = tk.Button(
        root,
        text="Click Me",
        image=photo4,
        compound="left", 
        font=("Arial", 12),
        bg=root["bg"],
        bd=0,
        highlightthickness=0
    )
    btn2.image = photo4
    btn2.pack(pady=10)

    # 5. Large Image Label
    img5 = Image.open("assets/images/py.png").resize((200, 200))
    photo5 = ImageTk.PhotoImage(img5)
    lbl3 = tk.Label(root, image=photo5, bg=root["bg"])
    lbl3.image = photo5
    lbl3.pack(pady=10)

    # 6. Multiple images in a row
    frame = tk.Frame(root, bg=root["bg"])
    frame.pack(pady=10)
    for i in range(4):
        img = Image.open("assets/images/py.png").resize((50, 50))
        photo = ImageTk.PhotoImage(img)
        lbl = tk.Label(frame, image=photo, bg=root["bg"])
        lbl.image = photo
        lbl.pack(side="left", padx=5)
