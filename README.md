# 🤖 AI Meeting Minutes Generator

An AI-powered Meeting Minutes Generator that converts raw meeting notes or meeting transcripts into structured and professional meeting minutes using Google Gemini AI.

## 🚀 Features

* Generate meeting summaries
* Extract key discussion points
* Identify important decisions
* Extract action items
* Identify responsible people
* Identify deadlines
* Generate future follow-up items
* Paste meeting notes directly
* Upload `.txt` meeting transcripts
* Download generated meeting minutes

## 🛠️ Technologies Used

* Python
* Google Colab
* Google Gemini API
* Google GenAI SDK
* IPyWidgets

## 🧠 How It Works

The user provides meeting notes by either:

1. Pasting the meeting transcript
2. Uploading a `.txt` meeting transcript

The Gemini AI model processes the meeting content and extracts important information.

The system generates structured meeting minutes containing:

* Meeting Summary
* Key Discussion Points
* Important Decisions
* Action Items
* Responsible Persons
* Deadlines
* Future Follow-up Items

## 📂 Project Structure

```text
AI-Meeting-Minutes-Generator/
│
├── AI_Meeting_Minutes_Generator.ipynb
├── requirements.txt
└── README.md
```

## 🔑 API Key Setup

This project uses the Google Gemini API.

For security reasons, the Gemini API key should **never be directly written in the source code or uploaded to GitHub**.

In Google Colab, add your API key to **Colab Secrets** using the following name:

```text
GEMINI_API_KEY
```

The application retrieves the API key securely using:

```python
from google.colab import userdata

api_key = userdata.get("GEMINI_API_KEY")
```

## 📦 Installation

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

The required packages are:

```text
google-genai
ipywidgets
```

## ▶️ How to Run

1. Clone or download this repository.
2. Open `AI_Meeting_Minutes_Generator.ipynb` in Google Colab.
3. Install the required dependencies.
4. Add your Gemini API key to Google Colab Secrets.
5. Make sure the secret is named `GEMINI_API_KEY`.
6. Run the notebook cells in order.
7. Paste meeting notes or upload a `.txt` meeting transcript.
8. Click **Generate Meeting Minutes**.
9. Review the generated meeting minutes.
10. Click **Download Minutes** to save the results.

## 📋 Example Output

The AI generates meeting minutes with the following structure:

### Meeting Summary

A concise summary of the meeting.

### Key Discussion Points

* Main topic discussed
* Important issues raised
* Topics requiring further discussion

### Important Decisions

* Decision made by the team
* Technology or strategy selected

### Action Items

| Task                   | Responsible Person | Deadline  |
| ---------------------- | ------------------ | --------- |
| Prepare project design | Sarah              | Wednesday |
| Develop backend API    | David              | Friday    |

### Future Follow-up Items

* Review project progress
* Begin testing
* Discuss pending tasks in the next meeting

## 🔒 Security

Never upload your Gemini API key to GitHub.

Do not include API keys directly in Python code, notebooks, or public repositories.

Use Google Colab Secrets to securely store your API key.

## 🚧 Project Status

**Current Version:** Prototype / MVP

The current version supports meeting note processing through pasted text and `.txt` file uploads.

## 🔮 Future Improvements

* PDF file upload
* Microsoft Word (`.docx`) file upload
* PDF export
* Word document export
* Professional Streamlit web interface
* Database for storing meeting minutes
* Meeting history
* User authentication
* Search previous meetings
* Calendar integration
* Email meeting minutes
* Audio-to-text meeting transcription

## 👨‍💻 Author

Maseera Begum

Developed as an AI Agent project demonstrating AI-powered summarization and information extraction.
