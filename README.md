Blog Generation with LLama-2-7B Model
This project uses Streamlit and the LLama-2-7B model to generate blogs based on a provided topic, writing style, and desired word count. It allows users to interact with the model, view previous requests, and see analytics on blog generation history.

Project Overview
This project utilizes the LLama-2-7B model for generating blog content. The application allows the user to input a blog topic, choose the desired writing style, and specify the word count. Once the input is provided, the model generates a blog post, displays it, and saves it to a history for later viewing.

Features:
Topic Input: Users can enter the blog topic.
Word Count Selection: Choose a word count between 50 and 300.
Blog Style Selection: Choose from different writing styles, including Common People, Researchers, and Students.
Response History: Keeps track of previous blog requests.
Analytics Overview: Provides stats like average word count, response time, and blog history.
Requirements
To run the project, you'll need to have the following dependencies:

Python 3.x
Streamlit
langchain
langchain_community
os
time
Install Dependencies
You can install the necessary dependencies using pip:

bash
Copy
Edit
pip install streamlit langchain langchain-community
Additionally, you must download the LLama-2-7B model file and place it in the model directory. Ensure that the model file is named llama-2-7b-chat.ggmlv3.q8_0.bin as expected by the code.

How to Run
Set Up the Model:

Download the LLama-2-7B model from your preferred source.
Place the model file in a directory named model/ in the same directory as your Python script.
Run the Streamlit App:

Open a terminal or command prompt.

Navigate to the directory containing the Streamlit script.

Run the following command to start the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Access the Application:

After running the command, the Streamlit app will open in your web browser.
You can input a blog topic, select a word count and style, and generate the blog.
Feedback and History:

Users can provide feedback through the sidebar.
The history of previous requests is stored and can be viewed in the "View Request History" section.
Folder Structure
bash
Copy
Edit
/blog-generation
    /model
        llama-2-7b-chat.ggmlv3.q8_0.bin  # LLama-2-7B model file
    app.py                               # Streamlit app script
Code Explanation
Streamlit Frontend:

The app interface uses streamlit to allow the user to input the blog topic, word count, and select the writing style.
LLama-2-7B Model:

The CTransformers from langchain_community is used to interface with the LLama-2-7B model to generate blog content.
Prompt Handling:

A custom prompt template is used to format the request sent to the LLama model.
History and Analytics:

All blog generation requests are stored in the session state and can be viewed later. Analytics on the number of blogs generated and response times are also displayed in the sidebar.
License
This project is licensed under the MIT License - see the LICENSE file for details.
