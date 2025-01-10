*NAME:* SAMPANGI NAGAVARDHAN
*COMPANY:* CODTECH IT SOLUTIONS  
*ID:* CT08DS540
*DOMAIN:* Cyber Security and Ethical Hacking  
*DURATION:* December 2024 to January 2025 
## **Task 3: Penetration Testing Toolkit**

### **Description**
A modular toolkit that provides functionalities such as port scanning and brute-forcing for penetration testing.

### **Features**
- Port scanning for open ports.
- Brute-forcing login credentials for services.

### **Requirements**
- Python 3.x

### **Setup**
1. Clone the repository.
2. Ensure Python 3.x is installed.

### **Usage**
1. **Port Scanner**:
   ```bash
   python penetration_toolkit.py --scan "127.0.0.1" --ports "21,22,80"
   ```
2. **Brute Force Login**:
   ```bash
   python penetration_toolkit.py --bruteforce "127.0.0.1" --port 22 --usernames "usernames.txt" --passwords "passwords.txt"
   ```

### **Example**
```bash
python penetration_toolkit.py --scan "192.168.1.1" --ports "21,22,80"
python penetration_toolkit.py --bruteforce "192.168.1.1" --port 22 --usernames "users.txt" --passwords "passwords.txt"
```

---
