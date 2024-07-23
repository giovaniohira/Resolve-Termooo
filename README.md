# Term.ooo Solver

## Overview

This project automates the daily completion of the online word game Term.ooo. It uses the `selenium` library to interact with the website and input a word for each day.

![Term.ooo Automation](media/readme.gif)

## Features

- Calculates the number of days since January 1, 2022.
- Reads a daily word from a file.
- Uses Selenium to automate entering the daily word into the Term.ooo game.

## Requirements

- Python 3.x
- Selenium
- Chrome WebDriver

## Installation

1 - **Clone this repo**

   ```

   git clone github.com/giovaniohira/Resolve-Termooo
   cd your-repository-directory

   ```
2 - **Create a Virtual Environment**

  *2.1 Windows*

  ```

  python -m venv venv
  .venv\Scripts\activate

  ```

  *2.2 Linux*
  ```

  python -m venv venv
  source venv/bin/activate

  ```
3 - **Install Dependencies**

  ```

  pip install -r requirements.txt

  ```
## Run the script
```

python main.py

```
