import streamlit as st
import re
import random
import string

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Lowercase and Uppercase Check
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Use both uppercase and lowercase letters.")
    
    # Number Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number.")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Use at least one special character (!@#$%^&* etc.).")
    
    return score, feedback

def generate_strong_password(length):
    if length < 8:
        return "Password length should be at least 8 characters."
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    st.title("🔒 Password Strength Meter")
    
    st.write("### Enter your password below to check its strength")
    
    password = st.text_input("Enter your password:", type="password")
    
    if st.button("Check Strength"):
        if password:
            score, feedback = check_password_strength(password)
            
            # Strength Messages
            if score == 4:
                st.success("✅ Strong Password!")
            elif score == 3:
                st.warning("⚠️ Moderate Password. Improve it by following suggestions below.")
            else:
                st.error("❌ Weak Password. Follow the suggestions below to strengthen it.")
            
            # Display Feedback
            if feedback:
                st.write("### Suggestions to Improve:")
                for tip in feedback:
                    st.write(f"- {tip}")
    
    st.write("### Choose Password Length")
    length = st.number_input("Enter desired password length:", min_value=8, step=1)
    
    if st.button("Generate Strong Password"):
        strong_password = generate_strong_password(int(length))
        st.write("### Suggested Strong Password:")
        st.code(strong_password)

if __name__ == "__main__":
    main()
