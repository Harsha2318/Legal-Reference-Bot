import streamlit as st
import requests

st.set_page_config(page_title="Legal Reference Bot", layout="centered")

st.title("⚖️ Legal Reference Bot")
st.write("Instant access to legal statutes, precedents, and summaries using Gemini AI.")

query = st.text_input("Enter your legal query")

if st.button("Search"):
    if not query:
        st.warning("Please enter a query.")
    else:
        with st.spinner("Fetching legal response..."):
            try:
                res = requests.post("http://localhost:8000/search/", json={"query": query})
                if res.status_code == 200:
                    data = res.json()
                    st.success("Legal Information Retrieved!")
                    st.markdown(f"**📜 Statute:** {data['statute']}")
                    st.markdown(f"**⚖️ Precedent:** {data['precedent']}")
                    st.markdown(f"**🧠 Summary:** {data['summary']}")
                else:
                    st.error("Failed to retrieve data. Please try again.")
            except Exception as e:
                st.error(f"Error: {str(e)}")
