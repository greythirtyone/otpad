from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import hashlib
import random
import string

def generate_one_time_pad(length):
    return ''.join(random.choices(string.ascii_uppercase, k=length))

def create_pdf(filename, rows, columns):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    c.drawString(72, height - 72, "One-Time Pad Table")

    col_width = width / (columns + 1)
    row_height = 20

    for row in range(rows):
        y_position = height - 72 - (row + 1) * row_height
        for col in range(columns):
            x_position = 72 + col * col_width
            pad = generate_one_time_pad(5)  # Each pad is 5 characters long
            c.drawString(x_position, y_position, pad)

    c.save()

if __name__ == "__main__":
    random_int = random.randint(0, 2**64)
    hash_object = hashlib.sha1(str(random_int).encode())
    prepend_hash = hash_object.hexdigest()[:8]
    prepended_filename = f'./pads/{prepend_hash}-otp.pdf'
    create_pdf(prepended_filename , 10, 5)
