
import streamlit as st
import pandas as pd
import qrcode
from PIL import Image
import io

# Virgin Atlantic Colors
PRIMARY_COLOR = "#8C1D40"  # Virgin Red
SECONDARY_COLOR = "#F2F2F2"  # Light Gray
ACCENT_COLOR = "#FFD100"  # Gold Accent

st.set_page_config(page_title="Aircraft Cabin Materials", layout="wide")

# Custom CSS for enhanced UI
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {SECONDARY_COLOR};
        font-family: 'Arial', sans-serif;
    }}
    .stButton>button {{
        background-color: {PRIMARY_COLOR};
        color: white;
        border-radius: 5px;
        padding: 0.5em 1em;
    }}
    .stDataFrame, table {{
        border: 2px solid {PRIMARY_COLOR};
        border-radius: 5px;
    }}
    .stSelectbox>div>div>select {{
        background-color: white;
        color: black;
    }}
    h1, h2, h3, h4, h5 {{
        color: {PRIMARY_COLOR};
    }}
    </style>
""", unsafe_allow_html=True)

st.title("✈ Aircraft Cabin Materials Tracker")
st.markdown("Explore materials, certifications, and lifecycle guidance with enhanced UI.")

# Load data
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "cabin_materials.csv")
data = pd.read_csv(csv_path)

# Material selection
material = st.selectbox("Select a Material", data['material'])
details = data[data['material'] == material].iloc[0]

# Display details in a clean table
st.subheader("Material Details")
st.table({
    "Property": ["Composition", "Certifications", "Repair/Refurb History", "End-of-Life Guidance"],
    "Value": [details['composition'], details['certifications'], details['repair_history'], details['end_of_life']]
})

# QR Code generation
st.subheader("Generate QR Code")
url = st.text_input("Enter URL for QR Code", "https://looptrack-8rq9q9ysgzkvfmcbuugwyz.streamlit.app/")
if url:
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buf = io.BytesIO()
    img.save(buf)
    st.image(buf, width=200)
