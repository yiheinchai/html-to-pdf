from flask import Flask, request, send_file
import streamlit as st
from utils.pdf_converter import convert_html_to_pdf

def main():
    st.title("HTML to PDF Converter")
    
    html_content = st.text_area("Enter HTML content:")
    
    if st.button("Convert to PDF"):
        if html_content:
            pdf_file_path = convert_html_to_pdf(html_content)
            st.success("PDF generated successfully!")
            st.download_button("Download PDF", pdf_file_path, file_name="converted.pdf")
        else:
            st.error("Please enter some HTML content.")

if __name__ == "__main__":
    main()