from PIL import Image
import sys

def embed_lsb_blue(cover_path, payload_path, out_path):
    # Load image
    img = Image.open(cover_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    pixels = img.load()
    w, h = img.size

    # Read payload and append null terminator
    with open(payload_path, 'rb') as f:
        data = f.read()
    data += b'\x00'

    # Convert to bit string
    bits = ''.join(f'{byte:08b}' for byte in data)
    if len(bits) > w * h:
        raise ValueError("Payload too large for this image!")

    # Embed bits into blue LSB
    idx = 0
    for y in range(h):
        for x in range(w):
            if idx >= len(bits):
                break
            r, g, b = pixels[x, y]
            bit = int(bits[idx])
            b = (b & ~1) | bit
            pixels[x, y] = (r, g, b)
            idx += 1
        if idx >= len(bits):
            break

    img.save(out_path)
    print(f"Embedded {len(data)-1} bytes + null in {out_path}.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python embed.py cover.png payload.bin stego.png")
        sys.exit(1)
    embed_lsb_blue(sys.argv[1], sys.argv[2], sys.argv[3])
