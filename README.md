# AI Phishing Email Detector

**Machine Learning-Based Phishing Email Detection Using Python and Natural Language Processing**

## Overview

AI Phishing Email Detector is an academic cybersecurity project designed to classify email messages as potentially phishing-related or legitimate using machine learning and Natural Language Processing (NLP).

The system analyzes email text, transforms it into numerical features using TF-IDF vectorization, and applies a trained Logistic Regression classifier.

A Streamlit web application allows users to paste email content and receive a classification result.

The project demonstrates how supervised machine learning can support phishing detection and email security analysis.

## Key Features

### 1. Phishing Email Classification

- Classification of email text into phishing and legitimate categories.
- Analysis of email subject and body content.
- Machine learning-based prediction.
- Simple result visualization through a web interface.

### 2. Natural Language Processing

- Text representation using TF-IDF vectorization.
- Unigram and bigram feature extraction.
- English stop-word removal.
- Numerical feature generation for machine learning.

### 3. Machine Learning Model

- Supervised classification using Logistic Regression.
- Model training using Scikit-learn.
- Train/test dataset splitting.
- Model evaluation using standard classification metrics.
- Model serialization using Joblib.

### 4. Dataset Processing

The training pipeline combines email data from three sources:

- `SpamAssasin.csv`
- `PhishingEmailData.csv`
- `PhishingEmails.txt`

The preprocessing pipeline:

1. Loads the datasets.
2. Standardizes email subject and content fields.
3. Assigns binary labels.
4. Combines subject and body text.
5. Merges the datasets.
6. Splits the data into training and testing sets.

The application uses a binary classification convention:

- `0` — Legitimate email
- `1` — Phishing or suspicious email

**Dataset limitation:** The training code maps SpamAssassin spam labels to the positive class alongside phishing samples. As a result, the model may learn indicators of general spam as well as phishing.

### 5. Interactive Web Application

The Streamlit interface provides:

- An email text input field.
- A button to analyze the submitted message.
- Input validation for empty messages.
- A visual warning for predicted phishing messages.
- A success message for predicted legitimate emails.

## Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| NLP | TF-IDF Vectorizer |
| Classification | Logistic Regression |
| Data Processing | Pandas |
| Model Serialization | Joblib |
| Web Application | Streamlit |
| Evaluation | Accuracy, Precision, Recall, F1-score, Confusion Matrix |

## Machine Learning Pipeline

```text
Email Datasets
      |
      v
Data Loading & Preprocessing
      |
      v
Subject + Body Combination
      |
      v
Train / Test Split (80% / 20%)
      |
      v
TF-IDF Vectorization
      |
      v
Logistic Regression Training
      |
      v
Model Evaluation
      |
      v
Model Serialization (.joblib)
      |
      v
Streamlit Web Application
      |
      v
Email Classification
```

## Model Configuration

The current training implementation uses:

**TF-IDF Vectorizer**

```python
TfidfVectorizer(
    stop_words="english",
    ngram_range=(1, 2),
    max_features=60000
)
```

**Logistic Regression**

```python
LogisticRegression(
    max_iter=500,
    solver="liblinear"
)
```

**Dataset Split**

```python
train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

The model uses 80% of the available data for training and 20% for evaluation.

## Project Structure

```text
ai-phishing-email-detector/
├── app.py
├── train.py
│
├── logistic_model.joblib
├── linear_model.joblib
├── vectorizer.joblib
│
├── SpamAssasin.csv
├── PhishingEmailData.csv
├── PhishingEmails.txt
│
└── README.md
```

## Installation and Setup

### Prerequisites

- Python 3
- pip
- Git

### Step 1 — Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-phishing-email-detector.git
cd ai-phishing-email-detector
```

### Step 2 — Create a Virtual Environment

On Windows:

```powershell
py -m venv .venv
.\.venv\Scripts\activate
```

### Step 3 — Install Dependencies

```bash
pip install streamlit pandas scikit-learn joblib
```

### Step 4 — Train the Model (Optional)

The repository contains serialized model artifacts.

To retrain the classifier:

```bash
python train.py
```

The script generates:

```text
logistic_model.joblib
vectorizer.joblib
```

The additional `linear_model.joblib` file is included in the original project but is not loaded by the current Streamlit application.

### Step 5 — Run the Application

```bash
streamlit run app.py
```

Open the local address displayed by Streamlit, typically:

```text
http://localhost:8501
```

### Step 6 — Analyze an Email

1. Copy the subject and content of an email.
2. Paste the text into the application.
3. Click the analysis button.
4. Review the predicted classification.

## Model Evaluation

The training script evaluates the classifier using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

The evaluation metrics are calculated on the test split and printed in the terminal.

Numerical performance results should be added after reproducing the training and evaluation process.

For example:

```text
Accuracy: [TO BE ADDED]
Precision: [TO BE ADDED]
Recall: [TO BE ADDED]
F1-score: [TO BE ADDED]
```

No performance values are claimed here without verified experimental results.

## Limitations

- The model analyzes email text rather than full email headers.
- It does not inspect attachments or execute malware analysis.
- It does not perform live URL reputation checks.
- Predictions depend on the quality and representativeness of training data.
- General spam and phishing labels are combined in the current training pipeline.
- The current split does not explicitly prevent duplicate or closely related emails from appearing across training and test sets.
- A legitimate prediction does not guarantee that an email is safe.

## Security Considerations

- Do not paste confidential emails into an untrusted deployment.
- Use only trusted serialized model files.
- Avoid loading unknown Joblib files because deserialization can execute malicious code.
- Review dataset licensing and privacy requirements before public distribution.
- Do not use the classifier as the sole basis for security decisions.

## Future Improvements

- Separate spam and phishing classification.
- Deduplication and leakage-resistant evaluation.
- Email header analysis.
- URL extraction and reputation checking.
- Attachment analysis.
- Additional ML model comparison.
- Explainable AI for prediction interpretation.
- Automated testing and CI/CD integration.
- Model performance monitoring.

## Skills Demonstrated

- Machine learning for cybersecurity.
- Natural Language Processing.
- Email threat classification.
- Data preprocessing and feature engineering.
- Supervised learning.
- Model evaluation.
- Streamlit application development.

## Author

**Asma Bensassi Nour**

Cyberdefense Engineering Student — ENSA Marrakech

Academic project focused on machine learning, phishing detection, and email security.
