# Cat Facts Flask App

This project is a simple Flask application that displays a random cat fact. It follows common Flask conventions and keeps the code organized and easy to understand. Facts and images are retrieved from public APIs at runtime.

## Features

- **Random cat facts** – The homepage loads with a unique fact every time, pulled from [catfact.ninja](https://catfact.ninja/fact).
- **New fact on demand** – A button allows users to fetch another cat fact without refreshing the page.
- **Cat images** – Each fact is paired with a random cat photo from the [Cataas](https://cataas.com/) API.
- **Clean, responsive layout** – The site uses a modern design that works well on both desktop and mobile.
- **Minimal setup** – Run locally with a single command to explore cat trivia.

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

Navigate to `http://localhost:5000` to view a random cat fact.
