import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-2.0-flash")
except Exception as e:
    print(f"Error configuring Gemini: {str(e)}")
    raise

def get_legal_response(query: str) -> dict:
    try:
        prompt = f"""
        You are a legal assistant bot. For the following query, provide a structured response with three sections:
        
        1. Statute: Provide the most relevant Indian statute or section that applies to this query.
        2. Precedent: Provide a relevant case law precedent, or state if no specific precedent exists.
        3. Summary: Provide a concise summary of the legal implications.
        
        Format your response with clear section headers:
        📜 Statute: [Your statute here]
        ⚖️ Precedent: [Your precedent here]
        🧠 Summary: [Your summary here]
        
        Query: "{query}"
        """
        
        response = model.generate_content(prompt)
        return parse_response(response.text)
    except Exception as e:
        print(f"Error getting legal response: {str(e)}")
        return {"error": str(e)}

def parse_response(text: str) -> dict:
    try:
        result = {
            "statute": "",
            "precedent": "",
            "summary": "",
        }
        
        # Split the text into sections
        sections = text.split("\n\n")
        
        for section in sections:
            if "statute" in section.lower():
                result["statute"] = section.split("Statute:")[1].strip()
            elif "precedent" in section.lower():
                result["precedent"] = section.split("Precedent:")[1].strip()
            elif "summary" in section.lower():
                result["summary"] = section.split("Summary:")[1].strip()
        
        # If any section is empty, return a default message
        for key in result:
            if not result[key].strip():
                result[key] = "Not available"
        
        return result
    except Exception as e:
        print(f"Error parsing response: {str(e)}")
        print(f"Response text: {text}")
        return {"error": str(e), "raw_response": text}
