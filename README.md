# PRODIGY_CS_02

Develop a simple image encryption tool using pixel manipulation. You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel. Allow users to encrypt and decrypt images.

Explanation:
Encryption Function (encrypt_image): This function takes an image path, an output path, and a key. For each pixel, it adds the key value to each RGB channel (wrapping values over 255). It then saves the modified image.

Decryption Function (decrypt_image): This function reverses the encryption by subtracting the key from each RGB channel (wrapping values under 0) and saves the result.

User Input: Users provide the image path, output path, key, and mode ('encrypt' or 'decrypt').

Note: Using large values for the key can distort colors, so try with small values (e.g., 10-50) for better results.
