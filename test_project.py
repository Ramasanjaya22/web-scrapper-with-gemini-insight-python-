import pytest
import pandas as pd
from unittest.mock import patch
from bs4 import BeautifulSoup
from project import (fetch_job_postings, extract_job_data, display_results)


# Mock Tests

@pytest.fixture
def sample_html_soup():
    """Loads a sample HTML for testing."""
    # If using 'test_data':
    # with open("tests/test_data/sample_jobs.html", "r") as f:
    #     html = f.read()
    # soup = BeautifulSoup(html, "html.parser")

    # Minimal HTML example for demo
    html = """
    <div id="ResultsContainer">
        <div class="card-content">
            <h2 class="title">Python Engineer</h2>
            <h3 class="company">Acme Corp.</h3>
            <p class="location">Remote</p>
        </div>
        <div class="card-content">
            <h2 class="title">Data Scientist</h2>
            <h3 class="company">Beta Industries</h3>
            <p class="location">New York, NY</p>
        </div>
    </div>
    """
    soup = BeautifulSoup(html, "html.parser")
    return soup


@patch("job_scrapper.requests.get")
def test_fetch_job_postings(mock_get):
    """Tests fetching job postings."""
    # Set up mock response
    mock_get.return_value.content = b"<html>Sample HTML</html>"
    mock_get.return_value.raise_for_status.return_value = None

    html_content = fetch_job_postings("https://some_url.com")
    assert html_content == b"<html>Sample HTML</html>"


def test_extract_job_data(sample_html_soup):
    """Tests extraction of job data."""
    search_term = "python"
    selected_jobs = extract_job_data(sample_html_soup, search_term)
    assert len(selected_jobs) == 1
    assert selected_jobs[0][0] == "python engineer"


def test_display_results_with_data(sample_html_soup):
    """Tests displaying results when jobs are found."""
    search_term = "python"
    selected_jobs = extract_job_data(sample_html_soup, search_term)
    with patch("builtins.print") as mock_print:
        display_results(selected_jobs)
        mock_print.assert_called()


def test_display_results_no_data(sample_html_soup):
    """Tests displaying results when no jobs are found."""
    search_term = "nonexistent"
    selected_jobs = extract_job_data(sample_html_soup, search_term)
    with patch("builtins.print") as mock_print:
        display_results(selected_jobs)
        mock_print.assert_called_with("No jobs found matching.")

#Testing the Gemini component could involve more complex mocking or API testing strategies.
