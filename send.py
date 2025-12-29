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

    # Fallback plain text
    msg.set_content(
        "HAPPY BIRTHDAY BRO!\n\n"
        "You are doing great, keep going 🔥\n\n"
        "I have insane level of faith in you\n\n"
        "Never gonna forget you man 🎂✨\n\n"
        "Surprise:\n"
        "https://yourusername.github.io/birthday-site\n\n"
        "- Pavan Hegde"
    )

    # HTML version
    msg.add_alternative("""
    <html>
      <body style="font-family: Arial, sans-serif; text-align: center;">
        <h1>🎉 HAPPY BIRTHDAY BRO! 🎉</h1>

        <p>You are doing great, keep going 🔥</p>
        <p><b>I have insane level of faith in you</b></p>
        <p>Never gonna forget you man 🎂✨</p>

        <img src="cid:bdayimg" style="max-width:100%; border-radius:16px; margin:20px 0;" />

        <p>
          👉 <a href="https://yourusername.github.io/birthday-site">
          Here’s the surprise [CLICK HEREEEEEEEEEE]
          </a>
        </p>

        <p>Have a great year 🚀</p>
        <p style="margin-top:30px;">— <b>Pavan Hegde</b></p>
      </body>
    </html>
    """, subtype="html")

    # Attach image inline
    with open("image.png", "rb") as f:
        msg.get_payload()[1].add_related(
            f.read(),
            maintype="image",
            subtype="png",
            cid="bdayimg"
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(os.environ["EMAIL_USER"], os.environ["EMAIL_PASS"])
        server.send_message(msg)


if __name__ == "__main__":
    #send_discord()
    send_email()
    print("Birthday wishes sent 🚀")
