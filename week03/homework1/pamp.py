import threading
import multiprocessing
import os
import re
import json
import ipaddress
import argparse
from ping3 import ping
import time



def pareser_ip(ip):

    iplist.append(ip)

iplist =[]

def pareser_port():
    pass

port_list = []
class ScanThread():
    pass

class ScanProcee():
    pass

def parser_agrs():
    parser = argparse.ArgumentParser(description='scan ip or port')
    parser.add_argument('-m', choices=['proc', 'thread'], default='thread', required=False, help='指定扫描器并发模型')
    parser.add_argument('-n', type=int, default=8, help='并发进程/线程数')
    parser.add_argument('-f', choices=['tcp', 'ping'], required=False, default='ping', help='工作方式: tcp/ip')
    parser.add_argument('-ip', type=str,default='127.0.0.1', help='ip地址')
    parser.add_argument('-port', type=str,default='1-1024', help='扫描端口')
    parser.add_argument('-w', type=str, help='扫描结果保存地址')
    parser.add_argument('-v', action="store_true", help='打印扫描器运行耗时,默认未开启')

    args = parser.parse_args()
    # if args.v:
    #     print('verbo is on')

def main():
    parser_agrs()
    pass

if __name__ == '__main__':
    main()




