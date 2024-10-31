from PIL import Image

def encrypt_image(input_image_path, output_image_path, key):
    # Open the image
    image = Image.open(input_image_path)
    pixels = image.load()

    # Encrypt by modifying each pixel
    for x in range(image.width):
        for y in range(image.height):
            r, g, b = pixels[x, y]
            # Modify each color channel by adding the key, wrapping around at 255
            pixels[x, y] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
    
    # Save the encrypted image
    image.save(output_image_path)
    print("Image encrypted and saved as", output_image_path)

def decrypt_image(input_image_path, output_image_path, key):
    # Open the encrypted image
    image = Image.open(input_image_path)
    pixels = image.load()

    # Decrypt by reversing the modification on each pixel
    for x in range(image.width):
        for y in range(image.height):
            r, g, b = pixels[x, y]
            # Modify each color channel by subtracting the key, wrapping around at 0
            pixels[x, y] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)
    
    # Save the decrypted image
    image.save(output_image_path)
    print("Image decrypted and saved as", output_image_path)

# User input for file paths and key
input_path = input("Enter the path to the image: ")
output_path = input("Enter the path to save the output image: ")
key = int(input("Enter an encryption key (integer): "))
mode = input("Enter 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()

# Encrypt or decrypt based on the user's choice
if mode == 'encrypt':
    encrypt_image(input_path, output_path, key)
elif mode == 'decrypt':
    decrypt_image(input_path, output_path, key)
else:
    print("Invalid mode selected. Please enter 'encrypt' or 'decrypt'.")
