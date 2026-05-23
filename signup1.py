def login_user(username, password):
    conn = sqlite3.connect("auth.db")
    c = conn.cursor()
    c.execute("SELECT password_hash FROM users WHERE username=?", (username,))
    data = c.fetchone()
    conn.close()

    if data:
        return data[0] == hash_password(password)
    return False

st.subheader("Login")

user = st.text_input("Username")
pwd = st.text_input("Password", type="password")

if st.button("Login"):
    if login_user(user, pwd):
        st.success("Login successful ✅")
        st.session_state["logged_in"] = True
        st.session_state["username"] = user
    else:
        st.error("Invalid username or password ❌")
