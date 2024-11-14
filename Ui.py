import streamlit as st
import requests

# Add CSS for shimmer effect
st.markdown(
    """
    <style>
    .shimmer {
        display: inline-block;
        height: 20px;
        width: 100%;
        background: linear-gradient(to right, #f0f0f0 8%, #e0e0e0 18%, #f0f0f0 33%);
        background-size: 200% 100%;
        animation: shimmer 1.5s infinite;
    }
@keyframes shimmer {
        0% {
            background-position: -200% 0;
        }
        100% {
            background-position: 200% 0;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)
def main():
    st.title("How May I Help You ? ")

    # Input box for user to enter data
    user_input = st.text_input("Enter your prompt:")

    # Submit button
    if st.button("Submit"):
        url = "http://127.0.0.1:8000/completion"
        payload = {"input_text": user_input}

        placeholder = st.empty()
        placeholder.markdown('''<div class="shimmer"></div>
                            <div class="shimmer"></div>
                              <div class="shimmer"></div>
                              ''', unsafe_allow_html=True)

        response = requests.post(url, json=payload, stream=True)
        if response.status_code == 200:
            response_text = ""
            for line in response.iter_content():
                if line:
                    words = line.decode('utf-8')
                    response_text += words
                    placeholder.markdown(f"<div>{response_text}</div>", unsafe_allow_html=True)
        else:
            st.error("Failed to submit data.")

if __name__ == '__main__':
    main()
