import streamlit as st
import pandas as pd
import numpy as np
import io
import re

st.set_page_config(page_title="Product(Shirts) Enrichment Tool")
st.title("Shirts Enrichment Tool")
st.markdown("""
Upload your Excel file with the Shirts articles. This tool will automatically enrich fields based on material percentage patterns
and provide a downloadable Excel file with the completed data.
""")

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

def enrich_data(df):
    df = df.copy()
    
    # Create the new enriched column based on conditions
    df["Product type shirts"] = df.apply(lambda row: (
        "Short Sleeve Shirts" if (
            pd.isna(row.get("Bullet3"))
            and any(int(n) >= 70 for n in re.findall(r'(\d+)%\s*polyester', str(row.get("Name", "")).lower()))) else
        "T Shirts" if (
            pd.isna(row.get("Bullet3"))
            and any(int(n) >= 70 for n in re.findall(r'(\d+)%\s*cotton', str(row.get("Name", "")).lower()))) else
        "Short Sleeve Shirts;T Shirts" if (
            pd.isna(row.get("Bullet3"))
            and re.search(r'50%\s*polyester', str(row.get("Name", "")).lower())
            and re.search(r'50%\s*cotton', str(row.get("Name", "")).lower())) else
        "Can't analize"
    ), axis=1)
    
    return df

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        enriched_df = enrich_data(df)

        # Show preview
        st.success("File processed successfully! Here's a preview:")
        st.dataframe(enriched_df.head())

        # Convert to Excel for download
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            enriched_df.to_excel(writer, index=False)
        
        st.download_button(
            label="📥 Download Enriched Excel",
            data=output.getvalue(),
            file_name="enriched_products.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    except Exception as e:
        st.error(f"There was an error processing the file: {e}")




