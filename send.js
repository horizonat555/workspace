import https from "https";
import nodemailer from "nodemailer";

// ---------- DISCORD ----------
function sendDiscord() {
  const data = JSON.stringify({
    content: "🎉 **HAPPY BIRTHDAY BRO!** 🎂\nHere’s your surprise 👉 https://yourusername.github.io/birthday-site"
  });

  const url = new URL(process.env.DISCORD_WEBHOOK);

  const req = https.request({
    hostname: url.hostname,
    path: url.pathname,
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Content-Length": data.length
    }
  });

  req.write(data);
  req.end();
}

// ---------- EMAIL ----------
async function sendEmail() {
  const transporter = nodemailer.createTransport({
    service: "gmail",
    auth: {
      user: process.env.EMAIL_USER,
      pass: process.env.EMAIL_PASS
    }
  });

  await transporter.sendMail({
    from: `"Birthday Bot 🎂" <${process.env.EMAIL_USER}>`,
    to: process.env.TO_EMAIL,
    subject: "🎉 HAPPY BIRTHDAY 🎉",
    text: "Happy Birthday bro 🎂🔥\nSurprise site:\nhttps://yourusername.github.io/birthday-site"
  });
}

(async () => {
  await sendDiscord();
  await sendEmail();
  console.log("Birthday wishes sent 🚀");
})();
