import openai
import typer
import signal
import os
from dotenv import load_dotenv

app = typer.Typer()

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
openai.organization = os.getenv('OPENAI_ORGANIZATION')


def signal_handler(sig, frame):
    print('\nExiting chat...')
    exit(0)


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)


def get_prompt():
    print('\rYou: ', end='')
    prompt = ''
    while True:
        temp = input()
        if temp.strip() == 'EOF':
            break

        prompt += temp
    return prompt


def ask_gpt(prompt):
    if prompt.strip() == '':
        return

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': prompt.strip()},
        ],
        stream=True
    )

    print('\rGPT: ', end='')
    for chunk in response:
        delta: dict = chunk['choices'][0]['delta']
        if delta and delta.get('content'):
            content: str = delta['content']
            print(content, end='', flush=True)
        if not delta:
            print('\n')


@app.command()
def chat():
    while True:
        try:
            prompt = get_prompt()

            if prompt.strip() == '':
                pass
            else:
                print('\n[WAITING]')
                ask_gpt(prompt)

        except KeyboardInterrupt:
            print('\nExiting chat...')
            break
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app()
