
# Carbon File Intelligence

## Overview

**Carbon File Intelligence** is a Streamlit-based application designed to facilitate intelligent file processing and analysis. Leveraging Generative AI from Google's `google.generativeai` API and `pypdf`, the application allows users to upload and analyze documents in various formats (e.g., PDF, DOCX) within an interactive, user-friendly interface. Custom styling enhances the experience, providing a visually appealing and responsive design for streamlined document intelligence.

## Features

-   **File Upload and Processing**: Supports PDF and DOCX uploads for analysis.
-   **Generative AI Integration**: Uses Google Generative AI for advanced file insights.
-   **User-Friendly Interface**: Clean, modern UI with interactive buttons and controls.
-   **On-the-Fly Document Processing**: Processes documents instantly upon upload.

## Prerequisites

-   Python 3.8 or higher
-   Required Python packages (see `requirements.txt`)

## Setup

1.  **Clone the Repository**:
    
    bash
    
    Copy code
    
    `git clone https://github.com/yourusername/carbon-file-intelligence.git
    cd carbon-file-intelligence`
    
2.  **Install Dependencies**:
    
    Ensure you have all required dependencies installed. Run the following:
    
    bash
    
    Copy code
    
    `pip install -r requirements.txt` 
    
3.  **API Setup**:
    
    Set up the `google.generativeai` API key. Create an `.env` file in the project root with:
    
    env
    
    Copy code
    
    `GOOGLE_API_KEY=your_google_api_key` 
    
4.  **Run the Application**:
    
    Start the Streamlit app with the following command:
    
    bash
    
    Copy code
    
    `streamlit run cafi.py` 
    

## Usage

1.  **Upload a File**: Drag and drop or upload a PDF or DOCX file.
2.  **Analyze**: The app automatically processes the file and provides analysis results.
3.  **Interact with Results**: Use interactive buttons and selections to navigate insights.

## Customization

-   The CSS in `cafi.py` allows for UI customization.
-   Modify the styling for buttons, text input, and file upload components.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.