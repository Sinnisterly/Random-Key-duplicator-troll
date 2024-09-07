
# Keyboard Troll Script

This Python script listens to keyboard inputs and randomly manipulates them based on the current hour. It duplicates or blocks key presses during specific hours, and allows normal typing at other times. The console window is hidden while the script runs in the background.

## Features

- **Hides Console Window:** The script hides the console window upon running using the `ctypes` library.
- **Key Manipulation Based on Hour:** 
  - If the current hour contains the digits '1' or '4' (e.g., 1, 10, 14, 21), the script:
    - Duplicates key presses with a 7% probability.
    - Blocks key presses with a 7% probability.
  - Outside these hours, key presses pass through normally.
- **Exit Mechanism:** The script stops when the `ESC` or `END` key is pressed.

## Parameters

- **DUPLICATE_PROBABILITY:** The probability (7%) of duplicating a key press.
- **BLOCK_PROBABILITY:** The probability (7%) of blocking a key press.

## How It Works

- **on_press(key):**
  - Checks the current hour.
  - If the hour contains '1' or '4', randomly duplicates or blocks the key press based on predefined probabilities.
  - Otherwise, allows the key press to pass through.
  
- **on_release(key):**
  - If the `ESC` or `END` key is released, stops the keyboard listener.

- **Keyboard Listener:**
  - Runs in the background, continuously listening for key presses and releases until the `ESC` or `END` key is pressed.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/repo-name.git
   cd repo-name
   ```

2. Install dependencies: (repeat for each)
   ```bash
   pip install pynput
   ```

3. Run the script:
   ```bash
   python scriptnamehere.py
   ```

## Usage

- The script will hide the console window and manipulate key presses based on the current hour.
- To stop the script, press the `ESC` or `END` key.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
