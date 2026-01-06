import streamlit as st
import requests

# 🔗 CHANGE THIS TO YOUR REAL API URL
API_BASE_URL = "https://nvy97is5w6.execute-api.us-east-1.amazonaws.com"

st.title("Notes Application")
st.write("Frontend connected to AWS backend")

st.subheader("Add New Note")

title = st.text_input("Title")
content = st.text_area("Content")

if st.button("Save Note"):
    if title.strip() and content.strip():
        payload = {
            "title": title,
            "content": content
        }

        response = requests.post(
            f"{API_BASE_URL}/notes",
            json=payload
        )

        st.write("Status Code:", response.status_code)
        st.write("Response Text:", response.text)

        if response.status_code in [200, 201]:
            st.success("Note saved successfully")
        else:
            st.error("Failed to save note")
    else:
        st.warning("Please fill in all fields")



if st.button("Load Notes"):
    response = requests.get(f"{API_BASE_URL}/notes")

    if response.status_code == 200:
        notes = response.json()

        if len(notes) == 0:
            st.info("No notes found")
        else:
            for note in notes:
                st.markdown(f"### {note['title']}")
                st.write(note["content"])
                st.divider()
    else:
        st.error("Failed to load notes")
