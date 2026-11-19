import streamlit as st
from joblib import load



model = load("logistic_model.joblib")
vectorizer = load("vectorizer.joblib")



def detect_email(text):
    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0]  # donne 0 (safe) ou 1 (phishing)
    
    if pred == 1:
        return "⚠ PHISHING"
    else:
        return "✔ Email légitime"



st.set_page_config(page_title="Détection de Phishing", page_icon="🔒")

st.title("Détection d’Email de Phishing")
st.write("Colle ton email ci-dessous (subject + contenu).")

email_input = st.text_area("📩 Votre email :", height=300)

if st.button("Analyser l'email"):
    if email_input.strip() == "":
        st.warning("⚠ Colle un email avant d'analyser.")
    else:
        result = detect_email(email_input)
        
        if "PHISHING" in result:
            st.error(result)
        else:
            st.success(result)