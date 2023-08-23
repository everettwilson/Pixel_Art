# Pixel Art Creator
I used ChatGPT to help recreate one of my first (long-lost) projects I made outside of class in high school. I had stayed up late several nights working on this. ChatGPT very quicly created this solution with probably 10% of the lines that I used originally, and functionality that I didn't know existed. Of course, it even wrote this README.md file. 

Pixel Art Creator is a simple GUI application written in Python using the `tkinter` library. It allows users to create pixel art by clicking on a grid of squares, cycling through a set of predefined colors.

## Features

- Create pixel art on a customizable grid.
- Click on squares to cycle through colors.
- Dynamically set grid size via command-line arguments.

## Installation

1. Ensure you have Python 3 installed. You can download it from [Python's official website](https://www.python.org/downloads/).

2. Clone the repository or download the `pixel_art_app.py` file:

```bash
git clone https://github.com/everettwilson/Pixel_Art.git
```

3. Navigate to the directory containing the `pixel_art.py` file:

```bash
cd Pixel_Art
```

## Usage

Run the program by specifying the grid size as an argument:

```bash
python3 pixel_art.py 5
```

The above command will produce a 5x5 grid. You can specify any grid size as per your preference.

## Customization

- **Changing Colors**: To customize the set of colors, modify the `self.colors` list in the `PixelArtApp` class.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is open-source and available under the [MIT License](https://choosealicense.com/licenses/mit/).
```

Remember that some terminals might not support direct pasting, and in such cases, `vim` provides a paste mode to handle pasting content properly. You can enable it by typing `:set paste` before entering the insert mode. Once you've pasted your content, exit paste mode with `:set nopaste`.
