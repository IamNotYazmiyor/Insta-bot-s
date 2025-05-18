import time
import schedule
from instagrapi import Client

username = "nulls.map.bot"
password = "Sypnex3436"
thread_id = "340282366841710301281161166131725931577"

cl = Client()

def login():
    print("Giriş yapılıyor...")
    cl.login(username, password)
    print("Giriş başarılı.")

def send_scheduled_message(message):
    try:
        full_message = f"{message} haritası aktif @everyone"
        cl.direct_send(full_message, thread_ids=[thread_id])
        print(f"Mesaj gönderildi: {full_message}")
    except Exception as e:
        print("Mesaj gönderme hatası:", e)

# Mesaj ve saat listesi
schedule_messages = {
    "16:09": "Nakavt",
    "18:09": "Temizlik",
    "20:09": "Elmas Kapmaca",
    "22:09": "Savaş Topu",
    "00:09": "Nakavt",
    "02:09": "Temizlik",
    "04:09": "Elmas Kapmaca",
    "06:09": "Savaş Topu",
    "08:09": "Nakavt",
    "10:09": "Temizlik",
    "12:09": "Elmas Kapmaca",
    "14:09": "Savaş Topu"
}

def setup_schedules():
    for saat, mesaj in schedule_messages.items():
        schedule.every().day.at(saat).do(send_scheduled_message, message=mesaj)
    print("Zamanlama ayarlandı.")

if __name__ == "__main__":
    login()
    setup_schedules()
    print("Program çalışıyor, bekleniyor...")
    while True:
        schedule.run_pending()
        time.sleep(1)
