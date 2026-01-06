# 📝 Serverless Notes Application

This is a full-stack **serverless Notes application** built using **AWS Lambda, API Gateway, DynamoDB**, and a **Streamlit frontend**.

---

## 🚀 Features
- Create notes using HTTP API
- Fetch all notes
- Serverless backend (no EC2)
- Cloud database (DynamoDB)
- Streamlit web interface

---

## 🏗️ Architecture

User → Streamlit → API Gateway → Lambda → DynamoDB

---

## 🧠 Technologies Used

### Backend
- AWS Lambda (Python)
- API Gateway
- DynamoDB
- IAM
- CloudWatch

### Frontend
- Streamlit
- Python Requests

---

## 📂 Project Structure

```
notes-project/
├── notes-backend/
│       └──function.py
│
├── notes-frontend/
│   ├── app.py
│   └── requirements.txt
│
└── README.md
```

---

## 🔧 API Endpoints

### GET /notes
Returns all notes from DynamoDB.

### POST /notes
Creates a new note.

---

## 🧪 Testing
- Postman
- AWS Lambda test events
- CloudWatch logs

---

## 📌 Learning Outcomes
- Serverless architecture
- API Gateway & Lambda integration
- DynamoDB operations
- Frontend–backend integration
- Git & GitHub usage

---

## 👤 Author
Ismail Saleel
