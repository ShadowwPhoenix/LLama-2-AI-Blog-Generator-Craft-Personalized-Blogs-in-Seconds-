# Blog Generation with LLama-2-7B Model


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

## Install Dependencies

You can install the necessary dependencies using pip:

```bash
pip install streamlit langchain langchain-community
```
Additionally, you must download the LLama-2-7B model file and place it in the model directory. Ensure that the model file is named llama-2-7b-chat.ggmlv3.q8_0.bin as expected by the code.

## How to Run

### Set Up the Model:
1. Download the LLama-2-7B model from your preferred source.
2. Place the model file in a directory named `model/` in the same directory as your Python script.

### Run the Streamlit App:
1. Open a terminal or command prompt.
2. Navigate to the directory containing the Streamlit script.
3. Run the following command to start the Streamlit app:

   ```bash
   streamlit run app.py
   ```
   ### Access the Application:
After running the command, the Streamlit app will open in your web browser. You can input a blog topic, select a word count and style, and generate the blog.

### Feedback and History:
Users can provide feedback through the sidebar. The history of previous requests is stored and can be viewed in the "View Request History" section.

## Folder Structure

```bash
/blog-generation
    /model
        llama-2-7b-chat.ggmlv3.q8_0.bin  # LLama-2-7B model file
    app.py                               # Streamlit app script
```
## Code Explanation

### Streamlit Frontend:
The app interface uses Streamlit to allow the user to input the blog topic, word count, and select the writing style.

### LLama-2-7B Model:
The `CTransformers` from `langchain_community` is used to interface with the LLama-2-7B model to generate blog content.

### Prompt Handling:
A custom prompt template is used to format the request sent to the LLama model.

### History and Analytics:
All blog generation requests are stored in the session state and can be viewed later. Analytics on the number of blogs generated and response times are also displayed in the sidebar.

---

Feel free to reach out with questions or suggestions.  
*by Shadow Phoenix*
