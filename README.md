# Simple Wi-Fi Packet Sniffer

A lightweight Python-based network utility designed to intercept and analyze Wi-Fi traffic in real-time. This project uses the Scapy library to capture IP packets and log source/destination information.
# 🚀 Features

    Real-time Sniffing: Captures network packets on a specified interface.

    IP Tracking: Extracts and displays source and destination IP addresses.

    Extensible: Easily customizable to log HTTP headers, DNS queries, or raw data.

# 🛠 Prerequisites

The tool is designed for Linux environments (tested on Arch Linux).

    I work with Python 3.12.2

    Scapy library:
    Bash

    sudo pacman -S python-scapy
    # or for other distros:
    # pip install scapy

    Root Privileges: Required to access raw sockets for network sniffing.

# 💻 Usage

    Clone the repository:
    Bash

    git clone https://github.com/docRonal/Simple-Wi-Fi-Packet-Sniffer.git
    cd wifi-packet-sniffer

    Check your network interface:
    Run ip link to find your Wi-Fi interface name (e.g., wlan0 or wlp2s0). Update the iface parameter in main.py if necessary.

    Run the sniffer:
    Bash

    sudo python main.py

# ⚠️ Disclaimer

This tool is for educational and ethical testing purposes only. Unauthorized interception of network traffic is illegal in many jurisdictions. Always ensure you have explicit permission before monitoring a network.
