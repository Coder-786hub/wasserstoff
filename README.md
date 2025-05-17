# Gemini-Powered Document Research Chatbot

A powerful document research assistant that leverages Google's Gemini API to analyze and extract insights from uploaded documents. This application allows users to upload documents, query them using natural language, and receive detailed responses with relevant citations.

## Features

- 📄 Document Upload: Support for various document formats
- 🔍 Smart Querying: Ask questions about your documents using natural language
- 🤖 Gemini AI Integration: Powered by Google's advanced Gemini API
- 📚 Theme Identification: Automatically identify key themes and topics
- 📝 Citation Support: Get responses with proper citations from source documents
- 💡 Intelligent Analysis: Deep understanding of document context and content

## Prerequisites

- Python 3.8 or higher
- Google Cloud account with Gemini API access
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd [repository-name]
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
```bash
cp .env.example .env
```
Edit the `.env` file and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your web browser and navigate to `http://localhost:5000`

3. Upload your documents through the web interface

4. Use the chat interface to ask questions about your documents

## API Documentation

The application provides the following main endpoints:

- `POST /upload`: Upload documents
- `POST /query`: Submit queries about documents
- `GET /themes`: Retrieve identified themes
- `GET /documents`: List uploaded documents

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google Gemini API for providing the AI capabilities
- All contributors who have helped shape this project

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.