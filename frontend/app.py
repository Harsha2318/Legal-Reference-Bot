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
                    
                    # Check if we got an error response
                    if "error" in data:
                        st.error(f"Error: {data['error']}")
                        if "raw_response" in data:
                            st.text("Raw response from API:")
                            st.code(data['raw_response'])
                    else:
                        st.success("Legal Information Retrieved!")
                        
                        # Display each section if available
                        if data.get('statute', '').strip():
                            st.markdown(f"**📜 Statute:** {data['statute']}")
                        if data.get('precedent', '').strip():
                            st.markdown(f"**⚖️ Precedent:** {data['precedent']}")
                        if data.get('summary', '').strip():
                            st.markdown(f"**🧠 Summary:** {data['summary']}")
                        
                        # If no sections were found
                        if not any(data.get(key, '').strip() for key in ['statute', 'precedent', 'summary']):
                            st.warning("No information could be retrieved for this query.")
                else:
                    st.error(f"API returned status code {res.status_code}")
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.text("Please try again with a different query.")
