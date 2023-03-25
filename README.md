# Chat GPT

Chat GPT is a simple chatbot that uses the OpenAI GPT-3.5 model to generate responses to user input.

# Getting Started

## Prerequisites

- Python 3.8 or higher
- An OpenAI API key

## Installing

1. Clone this repository:

    ```bash
    git clone https://github.com/pingyingping/chat-gpt.git
    cd chat-gpt
    ```

2. Create and activate a new virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set your OpenAI API key as an environment variable:

    ```bash
    cp env-sample .env
    vim .env
    ```

# Usage

To start the chatbot, run the following command:

```bash
python chat_gpt.py
```

Once the chatbot is running, you can start chatting by typing in the terminal. Press Ctrl+C to exit.

# Contributing

If you would like to contribute to Chat GPT, please create a pull request with your changes.

# License

This project is licensed under the MIT License - see the LICENSE file for details.
