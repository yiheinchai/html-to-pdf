# HTML to PDF Converter

This project is a Streamlit application that converts HTML content into PDF files using WeasyPrint. It provides a user-friendly interface for inputting HTML and downloading the generated PDF.

## Project Structure

```
html-to-pdf-converter
├── src
│   ├── app.py                # Main entry point of the Streamlit application
│   ├── utils
│   │   └── pdf_converter.py   # Utility functions for PDF conversion
│   └── components
│       └── ui_components.py   # UI components for the Streamlit app
├── templates
│   └── sample.html           # Sample HTML template for testing
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd html-to-pdf-converter
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```
   streamlit run src/app.py
   ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Input your HTML content in the provided text area and click the "Convert to PDF" button.

4. Download the generated PDF file.

## Dependencies

- Streamlit
- WeasyPrint

## License

This project is licensed under the MIT License.