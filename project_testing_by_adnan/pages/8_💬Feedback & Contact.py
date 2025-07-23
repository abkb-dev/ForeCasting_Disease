import streamlit as st

def feedback_and_contact():
    st.title("Feedback and Contact")

    st.markdown("""
    <style>
    .box {
        border-radius: 5px;
        padding: 20px;
        margin: 10px 0px;
        color: white;
    }
    .feedback-box {
        background: linear-gradient(to right, #e16622, #ed8a57);
    }
    .contact-box {
        background: linear-gradient(to right, #ed8a57, #e16622);
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="box feedback-box">Feedback</div>', unsafe_allow_html=True)
    st.write("Your Feedback is Valuable!")
    st.write("Please rate your overall experience in using our Web App")
    rating = st.slider('Rate our app', 0, 5)

    st.write("Have questions or suggestions? We'd love to hear from you.")
    feedback = st.text_area('Type here...')
    if st.button('Submit'):
        st.write("Thank you for your feedback!")

    st.markdown('<div class="box contact-box">Contact</div>', unsafe_allow_html=True)
    st.markdown("""
    - **Sohaib**: sohaib01011@gmail.com
    - **Ahmed**:  ahmed92455@gmail.com
    - **Adnan**:  adnan21002@gmail.com
    """)

if __name__ == "__main__":
    feedback_and_contact()
