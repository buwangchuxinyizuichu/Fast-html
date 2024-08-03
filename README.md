# Fast-HTML

Fast-HTML is a Python-based project that converts PSD files into HTML files. It extracts layer information from the PSD file and generates an HTML file with the same layout.

## Features

- Extracts layer information from PSD files including text, images, position, size, and visibility.
- Generates an HTML file with the same layout as the PSD file.
- Handles both text and image layers.
- Adjusts the size and position of layers to fit the HTML file.

## Requirements

- Python 3.6 or higher
- PIL (Pillow)
- psd-tools

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/fast-html.git
```
2. Install the requirements:
```bash
pip install -r requirements.txt
```

## Usage

1. Place your PSD files in the `./raw` directory.
2. Run the `main.py` script and follow the prompts:
```bash
python main.py
```
3. The generated HTML files will be saved in the `./results` directory.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

Please note that this project is released with a Contributor Code of Conduct. By participating in this project you agree to abide by its terms.
