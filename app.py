import streamlit as st
import requests

st.title("Project 1")

text=st.text_area("Write your name")
  

if st.button("Submit"):
    if text:
        response=requests.post(url="https://innogajala.app.n8n.cloud/webhook-test/9e6e942a-c581-49c8-bd7f-1dc7d34de034",json={"input":text})

        if response.status_code == 200:
            st.write(response.json()[0]["output"])
else:
    pass
