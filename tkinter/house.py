import tkinter as tk
from PIL import Image, ImageTk

moon_photo = None

def draw_house(canvas):
    global moon_photo

    # Draw sky
    canvas.create_rectangle(0, 0, 600, 400, fill='sky blue')

    # Draw grass
    canvas.create_rectangle(0, 300, 600, 400, fill='green')

    # Draw house border
    canvas.create_rectangle(150, 200, 450, 300, fill='lightyellow', outline='black', width=2)

    # Draw roof
    canvas.create_polygon(150, 200, 300, 100, 450, 200, fill='red', outline='black', width=2)

    # Draw door in the center
    canvas.create_rectangle(250, 230, 350, 300, fill='brown', outline='black', width=2)

    # Draw windows on either side
    window_width = 40
    window_height = 40
    canvas.create_rectangle(180, 230, 220, 270, fill='light grey', outline='black', width=2)
    canvas.create_rectangle(380, 230, 420, 270, fill='light grey', outline='black', width=2)

    # Load the moon image
    moon_image = Image.open("C:/Users/Rajat/Documents/GitHub/exploringPython/tkinter/moon.jpg")  
    moon_image = moon_image.resize((70, 70))  # Adjust the size if needed
    moon_photo = ImageTk.PhotoImage(moon_image)

    # Create the moon image on the canvas
    canvas.create_image(80, 80, anchor=tk.NW, image=moon_photo)

    # Write student name on top-center
    canvas.create_text(300, 30, text="Rajat Disawal", font=('Times New Roman', 16, 'bold'), fill='black')

    # Write "My Happy Home" on bottom-center
    canvas.create_text(300, 350, text="MY HAPPY HOME", font=('Times New Roman', 16, 'bold'), fill='black')

# Create the main window
root = tk.Tk()
root.title("Widget Creation")

# Create a canvas
canvas = tk.Canvas(root, width=600, height=400)
canvas.pack(expand=True)

# Call the draw_house function
draw_house(canvas)

# Run the Tkinter event loop
root.mainloop()
