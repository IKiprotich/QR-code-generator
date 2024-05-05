import tkinter as tk
import qrcode
from PIL import Image, ImageTk


def qr_generator():
    data = input_entry.get()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=12,
        border=6
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("Qrcode.png")

    qr_image = qr_image.resize((200, 200), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(qr_image)

    photo = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=photo)
    qr_label.photo = photo
    message_label.config(text="Fast QR code generation")


app = tk.Tk()
app.title("Generate QR code")

input_label = tk.Label(app, text="Enter the data for the QR code")
input_label.pack()

input_entry = tk.Entry(app, font=("Helvetica", 12))
input_entry.pack()

generate_button = tk.Button(app, text="Generate QR code", command=qr_generator, font=("Helvetica", 12))
generate_button.pack()

message_label = tk.Label(app, text="", font=("Helvetica", 12))
message_label.pack()

qr_label = tk.Label(app)
qr_label.pack()

app.mainloop()



