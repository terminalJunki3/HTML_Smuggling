import os

def build_payload_embed(input_file, output_html):
    with open(input_file, "rb") as f:
        byte_data = f.read()
    byte_array = ",".join(str(b) for b in byte_data)
    filename = os.path.basename(input_file)
    with open("template.html", "r", encoding="utf-8") as t:
        template = t.read()
    output = template.replace("{array_placeholder}", byte_array).replace("{filename_placeholder}", filename)
    with open(output_html, "w", encoding="utf-8") as out:
        out.write(output)
    print(f"Generated: {output_html}")

if __name__ == "__main__":
    input_folder = "./payloads"
    output_folder = "./output"
    for file in os.listdir(input_folder):
        full_path = os.path.join(input_folder, file)
        if os.path.isfile(full_path):
            name, _ = os.path.splitext(file)
            build_payload_embed(full_path, os.path.join(output_folder, name + "_embed.html"))
