from scapy.all import Ether, IP, UDP, Raw, sendp, get_if_list, get_if_addr
import time
import random

YANDEX_REMOTE_IP = "192.168.0.100" 
YANDEX_REMOTE_MAC = "00:11:22:33:44:55"

def generate_random_notification():
    titles = [
        "Обнаружено подозрительное устройство",
        "Несанкционированное подключение",
        "Попытка взлома",
        "Нестандартный порт открыт"
    ]
    extras = [
        "нестандартный порт",
        "многочисленные попытки подключения",
        "неизвестное устройство",
        "подозрительный трафик"
    ]

    title = random.choice(titles)
    extra = random.choice(extras)

    return title, extra

def get_interface_by_subnet(subnet_prefix="192.168.0."):
    for iface in get_if_list():
        try:
            ip = get_if_addr(iface)
            if ip.startswith(subnet_prefix):
                return iface
        except:
            continue
    raise RuntimeError("Подходящий интерфейс не найден для подсети: " + subnet_prefix)

def send_packet(title, extra, iface):
    packet = Ether(src=YANDEX_REMOTE_MAC, dst="FF:FF:FF:FF:FF:FF") / \
             IP(src=YANDEX_REMOTE_IP, dst="192.168.0.255") / \
             UDP(sport=12345, dport=54321) / \
             Raw(load=f"{title}: {extra}")

    sendp(packet, iface=iface)
    print(f"Отправлен пакет: {title}, {extra} через интерфейс {iface}")

def simulate_activity():
    iface = get_interface_by_subnet("192.168.0.")
    while True:
        title, extra = generate_random_notification()
        send_packet(title, extra, iface)
        time.sleep(30)

if __name__ == "__main__":
    simulate_activity()