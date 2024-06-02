# JOB SCRAPPER and Insight Recommendation with Gemini AI (Python)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_GITHUB_USERNAME/job_scrapper_project)

#### Video Demo: https://youtu.be/u3xyIUlrb50

## Description

This Python project is a job scraper and insight recommendation tool. It combines web scraping with the power of Gemini AI (Google's generative AI model) to provide you with valuable job information and insights.

### Key Features

1. **Web Scraping with BeautifulSoup:** Extracts job listings from a target website (e.g., fake-jobs website).
2. **Data Fetching with Requests:** Retrieves HTML content from the target URL.
3. **Structured Data Extraction:** Parses job titles, companies, and locations using BeautifulSoup.
4. **Visual Data Display (Pandas):** Presents the extracted job information in a clean, tabular format using Pandas DataFrames.
5. **Gemini AI Integration:** Leveraging Gemini AI to generate insightful recommendations, interview preparation tips, and skill requirement analyses for each job listing.
6. **Clear Output:**  Presents both the job details and the Gemini AI insights in a well-formatted manner.

## How It Works

1. **Specify Search Term:** Input the keyword you want to search for in job titles.
2. **Fetch and Parse:** The script fetches the HTML content of the target job board and parses it to extract job data.
3. **Display Results:** Job listings are displayed in a table, along with summary statistics.
4. **Gemini AI Insights:** For each job, the script sends a prompt to Gemini AI to get insights like practice recommendations, interview preparation, and required job skills.
5. **Output:** The script prints the job details followed by the corresponding insights from Gemini AI.

## Getting Started

### Prerequisites

- Python 3.x
- Required libraries (see `requirements.txt`)

### Installation

1. Clone this repository: `git clone https://github.com/YOUR_GITHUB_USERNAME/job_scrapper_project.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Obtain a Gemini API Key from Google (replace placeholder in the code).

### Usage

1. Run the script: `python project.py`
2. Follow the prompts to enter your desired search term.

## Example

```bash
python project.py
Enter keyword to search job titles: python
```
## Author
Rama Sanjaya | Note : Contributions are welcome! Feel free to open issues or submit pull requests.

