# My Zootopia

A Python application that fetches animal information from an API and generates an HTML website.

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file with your API key:
```
API_KEY=your_api_key_here
```

Get your API key from [API Ninjas](https://api-ninjas.com/).

## Usage

```bash
python animals_web_generator.py
```

Enter an animal name when prompted. The program will generate `animals.html` with the results.

## Project Structure

- `data_fetcher.py` - Fetches animal data from API
- `animals_web_generator.py` - Generates HTML website
- `animals_template.html` - HTML template
- `animals.html` - Generated output file
