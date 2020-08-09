# pmap.py -n 4 -f ping -ip 192.168.0.1-192.168.0.100
# pmap.py -n 10 -f tcp -ip 192.168.0.1 -w result_ip.json

import time
import argparse
from multiprocessing.pool import Pool
from concurrent.futures import ThreadPoolExecutor
from ping3 import ping
import ipaddress
import json
import socket

iplist = []
portlist = []
result_list = []


def is_ip(ip):
    try:
        ipaddress.ip_address(ip)
    except BaseException:
        print('请输入正确的ip地址, only support: ip or ip-ip(同一网段)')
        exit()


def parser_ip(ips):
    #print('开始解析ip')
    #ips = '192.168.0.1-192.168.0.100'
    if ips.find('-') == -1:
        is_ip(ips.split('-')[0])
        iplist.append(ips.split('-')[0])
    else:
        startip = ips.split('-')[0]
        endip = ips.split('-')[1]
        is_ip(startip)
        is_ip(endip)
        for i in range(int(startip.split('.')[3]), int(
                endip.split('.')[3]) + 1):
            iplist.append(
                startip.split('.')[0] +
                '.' +
                startip.split('.')[1] +
                '.' +
                startip.split('.')[2] +
                '.' +
                str(i))


def is_port(port):
    if int(port) < 0 or int(port) > 65536:
        print('请输入正确的端口')
        exit()


def parser_port(ports):
    #print('开始解析port')
    if ports.find('-') == -1:
        is_port(ports)
        portlist.append(ports)
    else:
        for i in range(int(ports.split('-')[0]), int(ports.split('-')[1]) + 1):
            is_port(i)
            portlist.append(i)


def tcp_scan(ip, port):
    #print('开始扫描端口', ip, port)
    s = socket.socket()
    s.settimeout(2)
    if s.connect_ex((ip, port)) == 0:
        result1 = {
            'ip': ip,
            'port': port,
            'status': 'open'
        }
        print(f'{ip}:{port} is open')
        result_list.append(result1)
        return result1

def ping_scan(ip):
    #print('开始扫描ip', ip, argvt)
    if ping(ip, timeout=argvt):
        #result = {'ip':ip}
        result = {'ip': ip, 'status': 'on'}
        print(f'{ip}: is up')
        result_list.append(result)
        #print(result_list)
        return result


def write_file(result, file):
    print('开始写入文件')
    data = {"result": result}
    try:
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(data, f)
    except:
        print(f'{file} 目录、文件不存在，或者无权写入。请联系管理员')


def mian():
    print('开始运行主程序', argvm, argvf)
    if argvm == 'proc':
        p = Pool(argvn)
        if argvf == 'ping':
            for ip in iplist:
                #print('p.apply_async(ping_scan, args=(ip,))')
                p.apply_async(ping_scan, args=(ip))
        elif argvf == 'tcp':
            for ip in iplist:
                for port in portlist:
                    p.apply_async(tcp_scan, args=(ip, port,))
        # time.sleep(5)
        p.close()
        p.join()
        # p.terminate()
    elif argvm == 'thread':
        with ThreadPoolExecutor(max_workers=argvn) as executor:
            if argvf == 'ping':
                executor.map(ping_scan, iplist)
            elif argvf == 'tcp':
                for ip in iplist:
                    for port in portlist:
                        executor.submit(tcp_scan, ip, port)
                        #print(future.result())


if __name__ == '__main__':
    time1 = time.time()
    parser = argparse.ArgumentParser(description='scan ip or port')
    parser.add_argument(
        '-m',
        choices=[
            'proc',
            'thread'],
        default='thread',
        required=False,
        help='指定扫描器并发模型')
    parser.add_argument('-n', type=int, default=8, help='并发进程/线程数')
    parser.add_argument(
        '-f',
        choices=[
            'tcp',
            'ping'],
        required=False,
        default='ping',
        help='工作方式: tcp/ip')
    parser.add_argument('-ip', type=str, default='127.0.0.1', help='ip地址')
    parser.add_argument('-port', type=str, default='1-1024', help='扫描端口')
    parser.add_argument('-w', type=str, help='扫描结果保存地址')
    parser.add_argument('-v', action="store_true", help='打印扫描器运行耗时,默认未开启')
    parser.add_argument('-t', type=int, default=1, help='连结超时时间')
    args = parser.parse_args()
    argvm, argvn, argvf, argvip, argvport, argvw, argvv, argvt = args.m, args.n, args.f, args.ip, args.port, args.w, args.v, args.t
    print(
        f'参数解析成功: ' +
        argvm,
        argvn,
        argvf,
        argvip,
        argvport,
        argvw,
        argvv,
        argvt)
    time2 = time.time()

    parser_ip(argvip)
    print(f'ip地址列表为: {iplist}')
    if argvf == 'tcp':
        parser_port(argvport)
        print(f'端口列表为: {portlist}')
    time3 = time.time()

    mian()
    print(result_list)

    time4 = time.time()
    if argvw:
        write_file(result_list,argvw)
        time4 = time.time()
    if argvv:
        print(f'解析参数消耗时间: {time2-time1}, 程序运行时间: {time3-time2} ')
        if argvw:
            print(f'保存文件消耗时间: {time4-time3}\n')
