def convert_html_to_pdf(html_content, output_file):
    from weasyprint import HTML

    # Convert HTML to PDF
    HTML(string=html_content).write_pdf(output_file)