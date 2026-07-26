import streamlit as st
from google import genai



# ============================================
# PAGE CONFIGURATION
# ============================================

st.set_page_config(
    page_title="AI Meeting Minutes Generator",
    page_icon="🤖",
    layout="wide"
)


# ============================================
# GEMINI API CONFIGURATION
# ============================================

api_key = st.secrets["GEMINI_API_KEY"]

if not api_key:
    st.error(
        "Gemini API key not found. "
        "Please configure the GEMINI_API_KEY environment variable."
    )
    st.stop()

client = genai.Client(api_key=api_key)


# ============================================
# AI MEETING MINUTES FUNCTION
# ============================================

def generate_meeting_minutes(meeting_notes):

    prompt = f"""
You are a professional AI Meeting Minutes Generator.

Analyze the meeting notes below and generate clear,
professional meeting minutes.

Use EXACTLY the following structure:

# Meeting Minutes

## 1. Meeting Summary

Write a concise summary of the meeting.

## 2. Key Discussion Points

List the main topics discussed.
Use bullet points.

## 3. Important Decisions

List the decisions made during the meeting.
Use bullet points.

If no decisions were mentioned, write:
- Not specified

## 4. Action Items

Create a table with these columns:

| Task | Responsible Person | Deadline |
|---|---|---|

If the responsible person or deadline is not mentioned,
write "Not specified".

## 5. Future Follow-up Items

List tasks or discussions that need to be followed up
in the future.

Use bullet points.

Important rules:

- Do not invent information.
- Only use information from the meeting notes.
- Do not assume missing names or deadlines.
- Keep the language professional.
- Keep the summary concise.
- Make the output easy to read.

Meeting Notes:

{meeting_notes}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# ============================================
# APPLICATION TITLE
# ============================================

st.title("🤖 AI Meeting Minutes Generator")

st.write(
    "Convert raw meeting notes or transcripts into "
    "structured and professional meeting minutes using AI."
)


# ============================================
# INPUT OPTIONS
# ============================================

st.subheader("📝 Enter Meeting Notes")

meeting_notes = st.text_area(
    "Paste your meeting transcript or notes here:",
    height=250,
    placeholder="Paste your meeting notes here..."
)


st.subheader("📁 Or Upload a Text File")

uploaded_file = st.file_uploader(
    "Upload a .txt meeting transcript",
    type=["txt"]
)


# ============================================
# GENERATE BUTTON
# ============================================

if st.button(
    "🚀 Generate Meeting Minutes",
    type="primary"
):

    # ----------------------------------------
    # Get meeting notes
    # ----------------------------------------

    notes = meeting_notes.strip()


    # ----------------------------------------
    # Check uploaded file
    # ----------------------------------------

    if uploaded_file is not None:

        try:

            file_content = uploaded_file.read()

            notes = file_content.decode(
                "utf-8"
            ).strip()

        except Exception as e:

            st.error(
                f"Error reading file: {e}"
            )

            st.stop()


    # ----------------------------------------
    # Check if notes exist
    # ----------------------------------------

    if not notes:

        st.warning(
            "Please paste meeting notes "
            "or upload a .txt file."
        )

    else:

        # ------------------------------------
        # Generate minutes
        # ------------------------------------

        with st.spinner(
            "🤖 Generating meeting minutes..."
        ):

            try:

                minutes = (
                    generate_meeting_minutes(
                        notes
                    )
                )


                # ----------------------------
                # Display result
                # ----------------------------

                st.success(
                    "Meeting minutes generated successfully!"
                )

                st.markdown(
                    minutes
                )


                # ----------------------------
                # Download button
                # ----------------------------

                st.download_button(
                    label="📥 Download Meeting Minutes",
                    data=minutes,
                    file_name="meeting_minutes.txt",
                    mime="text/plain"
                )


            except Exception as e:

                st.error(
                    f"An error occurred: {e}"
                )
