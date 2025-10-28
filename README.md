# Data Scraping Project

This repository contains example scripts to scrape data from two different websites and save the results in structured formats (CSV and JSON). It is an instructional project that demonstrates how to gather, clean, and persist web data while following respectful scraping practices.

## Project Overview

- Target: scrape useful data from two distinct websites (each site has its own scraper module).
- Goal: extract defined fields from each site, normalize and clean the data, and export to CSV/JSON for further analysis.
- Structure: modular scrapers (one per site), shared data-cleaning utilities, and an output module.

## Features

- One scraper per website for separation of concerns.
- Configurable rate limiting and polite request behavior (delays between requests).
- Basic error handling and logging to track progress and failures.
- Exports to CSV and JSON for easy consumption by other tools.

## Tech Stack

- Python 3.8+
- requests (HTTP)
- beautifulsoup4 (HTML parsing)
- pandas (data manipulation and export)
- Optional: tqdm for progress display, python-dotenv for configuration

## Ethics and Legal

- Always check the target website's Terms of Service and robots.txt before scraping.
- Respect rate limits and avoid overloading the site. Use exponential backoff when appropriate.
- Do not collect or store sensitive personal data without explicit permission.

## Contribution

Contributions are welcome. If you'd like to improve the scrapers, add tests, or expand export formats, please open an issue or submit a pull request describing your changes.


---

## 🧑‍💻 Author

**Wissem Benkhaled**

💌 **Email:** [wissembenkhaled85@gmail.com](mailto:wissembenkhaled85@gmail.com)  
💼 **LinkedIn:** [linkedin.com/in/wissem-benkhaled](https://www.linkedin.com/in/wissem-benkhaled/)  
🐙 **GitHub:** [github.com/Wissem-Benkhaled](https://github.com/Wissem-Benkhaled)  
🌐 **Portfolio:** [wissembenkhaled.netlify.app](https://wissembenkhaled.netlify.app/)

---
