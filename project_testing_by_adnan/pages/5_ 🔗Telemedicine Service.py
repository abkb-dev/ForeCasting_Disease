import streamlit as st
from PIL import Image

# Telemedicine services data
telemedicine_services = {
    "Plum Telehealth": {
        "Description": "Plum Telehealth by Plum insurance offers high-quality teleconsultations round the clock. From the convenience of your residence, you may schedule a teleconsultation with your preferred doctor, cutting travel expenses and reducing waiting times at clinics and hospitals by following a few easy steps. You have quicker access to medical treatment if you have access to experts who are located across the country.",
        "Availability": "24/7",
        "Link": "https://www.plumhq.com/telehealth"
    },
    "PharmEasy": {
        "Description": "PharmEasy is an e-pharmacy company that offers telemedicine services for remote consultation, prescription refills, and health checkups. Through its services, patients can access healthcare from the comfort of their own homes. The company’s services include a wide range of health-related services, including online medical records and video chats.",
        "Coverage": "1,000-plus cities across India",
        "Services": "Remote consultation, prescription refills, health checkups",
        "Link": "https://pharmeasy.in/help/doctor-consultation-43000550954"
    },
    "Tata 1mg": {
        "Description": "Tata 1mg, formerly known as 1mg, is a health solutions company that provides medical services such as e-pharmacy, tests, e-consultation, and healthcare content. The firm offers medication information, generic substitutes, home delivery services for pharmacies, FMCG, and laboratory tests, and telehealth services.",
        "Services": "E-pharmacy, tests, e-consultation, healthcare content",
        "Reach": "Across India",
        "Link": "https://www.1mg.com/online-doctor-consultation?wpsrc=Bing+Organic+Search"
    },
    "Practo Technologies": {
        "Description": "Practo offers remote consultations with doctors and health practitioners via its platform, making it one of India’s most prominent telemedicine firms. Patients can connect with doctors anywhere in India thanks to the company’s services, which are available in over 20 languages.",
        "Services": "Remote consultations, digital prescriptions, medication orders, doctor appointments, lab tests",
        "Languages": "Available in over 20 languages",
        "Link": "https://www.practo.com/"
    },
    "MFine Pvt Ltd": {
        "Description": "MFine is an AI-powered, on-demand healthcare startup that gives customers access to online appointments and hospital-based linked healthcare. Telemedicine and teleconsulting programs via the MFine app are allowing medical knowledge to reach people much more easily and conveniently.",
        "Services": "Online appointments, hospital-based linked healthcare",
        "Features": "AI-powered, on-demand healthcare",
        "Link": "https://www.mfine.co/online-doctor-consultation/"
    },
    "eSanjeevani": {
        "Description": "eSanjeevani - National Telemedicine Service of India is a step towards digital health equity to achieve Universal Health Coverage (UHC). eSanjeevani facilitates quick and easy access to doctors and medical specialists from your smartphones. You can also access quality health services remotely via eSanjeevani by visiting the nearest Ayushman Bharat Health & Wellness Centre.",
        "Accessibility": "Accessible from smartphones",
        "Access": "Visit the nearest Ayushman Bharat Health & Wellness Centre",
        "Website": "https://esanjeevani.mohfw.gov.in/#/"
    }
}

# Sidebar
st.sidebar.title("Telemedicine Services")

selected_service = st.sidebar.selectbox("Select Telemedicine Service", list(telemedicine_services.keys()))

# Main content
st.title("Telemedicine Services")
st.image("telemedicine.jpg", caption="Telemedicine Services", use_column_width=True)

if selected_service:
    st.subheader(selected_service)
    if selected_service != "eSanjeevani":
        st.write(telemedicine_services[selected_service]["Description"])
        st.write("**Key Features:**")
        for key, value in telemedicine_services[selected_service].items():
            if key != "Description" and key != "Link" and key != "Website":
                st.write(f"- **{key.capitalize()}:** {value}")
        st.markdown(f'<div style="background-color:#ED8A57; padding: 10px; border-radius: 5px;"><a style="color:black;" href="{telemedicine_services[selected_service]["Link"]}">Schedule Consultation</a></div>', unsafe_allow_html=True)
    else:
        st.write(telemedicine_services[selected_service]["Description"])
        st.write("**Accessibility:**", telemedicine_services[selected_service]["Accessibility"])
        st.write("**Access:**", telemedicine_services[selected_service]["Access"])
        st.markdown(f'<div style="background-color:#ED8A57; padding: 10px; border-radius: 5px;"><a style="color:black;" href="{telemedicine_services[selected_service]["Website"]}">Visit eSanjeevani Website</a></div>', unsafe_allow_html=True)
