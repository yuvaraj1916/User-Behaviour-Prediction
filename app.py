from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load model & scaler
model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # ==============================
        # 1. Get Input Values
        # ==============================
        payment_value = float(request.form['payment_value'])
        price = float(request.form['price'])
        delivery_time = float(request.form['delivery_time'])
        delivery_delay = float(request.form['delivery_delay'])

        # 🔥 FIX: Reverse logic
        fast_delivery_input = int(request.form['fast_delivery'])
        fast_delivery = 0 if fast_delivery_input == 1 else 1

        purchase_hour = int(request.form['purchase_hour'])
        purchase_day = int(request.form['purchase_day'])
        purchase_month = int(request.form['purchase_month'])

        # ==============================
        # 2. Feature Order
        # ==============================
        features = np.array([[
            payment_value,
            price,
            delivery_time,
            delivery_delay,
            fast_delivery,
            purchase_hour,
            purchase_day,
            purchase_month
        ]])

        features = scaler.transform(features)

        # ==============================
        # 3. Prediction
        # ==============================
        prediction = model.predict(features)[0]

        try:
            probability = model.predict_proba(features)[0][1]
        except:
            probability = 0.5

        probability_percent = round(probability * 100, 2)

        # ==============================
        # 4. Result
        # ==============================
        if prediction == 1:
            result = "Happy Customer 😊"
            color = "#00ffcc"
        else:
            result = "Unhappy Customer 😞"
            color = "#ff4d6d"

        # ==============================
        # 5. Risk
        # ==============================
        if probability_percent >= 75:
            risk = "Low Risk 🟢"
        elif 40 <= probability_percent < 75:
            risk = "Medium Risk 🟡"
        else:
            risk = "High Risk 🔴"

        # ==============================
        # 6. Insights
        # ==============================
        insights = []

        if delivery_delay > 2:
            insights.append("🚚 Improve delivery speed")

        if price > payment_value:
            insights.append("💸 Offer discount")

        if probability_percent < 50:
            insights.append("📩 Send apology email")

        if fast_delivery == 0:
            insights.append("⚡ Provide fast delivery option")

        if len(insights) == 0:
            insights.append("✅ Customer is satisfied — maintain service quality")

        # ==============================
        # 7. Return with values
        # ==============================
        return render_template(
            "index.html",
            prediction_text=result,
            color=color,
            probability=probability_percent,
            risk=risk,
            insights=insights,

            # Persist inputs
            payment_value=payment_value,
            price=price,
            delivery_time=delivery_time,
            delivery_delay=delivery_delay,
            fast_delivery=fast_delivery_input,
            purchase_hour=purchase_hour,
            purchase_day=purchase_day,
            purchase_month=purchase_month
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {str(e)}",
            color="red"
        )


if __name__ == "__main__":
    app.run(debug=True)