# ShieldForge — AI-Powered Digital Asset Protection

ShieldForge is a comprehensive security platform designed to protect your digital assets using real-time AI threat detection. Built as part of the GDG Solution Challenge 2026, it provides a unified dashboard to monitor accounts, wallets, and digital identities.

## 🚀 Features

- **AI Threat Analyzer**: Securely analyze URLs, emails, and suspicious text using Claude AI integration via a Python backend.
- **Dynamic Dashboard**: Monitor active threats, security scores, and connected assets in real-time.
- **Multi-Layer Protection**: Specialized models for phishing detection, anomaly monitoring, and behavior profiling.
- **Dark & Light Mode**: Seamlessly switch between themes with a dedicated toggle that persists your preference.
- **Instant Alerts**: Zero-delay notification system for critical security events.

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **AI Integration**: Anthropic Claude API
- **Frontend**: Semantic HTML5, Vanilla CSS, Modern JavaScript
- **Typography**: Google Fonts (Outfit, Bebas Neue, JetBrains Mono)

## 📦 Installation & Setup

### 1. Prerequisites
- Python 3.8+
- An Anthropic API Key (Claude)

### 2. Clone/Copy the Project
Ensure you are in the project root directory (`/solution`).

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configuration
Create a `.env` file in the root directory and add your Anthropic API key:
```env
ANTHROPIC_API_KEY=your_actual_api_key_here
```

### 5. Run the Application
```bash
python app.py
```
The application will be available at `http://127.0.0.1:5000`.

## 🛡️ Security Note
This application uses a Python backend to proxy requests to AI services. This ensures that your API keys are never exposed to the client-side browser, providing a secure production-ready architecture.

---
© 2026 Samarth Jaiswal · Team Shield Forge · GDG Solution Challenge
