import tkinter as tk
import qrcode
from PIL import Image, ImageTk

class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Genarator")

        self.url_label = tk.Label(root, text="Enter Website URl: ")
        self.url_label.pack()

        self.url_entry = tk.Entry(root)
        self.url_entry.pack()

        self.generate_button = tk.Button(root, text="Generate", command=self.generate_qr_code)
        self.generate_button.pack()

        self.qr_code_label = tk.Label(root)
        self.qr_code_label.pack()

    def generate_qr_code(self):
        url = self.url_entry.get()
        if url:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(url)
            qr.make(fit=True)
            qr_image = qr.make_image(fill_color="black", back_color="white")

            qr_photo = ImageTk.PhotoImage(qr_image)

            self.qr_code_label.config(image=qr_photo)
            self.qr_code_label.image = qr_photo
        else:
            self.qr_code_label.config(text="Please enter a valid URL.")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()
