# Playwright Web Scraping Examples

A small collection of Python scripts demonstrating web automation and scraping with Playwright.  
Two focused examples are included:

- `quickstart.py` — search arXiv and download PDFs
- `passCaptcha.py` — browse via a proxy (example workflow for proxy usage)

---

## Table of contents

- [Prerequisites](#prerequisites)  
- [Install](#install)  
- [Usage](#usage)  
- [Scripts](#scripts)  
    - [`quickstart.py`](#quickstartpy---searching-and-downloading-pdfs)  
    - [`passCaptcha.py`](#passcaptchapy---browsing-with-a-proxy)  
- [Notes](#notes)  
- [Contributing](#contributing)

---

## Prerequisites

- Python 3.7+
- pip

Playwright requires browser binaries (Chromium, Firefox, WebKit) which must be installed after installing the Python package.

---

## Install

Run the following commands:

```bash
pip install playwright
playwright install
```

If you use a virtual environment, activate it first.

---

## Usage

Open a terminal, cd to the repository directory and run one of the scripts:

```bash
# To run the arXiv PDF downloader
python quickstart.py

# To run the proxy browsing example
python passCaptcha.py
```

---

## Scripts

### quickstart.py — Searching and Downloading PDFs

Purpose: Automates searching arXiv and downloading result PDFs.

Workflow:
- Launches a Chromium browser (non-headless by default so you can observe actions).
- Navigates to https://arxiv.org/search.
- Enters a query (for example, "quantum computing") and submits the search.
- Parses the results page to find direct PDF links.
- Creates a `data/` directory (if missing) and downloads each PDF there.
- Takes a screenshot of the final page (`arxiv_search.png`) and closes the browser.

Notes:
- Adjust the search query and selectors as needed for reliability.
- Consider adding polite delays and rate limiting when scraping.

### passCaptcha.py — Browsing with a Proxy

Purpose: Demonstrates configuring Playwright to use a proxy server.

Workflow:
- Configure proxy credentials and server in a dictionary (server, username, password).
- Launches Chromium with proxy settings so traffic is routed through the proxy.
- Navigates to http://walmart.com and performs a simple search (example: "testing").
- Closes the browser.

Notes:
- Use reputable proxy providers and follow their usage terms.
- Proxying may help avoid simple IP blocks but does not guarantee bypassing advanced bot protections or CAPTCHAs.

---
