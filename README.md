# Chess.com PGN Downloader ♟️

A Python script that retrieves Chess.com games in PGN format either all or within a chosen timeframe and combines them into a single file.


## Table of Contents

1. [✨ Features](https://github.com/knox-ber/Chess.com-PGN-Downloader?tab=readme-ov-file#-features)
2. [🔧 How It Works](https://github.com/knox-ber/Chess.com-PGN-Downloader?tab=readme-ov-file#-how-it-works)
3. [💻 Requirements](https://github.com/knox-ber/Chess.com-PGN-Downloader?tab=readme-ov-file#-requirements)
4. [📥 Installation](https://github.com/knox-ber/Chess.com-PGN-Downloader?tab=readme-ov-file#-installation)
5. [⚖️ License](https://github.com/knox-ber/Chess.com-PGN-Downloader?tab=readme-ov-file#%EF%B8%8F-license)


## ✨ Features

- Prompt for a Chess.com username
- Choose between downloading all available games or games played within a specific number of days
- Automatically imports and merges games into a single `.pgn` file on your desktop

## 🔧 How It Works

1. **Run the script:**  
   Execute the Python script and enter your Chess.com username when prompted.
   
   ![](https://github.com/knox-ber/Chess.com-PGN-Downloader/blob/main/Pictures/Screenshot_20241215_212001.png)

3. **Choose download mode:**  
   **Option 1:** Download all games  
   **Option 2:** Download games played within a specified number of days
   
   ![](https://github.com/knox-ber/Chess.com-PGN-Downloader/blob/main/Pictures/Screenshot_20241215_212100.png)
  
5. **Import process:**  
   The script will fetch and combine all retrieved games into one PGN file.
   
   ![](https://github.com/knox-ber/Chess.com-PGN-Downloader/blob/main/Pictures/Screenshot_20241215_212213.png)

7. **Result:**  
   Once complete, the combined PGN file will appear on your desktop.
   
   ![](https://github.com/knox-ber/Chess.com-PGN-Downloader/blob/main/Pictures/Screenshot_20241215_212354.png)

## 💻 Requirements

- Python 3.x
- Internet connection
- A valid Chess.com username

## 📥 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/knox-ber/chess-pgn-downloader.git
2. Navigate into the project directory:
   ```bash
   cd chess-pgn-downloader
3. Run the script
   ```bash
   python3 chesscom-games.py

## ⚖️ License
This project is licensed under the MIT License.
