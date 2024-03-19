# LinkedIn Post Generator with Claude AI

This repository contains a Streamlit app that utilizes the Claude AI language model from Anthropic to generate LinkedIn posts based on user input. The app provides a user-friendly interface where users can enter content or a URL, and the app will generate a LinkedIn post optimized for the specified language, tone, and hashtags.

## Prerequisites

Before running the app, ensure that you have the following dependencies installed:

- anthropic
- streamlit
- streamlit_tags
- streamlit_analytics

You can install these dependencies using pip:
```
pip install anthropic streamlit streamlit-tags streamlit-analytics
```

## Usage

1. Run the Streamlit app using the following command:

```
streamlit run app.py
```

2. The app will open in your default web browser.

3. Enter the content or URL you want to use as the basis for the LinkedIn post in the provided text area.

4. In the sidebar, you can customize the following options:
   - **Model**: Select the Claude AI model to use for generating the post from the available options.
   - **Temperature**: Adjust the randomness of the generated text using the slider (0.0 for deterministic, 1.0 for more random).
   - **Language**: Choose the language (Spanish or English) for the generated post.
   - **Hashtags**: Enter relevant hashtags to include in the post. You can also add or remove hashtags using the suggested options.

5. Click the "Generate" button to generate the LinkedIn post based on your input and selected options.

6. The generated post will be displayed in the text area below the "Generate" button.

## Code Structure

- `import` statements: The code imports the required libraries and modules, including `anthropic` for the Claude AI integration, `streamlit_tags` for the hashtag input component, `streamlit` for the web application framework, `streamlit_analytics` for tracking analytics, and `datetime` for working with dates and times.

- `Variables`: The code defines variables such as `CURRENTDATE` (the current date and time), `NUMPARAGRAPH` (the number of paragraphs for the generated post), and `NUMWORDS` (the maximum number of words in the generated post).

- `streamlit_analytics.start_tracking()`: This line starts tracking analytics for the Streamlit app.

- `st.set_page_config()`: This function configures the page settings for the Streamlit app, including the title, icon, layout, sidebar state, and menu items.

- `st.title()` and `st.markdown()`: These functions display the app's title and a brief description, respectively.

- `topic_textbox` and `user_content`: The `st.text_area()` function creates a text area for the user to enter content or a URL. The user input is then wrapped in XML tags (`<content>...</content>`) and stored in the `user_content` variable.

- `with st.sidebar`: This block creates a sidebar section in the app.
  - `select_model`: A radio button for selecting the Claude AI model to use for post generation.
  - `temperature_selector`: A slider for adjusting the randomness of the generated text.
  - `select_language`: A radio button for choosing the language (Spanish or English) for the generated post.
  - `keywords`: A component for entering and suggesting relevant hashtags using `st_tags()`.

- `REG_PROMPT`: This string contains the prompt for the Claude AI model, which includes instructions for generating the LinkedIn post based on the user's input and selected options.

- `get_response()`: This function creates an instance of the `Anthropic` client, sends the user's input and selected options to the Claude AI model, and returns the generated post.

- `if st.button("Generate"):`: This block executes when the "Generate" button is clicked.
  - If no user input is provided, a warning message is displayed using `st.warning()`.
  - Otherwise, a spinner is shown using `st.spinner()` while the post is being generated.
  - If the post generation is successful, a success message is displayed using `st.success()`, and the generated post is displayed in a text area using `st.text_area()`.

- `streamlit_analytics.stop_tracking()`: This line stops tracking analytics for the Streamlit app.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Streamlit](https://streamlit.io/) for providing an excellent framework for building interactive web applications.
- [Anthropic](https://www.anthropic.com/) for developing Claude AI, the powerful language model used in this project.
- [streamlit-tags](https://github.com/sungjungBang/streamlit-tags) for the convenient hashtag input component.
- [streamlit-analytics](https://github.com/sungjungBang/streamlit-analytics) for providing analytics tracking for the Streamlit app.

