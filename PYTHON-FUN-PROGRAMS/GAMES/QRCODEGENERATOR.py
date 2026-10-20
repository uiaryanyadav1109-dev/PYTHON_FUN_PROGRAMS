#Install the required library
#Open PowerShell or your VS Code terminal and run:
#python -m pip install "qrcode[pil]

import qrcode
from pathlib import Path
from datetime import datetime


def generate_qr():
    print("\n" + "=" * 45)
    print("          PYTHON QR CODE GENERATOR")
    print("=" * 45)

    # Get content
    data = input("\nEnter text or URL: ").strip()

    if not data:
        print("Error: Input cannot be empty.")
        return

    # Get filename
    filename = input(
        "Enter output filename (default: my_qr): "
    ).strip()

    if not filename:
        filename = "my_qr"

    # Remove an optional .png extension
    if filename.lower().endswith(".png"):
        filename = filename[:-4]

    # Validate filename
    if not filename or filename in {".", ".."}:
        print("Error: Invalid filename.")
        return

    if any(char in filename for char in '<>:"/\\|?*'):
        print("Error: Filename contains invalid characters.")
        return

    # Get colors
    fill_color = input(
        "QR color (default: black): "
    ).strip() or "black"

    back_color = input(
        "Background color (default: white): "
    ).strip() or "white"

    # Generate QR code
    try:
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4
        )

        qr.add_data(data)
        qr.make(fit=True)

        image = qr.make_image(
            fill_color=fill_color,
            back_color=back_color
        )

        # Create output directory
        output_dir = Path("generated_qr")
        output_dir.mkdir(exist_ok=True)

        output_path = output_dir / f"{filename}.png"

        # Avoid overwriting existing files
        if output_path.exists():
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = output_dir / f"{filename}_{timestamp}.png"

        image.save(output_path)

        print("\nQR code generated successfully!")
        print(f"Saved to: {output_path.resolve()}")

    except ValueError:
        print("Error: Invalid color or QR code settings.")

    except OSError as error:
        print(f"File error: {error}")

    except Exception as error:
        print(f"Unexpected error: {error}")


def main():
    while True:
        generate_qr()

        again = input(
            "\nGenerate another QR code? (y/n): "
        ).strip().lower()

        if again not in ("y", "yes"):
            print("\nThanks for using the QR Code Generator!")
            break


if __name__ == "__main__":
    main()
