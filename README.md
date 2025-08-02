# File Zipper

A simple and intuitive GUI application for compressing files into ZIP archives and extracting ZIP files, built with Python and Tkinter.

## Features

- **File Compression**: Select multiple files and compress them into a single ZIP archive
- **File Extraction**: Extract ZIP files to any directory of your choice
- **User-Friendly Interface**: Clean and simple GUI with easy-to-use buttons
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **No Dependencies**: Uses only Python's built-in libraries

## Screenshots

The application provides a clean interface with:

- A main title "File Zipper and Unzipper"
- "Select Files to Compress" button for creating ZIP archives
- "Select ZIP to Extract" button for extracting ZIP files
- Status messages showing operation results

## Requirements

- Python 3.x
- tkinter (usually comes pre-installed with Python)

## Installation

1. Clone or download this repository:

```bash
git clone <repository-url>
cd zipper
```

2. No additional installation required! The application uses only Python's built-in libraries.

## Usage

### Running the Application

```bash
python main.py
```

### How to Use

1. **Compressing Files:**

   - Click "Select Files to Compress"
   - Choose the files you want to compress (you can select multiple files)
   - Choose where to save the ZIP file and give it a name
   - The files will be compressed and you'll see a success message

2. **Extracting Files:**
   - Click "Select ZIP to Extract"
   - Choose the ZIP file you want to extract
   - Select the destination folder where you want to extract the files
   - The files will be extracted and you'll see a success message

## Project Structure

```
zipper/
├── main.py          # Main GUI application
├── zipper.py        # Core compression/extraction functions
├── README.md        # This file
└── LICENSE          # License information
```

## How It Works

- **`main.py`**: Contains the `FileZipperGUI` class that creates the user interface using Tkinter
- **`zipper.py`**: Contains the core functions:
  - `compress_files()`: Compresses multiple files into a ZIP archive
  - `extract_zip()`: Extracts a ZIP file to a specified directory

## Contributing

Feel free to contribute to this project by:

- Reporting bugs
- Suggesting new features
- Submitting pull requests

## License

This project is licensed under the terms specified in the LICENSE file.

## Future Enhancements

Potential improvements for future versions:

- Password protection for ZIP files
- Progress bars for large files
- Support for other archive formats (RAR, 7Z, etc.)
- Drag and drop functionality
- Batch processing capabilities

## Troubleshooting

If you encounter any issues:

1. Make sure you have Python 3.x installed
2. Ensure tkinter is available (it's included with most Python installations)
3. Check that you have write permissions in the directories you're working with

---

**Note**: This is a simple utility tool designed for basic file compression and extraction needs. For more advanced features, consider using dedicated compression software.
