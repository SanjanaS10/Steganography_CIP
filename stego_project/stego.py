from PIL import Image

def encode_message(image_path, message, output_path):
    
    binary_msg = ''.join(format(ord(char), '08b') for char in message) + '11111110'

    
    img = Image.open(image_path)
    pixels = list(img.getdata())
    new_pixels = []

    msg_index = 0
    for pixel in pixels:
        new_pixel = []
        for channel in pixel[:3]:   
            if msg_index < len(binary_msg):
                new_channel = (channel & ~1) | int(binary_msg[msg_index])
                msg_index += 1
            else:
                new_channel = channel
            new_pixel.append(new_channel)

         
        if len(pixel) == 4:
            new_pixel.append(pixel[3])
        new_pixels.append(tuple(new_pixel))

    img.putdata(new_pixels)
    img.save(output_path)
    print(f" Message encoded into '{output_path}'")


def decode_message(image_path):
    img = Image.open(image_path)
    pixels = list(img.getdata())

    binary_msg = ''
    for pixel in pixels:
        for channel in pixel[:3]:
            binary_msg += str(channel & 1)

    chars = [binary_msg[i:i+8] for i in range(0, len(binary_msg), 8)]
    message = ''

    for byte in chars:
        if byte == '11111110':   
            break
        message += chr(int(byte, 2))

    print(f" Hidden message: {message}")
