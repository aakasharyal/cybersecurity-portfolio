from scapy.all import sniff, IP, TCP, UDP
from datetime import datetime
import csv

# ── Firewall rules ───────────────────────────────────────────
blocked_ips       = ["192.168.56.100"]
blocked_ports     = [23, 21, 4444]        # telnet, FTP, backdoor
blocked_protocols = ["OTHER"]

# ── Create log file ──────────────────────────────────────────
with open("firewall_log.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["time", "src_ip", "dst_ip", "protocol", "port", "verdict", "reason"])

# ── Firewall engine ──────────────────────────────────────────
def firewall(packet):
    if IP in packet:
        src_ip   = packet[IP].src
        dst_ip   = packet[IP].dst
        protocol = "TCP" if TCP in packet else "UDP" if UDP in packet else "OTHER"
        port     = packet[TCP].dport if TCP in packet else \
                   packet[UDP].dport if UDP in packet else 0
        time     = datetime.now().strftime("%H:%M:%S")

        # Rule checks
        if src_ip in blocked_ips:
            verdict, reason = "BLOCKED", "IP blacklisted"
        elif port in blocked_ports:
            verdict, reason = "BLOCKED", "Port blacklisted"
        elif protocol in blocked_protocols:
            verdict, reason = "BLOCKED", "Protocol not allowed"
        else:
            verdict, reason = "ALLOWED", "Passed all rules"

        # Print with colour indicator
        tag = "🔴 BLOCK" if verdict == "BLOCKED" else "🟢 ALLOW"
        print(f"[{time}] {tag}  {src_ip} → {dst_ip}  |  {protocol}  |  port {port}  |  {reason}")

        # Save to log
        with open("firewall_log.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([time, src_ip, dst_ip, protocol, port, verdict, reason])

# ── Start firewall ───────────────────────────────────────────
print("🔥 Firewall running... Ctrl+C to stop\n")
try:
    sniff(prn=firewall, count=20)
except KeyboardInterrupt:
    print("\n⛔ Firewall stopped")

print("✅ Log saved to firewall_log.csv")
