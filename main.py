#!/usr/bin/python3
import re
from dataclasses import dataclass
from random import shuffle
from colorama import Fore


@dataclass
class Protocol:
    port_number: str
    name: str
    description: str = ""


@dataclass
class Exercise:
    question: str
    answer: str
    description: str = None


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
    Protocol("69", "TFTP", "Trivial File Transfer Protocol"),
    Protocol("80", "HTTP", "Hypertext Transfer Protocol"),
    Protocol("88", "Kerberos", "Is also a dog with 3 heads"),
    Protocol("110", "POP3", "Post Office Protocol"),
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
    exercises: list[Exercise] = []
    wrong: list[tuple[str, Exercise]] = []
    for prot in protocols:
        exercises.append(Exercise(prot.name, prot.port_number, prot.description))

    print_line()
    print("\nPorts:")
    for exercise in exercises:
        answer = input(f"Give port for {exercise.question} ({exercise.description}): ")
        if answer != exercise.answer:
            wrong.append((answer, exercise))

    evaluate(wrong)


def play_protocols(protocols: list[Protocol]) -> None:
    """Give protocol name by given port number"""
    exercises: list[Exercise] = []
    wrong: list[tuple] = []
    for prot in protocols:
        exercises.append(Exercise(prot.port_number, prot.name))

    print_line()
    print("\nProtocols:")
    for exercise in exercises:
        answer = input(f"Give protocol for port {exercise.question}: ")
        re_pattern = re.compile('[ ()]')
        _answer = re.sub(re_pattern, '', answer).lower()
        right_answer = re.sub(re_pattern, '', exercise.answer).lower()
        if _answer != right_answer:
            wrong.append((answer, exercise))

    evaluate(wrong)


def evaluate(wrong_answers: list[tuple[str, Exercise]]) -> None:
    correct = len(PROTOCOLS) - len(wrong_answers)
    print_line()
    print(f"\nScore: {correct}/{len(PROTOCOLS)}")
    if len(wrong_answers) == 0:
        print(f"{Fore.GREEN}Perfect!{Fore.RESET}")

    if wrong_answers:
        print("Need to review:")
        align_col1 = max(len(i[1].question) for i in wrong_answers) + 1
        align_col2 = max([len(i[1].answer) for i in wrong_answers]) + 1  # Default answer len + max len of protocol name
        for item in wrong_answers:
            exercise = item[1]
            user_answer = f"Answered: '{item[0]}'" if item[0] != "" else "(No answer) "
            print(f"{exercise.question:<{align_col1}}"
                  f"-> {exercise.answer:<{align_col2}}"
                  f"{user_answer}")
    print_line()


def print_line() -> None:
    print("-" * 30)


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
