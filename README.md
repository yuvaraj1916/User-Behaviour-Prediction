# 🧠 User Behaviour Prediction System

## 🚀 Project Overview
This project predicts whether a customer is **satisfied or not** based on order details using Machine Learning.

If the customer is not satisfied, the system also provides **suggestions to improve satisfaction** such as faster delivery or reducing delays.

---

## 📊 Features
- Predicts customer satisfaction (Satisfied / Not Satisfied)
- Provides actionable suggestions:
  - Fast Delivery
  - Reduce Delivery Delay
  - Improve Pricing Strategy
- Interactive web-based UI
- Model Accuracy: **0.71**

---

## 🧾 Input Parameters
- Payment Value  
- Product Price  
- Delivery Time (days)  
- Delivery Delay (days)  
- Order Day  
- Order Month  

---

## 🎯 Output
- Customer Satisfaction Prediction  
- Suggestions for improvement  

---

## 🛠️ Tech Stack
- Python  
- Machine Learning (Scikit-learn)  
- Pandas, NumPy  
- Flask (Web Framework)  

---

## 📂 Project Structure
```
User-Behaviour-Prediction/
│
├── app.py
├── best_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
│
├── Datasets/
│   ├── olist_orders_dataset.csv
│   └── olist_order_reviews_dataset.csv
│
├── templates/
│   └── index.html
│
├── Output Screenshort/
│   ├── Home.png
│   ├── Inputs.png
│   └── Prediction.png
│
├── notebook/
│   └── Capstone_Project.ipynb
```

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python app.py
```

Then open in browser:
```
http://127.0.0.1:5000/
```

---

## 📈 Model Details
- Algorithms Used:
  - Logistic Regression (Baseline Model)
  - Random Forest Classifier (Final Model)
- Accuracy: **0.71**
- Random Forest performed better due to its ability to handle non-linear relationships and feature interactions.

---

## 💡 Future Improvements
- Improve accuracy (>0.85)
- Deploy on cloud (Render / AWS)
- Add real-time prediction system

---
