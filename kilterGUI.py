import tkinter as tk
from PIL import Image, ImageTk
import holdPositions as hp


roles = {
    "r12" : "#00FF00", # start
    "r13" : "#00FFFF", # middle
    "r14" : "#FF00FF", # finish
    "r15" : "#FFA500" # foot only
}

def split_string(s):
    #split the string into chunks of 8
    return [s[i:i+8] for i in range(0, len(s), 8)]

def create_kilterboard_gui(holdSequence):
    # Create the main window
    root = tk.Tk()
    root.title("Fake Kilterboard GUI")

    holds = split_string(holdSequence)

    # Load the Kilterboard image
    kilterboard_image = Image.open("GUI/kilter.jpg")  # Path to your image
    kilterboard_image = kilterboard_image.resize((kilterboard_image.width // 2, kilterboard_image.height // 2))
    kilterboard_photo = ImageTk.PhotoImage(kilterboard_image)
    

    # Create a canvas to display the image
    canvas = tk.Canvas(root, width=kilterboard_image.width, height=kilterboard_image.height)
    canvas.pack()

    # Place the image on the canvas
    canvas.create_image(0, 0, anchor=tk.NW, image=kilterboard_photo)
    
    # Label to show mouse coordinates
    coord_label = tk.Label(root, text="X: 0, Y: 0", font=("Arial", 12))
    coord_label.pack()

    # Function to update coordinates on hover
    def show_coordinates(event):
        coord_label.config(text=f"X: {event.x}, Y: {event.y}")
        
    # Bind mouse movement to show coordinates
    canvas.bind("<Motion>", show_coordinates)

    # Iterate through the dictionary and draw the holds
    for hold in holds:
        position = hold[0:5]
        role = hold[5:8]
        color = roles[role]
        coordinates = hp.hold_positions[position]
        x = coordinates[0]
        y = coordinates[1]
        canvas.create_oval(x-10, y-10, x+10, y+10, outline=color, width=3)
        
        
    # Start the Tkinter event loop
    root.mainloop()
    
def show_coordinates(self, event):
        """Displays the mouse coordinates when hovering over the image."""
        self.coord_label.config(text=f"X: {event.x}, Y: {event.y}")

# Run the GUI
create_kilterboard_gui("p1081r15p1146r12p1148r12p1250r13p1283r13p1352r13p1371r13p1392r14p1561r15")