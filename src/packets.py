import socket
import time
from util import load_settings as lset

def send_packets(ip_address, port):
    # create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet_count = 0
    # set the starting time
    start_time = time.time()
    update_interval = float(lset.get_setting('misc settings','update_interval'))
    # send packets indefinitely
    while True:
        # send an 8-byte packet to the specified IP address and port
        s.sendto(b'32bytes', (ip_address, port))
        # increment the packet count
        packet_count += 1

        # calculate the elapsed time
        elapsed_time = time.time() - start_time
        
        # if the elapsed time is greater than 1 second, print the packet count and reset the start time
        if elapsed_time >= update_interval:
            throughput = packet_count * 32 / elapsed_time / 1e9
            #prints over the same line to show the throughput
            print(f'sent {packet_count} packets in {elapsed_time:.3f} seconds ({throughput:.4f} Gbps)', end='\r')
            packet_count = 0
            start_time = time.time()
            #draw the graph           
if __name__ == '__main__':
    send_packets('18.0.70.16', 12345)
