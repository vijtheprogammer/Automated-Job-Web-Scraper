# Automated Job Web Scraper

This Python script scrapes job listings from TimesJobs and filters out jobs that require skills you're not familiar with. The filtered job data is saved into an Excel file for easy review.

## Features

- **Skill Filtering**: Excludes job postings that require a specific skill you're not familiar with.
- **Data Extraction**: Retrieves company names, required skills, published dates, and more information links.
- **Scheduled Scraping**: Continuously scrapes data for a set duration (10 minutes) with pauses (30 seconds) between runs.
- **Logging**: Logs the scraping process and errors to a file.
- **Excel Export**: Saves the filtered job data into an Excel file (`jobs.xlsx`).

## Dependencies

- `logging` - For logging information and errors.
- `beautifulsoup4` - For parsing HTML.
- `requests` - For making HTTP requests.
- `pandas` - For data manipulation and exporting to Excel.
- `lxml` - XML and HTML parser for BeautifulSoup.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/job-scraper.git
    cd job-scraper
    ```

2. **Install the required dependencies**:

    ```bash
    pip install beautifulsoup4 requests pandas lxml
    ```

## Usage

1. **Run the script**:

    ```bash
    python job_scraper.py
    ```

2. **Input a skill**: When prompted, enter a skill you are not familiar with. The script will filter out job postings requiring that skill.

3. **Check the results**: The filtered job data will be saved to `jobs.xlsx`.

## Logging

Logs are written to `scraper.log` and include:
- Start and end times of the script
- Information about each scraping cycle
- Any errors or exceptions encountered

## Contact

For any questions or comments, please contact [aryan.vij@gmail.com](mailto:aryan.vij@gmail.com).
