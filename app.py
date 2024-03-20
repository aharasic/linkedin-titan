from streamlit_tags import st_tags
import boto3
import json
import streamlit as st
import datetime
import logging

# Variables
now = datetime.datetime.now()
CURRENTDATE = now.strftime("%Y-%m-%d %H:%M:%S")
NUMPARAGRAPH = 1
NUMWORDS = 100

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
        #["meta.llama2-70b-chat-v1", "amazon.titan-text-express-v1"],
        ["amazon.titan-text-express-v1"],
        index=0)

        temperature_selector = st.slider('Temperature', 0.0, 1.0, 0.3, 0.1)

SYSTEM_PROMPT = f"""
    Imagine you are an expert LinkedIn post writer that knows how to optimize hashtags to increase views. 
    
    Write an appealing linkedin post with these instructions:
    - Make sure the response is not more than {NUMPARAGRAPH} paragraph, and no more than {NUMWORDS} words
    - Use the {select_language} language to create the content
    - Add linkedin hashtags from this list {keywords}
    - Add additional linkedin hashtags from the content.
    - Today date is {CURRENTDATE}
    - Use content provided in <content> xml tags
    """

class ImageError(Exception):
    "Custom exception for errors returned by Amazon &titan-text-express; model"

    def __init__(self, message):
        self.message = message

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def get_response(body): 
    #accept = "application/json"
    content_type = "application/json"

    response = bedrock.invoke_model(
        body=body, modelId=select_model, contentType=content_type
    )
    response_body = json.loads(response.get("body").read())

    finish_reason = response_body.get("error")

    if finish_reason is not None:
        raise ImageError(f"Text generation error. Error is {finish_reason}")

    logger.info(
        "Successfully generated text with Amazon &titan-text-express; model %s", select_model)

    return response_body

prompt = USER_PROMPT + ' ' + SYSTEM_PROMPT

body = json.dumps({
            "inputText": prompt,
            "textGenerationConfig": {
                "maxTokenCount": 500,
                "stopSequences": [],
                "temperature": temperature_selector,
                "topP": 1
            }
        })

if st.button("Generate"):
    if not USER_PROMPT:
        st.warning("Please enter a text.", icon = "⚠️")
    else:
        with st.spinner('Generating post...'):
            response_body = get_response(body)
            if response_body:
                st.success('Done!')
                result = response_body['results']
                generation = result[0]
                output = generation['outputText']
            st.text_area("", value=output, height=300)

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
