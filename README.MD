# 🤖 Advanced Crawler Bot

A powerful **Telegram crawler bot** with intelligent message monitoring, keyword tracking, and forwarding capabilities.

---

## 🚀 Features

### 🧠 Smart Message Crawler
- Monitor messages in real-time for **specific keywords**
- Automatically **forward matching messages** to selected chats
- Support for **multiple keywords** with precise filtering

### 📡 Channel Message Tracker
- Crawl and monitor **Telegram channels**
- **Forward all posts** from channels to target chats
- Real-time **content tracking**

### 👤 User Activity Monitor
- Track activity of **specific users** across multiple groups
- Forward user messages automatically to monitoring chats
- Smart **user surveillance system**

---

## ⚙️ Technical Highlights

- **Real-time Monitoring** — Instant processing of new messages  
- **Multi-Source Crawling** — Monitor groups, channels, and users simultaneously  
- **Smart Filtering** — Keyword-based content detection  
- **Selective Forwarding** — Send only what matters to the right places  
- **Error Handling** — Reliable operation even under load  

---

## 🧩 Use Cases

- 🛡️ **Content Moderation** – Detect and track sensitive keywords in groups  
- 🕵️ **Competitor Tracking** – Monitor target channels automatically  
- 👀 **User Surveillance** – Follow activities of specific users  
- 🔔 **Keyword Alerts** – Receive instant alerts for mentions or topics  

---

## ⚙️ Environment Configuration

Create a `.env` file in the **project root** and add the following variables:

```bash
SOUND_ID=
API_ID=
API_HASH=
```

> ⚠️ Make sure to replace values with your own credentials.

---

## 🧰 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Hossein-YB/telegram_crawler.git
   cd advanced-crawler-bot
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv   
   venv\Scripts\activate 
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Running the Bot

Once everything is set up, run:

```bash
python main.py
```

> The bot will start monitoring configured sources instantly.


### 🌟 Star this repo if you find it useful!
### Made with ❤️ using Python and the Telegram API.
