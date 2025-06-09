import streamlit as st
import openai

# Set your API key
openai.api_key = "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"  # ← paste your actual API key here

st.set_page_config(page_title="PluggedIn AI", layout="centered")

st.title("🎧 PluggedIn AI: Music Marketing Assistant")
st.markdown("Craft smarter rollouts and content with AI. Built for independent artists.")

artist_name = st.text_input("Artist Name")
release_type = st.selectbox("Type of Release", ["Single", "EP", "Album", "Music Video"])
mood = st.text_input("Mood / Vibe of the Release (e.g. heartbreak, summer turn-up, introspective)")

if st.button("Generate Plan"):
    if artist_name and release_type and mood:
        with st.spinner("Thinking..."):
            prompt = (
                f"You're a music marketing expert. Create a social media rollout plan for a {release_type.lower()} "
                f"by an artist named {artist_name}. The vibe is '{mood}'. Include 3 Instagram captions, "
                f"a 1-week rollout schedule, and 2 content ideas."
            )
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.8,
                    max_tokens=700,
                )
                output = response.choices[0].message.content
                st.markdown("### 🔥 AI-Powered Rollout Plan")
                st.markdown(output)
            except Exception as e:
                st.error(f"Something went wrong: {e}")
    else:
        st.warning("Please fill in all fields.")
