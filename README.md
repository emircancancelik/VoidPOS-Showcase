# VoidPOS-Showcase
Technical showcase for an AI-powered Retail POS System built with Python, PySide6, and Scikit-learn.

# 🚀 VoidPOS: AI-Powered Smart Sales System

**VoidPOS** is a commercial desktop application built with Python. It is not just a standard sales software; it uses Data Science to guide business owners and help them make better decisions.

> 🔒 *Note: Since this project has commercial potential, I am keeping the main source code private for now. I created this repository to showcase the architecture and technical capabilities of the project.*

## 📸 Project Screenshots
<img width="1700" height="1044" alt="Ekran Resmi 2026-02-17 18 53 27" src="https://github.com/user-attachments/assets/135bdfd0-b9e9-4848-a192-46111d34d6ed" />

<img width="701" height="874" alt="Ekran Resmi 2026-02-17 18 55 10" src="https://github.com/user-attachments/assets/fe882657-d140-42ab-baac-55e91f8ddf3d" />


## 🔥 Key Features

### 1. Embedded AI (On-Device)
I integrated **Scikit-learn** directly into the application. It works locally on the machine without needing any cloud API:
* **Sales Prediction:** It uses `Gradient Boosting` to predict stock needs for the next week.
* **Customer Analysis:** It uses `K-Means Clustering` to analyze customer baskets and segments them.
* **Dynamic Pricing:** It suggests automatic pricing strategies based on sales speed.

### 2. Hardware Integration (IPC)
* **Ingenico Cash Register:** Python communicates with the device using a custom XML-based protocol.
* **Fiscal Approval:** Sales data is processed instantly, and the official receipt is printed automatically.

### 3. Natural Language Processing (NLP)
* The user can type free text commands like *"Increase Marlboro stock by 5"*. The system understands this using Regex and Fuzzy Logic, then updates the database.

## 🛠 Technologies Used

* **Language:** Python 3.10+
* **UI:** PySide6 (Qt for Python)
* **AI/ML:** Scikit-learn, Pandas, NumPy
* **Database:** SQLite (Optimized)
* **Multithreading:** QThread (For non-blocking UI)

---
*Developer: Emircan Cançelik*
