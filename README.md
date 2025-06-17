# Turtle Facts Flask App

This project is a simple Flask application that displays a random turtle fact. It follows common Flask conventions and keeps the code organized and easy to understand. Facts and images are retrieved from public APIs at runtime.

## Features

- **Random turtle facts** – The homepage loads with a unique fact every time, pulled from a [GitHub dataset](https://raw.githubusercontent.com/Val7498/Turtle-facts-json/master/facts.json).
- **New fact on demand** – A button allows users to fetch another turtle fact without refreshing the page.
- **Turtle images** – Each fact is paired with a random turtle emoji from the [Twemoji](https://github.com/twitter/twemoji) or [OpenMoji](https://github.com/hfg-gmuend/openmoji) projects.
- **Clean, responsive layout** – The site uses a modern design that works well on both desktop and mobile.
- **Minimal setup** – Run locally with a single command to explore turtle trivia.

## Setup

1. **Create and activate a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the development server**

```bash
python app.py
```

Navigate to `http://localhost:5000` to view a random turtle fact.
