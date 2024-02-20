# Libraries
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

# Function to get response from the Llama2 model
def llama2response(iptext, num_words, blog_style):
    
    ## llama 2 model
    llm = CTransformers(model=r'./model/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens':256,
                                'temperature': 0.01})
    
    ## create prompt template
    template = """
                Being a world renknowned expert in content writing having experience in virtually all fields of knowledge, 
                write a blog for {blog_style} on the topic of {iptext} within {num_words} words.
                """
    prompt = PromptTemplate(input_variables=['iptext','num_words','blog_style'],
                            template=template)
    
    ## generate response from llama2 model
    response = llm(prompt.format(blog_style=blog_style, iptext=iptext, num_words=num_words))
    print(response)
    return response


## GUI App
st.set_page_config(page_title = "Wiz Blogger",page_icon =  "🧙🏻‍♂️",layout = 'centered',initial_sidebar_state = 'collapsed')

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