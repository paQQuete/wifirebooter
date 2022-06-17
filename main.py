import telnetlib
from cred import *


def worker(conn, seconds):
    conn.read_until(b"Login:")
    conn.write(user.encode('ascii') + b"\n")

    conn.read_until(b"Password:")
    conn.write(password.encode('ascii') + b"\n")

    conn.read_until(b"(config)>")

    b = r'system reboot {}\n'.format(next(seconds))
    conn.write(b.encode('ascii'))

if __name__ == '__main__':
    hosts_port_mapping = {
        '1': 1001,
        '3': 1003,
        '4': 1004
    }
    sec_counter = (str(int(router) * 3 + 15) for router in hosts_port_mapping.keys())


    for port in hosts_port_mapping.values():
        with telnetlib.Telnet(host=HOST, port=port) as telnet_connector:
            worker(telnet_connector, sec_counter)
