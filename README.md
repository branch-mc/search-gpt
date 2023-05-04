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

## Usage: search-gpt.py 

Run the following command to start the script:

```
python search-gpt.py
```

The script will prompt you to enter a URL to summarize.

You can also provide the URL as the first argument to the script

```
python search-gpt.py https://example-site
```

Example output

```
% python search-gpt.py http://github.com

== http://github.com
== GitHub: Let’s build from here · GitHub
Key points:

- Explore the platform built for productivity, collaboration, and security that developers love.
- Trusted by leading organizations worldwide.
- Productivity is accelerated through tools that boost developer velocity.
- GitHub Copilot is an AI pair programmer that completes tasks 55% faster using natural language prompts.
- GitHub Actions automates build, test, and deployment workflow with secure CI/CD.
- GitHub Mobile lets you access your projects from anywhere.
- Collaboration is supercharged with unlimited repositories, version control, discussions, and pull requests.
- GitHub Sponsors lets you support open source maintainers and projects.
- GitHub Advanced Security provides visibility into security posture and helps organizations comply with regulations.
- Dependabot helps find and fix vulnerable dependencies.
- Code scanning is GitHub's static code analysis tool.
- The platform is for anyone to build anything, whether scaling a startup or learning to code.
- A study conducted by Forrester Consulting found a positive economic impact for organizations using GitHub Enterprise Cloud and Advanced Security.
- GitHub has over 56 million projects that fixed vulnerabilities.
```

## Usage: news.py 

news.py will find links on a given news subject.  You can then use the output and pipe it to search-gpt.py to summarize a set of links.

Run the following command to start the script:

```
python news.py
```

The script will prompt you for news to find links for

You can also provide the news subject as the first argument to the script and the last number of days to search.  The following will look for news about "stock market" in the last 7 days:

```
% python news.py "stock market" 7
```

## Limitations
This is proof of concept code and should be treated as such.  It is tested on Mac OS so you may need to tweak to run elsewhere.
