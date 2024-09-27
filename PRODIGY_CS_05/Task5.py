from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP
from scapy.packet import Raw  # Correct import for Raw layer

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        print(f"\nNew Packet: {ip_layer.src} -> {ip_layer.dst}")
        
        # Display protocol type
        if packet.haslayer(TCP):
            print(f"Protocol: TCP | Source Port: {packet[TCP].sport} | Destination Port: {packet[TCP].dport}")
        elif packet.haslayer(UDP):
            print(f"Protocol: UDP | Source Port: {packet[UDP].sport} | Destination Port: {packet[UDP].dport}")
        else:
            print(f"Protocol: Other")
        
        # Check for payload (Raw layer)
        if packet.haslayer(Raw):
            print(f"Payload detected: {packet[Raw].load}")
            return True  # Signal that we want to stop sniffing

def start_sniffing():
    print("Starting packet sniffing... Stopping after encountering a payload.")
    
    # Stop sniffing once a packet with payload (Raw layer) is found
    sniff(filter="ip", prn=packet_callback, store=0, stop_filter=lambda x: packet_callback(x))

if __name__ == "__main__":
    start_sniffing()

