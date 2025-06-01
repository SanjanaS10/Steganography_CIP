from stego import encode_message, decode_message

def main():
    print("Steganography Tool")
    choice = input("1. Encode\n2. Decode\nChoose (1/2): ")

    if choice == '1':
        img_in = input("Enter input image path: ") or "input.png"
        msg = input("Enter message to hide: ")
        img_out = input("Enter output image path: ") or "stego_output.png"
        encode_message(img_in, msg, img_out)
    elif choice == '2':
        img_in = input("Enter image to decode: ") or "stego_output.png"
        decode_message(img_in)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
