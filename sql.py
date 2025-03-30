import streamlit as st
import requests

# API configuration
API_KEY = "BarPXqJuGUDBiQxtXz8q9jJ7qNvMjUZX"
API_ENDPOINT = "https://api.mistral.ai/v1/chat/completions"

# Static context for SQL generation
static_context = """
Generate an SQL query based on a natural language description. The response should include:
1. The SQL query.
2. An explanation of the query.
3. Possible optimizations for better performance.
"""

def call_mistral_api(prompt):
    """Calls the Mistral API's chat completions endpoint with the given prompt."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "open-mixtral-8x22b",  # Replace with the desired model ID
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        response = requests.post(API_ENDPOINT, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result.get("choices", [])[0].get("message", {}).get("content", "")
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
    except (IndexError, KeyError) as e:
        return f"Unexpected response format: {e}"

def main():
    """Main function to run the Streamlit app."""
    st.markdown(
        """
        <h1 style='text-align: center;'>SQL Query Generator & Debugger</h1>
        <h3 style='text-align: center; font-weight: normal;'>Generate SQL Queries with Explanations and Optimizations</h3>
        """,
        unsafe_allow_html=True
    )

    # Input section
    st.markdown("---")
    st.header("Enter Your Query Description")
    query_description = st.text_area("Enter a description of the SQL query:", placeholder="e.g., Find the top 5 highest-paid employees in a company")

    # Button to Generate SQL Query
    if st.button("Generate SQL Query"):
        if not API_KEY or not API_ENDPOINT:
            st.error("API key or endpoint is missing. Please check your configuration.")
            return
        
        # Create prompt
        prompt = (
            f"{static_context}\n\n"
            "User Inputs:\n"
            f"Description: {query_description}\n"
        )
        
        # Call API and display response
        output = call_mistral_api(prompt)
        st.write(output)

# Run the main function
if __name__ == "__main__":
    main()
