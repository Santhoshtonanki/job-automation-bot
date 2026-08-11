import os
import requests

TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
CHAT_ID = os.environ['TELEGRAM_CHAT_ID']

jobs = [
    ("DevOps Engineer", "TCS", "Hyderabad", 92, "DevOps Resume",
     "https://www.linkedin.com/jobs/search/?keywords=DevOps%20Engineer"),
    ("Cloud Support Engineer", "Accenture", "Bangalore", 88, "Cloud Resume",
     "https://www.linkedin.com/jobs/search/?keywords=Cloud%20Support%20Engineer"),
    ("Linux Administrator", "HCL", "Remote", 84, "Linux Resume",
     "https://www.linkedin.com/jobs/search/?keywords=Linux%20Administrator"),
    ("NOC Engineer", "Wipro", "Pune", 80, "NOC Resume",
     "https://www.linkedin.com/jobs/search/?keywords=NOC%20Engineer"),
]

message = "📌 Top Matching Jobs Today\n\n"

for title, company, location, score, resume, link in jobs:
    message += f"🔹 {title}\n"
    message += f"🏢 {company}\n"
    message += f"📍 {location}\n"
    message += f"🎯 Match: {score}%\n"
    message += f"📄 Use: {resume}\n"
    message += f"🔗 {link}\n\n"

message += "🚀 Daily target: 20 applications"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(url, json={
    "chat_id": CHAT_ID,
    "text": message
})

print("Real job message sent successfully")
