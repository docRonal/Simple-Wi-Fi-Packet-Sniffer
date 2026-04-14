from scapy.all import sniff

def packet_callback(packet):
    # Check if the packet has an IP layer
    if packet.haslayer("IP"):
        ip_src = packet["IP"].src
        ip_dst = packet["IP"].dst
        print(f"[+] IP Packet: {ip_src} -> {ip_dst}")
    
    # Check for raw data (e.g., payload)
    if packet.haslayer("Raw"):
        # Use repr() to make non-printable characters visible
        print(f"    [!] Raw Data: {repr(packet['Raw'].load)}")

def main():
    print("Starting packet capture... Press Ctrl+C to stop.")
    
    # iface: Name of your interface (e.g., 'wlan0', 'eth0', or 'wlan0mon')
    # prn: Callback function applied to every packet
    # store: Set to 0 to avoid keeping packets in memory
    try:
        sniff(iface="wlan0", prn=packet_callback, store=0)
    except PermissionError:
        print("Error: Permission denied. Please run as root (sudo).")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
