"""
Application Software Engineering Student
Name: Rama Sanjaya
From: Bandung City, Indonesia
linkedin: https://www.linkedin.com/in/rama-sanjaya22/
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from gemini import initialize_gemini_model,generate_gemini_response

def fetch_job_postings(url):
    """Fetches the raw HTML content of a job postings webpage."""
    response = requests.get(url)
    response.raise_for_status()
    return response.content


def extract_job_data(soup, search_term):
    """Extracts job data (title, company, location) from the HTML content based on a search term."""
    results = soup.find(id="ResultsContainer")
    job_elements = results.find_all("div", class_="card-content")

    selected_jobs = []
    for job_element in job_elements:
        title = job_element.find("h2", class_="title").text.strip().lower()
        if search_term in title:
            company = job_element.find("h3", class_="company").text.strip()
            location = job_element.find("p", class_="location").text.strip()
            selected_jobs.append([title, company, location])

    return selected_jobs


def display_results(selected_jobs):
    """Displays job data in a DataFrame and provides summary statistics."""
    if selected_jobs:
        df = pd.DataFrame(selected_jobs, columns=["Title", "Company", "Location"])
        print(df)
        print("\nJob posting statistics:\n")
        print(df["Title"].describe())
    else:
        print(f"No jobs found matching.")


def main():
    """Orchestrates the job search process."""
    url = "https://realpython.github.io/fake-jobs/"
    html_content = fetch_job_postings(url)
    soup = BeautifulSoup(html_content, "html.parser")
    search_term = input("Enter keyword to search job titles: ").lower()
    selected_jobs = extract_job_data(soup, search_term)
    display_results(selected_jobs)

    #gemini
    api_key = "your api key" #get your api key from here https://aistudio.google.com/app/apikey
    chat_session = initialize_gemini_model(api_key)

    if selected_jobs:
    # Loop over each job data individually
        for job in selected_jobs:
            job_title, company, location = job
            # Build the prompt string for Gemini (focused on the individual job)
            prompt = (
                f"Please analyze the following job posting found for the keyword '{search_term}':\n\n"
                f"- Job Title: {job_title}\n"
                f"- Company: {company}\n"
                f"- Location: {location}\n\n"
                "make a insight schedule, practice recommendation, job skill requirement"
            )
            # Get the summary from Gemini
            summary = generate_gemini_response(chat_session, prompt)
            # Print the plain text output
            print("Title:", job_title)
            print("Company:", company)
            print("Location:", location)
            print("Insights:", summary)
            print("--------------------")  # Separator between jobs


if __name__ == "__main__":
    main()
