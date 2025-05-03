# Lan-Based-Messenger

A simple LAN-based real-time chat application built with **Flask**, **Socket.IO**, and Python. It features user registration, login, emoji support, file sharing, and basic XOR encryption for educational purposes.

---

## 📁 Project Structure

```
├── templates/             # HTML templates (e.g., index.html)
├── LICENSE                # Project license file
├── README.md              # Project documentation
├── chat_features.py       # Emoji formatting, message creation, file handling
├── encryption.py          # XOR-based encryption/decryption
├── requirements.txt       # Python package requirements
├── user_manager.py        # User registration and login logic
├── web_server.py          # Flask + Socket.IO backend logic
```

---

## 🚀 Features

* 🔐 **User Authentication** – Register and log in with basic credential checking.
* 😎 **Real-Time Messaging** – Built using Flask-SocketIO.
* 😊 **Emoji Support** – Replace codes like `:smile:` with emojis.
* 📁 **File Sharing** – Send and receive files using base64 encoding.
* 🟢 **Online/Offline Status** – Track connected users in real-time.
* 🔑 **Basic XOR Encryption** – Educational demonstration only.

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/23CS020DhadukJeet/lan-chat-app.git
cd lan-chat-app
```

### 2. (Optional) Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python web_server.py
```

Visit `http://localhost:5000` in your browser.

---

## 🔐 Security Note

This application uses XOR encryption, which is **not secure** and should only be used for demonstration. Use proper cryptographic libraries like `cryptography` or `PyNaCl` for real applications.

---

## 👨‍💻 Author

**Jeet Dhaduk**
B.Tech Computer Science and Engineering
GitHub: [@23CS020DhadukJeet](https://github.com/23CS020DhadukJeet)

---

## 📌 License

This project is licensed under the [MIT License](./LICENSE).
