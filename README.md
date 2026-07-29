# 📧 AI Email Reply Generator

An AI-powered web application that automatically generates professional email replies using **Google Gemini API** and **Flask**. Users simply paste an email, choose a reply tone, and receive a context-aware response within seconds.

---

## 🚀 Features

- 🤖 AI-powered email reply generation
- ✉️ Generates context-aware responses
- 🎭 Multiple reply tones
  - Professional
  - Friendly
  - Formal
  - Polite
- ⚡ Fast response generation using Google Gemini
- 🌐 Simple and responsive web interface
- 🔒 Secure API key management using `.env`

---

## 🛠️ Technologies Used

- Python
- Flask
- Google Gemini API
- HTML
- CSS
- JavaScript
- python-dotenv

---

## 📂 Project Structure

```
AI-Email-Reply-Generator/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
├── screenshots/
│   ├── home.png
│   └── reply.png
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/AI-Email-Reply-Generator.git
```

### 2. Navigate to the project folder

```bash
cd AI-Email-Reply-Generator
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### 7. Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 💡 How It Works

1. Paste the received email.
2. Select the desired reply tone.
3. Click **Generate Reply**.
4. The application sends the email and tone to the Flask backend.
5. Flask communicates with the Google Gemini API.
6. Gemini generates a context-aware email reply.
7. The generated response is displayed instantly.

---


## 📈 Future Enhancements

- Copy reply to clipboard
- Download generated reply
- Email summarization
- Multi-language support
- User authentication
- Reply history
- Dark mode

--

## 📸 Screenshots

### Home Page

![Home Page](screenshots/home.png)

### Generated Reply

![Generated Reply](screenshots/reply.png)
