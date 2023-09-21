# PyChatGPT

A simple python chat program that uses the OpenAI API

- Keeps a history of the chat in memory and passes the whole chat back to the API for each new request
- This means that the AI can use the history to provide context for the response
- The program saves the history of the chat from each run in a json file
- You can change the system prompt and the temperature of the AI response using the system: and temp: commands
- See the help command for more information


The purpose of this program is to illustrate the basics of using the OpenAI API.
This working example can be used as a basis for creating more sophisticated programs.
Or you can just use it to have your local chat results stored in json files you can process in other ways!

# Installation
Edit the setenv.sh file and add your OpenAI API key.

```python
source setenv.sh
pipenv install openai
pipenv run python pychat.py
```

# API reference
Refer to the OpenAI documentation for more information:
https://platform.openai.com/docs/api-reference/introduction
