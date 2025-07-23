import streamlit as st

# Function to display communities and forums for each disease
def show_communities_for_disease(disease):
    st.title(f"{disease} Community")

    if disease == "Diabetes":
        st.write("Welcome to the Diabetes community!")
        st.write("Here you can find forums, support groups, and user-generated content related to diabetes.")
        st.markdown("""<div style="background-color:#ED8A57; padding: 10px; border-radius: 5px;">
                        <div><a style="color:black;" href="https://www.diabetesforum.com/">Visit Diabetes Forums</a></div><br>
                        <div><a style="color:black;" href="https://www.diabetes.org.uk/in_your_area">Join Diabetes Support Group</a></div><br>
                        <div><a style="color:black;" href="https://www.diabetes.org/diabetes">Explore Diabetes Articles</a></div><br>
                      </div>""", unsafe_allow_html=True)

    elif disease == "Heart Disease":
        st.write("Welcome to the Heart Disease community!")
        st.write("Here you can find forums, support groups, and user-generated content related to heart disease.")
        st.markdown("""<div style="background-color:#ED8A57; padding: 10px; border-radius: 5px;">
                        <div><a style="color:black;" href="https://community.bhf.org.uk/">Visit Heart Disease Forums</a></div><br>
                        <div><a style="color:black;" href="https://www.heart.org/en/online-communities">Join Heart Disease Support Group</a></div><br>
                        <div><a style="color:black;" href="https://www.heart.org/en/health-topics">Explore Heart Disease Articles</a></div><br>
                      </div>""", unsafe_allow_html=True)

    elif disease == "Parkinson's":
        st.write("Welcome to the Parkinson's community!")
        st.write("Here you can find forums, support groups, and user-generated content related to Parkinson's disease.")
        st.markdown("""<div style="background-color:#ED8A57; padding: 10px; border-radius: 5px;">
                        <div><a style="color:black;" href="https://parkinsonsforum.org/">Visit Parkinson's Forums</a></div><br>
                        <div><a style="color:black;" href="https://www.parkinsons.org.uk/information-and-support">Join Parkinson's Support Group</a></div><br>
                        <div><a style="color:black;" href="https://www.parkinson.org/Understanding-Parkinsons">Explore Parkinson's Articles</a></div><br>
                      </div>""", unsafe_allow_html=True)

    elif disease == "Liver Disease":
        st.write("Welcome to the Liver Disease community!")
        st.write("Here you can find forums, support groups, and user-generated content related to liver disease.")
        st.markdown("""<div style="background-color:#ED8A57; padding: 10px; border-radius: 5px;">
                        <div><a style="color:black;" href="https://www.hepb.org/">Visit Liver Disease Forums</a></div><br>
                        <div><a style="color:black;" href="https://www.liverfoundation.org/for-patients/connect-with-others/">Join Liver Disease Support Group</a></div><br>
                        <div><a style="color:black;" href="https://www.niddk.nih.gov/health-information/liver-disease">Explore Liver Disease Articles</a></div><br>
                      </div>""", unsafe_allow_html=True)

    elif disease == "Hepatitis":
        st.write("Welcome to the Hepatitis community!")
        st.write("Here you can find forums, support groups, and user-generated content related to hepatitis.")
        st.markdown("""<div style="background-color:#ED8A57; padding: 10px; border-radius: 5px;">
                        <div><a style="color:black;" href="https://www.hepmag.com/">Visit Hepatitis Forums</a></div><br>
                        <div><a style="color:black;" href="https://www.hepatitis.va.gov/community/support-groups/index.asp">Join Hepatitis Support Group</a></div><br>
                        <div><a style="color:black;" href="https://www.hepatitiscentral.com/">Explore Hepatitis Articles</a></div><br>
                      </div>""", unsafe_allow_html=True)

    elif disease == "Lung Cancer":
        st.write("Welcome to the Lung Cancer community!")
        st.write("Here you can find forums, support groups, and user-generated content related to lung cancer.")
        st.markdown("""<div style="background-color:#ED8A57; padding: 10px; border-radius: 5px;">
                        <div><a style="color:black;" href="https://forums.lungevity.org/">Visit Lung Cancer Forums</a></div><br>
                        <div><a style="color:black;" href="https://www.lungcancer.org/find_support">Join Lung Cancer Support Group</a></div><br>
                        <div><a style="color:black;" href="https://www.cancer.org/cancer/lung-cancer.html">Explore Lung Cancer Articles</a></div><br>
                      </div>""", unsafe_allow_html=True)

    elif disease == "Chronic Kidney Disease":
        st.write("Welcome to the Chronic Kidney Disease community!")
        st.write("Here you can find forums, support groups, and user-generated content related to chronic kidney disease.")
        st.markdown("""<div style="background-color:#ED8A57; padding: 10px; border-radius: 5px;">
                        <div><a style="color:black;" href="https://forums.davita.com/">Visit CKD Forums</a></div><br>
                        <div><a style="color:black;" href="https://www.kidney.org/patients/kidney-community">Join CKD Support Group</a></div><br>
                        <div><a style="color:black;" href="https://www.niddk.nih.gov/health-information/kidney-disease">Explore CKD Articles</a></div><br>
                      </div>""", unsafe_allow_html=True)

    elif disease == "Breast Cancer":
        st.write("Welcome to the Breast Cancer community!")
        st.write("Here you can find forums, support groups, and user-generated content related to breast cancer.")
        st.markdown("""<div style="background-color:#ED8A57; padding: 10px; border-radius: 5px;">
                        <div><a style="color:black;" href="https://www.breastcancer.org/community">Visit Breast Cancer Forums</a></div><br>
                        <div><a style="color:black;" href="https://www.cancer.org/cancer/breast-cancer.html">Join Breast Cancer Support Group</a></div><br>
                        <div><a style="color:black;" href="https://www.nationalbreastcancer.org/breast-cancer-awareness-month">Explore Breast Cancer Articles</a></div><br>
                      </div>""", unsafe_allow_html=True)
        # Main function
def main():
    st.title("Health Community Platform")
    st.write("Welcome to our vibrant health community, where support, connection, and empowerment intersect. Join us as we journey together towards healthier, happier lives!")
    st.image("community.jpg", caption="Community Engagement platform")
    
    # Select disease
    selected_disease = st.selectbox("Select Disease:", [
        "Diabetes", "Heart Disease", "Parkinson's", "Liver Disease",
        "Hepatitis", "Lung Cancer", "Chronic Kidney Disease", "Breast Cancer"
    ])

    # Display communities and forums for selected disease
    show_communities_for_disease(selected_disease)

if __name__ == "__main__":
    main()
