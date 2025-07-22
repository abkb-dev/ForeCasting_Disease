# 🧠 A Comprehensive Multiple Disease Forecasting Using Machine Learning Algorithms and Streamlit Interface

## 🚀 Project Overview 

In today's world, finding and treating diseases early can save lives and reduce health problems. This project is designed to make that process easier and smarter.

We’ve built a single, easy-to-use platform that can predict multiple diseases using machine learning (a type of smart computer program) and a user-friendly app made with Streamlit.

### 💡 What Can It Predict?

Our system helps detect several major diseases, including:

- 🩸 **Diabetes**
- ❤️ **Heart Disease**
- 🧠 **Parkinson’s Disease**
- 🏥 **Liver Disorders**
- 🦠 **Hepatitis**
- 🫁 **Lung Cancer**
- 💧 **Chronic Kidney Disease**
- 🎗️ **Breast Cancer**
- ...and many more!

---

## 🎯 What Are Our Goals?

- ✅ **Make accurate disease predictions** using machine learning to help people understand their health risks early.
- 🌍 **Use real medical data** from different countries to ensure the system works well for everyone.
- 🖥️ **Create a simple and clean web app** using Streamlit so anyone can use it without technical knowledge.
- 💬 **Add useful health features** like:
  - Video calls with doctors (Telemedicine)
  - Online support groups (Community Platform)
  - Personal health advice (Fitness & Diet Chatbots)
  - Organized medical records (EHR System)
- 🔐 **Keep health data private and secure**, while building a system that can grow and improve over time.


---

## 📊 Data Sources

- Kaggle
- UCI Machine Learning Repository
- WHO Global Health Observatory (GHO)
- CDC WONDER
- HealthData.gov

---

## 🧠 Machine Learning Techniques

We utilized a wide range of models including:

- K-Nearest Neighbors (KNN)  
- Support Vector Machine (SVM)  
- Logistic Regression  
- Decision Trees  
- Random Forest  
- Naïve Bayes  
- Gradient Boosting  
- AdaBoost  
- XGBoost  
- LightGBM  
- CatBoost  
- Stacking & Voting Classifiers

Each model was trained on disease-specific datasets and evaluated using standard accuracy metrics to select the most performant ones.

---

## 🧪 Model Performance Highlights

| Disease                   | Best Model            | Accuracy (%) |
|---------------------------|------------------------|--------------|
| Multiple Disease          | XGBoost                | 94.9         |
| Diabetes                  | XGBoost                | 89.0         |
| Heart Disease             | Logistic Regression    | 88.5         |
| Parkinson’s Disease       | Random Forest          | 96.1         |
| Hepatitis                 | Random Forest          | 93.0         |
| Chronic Kidney Disease    | Logistic Regression    | 97.2         |
| Breast Cancer             | Voting Classifier      | 97.3         |

---

## 🌐 Streamlit Interface Features 

- 🔍 **One Place for Disease Predictions**  
  Our platform checks for 9 different diseases all in one place. Just enter your health details and get instant results—no need to switch between multiple apps.

- 🧾 **Electronic Health Records (EHR)**  
  Your health records like test results and predictions are stored securely, so you can view and track your health history anytime. We use MongoDB to manage and protect this data.

- 💬 **Helpful Chatbots for Fitness & Diet**  
  Not sure what to eat or how to stay active? Our chatbots give you personalized advice on diet and exercise, tailored to the disease you're checking for.

- 🤝 **Connect with Others**  
  Join support groups and chat with others facing similar health issues. Share stories, tips, and stay motivated through our community platform.

- 💻 **Talk to Doctors from Home (Telemedicine)**  
  You can have video consultations with doctors without leaving your home, making healthcare more accessible and convenient.

- 🔐 **Your Data is Safe**  
  We protect your personal health data with strong privacy and security measures, so your information stays confidential.
*Scalable & Flexible Design**: Easily adaptable for future disease integrations.

---


## 📦 Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python (scikit-learn, pandas, pickle)  
- **Database**: MongoDB  
- **ML Libraries**: scikit-learn, XGBoost, LightGBM, CatBoost  
- **Deployment**: Localhost / Cloud-compatible  

---
## 🧩 System Architecture
![System Architecture](https://raw.githubusercontent.com/abkb-dev/ForeCasting_Disease/main/images/system_architecture.jpeg)
1. **Data Aggregation **  
   This component gathers datasets from various sources like Kaggle, UCI, and WHO for analysis.

2. **Data Processing**  
   The collected data undergoes preprocessing to clean and prepare it for analysis.

3. **Data Splitting**  
   The prepared data is divided into training and testing sets.

4. **Machine Learning Model**  
   Utilizes algorithms like SVM, decision trees, etc., to build predictive models based on input symptoms for disease prediction.

5. **Telemedicine Service**  
   Offers various services for remote medical consultation.

6. **Community Engagement Platform**  
   Connects patients to forums based on their diseases of interest.

7. **Chatbot Components**
   - **DietNutriBot**: Provides tailored dietary recommendations for specific diseases.  
   - **FitGuideBot**: Generates personalized fitness plans for diseases.

8. **Electronic Health Record (EHR) System Integration**  
   Includes a system to manage patients' health records within the platform.



