import tkinter as tk
from tkinter.colorchooser import askcolor

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("برنامج الرسم")

        self.canvas = tk.Canvas(root, width=400, height=300, bg="white")
        self.canvas.pack()

        self.draw_button = tk.Button(root, text="بدء الرسم", command=self.start_drawing)
        self.draw_button.pack()

        self.color_button = tk.Button(root, text="اختيار اللون", command=self.choose_color)
        self.color_button.pack()

        self.clear_button = tk.Button(root, text="مسح الرسم", command=self.clear_canvas)
        self.clear_button.pack()

        self.drawing = False
        self.prev_x = None
        self.prev_y = None
        self.current_color = "black"

        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)

    def start_drawing(self, event):
        self.drawing = True
        self.prev_x = event.x
        self.prev_y = event.y

    def draw(self, event):
        if self.drawing and self.prev_x is not None and self.prev_y is not None:
            x, y = event.x, event.y
            self.canvas.create_line(self.prev_x, self.prev_y, x, y, fill=self.current_color, width=2)
            self.prev_x = x
            self.prev_y = y

    def choose_color(self):
        color = askcolor()[1]
        if color:
            self.current_color = color

    def clear_canvas(self):
        self.canvas.delete("all")
        self.drawing = False
        self.prev_x = None
        self.prev_y = None

root = tk.Tk()
app = DrawingApp(root)
root.mainloop()
