import streamlit as st
import tempfile
import os
from weasyprint import HTML
from io import BytesIO

def convert_html_to_pdf(html_content):
    """Convert HTML content to PDF using WeasyPrint"""
    try:
        html_doc = HTML(string=html_content)
        pdf_bytes = html_doc.write_pdf()
        return pdf_bytes
    except Exception as e:
        st.error(f"Error converting HTML to PDF: {str(e)}")
        return None

def main():
    st.title("HTML to PDF Converter")
    st.markdown("Convert your HTML content to PDF and download it!")
    
    # HTML input methods
    input_method = st.radio(
        "Choose input method:",
        ["Text Area", "File Upload"]
    )
    
    html_content = ""
    
    if input_method == "Text Area":
        html_content = st.text_area(
            "Enter your HTML content:",
            height=300,
            placeholder="<html><body><h1>Hello World!</h1></body></html>"
        )
    else:
        uploaded_file = st.file_uploader(
            "Upload HTML file",
            type=['html', 'htm'],
            accept_multiple_files=False
        )
        if uploaded_file is not None:
            html_content = uploaded_file.read().decode('utf-8')
            st.text_area("HTML Content Preview:", html_content, height=200, disabled=True)
    
    if html_content:
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Convert to PDF", type="primary"):
                with st.spinner("Converting HTML to PDF..."):
                    pdf_bytes = convert_html_to_pdf(html_content)
                    
                    if pdf_bytes:
                        st.success("PDF generated successfully!")
                        
                        # Download button
                        st.download_button(
                            label="Download PDF",
                            data=pdf_bytes,
                            file_name="converted_document.pdf",
                            mime="application/pdf"
                        )
        
        with col2:
            if st.button("Preview HTML"):
                st.components.v1.html(html_content, height=400, scrolling=True)

if __name__ == "__main__":
    main()