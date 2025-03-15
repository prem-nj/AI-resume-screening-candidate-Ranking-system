

# AI Resume Screening & Candidate Ranking System

## Overview
This project is a web-based application built using **Streamlit** that automates resume screening and ranks candidates based on their resume's relevance to a provided job description. It leverages natural language processing (NLP) techniques, specifically **TF-IDF (Term Frequency-Inverse Document Frequency)** and **cosine similarity**, to calculate how well each resume matches the job description. The application accepts PDF resumes and outputs a ranked list of candidates with match percentages.

The system is designed to assist recruiters and HR professionals in quickly identifying top candidates from a pool of resumes.

## Features
- **Job Description Input**: Enter a job description via a text area.
- **Resume Upload**: Upload multiple PDF resumes for analysis.
- **Text Extraction**: Extracts text from PDF files using `PyPDF2`.
- **Ranking Algorithm**: Uses TF-IDF vectorization and cosine similarity to rank resumes based on their similarity to the job description.
- **Interactive UI**: Displays results in a sorted table with resume filenames and match percentages using Streamlit.

## Technologies Used
- **Python**: Core programming language.
- **Streamlit**: Framework for building the web application.
- **PyPDF2**: Library for extracting text from PDF files.
- **scikit-learn**: For TF-IDF vectorization and cosine similarity computation.
- **pandas**: For organizing and displaying results in a tabular format.

## Prerequisites
Before running the application, ensure you have the following installed:
- Python 3.8 or higher
- A package manager like `pip`

## Installation
1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install Dependencies**:
   Create a virtual environment (optional but recommended) and install the required packages:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

   If you don’t have a `requirements.txt` file yet, install the dependencies manually:
   ```bash
   pip install pandas PyPDF2 streamlit scikit-learn
   ```

3. **Verify Installation**:
   Ensure all libraries are installed correctly by running:
   ```bash
   python -c "import pandas, PyPDF2, streamlit, sklearn"
   ```

## Usage
1. **Run the Application**:
   Start the Streamlit app by running the following command in your terminal:
   ```bash
   streamlit run app.py
   ```
   Replace `app.py` with the filename of your script if it’s different.

2. **Access the Web Interface**:
   Open your web browser and go to `http://localhost:8501` (or the URL provided by Streamlit).

3. **Steps to Use**:
   - Enter the job description in the provided text area.
   - Upload one or more PDF resumes using the file uploader.
   - View the ranked list of resumes with their match percentages under the "Ranking Resumes" section.

## Code Structure
- **Text Extraction**: The `extract_text_from_pdf()` function uses `PyPDF2` to extract text from uploaded PDF resumes.
- **Ranking Logic**: The `rank_resumes()` function computes TF-IDF vectors and cosine similarity scores between the job description and resumes.
- **Streamlit UI**: The main app logic handles user input, file uploads, and result display.

## Example Output
For a job description like "Python developer with experience in machine learning and web development," and three uploaded resumes:
- `resume1.pdf`: 85.23%
- `resume2.pdf`: 67.89%
- `resume3.pdf`: 45.12%

The results will be displayed in a table sorted by match percentage in descending order.
## Screenshots

### 1. Uploading Resumes  
![image](https://github.com/user-attachments/assets/1e5878af-fe03-427d-a5ec-7c747671335a)


### 2. Ranking Results  
![image](https://github.com/user-attachments/assets/2e592887-1ae0-40cc-a025-fe7401f939bb)


## Limitations
- Only supports PDF files for resume uploads.
- Accuracy depends on the quality of text extraction from PDFs (e.g., scanned PDFs may not work well).
- Simple TF-IDF and cosine similarity may not capture semantic meaning as effectively as advanced NLP models (e.g., BERT).

## Future Improvements
- Add support for other file formats (e.g., DOCX).
- Integrate more advanced NLP models for better matching.
- Include a feature to export results as a CSV file.
- Enhance the UI with visualizations (e.g., bar charts of match percentages).

## Troubleshooting
- **PDF Text Extraction Issues**: Ensure PDFs are text-based, not image-based. Use OCR tools if necessary before uploading.
- **Module Not Found**: Verify all dependencies are installed (`pip list`).
- **Streamlit Not Running**: Check if port 8501 is available or specify a different port with `streamlit run app.py --server.port 8502`.

## Contributing
Feel free to fork this repository, submit issues, or create pull requests with enhancements. Contributions are welcome!

## License
This project is open-source and available under the [MIT License](LICENSE).

## Contact
For questions or feedback, reach out to premjadhav21314@gmail.com or open an issue on the repository.

---

### Notes for You
- Save this content in a file named `README.md` in your project directory.
- Replace `<repository-url>` and `<repository-folder>` with your actual Git repository details if you’re hosting it online.
- Update the "Contact" section with your actual email or preferred contact method.
- If you haven’t created a `requirements.txt` yet, you can generate one by running:
  ```bash
  pip freeze > requirements.txt
  ```
  after installing the dependencies.
