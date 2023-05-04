# search-gpt
Examples using available GPT tools and APIs to search and summarize the web


## Description

`search-gpt` is a Python script that uses the OpenAI API to summarize web pages. The script extracts relevant content from a web page and passes it to the OpenAI API to summarize. The script runs in the command line and requires an OpenAI API key.

## Requirements

- Python 3 (not included in this guide)
- pip (included with Python 3)
- OpenAI API key (get one [here](https://beta.openai.com/signup/))

## Installation
First download or clone this repo.

1. Install Python 3 if not already installed on your machine.
2. Open a terminal window.
3. Install the required packages by running the following command:

```
pip install -r requirements.txt
```

4. Set your OpenAI API key as an environment variable by running the following command in the terminal:

```
export OPENAI_API_KEY=<your-api-key>
```

   Replace `<your-api-key>` with your actual OpenAI API key.

## Usage

Run the following command to start the script:

```
python search-gpt.py
```

The script will prompt you to enter a URL to summarize.

You can also provide the URL as the first argument to the script

```
python search-gpt.py https://example-site
```


## Limitations
This is proof of concept code and should be treated as such.  It is tested on Mac OS so you may need to tweak to run elsewhere.
