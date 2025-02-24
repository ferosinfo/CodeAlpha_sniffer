from scapy.all import sniff, Ether, IP, TCP, UDP
from .models import Packet

def packet_callback(packet):
    if Ether in packet:
        eth_src = packet[Ether].src
        eth_dst = packet[Ether].dst
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = "Unknown"
        src_port = None
        dst_port = None
        payload = None

        if TCP in packet:
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            payload = str(packet[TCP].payload)
        elif UDP in packet:
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            payload = str(packet[UDP].payload)

        # Save packet to the database
        Packet.objects.create(
            src_ip=src_ip,
            dst_ip=dst_ip,
            protocol=protocol,
            src_port=src_port,
            dst_port=dst_port,
            payload=payload
        )

def start_sniffing(interface=None, count=10):
    print(f"Starting sniffer on interface {interface}...")
    sniff(iface=interface, prn=packet_callback, count=count)