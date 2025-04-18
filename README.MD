# Tacticus Autoclicker

This program automates certain actions in the game Tacticus, such as skipping turns and setting the battle speed. It uses image recognition to locate UI elements on the screen and perform clicks. It *is* dumb and its on purpose.

## ⚠️ Warning ⚠️

**Important:** Snowprint Studios, the developer of the mobile game Tacticus, explicitly prohibits the following in their [Terms of Service](https://snowprintstudios.com/en/snowprint-studios-terms-of-service/#:~:text=Use%2C%20develop%2C%20distribute%20or%20sell%20cheats%2C%20automation%20software%20(bots)%2C%20hacks%20or%20any%20other%20unauthorized%20third%2Dparty%20software%20designed%20to%20modify%20a%20Game%3B):

> "Use, develop, distribute or sell cheats, automation software (bots), hacks or any other unauthorized third-party software **designed to modify a Game**."

Tacticus Autoclicker is designed to comply with these terms by not modifying the game in any way. It does not grant users any unfair advantages or privileges. Instead, it simply automates repetitive actions by simulating user input through image recognition.
Anyway the developer of Tacticus Autoclicker does not encourage anyone to use it and is not responsible for any consiquences that may or may not follow. Use this software responsibly and at your own risk.

## Installation


1. Clone this repository to your local machine:
   ```sh
   git clone https://github.com/your-repo/tacticus_autoclicker.git
   cd tacticus_autoclicker
   ```

2. Create a virtual environment to isolate dependencies:
   ```sh
   python -m venv venv
   ```

3. Activate the virtual environment:
    On Windows
    ```bat
    venv\Scripts\activate.bat
    ```
    On Linux/Mac
    ```sh
    source venv/bin/activate
    ```

4. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## How to Run

To run the program, execute the `run.py` script using Python:

```sh
python run.py [arguments]
```

## Arguments

The script accepts the following arguments:

- `--skip_turns`: Specifies the number of turns to skip. If provided, the program will set the battle speed to the fastest and skip the specified number of turns. Example:
  ```sh
  python run.py --skip_turns 10
  ```
  This will skip 10 turns in the game.

## Features

1. **Skip Turns**: The `skip_turns` function locates the "Next Turn" button on the screen and clicks it the specified number of times.
2. **Set Battle Speed**: The `set_battle_speed` function sets the battle speed to the fastest by interacting with the game's UI.

## Notes

- Ensure that the game is running and the UI elements (e.g., "Next Turn" button, battle speed settings) are visible on the screen for the program to work correctly.
- The program uses image files located in the `images` directory to identify UI elements. Do not modify or delete these files.
- The program is designed for specific screen resolutions and may require adjustments for different setups.