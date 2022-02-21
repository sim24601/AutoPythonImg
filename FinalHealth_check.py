#!/usr/bin/env python3

import socket
import psutil

# TODO : create class error with function mail


def main():

    cpu = psutil.cpu_percent(interval=1)
    print("CPU is "+str(cpu))
    if cpu > 80:
        print("warning")

    mem = psutil.virtual_memory()
    alert = 500 * 1024 * 1024
    print("memory is "+str(mem.available))
    if mem.available <= alert:
        print("warning")

    disk = psutil.disk_usage('/')
    print("disk is "+str(disk.percent))
    if disk.percent > 80:
        print("warning")

    network = socket.gethostbyname('localhost')
    print("network is "+network)
    if network != "127.0.0.1":
        print("warning")


if __name__ == "__main__":
    main()
