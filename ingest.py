import subprocess
import os

pdf_path = "data/input/ekstedts-1.pdf"

try:
    # Attempt to run docling as a command line tool
    result = subprocess.run(
        ["docling", pdf_path], capture_output=True, text=True, check=True
    )
    print("Docling executed successfully.")
    print("Stdout:", result.stdout)
    print("Stderr:", result.stderr)
except FileNotFoundError:
    print(
        "Error: 'docling' command not found. Please ensure docling is installed and in your PATH."
    )
except subprocess.CalledProcessError as e:
    print(f"Error executing docling: {e}")
    print("Stdout:", e.stdout)
    print("Stderr:", e.stderr)
