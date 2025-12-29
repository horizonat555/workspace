import os
import requests
import smtplib
from email.message import EmailMessage

# ---------- DISCORD ----------
def send_discord():
    webhook = os.environ["DISCORD_WEBHOOK"]

    payload = {
        "content": "🎉 **HAPPY BIRTHDAY BRO!** 🎂\nSurprise 👉 https://yourusername.github.io/birthday-site"
    }

    r = requests.post(webhook, json=payload)
    r.raise_for_status()

# ---------- EMAIL ----------
def send_email():
    msg = EmailMessage()
    msg["From"] = os.environ["EMAIL_USER"]
    msg["To"] = os.environ["TO_EMAIL"]
    msg["Subject"] = "🎉 HAPPY BIRTHDAY 🎉"
    msg.set_content(
        "Happy Birthday bro 🎂🔥\n\nSurprise site:\nhttps://yourusername.github.io/birthday-site"
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(os.environ["EMAIL_USER"], os.environ["EMAIL_PASS"])
        server.send_message(msg)

if __name__ == "__main__":
    send_discord()
    send_email()
    print("Birthday wishes sent 🚀")
