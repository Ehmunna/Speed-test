#!/usr/bin/env python3
import speedtest
import requests
import time
import sys
import os
import shutil
from datetime import datetime
from rich import print

# ===== Clear Screen =====
def clear():
    os.system("clear")

# ===== EH ASCII Banner (RED / CENTER / FIXED) =====
def show_header():
    width = shutil.get_terminal_size().columns
    lines = [
        "███████╗██╗  ██╗",
        "██╔════╝██║  ██║",
        "█████╗  ███████║",
        "██╔══╝  ██╔══██║",
        "███████╗██║  ██║",
        "╚══════╝╚═╝  ╚═╝",
        "",
        "Facebook  EH Munna",
        "Telegram  https://t.me/ehmunna999",
        "-" * 40
    ]
    for line in lines:
        print(f"[bold red]{line.center(width)}[/bold red]")

# ===== Refresh Screen with Header =====
def refresh_screen():
    clear()
    show_header()

# ===== Slow Print =====
def slow_print(text, delay=0.02):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()

# ===== Sound Alert =====
def play_alert():
    os.system("play -nq -t alsa synth 0.2 sine 440")

# ===== IP Info =====
def get_ip_info():
    try:
        r = requests.get("https://ipinfo.io/json", timeout=5).json()
        return (
            r.get("ip", "Unknown"),
            r.get("city", "Unknown"),
            r.get("country", "Unknown"),
            r.get("org", "Unknown")
        )
    except:
        return "Unknown", "Unknown", "Unknown", "Unknown"

# ===== Speed Test =====
def run_speedtest():
    refresh_screen()
    slow_print("\n🌐 Detecting best server...")
    st = speedtest.Speedtest()
    st.get_best_server()

    slow_print("⏬ Testing download speed...")
    down = st.download() / 1_000_000

    slow_print("⏫ Testing upload speed...")
    up = st.upload() / 1_000_000

    ping = st.results.ping
    ip, city, country, isp = get_ip_info()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n[bold green]===== SPEED TEST RESULT =====[/bold green]")
    print(f"[cyan]Time     :[/cyan] {now}")
    print(f"[cyan]IP       :[/cyan] {ip}")
    print(f"[cyan]Location :[/cyan] {city}, {country}")
    print(f"[cyan]ISP      :[/cyan] {isp}")
    print(f"[cyan]Download :[/cyan] [bold green]{down:.2f} Mbps[/bold green]")
    print(f"[cyan]Upload   :[/cyan] [bold green]{up:.2f} Mbps[/bold green]")
    print(f"[cyan]Ping     :[/cyan] [bold green]{ping} ms[/bold green]")

    with open("speedtest_results.txt", "a") as f:
        f.write(
            f"{now} | {ip} | {city},{country} | {isp} | "
            f"DL:{down:.2f} | UL:{up:.2f} | Ping:{ping}\n"
        )

    play_alert()
    input("\nPress Enter to return menu...")

# ===== History =====
def view_history():
    refresh_screen()
    print("\n[bold cyan]📜 HISTORY[/bold cyan]\n")
    if os.path.exists("speedtest_results.txt"):
        print(open("speedtest_results.txt").read())
    else:
        print("[red]No history found![/red]")
    input("\nPress Enter to return menu...")

# ===== Menu =====
def main_menu():
    while True:
        refresh_screen()
        print("[bold magenta]\n====== INTERNET SPEED TEST ======[/bold magenta]")
        print("[cyan]1[/cyan] Run Speed Test")
        print("[cyan]2[/cyan] View History")
        print("[cyan]3[/cyan] Exit")

        choice = input("\nSelect option: ").strip()

        if choice == "1":
            run_speedtest()
        elif choice == "2":
            view_history()
        elif choice == "3":
            slow_print("Exiting... Bye 👋")
            sys.exit()
        else:
            print("[red]Invalid choice![/red]")
            time.sleep(1)

# ===== Main =====
if __name__ == "__main__":
    main_menu()
