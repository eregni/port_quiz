#!/usr/bin/python3
# TODO: colors...
import re
from dataclasses import dataclass
from random import shuffle


@dataclass
class Protocol:
    port_number: str
    name: str
    description: str = ""


PROTOCOLS = [
    Protocol("20", "FTP data", "File Transfer Protocol"),
    Protocol("21", "FTP control", "File Transfer Protocol"),
    Protocol("22", "SSH", "Secure Socket Shell"),
    Protocol("23", "TELNET", "TELetype NETwork"),
    Protocol("25", "SMTP", "Simple Mail Transfer Protocol"),
    Protocol("49", "TACACS", "Terminal Access Controller Access-Control System"),
    Protocol("53", "DNS", "Domain Name System"),
    Protocol("67", "DHCP", "Dynamic Host Control Protocol - server - bootps"),
    Protocol("68", "DHCP", "Dynamic Host Control Protocol - client - bootpc"),
    Protocol("69", "TFPT", "Trivial File Transfer Protocol"),
    Protocol("80", "HTTP", "Hypertext Transfer Protocol"),
    Protocol("88", "Kerberos", "Is also a dog with 3 heads"),
    Protocol("110", "POP3", "Post Office Protocol"),
    Protocol("119", "NNTP", "Network News Transfer Protocol"),
    Protocol("123", "NTP", "Network Time Protocol"),
    Protocol("139", "Netbios", "Network Basic Input Output System"),
    Protocol("143", "IMAP", "Internet Message Access Protocol"),
    Protocol("161", "SNMP", "Simple Network Management Protocol"),
    Protocol("162", "SNMPTRAP", "SNMP notifications"),
    Protocol("194", "IRC", "Internet Relay Chat"),
    Protocol("389", "LDAP", "Lightweight Directory Access Protocol"),
    Protocol("443", "HTTPS", "Secure HTTP"),
    Protocol("445", "SMB", "Server Message Block"),
    Protocol("465", "SMTPS", "Secure SMTP"),
    Protocol("514", "RSH", "Remote Shell, syslog"),
    Protocol("587", "Submission", "SMTP submission"),
    Protocol("631", "IPP", "Internet Printing Protocol"),
    Protocol("636", "LDAPS", "Lightweight Directory Access Protocol Secure"),
    Protocol("993", "IMAPS", "Internet Message Access Protocol Secure"),
    Protocol("995", "POP3S", "Post Office Protocol Secure"),
    Protocol("3389", "RDP", "Remote Desktop Protocol")
]


def play_ports(protocols: list[Protocol]) -> None:
    """Give port number by given protocol name"""
    wrong = []
    for protocol in protocols:
        answer = input(f"Give port for {protocol.name} ({protocol.description}): ")
        if answer != protocol.port_number:
            wrong.append((answer, protocol))

    evaluate(wrong)


def play_protocols(protocols: list[Protocol]) -> None:
    """Give protocol name by given port number"""
    wrong: list[tuple] = []
    for protocol in protocols:
        answer = input(f"Give protocol for port {protocol.port_number}: ")
        re_pattern = re.compile('[ ()]')
        _answer = re.sub(re_pattern, '', answer).lower()
        right_answer = re.sub(re_pattern, '', protocol.name).lower()
        if _answer != right_answer:
            wrong.append((answer, protocol))

    evaluate(wrong)


def evaluate(wrong_answers: list[tuple:[str, Protocol]]) -> None:
    correct = len(PROTOCOLS) - len(wrong_answers)
    print(f"\nScore: {correct}/{len(PROTOCOLS)}")
    if len(wrong_answers) == 0:
        print("Perfect!")

    if wrong_answers:
        align_col1 = max(len(p.name) for p in PROTOCOLS) + 2
        align_col2 = 12 + max([len(a[0]) for a in wrong_answers]) + 2  # Default answer len + max len of protocol name
        for item in wrong_answers:
            protocol = item[1]
            answer = f"Answered: '{item[0]}'" if item[0] != "" else "No answer. "
            print(f"{protocol.name:<{align_col1}} {answer:<{align_col2}}"
                  f"Right answer -> {protocol.port_number:<{align_col2}}")


print("#########################")
print("# Port & Protocol quiz! #")
print("#########################\n")
print("Ports: Give the corresponding port for given protocol:")
print("Protocols: Give the corresponding protocol for given port:")

if __name__ == "__main__":
    while True:
        print("\nSelect quiz")
        choice = input("Ports(1) of Protocols(2) or quit(q): ")
        shuffle(PROTOCOLS)
        if choice in ["Q", "q"]:
            exit(0)
        elif choice == "1":
            play_ports(PROTOCOLS)
        elif choice == "2":
            play_protocols(PROTOCOLS)
