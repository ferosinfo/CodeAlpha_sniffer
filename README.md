```markdown
# Network Sniffer with Django

A simple network sniffer built with Django and Scapy. This application captures network packets and displays them in a web interface.

## 🚀 Features
✅ Capture network packets (Ethernet, IP, TCP, UDP).  
✅ Save captured packets to a database.  
✅ Display packets in a web interface.

---

## 📌 Requirements
🟢 Python 3.8+  
🟢 Django 4.2+  
🟢 Scapy 2.5+  

---

## 🛠 Installation

### 1️⃣ Clone the repository:
```bash
git clone https://github.com/yourusername/networksniffer.git
cd networksniffer
```

### 2️⃣ Create a virtual environment:
```bash
python -m venv venv
```

### 3️⃣ Activate the virtual environment:
```bash
# macOS/Linux
source venv/bin/activate  

# Windows
venv\Scripts\activate  
```

### 4️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

### 5️⃣ Run migrations:
```bash
python manage.py migrate
```

### 6️⃣ Start the development server:
```bash
python manage.py runserver
```

### 7️⃣ Open your browser and navigate to:
🔗 [http://127.0.0.1:8000/sniffer/](http://127.0.0.1:8000/sniffer/)

---

## 🎯 Usage
1️⃣ Enter the network interface (e.g., `eth0`).  
2️⃣ Enter the number of packets to capture.  
3️⃣ Click **"Start Sniffing"** to begin capturing packets.  
4️⃣ View the captured packets displayed in a table.  

---

✨ **Enjoy using Network Sniffer! 🚀**
```

