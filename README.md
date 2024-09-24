# Youtube to MP3 Converter API

## Project Description
The YouTube to MP3 Converter API is a RESTful web service that allows users to convert and download audio from YouTube videos in MP3 format. Designed for simplicity and efficiency, this API enables seamless integration into various applications, providing a user-friendly interface for accessing YouTube's extensive library of audio content.

### Key Features:
Audio Extraction: Extracts high-quality audio from YouTube videos, supporting various audio formats with an emphasis on MP3.

Search Functionality: Users can search for videos by title, retrieving relevant video information including titles, URLs, and IDs.

Error Handling: Implements robust error handling and logging to ensure reliable operation, even when encountering unexpected issues.

Cache Management: Efficiently manages temporary files to optimize storage and performance.

### Technical Stack:
Backend Framework: Flask (Python) for building the API endpoints.

Video Downloading: Utilizes the yt-dlp library for fetching video content and extracting audio.

Data Handling: JSON for structured data exchange between the client and the API.

Error Logging: Implements error logging for tracking issues during audio extraction and downloading processes.

### Use Cases:
Media Applications: This API is for the integration into the Vyber companion music application.

## Dependencies
To install Dependencies, run the command:
$ pip install -r requirements.txt

## Resources

### Postman Collection
https://documenter.getpostman.com/view/30202529/2sAXqv6gMU
