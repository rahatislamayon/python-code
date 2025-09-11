import qrcode

def generate_qr_code(link, file_name="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Fixed uppercase H
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)
    print(f"QR code generated and saved as {file_name}")

if __name__ == "__main__":
    link = input("Enter the link to generate QR code: ")
    generate_qr_code(link)