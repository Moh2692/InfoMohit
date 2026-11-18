# Mohit Bhartiya — interactive resume

A single-deployment Python resume website built with Streamlit. The profile,
interactive experience and skills filters, contact details, and JSON download
all run inside one Streamlit app. No separate frontend or backend service is
required.

## Deploy to Streamlit Community Cloud

1. Push this project to a GitHub repository.
2. In [Streamlit Community Cloud](https://share.streamlit.io/), create an app
   and select that repository and branch.
3. Set the app's main file path to `app.py` and deploy.

Keep `app.py`, `resume_data.py`, and `requirements.txt` in the selected app's
repository directory. Streamlit Cloud installs the dependencies from
`requirements.txt` and runs the Streamlit app. The site does not provide
FastAPI/REST endpoints.

## Run locally

Python 3.10 or newer is recommended.

```bash
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
streamlit run app.py
```

The local website opens at <http://localhost:8501>.
