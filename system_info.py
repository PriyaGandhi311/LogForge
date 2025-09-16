#!/usr/bin/env python3

import psutil
import platform
from datetime import datetime
from sql_logger import logger

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def get_system_info():
    uname = platform.uname()
    logger.info(f"System: {uname.system}")
    logger.info(f"Node Name: {uname.node}")
    logger.info(f"Release: {uname.release}")
    logger.info(f"Version: {uname.version}")
    logger.info(f"Machine: {uname.machine}")
    logger.info(f"Processor: {uname.processor}")

def get_boot_time():
    bt = datetime.fromtimestamp(psutil.boot_time())
    logger.info(f"Boot Time: {bt.strftime('%Y-%m-%d %H:%M:%S')}")

def get_cpu_info():
    logger.info(f"Physical cores: {psutil.cpu_count(logical=False)}")
    logger.info(f"Total cores: {psutil.cpu_count(logical=True)}")
    freq = psutil.cpu_freq()
    logger.info(f"Max Frequency: {freq.max:.2f}Mhz")
    logger.info(f"Min Frequency: {freq.min:.2f}Mhz")
    logger.info(f"Current Frequency: {freq.current:.2f}Mhz")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        logger.info(f"Core {i + 1}: {percentage}%")
    logger.info(f"Total CPU Usage: {psutil.cpu_percent()}%")

def get_memory_info():
    svmem = psutil.virtual_memory()
    logger.info(f"Total: {get_size(svmem.total)}")
    logger.info(f"Available: {get_size(svmem.available)}")
    logger.info(f"Used: {get_size(svmem.used)}")
    logger.info(f"Percentage: {svmem.percent}%")

def get_disk_info():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            logger.info(f"{partition.device} ({partition.mountpoint}) - {usage.percent}% used")
        except PermissionError:
            continue

def get_network_info():
    if_addrs = psutil.net_if_addrs()
    for interface_name, addresses in if_addrs.items():
        for address in addresses:
            if str(address.family) == 'AddressFamily.AF_INET':
                logger.info(f"{interface_name} IP: {address.address}")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                logger.info(f"{interface_name} MAC: {address.address}")

def run_system_logging():
    get_system_info()
    get_boot_time()
    get_cpu_info()
    get_memory_info()
    get_disk_info()
    get_network_info()
