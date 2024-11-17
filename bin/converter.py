import os
import sys
from tkinter import Tk, filedialog

import markdown


def convert_markdown_to_html(input_file, output_file):
    """
    Converts a Markdown file to an HTML file.
    Args:
        input_file (str): Path to the input Markdown file.
        output_file (str): Path to save the output HTML file.
    """
    try:
        with open(input_file, "r", encoding="utf-8") as md_file:
            md_content = md_file.read()

        html_content = markdown.markdown(md_content)

        with open(output_file, "w", encoding="utf-8") as html_file:
            html_file.write(html_content)

        print(f"✅ Conversion successful! HTML saved at: {output_file}")
    except Exception as e:
        print(f"❌ Error during conversion: {e}")


def select_file():
    """
    Opens a file dialog to select a Markdown file.
    Returns:
        str: Path of the selected file.
    """
    root = Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select a Markdown file",
        filetypes=[("Markdown files", "*.md"), ("All files", "*.*")],
    )
    root.destroy()
    return file_path


if __name__ == "__main__":
    print("✨ Markdown to HTML Converter ✨")
    print("This script converts your Markdown file to an HTML file.\n")

    # Allow file selection through GUI
    input_path = select_file()
    if not input_path:
        print("❌ No file selected. Exiting.")
        sys.exit(1)

    # Determine output file path
    output_path = os.path.splitext(input_path)[0] + ".html"

    print(f"\nConverting:\n  📄 {input_path} \nTo:\n  🌐 {output_path}\n")
    convert_markdown_to_html(input_path, output_path)

    # Offer to open the resulting file
    if os.name == "nt":  # Windows
        os.system(f"start {output_path}")
    elif os.name == "posix":  # macOS/Linux
        os.system(f"open {output_path}")
    else:
        print(f"➡️ HTML file ready: {output_path}")
