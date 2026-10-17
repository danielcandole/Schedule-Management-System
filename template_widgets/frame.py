import tkinter as tk

def create_frames_demo(root):
    """
    Frame Widget 
    """
    
    # Main container
    main_frame = tk.Frame(root, bg='#f0f0f0', padx=20, pady=20)
    main_frame.pack(fill=tk.BOTH, expand=True)

    title_label = tk.Label(main_frame, text="Frame Examples",
                           font=("Arial", 16, "bold"), bg='#f0f0f0')
    title_label.pack(pady=(0, 20))
    
    # -------------------------
    # Basic Frames
    basic_frame = tk.LabelFrame(main_frame, text="Basic Frames",
                                padx=10, pady=10, bg='#f0f0f0', font=("Arial", 10, "bold"))
    basic_frame.pack(fill=tk.X, pady=5)
    
    frame1 = tk.Frame(basic_frame, bg="#d1e7dd", height=50)
    frame1.pack(fill=tk.X, pady=5)
    tk.Label(frame1, text="Simple Frame", bg="#d1e7dd").pack()
    
    frame2 = tk.Frame(basic_frame, bg="#f8d7da", height=50, relief=tk.SUNKEN, bd=2)
    frame2.pack(fill=tk.X, pady=5)
    tk.Label(frame2, text="SUNKEN Frame", bg="#f8d7da").pack()
    
    # -------------------------
    # Layout Frames
    layout_frame = tk.LabelFrame(main_frame, text="Layout Frames",
                                 padx=10, pady=10, bg='#f0f0f0', font=("Arial", 10, "bold"))
    layout_frame.pack(fill=tk.X, pady=5)
    
    top = tk.Frame(layout_frame, bg="#cff4fc", height=40)
    top.pack(fill=tk.X, pady=5)
    tk.Label(top, text="Top Section", bg="#cff4fc").pack()
    
    middle = tk.Frame(layout_frame)
    middle.pack(fill=tk.BOTH, expand=True, pady=5)
    
    left = tk.Frame(middle, bg="#fff3cd", width=100)
    left.pack(side=tk.LEFT, fill=tk.Y)
    tk.Label(left, text="Left Column", bg="#fff3cd").pack(pady=5)
    
    right = tk.Frame(middle, bg="#e2e3e5")
    right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    tk.Label(right, text="Right Column", bg="#e2e3e5").pack(pady=5)
    
    bottom = tk.Frame(layout_frame, bg="#d6d8d9", height=40)
    bottom.pack(fill=tk.X, pady=5)
    tk.Label(bottom, text="Bottom Section", bg="#d6d8d9").pack()
    
    # -------------------------
    # Nested Frames
    nested_frame = tk.LabelFrame(main_frame, text="Nested Frames",
                                 padx=10, pady=10, bg='#f0f0f0', font=("Arial", 10, "bold"))
    nested_frame.pack(fill=tk.X, pady=5)
    
    outer = tk.Frame(nested_frame, bg="#e2f0cb", padx=5, pady=5)
    outer.pack(fill=tk.BOTH, expand=True, pady=5)
    tk.Label(outer, text="Outer Frame", bg="#e2f0cb").pack(pady=2)
    
    inner = tk.Frame(outer, bg="#fce5cd", padx=5, pady=5)
    inner.pack(fill=tk.BOTH, expand=True, pady=2)
    tk.Label(inner, text="Inner Frame", bg="#fce5cd").pack()
    
    # -------------------------
    # Styled Frames
    style_frame = tk.LabelFrame(main_frame, text="Styled Frames",
                                padx=10, pady=10, bg='#f0f0f0', font=("Arial", 10, "bold"))
    style_frame.pack(fill=tk.X, pady=5)
    
    for relief in [tk.RAISED, tk.SUNKEN, tk.GROOVE, tk.RIDGE]:
        f = tk.Frame(style_frame, relief=relief, bd=3, height=50, width=80)
        f.pack(side=tk.LEFT, padx=5)
        tk.Label(f, text=relief).place(relx=0.5, rely=0.5, anchor="center")
        f.pack_propagate(False)

