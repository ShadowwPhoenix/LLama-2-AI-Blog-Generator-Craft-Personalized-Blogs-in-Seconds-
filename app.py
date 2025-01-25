import streamlit as st
from langchain_community.llms import CTransformers
from langchain.prompts import PromptTemplate
import os
import time

def getLLamaresponse(input_text, no_words, blog_style):
    llm = CTransformers(
        model=os.path.join("model", "llama-2-7b-chat.ggmlv3.q8_0.bin"),
        model_type="llama",
        config={"max_new_tokens": 256, "temperature": 0.01},
    )

    template = """
        Write a blog for {blog_style} job profile for a topic "{input_text}"
        within {no_words} words.
    """
    prompt = PromptTemplate(input_variables=["blog_style", "input_text", "no_words"], template=template)

    response = llm.invoke(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    
    word_count = len(response.split())
    
    return response, word_count

st.set_page_config(
    page_title="Generate Blogs",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.header("Generating Blogs 🤖 using LLama-2-7B General Graphical Machine Learning for Quantization and CPU-Friendly")

input_text = st.text_input("Enter the Blog Topic")

col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input("Number of Words (50 to 300)")
with col2:
    blog_style = st.selectbox(
        "Writing the blog for", ("Common People", "Researchers", "Students"), index=0
    )

with st.sidebar:
    st.markdown("View statistics and share your thoughts!")
    
    feedback = st.text_area("Your Feedback", placeholder="Let us know how we're doing!")
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")

if "history" not in st.session_state:
    st.session_state["history"] = []

def save_to_history(topic, style, words, response, response_time):
    st.session_state["history"].append({
        "topic": topic, "style": style, "words": words, "content": response, "response_time": response_time
    })

def display_history():
    if st.session_state["history"]:
        st.subheader("Your Previous Blog Requests")
        for idx, item in enumerate(st.session_state["history"], start=1):
            st.markdown(f"**{idx}. Topic:** {item['topic']}, **Style:** {item['style']}, **Words:** {item['words']}")
    else:
        st.info("No history available.")

with st.expander("View Request History"):
    display_history()

submit = st.button("Generate")

if submit:
    if not input_text or not no_words.isdigit() or not (50 <= int(no_words) <= 300):
        st.error("Please provide a valid topic and ensure the word count is between 50 and 300.")
    else:
        st.write(f"Generating blog for topic **'{input_text}'** with **{no_words} words**...")

        start_time = time.time()
        
        with st.spinner("Generating your blog..."):
            time.sleep(2)
            response, word_count = getLLamaresponse(input_text, int(no_words), blog_style)
        
        response_time = time.time() - start_time
        
        st.text_area("Generated Blog", response, height=300)
        
        save_to_history(input_text, blog_style, no_words, response, response_time)

        with st.sidebar:
            word_counts = [len(item['content'].split()) for item in st.session_state['history']]
            avg_word_count = sum(word_counts)/len(word_counts) if word_counts else 0
            max_word_count = max(word_counts) if word_counts else 0
            min_word_count = min(word_counts) if word_counts else 0

            length_deviation = abs(word_count - int(no_words))
            
            st.subheader("Analytics Overview")
            st.markdown(f"**Total Blogs Generated:** {len(st.session_state['history'])}")
            st.markdown(f"**Average Word Count:** {avg_word_count:.2f} words")
            st.markdown(f"**Max Word Count:** {max_word_count} words")
            st.markdown(f"**Min Word Count:** {min_word_count} words")
            st.markdown(f"**Current Blog Length:** {word_count} words")
            st.markdown(f"**Expected Length:** {no_words} words")
            st.markdown(f"**Length Deviation:** {length_deviation} words")
            
            response_times = [item['response_time'] for item in st.session_state['history']]
            avg_response_time = sum(response_times)/len(response_times) if response_times else 0
            
            st.markdown(f"**Average Response Time:** {avg_response_time:.2f} seconds")
            st.markdown(f"**Current Response Time:** {response_time:.2f} seconds")
