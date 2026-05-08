# =========================================================
#        Pixel Manipulation Image Encryption Tool
# =========================================================

# Import required libraries
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image

# Variable to store selected image path
file_path = ""


# =========================================================
# Function to Select Image
# =========================================================
def select_image():

    global file_path

    # Open file explorer
    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )

    # Show selected image message
    if file_path:
        path_label.config(text="Image Selected Successfully")


# =========================================================
# Function to Encrypt Image
# =========================================================
def encrypt_image():

    global file_path

    # Check image selected or not
    if file_path == "":
        messagebox.showerror("Error", "Please select an image first!")
        return

    # Get secret key
    key = key_entry.get().strip()

    # Check empty key
    if key == "":
        messagebox.showerror("Error", "Please enter secret key!")
        return

    # Check numeric key
    if not key.isdigit():
        messagebox.showerror("Error", "Secret key must be a number!")
        return

    # Convert key to integer
    key = int(key)

    try:

        # Open image
        img = Image.open(file_path)

        # Convert image into RGBA mode
        img = img.convert("RGBA")

        # Load pixels
        pixels = img.load()

        # Loop through all pixels
        for i in range(img.size[0]):
            for j in range(img.size[1]):

                # Get RGBA values
                r, g, b, a = pixels[i, j]

                # Encrypt RGB values
                pixels[i, j] = (
                    (r + key) % 256,
                    (g + key) % 256,
                    (b + key) % 256,
                    a
                )

        # Save encrypted image
        encrypted_path = "encrypted_image.png"
        img.save(encrypted_path)

        # Success message
        messagebox.showinfo(
            "Success",
            f"Image Encrypted Successfully!\n\nSaved as:\n{encrypted_path}"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


# =========================================================
# Function to Decrypt Image
# =========================================================
def decrypt_image():

    global file_path

    # Check image selected or not
    if file_path == "":
        messagebox.showerror("Error", "Please select an image first!")
        return

    # Get secret key
    key = key_entry.get().strip()

    # Check empty key
    if key == "":
        messagebox.showerror("Error", "Please enter secret key!")
        return

    # Check numeric key
    if not key.isdigit():
        messagebox.showerror("Error", "Secret key must be a number!")
        return

    # Convert key to integer
    key = int(key)

    try:

        # Open image
        img = Image.open(file_path)

        # Convert image into RGBA mode
        img = img.convert("RGBA")

        # Load pixels
        pixels = img.load()

        # Loop through all pixels
        for i in range(img.size[0]):
            for j in range(img.size[1]):

                # Get RGBA values
                r, g, b, a = pixels[i, j]

                # Decrypt RGB values
                pixels[i, j] = (
                    (r - key) % 256,
                    (g - key) % 256,
                    (b - key) % 256,
                    a
                )

        # Save decrypted image
        decrypted_path = "decrypted_image.png"
        img.save(decrypted_path)

        # Success message
        messagebox.showinfo(
            "Success",
            f"Image Decrypted Successfully!\n\nSaved as:\n{decrypted_path}"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


# =========================================================
# Main GUI Window
# =========================================================

root = Tk()

root.title("PixelCrypt")
root.geometry("500x550")
root.config(bg="#0f172a")


# =========================================================
# Heading
# =========================================================
heading = Label(
    root,
    text="PixelCrypt",
    font=("Arial", 28, "bold"),
    bg="#0f172a",
    fg="cyan"
)

heading.pack(pady=20)


# =========================================================
# Select Image Button
# =========================================================
select_btn = Button(
    root,
    text="Select Image",
    command=select_image,
    font=("Arial", 12, "bold"),
    bg="cyan",
    fg="black",
    padx=15,
    pady=8
)

select_btn.pack(pady=15)


# =========================================================
# Selected File Label
# =========================================================
path_label = Label(
    root,
    text="No Image Selected",
    font=("Arial", 10),
    bg="#0f172a",
    fg="white"
)

path_label.pack(pady=10)


# =========================================================
# Secret Key Label
# =========================================================
key_label = Label(
    root,
    text="Enter Secret Key",
    font=("Arial", 13, "bold"),
    bg="#0f172a",
    fg="white"
)

key_label.pack(pady=10)


# =========================================================
# Secret Key Entry Box
# =========================================================
key_entry = Entry(
    root,
    font=("Arial", 14),
    justify="center",
    width=20
)

key_entry.pack(pady=10)


# =========================================================
# Encrypt Button
# =========================================================
encrypt_btn = Button(
    root,
    text="Encrypt Image",
    command=encrypt_image,
    font=("Arial", 12, "bold"),
    bg="lime",
    fg="black",
    padx=20,
    pady=10
)

encrypt_btn.pack(pady=15)


# =========================================================
# Decrypt Button
# =========================================================
decrypt_btn = Button(
    root,
    text="Decrypt Image",
    command=decrypt_image,
    font=("Arial", 12, "bold"),
    bg="orange",
    fg="black",
    padx=20,
    pady=10
)

decrypt_btn.pack(pady=10)


# =========================================================
# Footer
# =========================================================
footer = Label(
    root,
    text="Developed by Amir Shaikh | Prodigy InfoTech Internship",
    font=("Arial", 10),
    bg="#0f172a",
    fg="gray"
)

footer.pack(side=BOTTOM, pady=20)


# Run GUI Window
root.mainloop()