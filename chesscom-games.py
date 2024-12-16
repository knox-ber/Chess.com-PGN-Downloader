import urllib.request
import json
import datetime
import sys
import time

def show_header():
    # Prints a stylized header at program start
    red = "\033[91m"
    green = "\033[92m"
    yellow = "\033[93m"
    blue = "\033[94m"
    magenta = "\033[95m"
    cyan = "\033[96m"
    reset = "\033[0m"

    print(f"{red} ____            _       _             _               _           {reset}")
    print(f"{red}/ ___|  ___ _ __(_)_ __ | |_          | |__   ___  ___| |__   ___  {reset}")
    print(f"{yellow}\\___ \\ / __| '__| | '_ \\| __|         | '_ \\ / _ \\/ __| '_ \\ / _ \\ {reset}")
    print(f"{yellow} ___) | (__| |  | | |_) | |_          | | | |  __/ (__| | | | (_) |{reset}")
    print(f"{green}|____/ \\___|_|  |_| .__/ \\__|         |_| |_|\\___|\\___|_| |_|\\___/ {reset}")
    print(f"{green}                  |_|                                              {reset}")
    print(f"{blue}                             _           ___       ____            {reset}")
    print(f"{blue} _ __   ___  _ __    _      | | ___ __  / _ \\__  _| ___|           {reset}")
    print(f"{magenta}| '_ \\ / _ \\| '__|  (_)     | |/ / '_ \\| | | \\ \\/ /___ \\           {reset}")
    print(f"{magenta}| |_) | (_) | |      _      |   <| | | | |_| |>  < ___) |          {reset}")
    print(f"{cyan}| .__/ \\___/|_|     (_)     |_|\_\\_| |_|\\___//_/\\_\\____/           {reset}")
    print(f"{cyan}|_|                                                               \n{reset}")

def show_progress_bar(progress, total, width=30):
    # Displays a real-time progress bar during the download process
    percentage = progress / total
    filled = int(width * percentage)
    bar = "#" * filled + "-" * (width - filled)
    sys.stdout.write(f"\rImporting games: [{bar}] {int(percentage*100)}%")
    sys.stdout.flush()

def get_archives(username):
    # Fetches all archive URLs for a given chess.com user
    base_url = f"https://api.chess.com/pub/player/{username}/games/archives"
    with urllib.request.urlopen(base_url) as response:
        data = json.loads(response.read().decode("utf-8"))
    return data.get("archives", [])

def filter_by_time(pgn, days):
    # Filters the downloaded PGN data based on the specified time range
    games = pgn.strip().split("\n\n\n")
    now = datetime.datetime.utcnow()
    delta_days = datetime.timedelta(days=days)
    limit = now - delta_days

    filtered_games = []
    for game in games:
        lines = game.strip().split("\n")
        game_date_utc = None
        for line in lines:
            if line.startswith("[UTCDate"):
                date_str = line.split('"')[1]
                game_date = datetime.datetime.strptime(date_str, "%Y.%m.%d")
                game_date_utc = game_date
                break
        if game_date_utc and game_date_utc >= limit:
            filtered_games.append(game.strip())

    return "\n\n\n".join(filtered_games) + "\n\n" if filtered_games else ""

def main():
    show_header()
    username = input("Enter the chess.com username: ").strip()
    print("\nDownload options:")
    print("1) Download all games")
    print("2) Download games from a specific timeframe (in days)")
    choice = input("Choose an option (1 or 2): ").strip()

    days = None
    if choice == "2":
        days = int(input("Enter the number of days: ").strip())

    archives = get_archives(username)
    if not archives:
        print("No games found for this user.")
        return

    output_file = f"{username}-Games.pgn"
    total = len(archives)
    progress = 0

    # Writes combined PGN data into a single file
    with open(output_file, "w", encoding="utf-8") as outfile:
        for archive_url in archives:
            progress += 1
            show_progress_bar(progress, total)

            # Download each month's PGN file
            pgn_url = archive_url + "/pgn"
            with urllib.request.urlopen(pgn_url) as resp:
                pgn_content = resp.read().decode("utf-8")

            # If a timeframe is specified, filter the games
            if pgn_content.strip():
                if days is not None:
                    pgn_content = filter_by_time(pgn_content, days)
                    if not pgn_content.strip():
                        continue
                outfile.write(pgn_content + "\n")

    show_progress_bar(total, total)
    print("\n\nGames have been downloaded and combined into", output_file)

if __name__ == "__main__":
    main()
