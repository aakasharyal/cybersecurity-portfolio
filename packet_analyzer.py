from scapy.all import sniff, IP, TCP, UDP
import csv
from datetime import datetime

# ── Firewall rules ───────────────────────────────────────────
blocked_ips   = ["192.168.56.100"]   # add any IP you want to block
blocked_ports = [23, 21, 4444]       # telnet, FTP, backdoor port

# ── Analyze each packet ──────────────────────────────────────
def analyze_packet(packet):
    if IP in packet:
        src_ip   = packet[IP].src
        dst_ip   = packet[IP].dst
        protocol = "TCP" if TCP in packet else "UDP" if UDP in packet else "OTHER"
        port     = packet[TCP].dport if TCP in packet else \
                   packet[UDP].dport if UDP in packet else 0

        # Firewall decision
        if src_ip in blocked_ips:
            verdict = "BLOCKED (bad IP)"
        elif port in blocked_ports:
            verdict = "BLOCKED (bad port)"
        else:
            verdict = "ALLOWED"

        # Timestamp
        time = datetime.now().strftime("%H:%M:%S")

        # Print to screen
        print(f"[{time}] {src_ip} → {dst_ip}  |  {protocol}  |  port {port}  |  {verdict}")

        # Save to log
        with open("packet_log.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([time, src_ip, dst_ip, protocol, port, verdict])

# ── Write CSV header once ────────────────────────────────────
with open("packet_log.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["time", "src_ip", "dst_ip", "protocol", "port", "verdict"])

# ── Start capturing ──────────────────────────────────────────
print("📡 Capturing packets... Ctrl+C to stop\n")
sniff(prn=analyze_packet, count=20)

print("\n✅ Log saved to packet_log.csv")

