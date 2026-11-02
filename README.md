# 🏏 Cricbuzz LiveStats: Real-Time Cricket Insights & SQL-Based Analytics

A comprehensive cricket analytics dashboard that integrates live data from the Cricbuzz API with a SQL database, featuring an interactive Streamlit web application.

## 🚀 Features
- **Live Match Updates**: Real-time scores, commentary, and scorecard details via Cricbuzz API.
- **Player Statistics**: Detailed batting and bowling stats visualization.
- **SQL-Driven Analytics**: 25+ structured SQL queries ranging from beginner to advanced levels.
- **CRUD Operations**: Full Create, Read, Update, Delete management for players and matches.

---

## 🛠️ Project Structure
```
cricbuzz_livestats/
├── main.py                  # Streamlit Multi-page Application
├── utils/
│   └── db_connection.py     # Database connection helper
├── data/
│   ├── schema.sql           # Database DDL schema
│   └── sample_data.sql      # Initial seed data
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## ⚙️ Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cricbuzz-livestats.git
   cd cricbuzz-livestats
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit application:
   ```bash
   streamlit run main.py
   ```
