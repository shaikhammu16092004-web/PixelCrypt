# =========================================================
#        Pixel Manipulation Image Encryption Tool
#           Developed for Prodigy InfoTech
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
        title="Select an Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )

    # Show selected file path
    if file_path:
        selected_label.config(text=f"Selected File:\n{file_path}")


# =========================================================
# Function to Encrypt Image
# =========================================================
def encrypt_image():

    try:
        # Check if image is selected
        if file_path == "":
            messagebox.showerror("Error", "Please select an image first!")
            return

        # Get secret key from user
        key = int(key_entry.get())

        # Open image
        img = Image.open(file_path)

        # Load image pixels
        pixels = img.load()

        # Loop through image pixels
        for i in range(img.size[0]):
            for j in range(img.size[1]):

                # Get RGB values
                r, g, b = pixels[i, j]

                # Encrypt RGB values using secret key
                pixels[i, j] = (
                    (r + key) % 256,
                    (g + key) % 256,
                    (b + key) % 256
                )

        # Save encrypted image
        encrypted_path = "encrypted_image.png"
        img.save(encrypted_path)

        # Success message
        messagebox.showinfo(
            "Success",
            f"Image Encrypted Successfully!\n\nSaved as:\n{encrypted_path}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric key!")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# =========================================================
# Function to Decrypt Image
# =========================================================
def decrypt_image():

    try:
        # Check if image is selected
        if file_path == "":
            messagebox.showerror("Error", "Please select an image first!")
            return

        # Get secret key from user
        key = int(key_entry.get())

        # Open encrypted image
        img = Image.open(file_path)

        # Load pixels
        pixels = img.load()

        # Loop through image pixels
        for i in range(img.size[0]):
            for j in range(img.size[1]):

                # Get RGB values
                r, g, b = pixels[i, j]

                # Decrypt RGB values
                pixels[i, j] = (
                    (r - key) % 256,
                    (g - key) % 256,
                    (b - key) % 256
                )

        # Save decrypted image
        decrypted_path = "decrypted_image.png"
        img.save(decrypted_path)

        # Success message
        messagebox.showinfo(
            "Success",
            f"Image Decrypted Successfully!\n\nSaved as:\n{decrypted_path}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric key!")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# =========================================================
# Main GUI Window
# =========================================================

root = Tk()

root.title("Image Encryption Tool")
root.geometry("650x500")
root.config(bg="#0f172a")


# =========================================================
# Heading
# =========================================================
heading = Label(
    root,
    text="Pixel Manipulation Image Encryption Tool",
    font=("Arial", 20, "bold"),
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
selected_label = Label(
    root,
    text="No Image Selected",
    font=("Arial", 10),
    bg="#0f172a",
    fg="white",
    wraplength=500
)

selected_label.pack(pady=10)


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