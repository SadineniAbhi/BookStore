# 📚 BookStore — Flask-Based E-commerce Web App

This is a **BookStore web application** built using **Flask**, a lightweight Python web framework. It allows users to register, login, browse a catalog of books, add them to their cart, and place orders — all with admin functionality and SQLite database support.

---

## ✨ Features

- 👤 User registration and authentication (Flask-Login)
- 🛒 Add to cart, checkout, and order tracking
- 📚 Book listing and search
- 🧾 Admin dashboard for managing books and orders (Flask-Admin)
- 💾 SQLite as the database
- 📦 Modular architecture with clear separation of concerns
- 🔐 Secure forms using Flask-WTF and bcrypt

---

### Prerequisites
- python
- pip

### 🐳 Docker Setup
```bash
  docker run -p 5000:5000 sadineniabhi/bookstore
```
**Access the application**:  
   Open your browser and visit [http://localhost:5000](http://localhost:5000)

### 🧰 Local Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/SadineniAbhi/BookStore.git
   ```

2. **Install Dependencies
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirement.txt
   ```

4. **Start the development server**:
   ```bash
   cd BookStore/BookStore
   python app.py
   ```

5. **Access the application**:  
   Open your browser and visit [http://localhost:5000](http://localhost:5000)
   
---

## 🤝 Contributing

Contributions are what make the open-source community amazing!  
If you would like to improve SmartBoard:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/yourFeature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/yourFeature`)
5. Open a Pull Request




