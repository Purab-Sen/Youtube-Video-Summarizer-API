
# RAG Server API

A retrieval-augmented generation (RAG) API server that summarizes YouTube videos using their transcripts.

## Features

- Fetch YouTube video transcripts by video ID
- Generate concise summaries using RAG techniques
- RESTful API endpoints for easy integration

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### API Endpoint

```bash
GET /search?video_id="xyz"&question="question about video"
```

### Response

```json
{
    "message": "Concise summary of the video content...",
}
```

## Requirements

- Python 3.8+
- YouTube Transcript API
- LangChain or similar RAG framework

## Configuration

Set environment variables in `.env`:

```
GEMINI_API_KEY="KEY"
```

## Running the Server

```bash
python main.py
```

Server runs on `http://localhost:5000`

