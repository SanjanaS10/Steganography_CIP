Simple Steganography Tool 



Overview

This project demonstrates a basic image steganography tool using Python and the Pillow library.
It hides a secret text message inside an image by modifying the least significant bits (LSB) of the image pixels.
You can encode a message into an image and later decode the hidden message from the image.


Features

- Encode a secret message into a PNG image
- Decode the hidden message from an encoded image
- Simple command-line interface (CLI)
- Uses an 8-bit delimiter to mark the end of the message
- Supports RGB and RGBA images



Requirements

=> Python 3.x
=> Pillow library
(pip install pillow)


How to Use

- Prepare an input image (PNG format recommended) in the project folder.

- Run the main script: python main.py

- Follow the on-screen instructions:

Encoding a Message:

Choose option 1 to encode
Enter the input image filename (default: input.png)
Enter the message you want to hide
Enter the output image filename (default: stego_output.png)
The program saves the image with the hidden message.

Decoding a Message
Choose option 2 to decode

- Enter the stego image filename (default: stego_output.png)
- The program prints the hidden message.

 


How It Works


Encoding: Converts the secret message to binary and appends an 8-bit delimiter (11111110) to mark the end.
Then replaces the least significant bit of each RGB pixel channel with bits from the message.

Decoding: Reads the least significant bit from each RGB channel in sequence, reconstructs bytes, and stops at the delimiter.



Notes:

- Use PNG images to avoid compression artifacts that can corrupt the hidden message.

- Keep the input image large enough to hide your message (each character needs 8 bits, and each pixel provides 3 bits for RGB).

- The current delimiter is 11111110 (one byte) to indicate the end of the message.

 
