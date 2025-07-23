import streamlit as st
from PIL import Image

def main():
    st.title("Nutritional and Diet Plans")

    # Info about the chatbot
    st.write("DietNutriBot is your personal nutrition assistant, providing tailored diet plans and nutritional guidance for various health conditions. Whether you're managing diabetes, heart disease, or other health concerns, DietNutiBot offers expert advice to help you achieve your health goals.")

    # Image
    image = Image.open("bot.jpg")  # Replace "your_image.jpg" with the path to your downloaded image
    st.image(image, caption="DietNutriBot")

    # Style for the link
    link_style = (
        "text-decoration: none; "
        "color: #2e2e2e; "  # Dark gray
        "display: inline-block; "
        "padding: 10px 20px; "
        "background-color: #ED8A57; "  # Light orange
        "border-radius: 5px; "
    )

    # Redirect to chatbot page
    st.markdown(
        f'<div style="text-align:center;"><a href="https://www.chatbase.co/chatbot-iframe/wGzL6fanM3K-JJGpxuICB" style="{link_style}" target="_blank">Click here to chat with DietNutiBot</a></div>',
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
