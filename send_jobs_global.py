import os
import requests

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

jobs = [
    ("Remote DevOps Engineer", "Remote", "Worldwide", 95, "DevOps Resume",
     "https://www.linkedin.com/jobs/search/?keywords=DevOps%20Engineer&location=Worldwide&f_WT=2"),

    ("Remote SRE (Fresher)", "Remote", "Worldwide", 92, "DevOps Resume",
     "https://www.linkedin.com/jobs/search/?keywords=Site%20Reliability%20Engineer&location=Worldwide&f_WT=2"),

    ("Cloud Support Engineer", "Remote/Hybrid", "Europe", 90, "Cloud Resume",
     "https://www.linkedin.com/jobs/search/?keywords=Cloud%20Support%20Engineer&location=Europe"),

    ("Linux Administrator", "Remote", "Worldwide", 88, "Linux Resume",
     "https://www.linkedin.com/jobs/search/?keywords=Linux%20Administrator&location=Worldwide&f_WT=2"),

    ("DevOps Engineer Visa Sponsorship", "Relocation", "Germany", 94, "DevOps Resume",
     "https://www.linkedin.com/jobs/search/?keywords=DevOps%20Engineer%20visa%20sponsorship&location=Germany"),

    ("Cloud Engineer Relocation", "Relocation", "Netherlands", 91, "Cloud Resume",
     "https://www.linkedin.com/jobs/search/?keywords=Cloud%20Engineer%20relocation&location=Netherlands"),
]

message = "🌍 Global Remote & Sponsorship Job Alert\n\n"

for title, company, location, score, resume, link in jobs:
    message += f"🔹 {title}\n"
    message += f"🏢 {company}\n"
    message += f"📍 {location}\n"
    message += f"🎯 Match: {score}%\n"
    message += f"📄 Use: {resume}\n"
    message += f"🔗 {link}\n\n"

message += "🚀 Target: Remote + Visa Sponsorship + Relocation"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(url, json={
    "chat_id": CHAT_ID,
    "text": message
})

print("Global remote job alert sent successfully")
