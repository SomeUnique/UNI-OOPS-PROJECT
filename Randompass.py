import streamlit as st
import random
import string

# Password generator function
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure minimum security
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest of the password
    password += random.choices(characters, k=length - len(password))
    random.shuffle(password)

    return ''.join(password)

# Streamlit App
st.title("🔐 Simple Password Generator")

st.write("Generate a strong and secure password with custom length.")

# Slider to select length
password_length = st.slider("Select password length", min_value=8, max_value=32, value=12)

# Generate button
if st.button("Generate Password"):
    new_password = generate_password(password_length)
    st.success(f"Your password: `{new_password}`")

    # Optional: Copy to clipboard (Streamlit does not have built-in clipboard support)
    st.write("✅ Copy the password manually or use a password manager.")
