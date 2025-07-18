# HTML Smuggling Payload Delivery Techniques

This repository demonstrates advanced HTML smuggling techniques that bypass Secure Web Gateways (SWGs), network defenses, and file-based malware detection. Each technique reconstructs the payload on the client-side, avoiding traditional file delivery methods and perimeter detection systems.

## Usage

1. Place your test payload into the `payloads/` folder  
2. Start a local Node.js web server:

   bash
   npm install -g http-server
   http-server -p 8080

## Overview

This project includes 3 core payload delivery techniques:

### 1. Image Steganography ("Steg")
- Embeds a payload within a PNG image using least significant bit (LSB) steganography  
- Payload is extracted in the browser using JavaScript and dropped via a Blob  
- No `Content-Disposition`, no file headers, and nothing malicious in transit  

### 2. Chunked Payload Reassembly ("Chunk")
- Splits a binary file into small byte arrays or files  
- Delivers each chunk via separate HTTP requests or inline JavaScript  
- Client-side JS reassembles the payload using `Uint8Array` + `Blob`  

### 3. Base64-Embedded JavaScript Blob ("Embed")
- Full binary is Base64-encoded and embedded directly in JavaScript  
- JS reconstructs and triggers download  
- Entire file is self-contained in the HTML page
Note: For this one, builder.py will place the update template in ouput folder. Test using the file otherwise it wont work. 

## Theory Around Why It Works

These techniques avoid signature detection by reconstructing the malicious file entirely within the browser using native APIs. There is no observable file download over the wire, making it extremely difficult for network-based security tools to detect or block.

