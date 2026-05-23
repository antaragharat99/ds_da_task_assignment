import streamlit as st
import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_user(username, password):
    conn = sqlite3.connect("auth.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
                  (username, hash_password(password)))
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()

st.subheader("Signup")

new_user = st.text_input("Create Username")
new_pass = st.text_input("Create Password", type="password")

if st.button("Signup"):
    if new_user and new_pass:
        ok = create_user(new_user, new_pass)
        if ok:
            st.success("Account created! Now login.")
        else:
            st.error("Username already exists!")
    else:
        st.warning("Please fill all fields.")
