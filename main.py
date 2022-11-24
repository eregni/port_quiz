#!/usr/bin/python3
#TODO: add protocol + port + TCP|UDP
#TODO: Mix it all ports <-> nrs
import re
from random import shuffle

# TODO:
# 1701 Layer 2 Tunneling
# 1720 H.323
# 1723 PPTP
# 2427, 2727 MGCP
# 5004, 5005 RTP
# 5060, 5061 SIP
# 5900 TightVNC 
DATA = [
    ("20", "FTP data", "(File Transfer Protocol)"),
    ("21", "FTP control", "(File Transfer Protocol)"),
    ("22", "SSH", "(Secure Socket Shell)"),
    ("23", "TELNET", "(TELetype NETwork)"),
    ("25", "SMTP", "(Simple Mail Transfer Protocol)"),
    ("49", "TACACS+", "(Terminal Access Controller Access-Control System plus)")
    ("53", "DNS", "(Domain Name System)"),
    ("67", "DHCP - bootpc", "(Dynamic Host Control Protocol - server)"),
    ("68", "DHCP - bootpc", "(Dynamic Host Control Protocol - client)"),
    ("69", "TFPT", "(Trivial File Transfer Protocol)"),
    ("80", "HTTP", "(Hypertext Transfer Protocol)"),
    ("88", "Kerberos", ""),
    ("110", "POP3", "(Post Office Protocol)"),
    ("119", "NNTP", "Network News Transfer Protocol"),
    ("123", "NTP", "(Network Time Protocol)"),
    ("139", "Netbios", "(Network Basic Input Output System)"),  # TODO: netbios uses 3 ports
    ("143", "IMAP", "(Internet Message Access Protocol)"),
    ("161", "SNMP", "(Simple Network Management Protocol)"),
    ("162", "SNMPTRAP", "(SNMP notifications)"),
    ("194", "IRC", "(Internet Relay Chat)"),
    ("389", "LDAP", "(Lightweight Directory Access Protocol)"),
    ("443", "HTTPS", "(Secure HTTP)"),
    ("445", "SMB", "(Server Message Block)"),
    ("465", "SMTPS", "(Secure SMTP)"),
    ("514", "RSH", "(Remote Shell, syslog)"),
    ("631", "IPP", "(Internet Printing Protocol)"),
    ("636", "LDAPS", "(Lightweight Directory Access Protocol Secure)"),
    ("993", "IMAPS", "(Internet Message Access Protocol Secure)"),
    ("995", "POP3S", "(Post Office Protocol Secure)"),
    ("1812", "RADIUS", "(Remote Authentication Dial-In User Service)"),
    ("1813", "RADIUS - accounting", "(Remote Authentication Dial-In User Service)") # TODO: RADIUS uses more ports: 1645, 1646, 7082
    ("3389", "RDP", "(Remote Desktop Protocol)")
]

def play_ports(data: list[tuple]) -> None:
    shuffle(DATA)
    wrong = []
    for item in data:
        answer = input(f"Give port for {item[1]} {item[2]}: ")
        if answer != item[0]:
            wrong.append((answer, item))
    
    correct = len(data) - len(wrong)
    print(f"\nScore: {correct}/{len(data)}")
    if len(wrong) == 0:
        print("Perfect!")
    else:
        print("\nThese answers where incorrect:")
        for item in wrong:
            print(f"{item[1][1]}: You answered '{item[0]}'. Right answer -> {item[1][0]}")


def play_protocols(data: list[tuple]) -> None:
    shuffle(DATA)
    wrong = []
    for item in data:
        answer = input(f"Give protocol for port {item[0]}: ")
        re_pattern = re.compile('[ ()]')
        _answer = re.sub(re_pattern, '', answer).lower()
        right_answer = re.sub(re_pattern, '', item[1]).lower()
        if _answer != right_answer:
            wrong.append((answer, item))
           
    print(f"\nScore: {correct}/{len(data)}")
    if len(wrong) == 0:
        print("Perfect!")
    else:
        print("\nThese answers where incorrect:")
        for item in wrong:
            print(f"Port {item[1][0]}: You answered '{item[0]}'. Right answer -> {item[1][1]}")

def evaluation():
    Raise NotImplentedError

print("#########################")
print("# Port & Protocol quiz! #")
print("#########################\n")
print("Ports: Give the corresponding port for given protocol:")
print("Protocols: Give the corresponding protocol for given port:")

if __name__ == "__main__":
    while True:
        print("\nSelect quiz")
        choice = input("Ports(1) of Protocols(2) or quit(q): ")
        if choice in ["Q", "q"]:
            exit(0)
        elif choice == "1":
            play_ports(DATA)
        elif choice == "2":
            play_protocols(DATA)
