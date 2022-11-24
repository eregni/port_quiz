#!/usr/bin/python3
#TODO: add protocol + port + TCP|UDP
#TODO: Mix it all ports <-> nrs
import re
from random import shuffle

DATA = [
    ("20", "FTP data", "(File transfer Protocol)"),
    ("21", "FTP control", "(File transfer Protocol)"),
    ("22", "SSH", "(Secure Socket Shell)"),
    ("23", "TELNET", "(Remote connection without encryption)"),
    ("25", "SMTP", "(Simple Mail Transfer Protocol)"),
    ("53", "DNS", "(Domain Name System)"),
    ("67", "DHCP", "(Dynamic host control protocol)"),
    ("69", "TFPT", "(Trivial File Transfer Protocol)"),
    ("80", "HTTP", "(Hypertext Transfer Protocol)"),
    ("110", "POP3", "(Post Office Protocol)"),
    ("123", "NTP", "(Network Time Protocol)"),
    ("139", "Netbios", ""),
    ("143", "IMAP", "(Internet Message Access Protocol)"),
    ("161", "SNMP", "(Simple Network Management Protocol)"),
    ("162", "SNMPTRAP", "(SNMP notifications)"),
    ("389", "LDAP", "(Lightweight Directory Access Protocol)"),
    ("443", "HTTPS", "(Secure HTTP)"),
    ("465", "SMTPS", "(Secure SMTP)"),
    ("514", "RSH", "(Remote Shell, syslog)"),
    ("631", "IPP", "(Internet printing protocol)"),
    ("636", "LDAPS", "(Secure LDAP)"),
    ("993", "IMAPS", "(Secure IMAP)"),
    ("995", "POP3S", "(Secure POP3)")
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
