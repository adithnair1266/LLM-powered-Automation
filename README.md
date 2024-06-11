# LLM Powered Automation and Text Generation

Welcome to the LLM Powered Automation and Text Generation project! This project leverages several open-source Large Language Models (LLMs) to power text-based generation and automation scripts, allowing you to create sequential workflow scripts quickly based on your use case.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
   - [Ollama Server](#installing-ollama-server)
   - [Groq Cloud](#using-groq-to-run-inference)
   - [LM Studio](#installing-lm-studio-for-supported-huggingface-models)
3. [Creating an Agent](#creating-an-agent)
4. [Using Tools](#using-tools)
5. [Examples](#examples)
   - [Code Generator](#code-generator)
   - [Content Writer](#content-writer)
6. [Potential Use Cases](#potential-use-cases)

## Prerequisites

This project supports two local LLM inference servers (Ollama and LM Studio) and one cloud-based inference server (Groq).

## Installation

### Installing Ollama Server

1. Follow the instructions on [Ollama's website](https://ollama.com) to install and run open-source models on your system.
2. Ensure the Ollama server is running by checking `http://localhost:11434`.

### Using Groq to Run Inference

1. Create an account on [GroqCloud](https://console.groq.com) and obtain an API key.
2. Store the API key in a `.env` file.

### Installing LM Studio (for supported HuggingFace Models)

1. Follow [this tutorial](https://4sysops.com/archives/lm-studio-run-a-local-ai-on-your-desktop-or-server/) to install LM Studio.
2. Ensure the LM Studio server is running before using it.

## Creating an Agent

The `agents.py` script demonstrates how each inference endpoint is implemented. To create an agent:

1. Import the `Agent` class from the `agents.py` script.
2. Create an object of the `Agent` class, providing the model, a system prompt, and the type of server to run inference (`'local'` for local Ollama models, `'groq'` for GroqCloud, and `'LM'` for LM Studio models).
3. Use the `runAgent(query)` method to get the response from a model.

## Using Tools

The `tools.py` script includes several basic tools, from simple web searches using the Serper API to scraping websites and saving text to files. To use tools:

1. Import the `Tools` class from the `tools.py` script.
2. Access tools directly from the class.

## Examples

### Code Generator

The `code_generator.py` script demonstrates the generation of code using the Groq server with the `llama3:70b` model. Auto-generated codes are stored in the `auto_code` directory.

### Content Writer

The `content_writer.py` script generates factual content based on a given topic, scraping information from the Internet. Generated content, including blogs and news articles, is stored in the `auto_articles` directory.

**Note:** Ensure the Serper API key is stored in the `.env` file as this script uses the web search tool.

## Potential Use Cases

1. Simple sentiment analysis using HuggingFace Models.
2. Information collection from a large corpus of data.
3. Facilitating project documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.

## Acknowledgements

Thanks to the developers of Ollama, Groq, and LM Studio for their amazing tools and models.

---

We hope this project helps you leverage the power of LLMs for your automation and text generation needs. Happy coding!
