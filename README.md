# LinkedIn Post Generator with Amazon Bedrock and Open LLMs

This repository contains a Streamlit app that generates LinkedIn posts using Amazon Bedrock and Open LLMs (Large Language Models). The app provides a user-friendly interface where users can enter content or a URL, and the app will generate a LinkedIn post optimized for the specified language, tone, and hashtags.

## Features

- **User-friendly Streamlit interface**: The app provides an intuitive interface for users to input content, customize options, and generate LinkedIn posts.
- **Amazon Bedrock integration**: The app leverages the power of Amazon Bedrock, a fully managed service for foundation models, to generate high-quality LinkedIn posts.
- **Open LLM support**: The app utilizes Open LLMs, specifically the `meta.llama2-70b-chat-v1` model, to generate human-like text for the LinkedIn posts.
- **Customizable options**: Users can select the language (Spanish or English) for the generated post, adjust the temperature for text generation, and specify relevant hashtags.
- **Hashtag suggestions**: The app provides a list of suggested hashtags to help users easily add relevant hashtags to their posts.
- **Dynamic post generation**: The app dynamically generates the LinkedIn post based on the user's input, selected options, and the current date.
- **Streamlit Analytics**: The app integrates Streamlit Analytics to track user interactions and gain insights into app usage.

## Prerequisites

Before running the app, ensure that you have the following dependencies installed:

- Python 3.7 or above
- Streamlit
- Streamlit Tags
- Boto3
- Streamlit Analytics

You can install the required dependencies using the following command:

```
pip install streamlit streamlit-tags boto3 streamlit-analytics
```

## Usage

1. Clone the repository:

```
git clone https://github.com/your-username/linkedin-post-generator.git
```

2. Navigate to the project directory:

```
cd linkedin-post-generator
```

3. Run the Streamlit app:

```
streamlit run app.py
```

4. The app will open in your default web browser.

5. Enter the content or URL in the provided text area.

6. Customize the options in the sidebar, such as hashtags, language, and temperature.

7. Click the "Generate" button to generate the LinkedIn post.

8. The generated post will be displayed in the text area below the "Generate" button.

## Configuration

The app uses the following configuration variables:

- `CURRENTDATE`: The current date and time in the format "YYYY-MM-DD HH:MM:SS".
- `NUMPARAGRAPH`: The number of paragraphs in the generated post (default: 1).
- `NUMWORDS`: The maximum number of words in the generated post (default: 1000).
- `SYSTEM_PROMPT`: The system prompt used to guide the text generation process.

You can modify these variables according to your requirements.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Streamlit](https://streamlit.io/) for providing an excellent framework for building interactive web applications.
- [Amazon Bedrock](https://aws.amazon.com/bedrock/) for providing a fully managed service for foundation models.
- [Open LLMs](https://github.com/s-JoL/Open-LLMs) for providing open-source large language models.
- [Streamlit Tags](https://github.com/gagan3012/streamlit-tags) for the convenient hashtag input component.
- [Streamlit Analytics](https://github.com/jrieke/streamlit-analytics) for providing analytics tracking for the Streamlit app.


