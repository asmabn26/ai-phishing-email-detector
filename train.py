import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from joblib import dump

# =====================================================================
# 1. Charger SpamAssassin.csv
# =====================================================================

spamassassin = pd.read_csv("SpamAssasin.csv")

# Colonnes : sender,receiver,date,subject,body,label,urls
spamassassin = spamassassin.rename(columns={"body": "content"})
spamassassin = spamassassin[["subject", "content", "label"]].fillna("")

# Convertir spam/ham → 1/0 si texte
if spamassassin["label"].dtype == "object":
    spamassassin["label"] = spamassassin["label"].apply(
        lambda x: 1 if str(x).lower() == "spam" else 0
    )

# =====================================================================
# 2. Charger PhishingEmailData.csv (avec encodage compatible Windows)
# =====================================================================

phish_data = pd.read_csv("PhishingEmailData.csv", encoding="latin1")

phish_data = phish_data.rename(columns={
    "Email_Subject": "subject",
    "Email_Content": "content"
})

phish_data["label"] = 1  # Tous = phishing
phish_data = phish_data[["subject", "content", "label"]].fillna("")

# =====================================================================
# 3. Charger PhishingEmails.txt
# =====================================================================

parsed_emails = []
with open("PhishingEmails.txt", "r", encoding="utf-8", errors="ignore") as f:
    raw = f.read()

blocks = raw.split("--------------------------------------------------")

for block in blocks:
    s = re.search(r"Subject:\s*(.*)", block)
    c = re.search(r"Content:\s*(.*)", block, re.DOTALL)

    if s and c:
        parsed_emails.append({
            "subject": s.group(1).strip(),
            "content": c.group(1).strip(),
            "label": 1
        })

txt_df = pd.DataFrame(parsed_emails)

# =====================================================================
# 4. Fusion datasets
# =====================================================================

df = pd.concat([spamassassin, phish_data, txt_df], ignore_index=True)
df = df.fillna("")

df["text"] = df["subject"] + " " + df["content"]

# =====================================================================
# 5. Train/Test Split
# =====================================================================

X_train, X_test, y_train, y_test = train_test_split(
    df["text"], df["label"], test_size=0.2, random_state=42
)

# =====================================================================
# 6. TF-IDF Vectorization
# =====================================================================

vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1,2),
    max_features=60000
)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec  = vectorizer.transform(X_test)

# =====================================================================
# 7. Logistic Regression (le bon modèle)
# =====================================================================

model = LogisticRegression(max_iter=500, solver="liblinear")
model.fit(X_train_vec, y_train)

# =====================================================================
# 8. Évaluation
# =====================================================================

y_pred = model.predict(X_test_vec)

print("\nAccuracy :", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# =====================================================================
# 9. Sauvegarde
# =====================================================================

dump(model, "logistic_model.joblib")
dump(vectorizer, "vectorizer.joblib")

print("\n✅ Modèle sauvegardé : logistic_model.joblib")
print("✅ Vectorizer sauvegardé : vectorizer.joblib")
