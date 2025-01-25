# Blog Generation with LLama-2-7B Model

This project uses Streamlit and the LLama-2-7B model to generate blogs based on a provided topic, writing style, and desired word count. It allows users to interact with the model, view previous requests, and see analytics on blog generation history.

## Project Overview

This project utilizes the LLama-2-7B model for generating blog content. The application allows the user to input a blog topic, choose the desired writing style, and specify the word count. Once the input is provided, the model generates a blog post, displays it, and saves it to a history for later viewing.

### Features:
- **Topic Input**: Users can enter the blog topic.
- **Word Count Selection**: Choose a word count between 50 and 300.
- **Blog Style Selection**: Choose from different writing styles, including Common People, Researchers, and Students.
- **Response History**: Keeps track of previous blog requests.
- **Analytics Overview**: Provides stats like average word count, response time, and blog history.

## Requirements

To run the project, you'll need to have the following dependencies:

- Python 3.x
- Streamlit
- langchain
- langchain_community
- os
- time

## Install Dependencies

You can install the necessary dependencies using pip:

```bash
pip install streamlit langchain langchain-community

