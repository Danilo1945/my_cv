import qrcode

# URL to encode in the QR code
url = "https://dmoya.ddns.net/"

# Generate the QR code
img = qrcode.make(url)

# Save the QR code image
img.save("data/qr_code.png")

print("QR code generated and saved to data/qr_code.png")
