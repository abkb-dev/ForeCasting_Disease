import streamlit as st

def about_us():
    st.markdown("""
    <style>
    .gradient-line {
        height: 3px;
        background: linear-gradient(to right, darkorange, orange);
    }
    .title {
        font-size: 26px;
        font-weight: 600;
    }
    .gradient-box {
        padding: 10px;
        color: white;
        font-weight: bold;
        background: linear-gradient(to right, #e16622, #ed8a57);
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('## 💡 Discover Our Team')
    st.markdown('<div class="gradient-line"></div>', unsafe_allow_html=True)

    st.write("""
    As a team of passionate individuals, we embarked on a journey to create a user-friendly and efficient application to predict diseases such as Diabetes, Heart Disease and Lung Cancer.
    """)

    st.markdown('<div class="gradient-box">🔶 Team Members:</div>', unsafe_allow_html=True)
    st.markdown("""
    -  **Syed Sohaib Musharaf** - Team Lead
    -  **Mohammed Ahmed**
    -  **Adnan Khalid**
                
    
    """)

    st.markdown('<div class="gradient-box">🔶 Guide:</div>', unsafe_allow_html=True)
    st.markdown("""
    -  **Dr.Syed AsadUllah Hussaini, M.Tech, Ph.D**
    """)
    st.markdown('<div class="gradient-line"></div>', unsafe_allow_html=True)

    st.write("""
    🔸Our mentor and guide, whose invaluable support and expertise have been instrumental in shaping this project.
    """)

    st.write("""
    🔸Throughout the development process, we have combined our diverse skills and knowledge to deliver a robust and accurate disease prediction system. We are committed to promoting health awareness and providing a valuable tool for individuals to assess their health risks.
    """)

    st.write("""
    🔸Thank you for choosing our Multiple Disease Prediction Web App. We hope it proves to be a valuable resource for you and others.
    """)

if __name__ == "__main__":
    about_us()
