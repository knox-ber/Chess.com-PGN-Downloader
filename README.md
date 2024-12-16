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
   ![Screenshot_20241215_212001](https://github.com/user-attachments/assets/e66402c5-ffdb-4a2f-aeb7-9359fbba969c)

2. **Choose download mode:**  
   - **Option 1:** Download all games  
   - **Option 2:** Download games played within a specified number of days
   ![Screenshot_20241215_212100](https://github.com/user-attachments/assets/1484b64c-4bd2-4b0f-bac2-d03b18fe234a)
  
3. **Import process:**  
   The script will fetch and combine all retrieved games into one PGN file.
   ![Screenshot_20241215_212213](https://github.com/user-attachments/assets/c0840a79-695a-43ee-8e23-da84584836a6)

4. **Result:**  
   Once complete, the combined PGN file will appear on your desktop.
   ![Screenshot_20241215_212354](https://github.com/user-attachments/assets/661daa06-a450-42ee-9e02-1eb642c08787)

## 💻 Requirements

- Python 3.x
- Internet connection
- A valid Chess.com username

## 📥 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/chess-pgn-downloader.git
2. Navigate into the project directory:
   ```bash
   cd chess-pgn-downloader
3. Run the script
   ```bash
   python3 chesscom-games.py

## ⚖️ License
This project is licensed under the MIT License.
