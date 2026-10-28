# QR Nova — QR Code Studio

A static, browser-based QR generator and scanner.

## Features
- Generate QR codes for websites, text, Wi-Fi, email, phone and SMS.
- Customize colors, size, error correction, optional logo and label.
- Download QR codes as PNG.
- Scan QR codes using a camera or an uploaded image.
- Display scanned content as text; only show an Open link action for HTTP(S) URLs.
- Camera is started only after the user clicks **Start camera**.

## Run locally
Use a local web server (camera APIs generally require HTTPS or localhost). For example, with Python installed:
```bash
python -m http.server 8000
```
Then open `http://localhost:8000`.

## Deploy to Vercel
1. Upload `index.html`, `app.js`, and `vercel.json` to a GitHub repository.
2. Import the repository into Vercel as a static site (no build command needed).
3. Deploy. Use the HTTPS deployment URL for camera scanning.
4. Test camera permissions, image scanning, generation, downloads and mobile layout.

## Security notes
- This is a static client-side tool; it has no login, server, database or API that stores QR contents.
- QR data is treated as untrusted text and inserted with `textContent`, not HTML. Links are never opened automatically and only HTTP(S) links can be opened from the result.
- Vercel security headers are configured in `vercel.json`. If hosting elsewhere, configure equivalent headers at that host.
- Libraries are loaded from pinned CDN URLs. A CDN outage can affect the generator/scanner. For stricter supply-chain security, self-host reviewed library files and use Subresource Integrity hashes.
- No website can be guaranteed completely safe from all attackers, viruses or future dependency vulnerabilities. Keep dependencies updated, review changes, and avoid adding unknown scripts or extensions.
- Camera access requires browser permission and HTTPS (or localhost). The scanner does not upload camera frames to a QR Nova backend.
- A QR code may point to a phishing or malicious website. Always inspect the full URL before opening it.
