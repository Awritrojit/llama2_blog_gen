# Libraries
import streamlit as st
from langchain.prompts import PromptTemplate
from huggingface_hub import InferenceClient
# Use a pipeline as a high-level helper
from transformers import pipeline

from dotenv import find_dotenv, load_dotenv

import requests
load_dotenv(find_dotenv())

# Function to get response from the Llama2 model
def llama2response(iptext, num_words, blog_style):
    
    ## llama 2 model
    access_token = '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'

    print('before pipe')
    client = InferenceClient(model="TheBloke/Llama-2-7B-Chat-GGML",
                             token=access_token)
    
    print('after pipe')

    ## create prompt template
    template = f"Being a world renknowned expert in content writing having experience in virtually all fields of knowledge, write a blog for {blog_style} on the topic of {iptext} within {num_words} words."
    prompt = template.format(blog_style,iptext,num_words)
    
    ## generate response from llama2 model
    response = client.text_generation(prompt=prompt, do_sample=False)[0]['generated_text']
    print(response)
    return response

## GUI App
def main():
    st.set_page_config(page_title = "Wiz Blogger",
                       page_icon =  "🧙🏻‍♂️",
                       layout = 'centered',
                       initial_sidebar_state = 'collapsed')

    st.header("WizBlogger 🧙🏻‍♂️: Generate Blogs in a pinch!!")

    iptext = st.text_input("Enter blog topic")

    # 2 columns for 2 additional fields

    col1, col2 = st.columns([5,5])

    with col1:
        num_words = st.text_input("Number of words")
    with col2:
        # who the blog is for
        blog_style = st.selectbox("Writing the blog for", 
                                ("Researchers", "Content Creator", "Fiction Writer", "Common People"), index=0)

    submit = st.button("Generate")

    # final response
    if submit:
        st.write(llama2response(iptext, num_words, blog_style))

if __name__ == '__main__':
    
    main()