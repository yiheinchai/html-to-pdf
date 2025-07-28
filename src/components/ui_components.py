def render_html_input():
    import streamlit as st

    st.title("HTML to PDF Converter")
    html_content = st.text_area("Enter your HTML content here:", height=300)
    return html_content

def render_convert_button():
    import streamlit as st

    if st.button("Convert to PDF"):
        return True
    return False

def render_download_link(pdf_file):
    import streamlit as st

    st.download_button(
        label="Download PDF",
        data=pdf_file,
        file_name="converted.pdf",
        mime="application/pdf"
    )