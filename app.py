from streamlit_tags import st_tags
import boto3
import json
import streamlit as st
import streamlit_analytics
import datetime

# Variables
now = datetime.datetime.now()
CURRENTDATE = now.strftime("%Y-%m-%d %H:%M:%S")
NUMPARAGRAPH = 1
NUMWORDS = 1000

streamlit_analytics.start_tracking()

bedrock = boto3.client(service_name="bedrock-runtime")

if 'last_time' not in st.session_state:
    st.session_state['last_time'] = now

st.set_page_config(
    page_title="LinkedIn Generator",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
st.title("LinkedIn Generator")
st.markdown(
    "This app generates LinkedIn Posts using Amazon Bedrock and Open LLMs"
)

user_textbox = st.text_area('Enter Content or URL', height=50)
USER_PROMPT = '<content>' + user_textbox + '</content>'

with st.sidebar:
    with st.expander("Options", expanded = True):
        keywords = st_tags(
        label='Enter Hashtags',
        text='Press enter to add more',
        value=['#aws', '#awscloud', '#awsstartups', '#startups'],
        suggestions=['#vc', '#venturecapital', '#innovation', 
                    '#entrepreneurship', '#chile', '#argentina'],
        maxtags = 10,
        key='1')

        select_language = st.radio(
        "Language",
        ["Spanish", "English"],
        index=0)

    with st.expander("Advanced"):
        select_model = st.radio(
        "Model",
        ["meta.llama2-70b-chat-v1"],
        index=0)

        temperature_selector = st.slider('Temperature', 0.0, 1.0, 0.3, 0.1)

SYSTEM_PROMPT = f"""
Imagine you are an expert LinkedIn post writer that knows how to optimize hashtags to increase views. 
You are tasked to write a LinkedIn post using the content at the end of this prompt. 
Make sure to review all the text in the content and take the most relevant parts to write the post.

Instructions:
Audience = young startup founders and investors
Tone = if the content is sad, use a sad tone. If the content is possitive use a positive tone.
Size of response = {NUMPARAGRAPH} paragraph, no more than {NUMWORDS} words
Language = use the {select_language} language to create the content
Hashtags: Add hashtags from this list {keywords}. Add additional hashtags from the content.
Date: Today date is {CURRENTDATE}
"""

def get_response(USER_PROMPT): 
    payload = {
        "prompt": SYSTEM_PROMPT + ' ' + USER_PROMPT,
        "max_gen_len": NUMWORDS,
        "temperature": temperature_selector,
        "top_p": 0.9
    }
    body = json.dumps(payload)
    
    response = bedrock.invoke_model(
        modelId=select_model,
        accept="application/json",
        contentType="application/json",
        body=body
    )
    
    return json.loads(response.get("body").read())

if st.button("Generate"):
    if not USER_PROMPT:
        st.warning("Please enter a text.", icon = "⚠️")
    else:
        with st.spinner('Generating post...'):
            prompt = get_response(USER_PROMPT)
            if prompt:
                st.success('Done!')
                response_body = prompt
                generation = response_body['generation']
            st.text_area("", value=generation, height=300)

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: gray;
text-align: center;
}
</style>
<div class="footer">
<p>Developed by harasic@</p>
</div>
"""
st.markdown(footer, unsafe_allow_html = True)

streamlit_analytics.stop_tracking()
