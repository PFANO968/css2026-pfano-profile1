import streamlit as st

# Set page title
st.set_page_config(page_title="Researcher Profile", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Contact"],
)

# Sections based on menu selection
if menu == "Researcher Profile":
    st.title("Researcher Profile")
    st.sidebar.header("Profile Options")

    # Collect basic information
    name = "Miss Tshiovhe pfano"
    field = "Cyber security analyst "
    institution = "University of Limpopo"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")
    
    st.image(
        "https://www.ul.ac.za/wp-content/uploads/2023/10/university-of-limpopo-logo.png",
        caption="University of Limpopo Logo"
    )
elif menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    email = "Tshiovhepfano615@gmail.com"
    cellphone = "0793696741"
    st.write(f"You can reach me at {email}.")
    st.write(f"Cellphone: {cellphone}")