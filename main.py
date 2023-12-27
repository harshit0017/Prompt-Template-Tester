import openai

import os 
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
client = OpenAI()
openai.api_key = os.getenv("OPENAI_API_KEY")
import streamlit as st


st.title("Prompt Testing with OpenAI")



def get_reply( prompt_template, context):
    response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
        "role": "system",
        "content": f"You are an expert linkedin post creator. You have to write post in the provided template  {prompt_template} only."
        },
        {
            "role": "system",
            "content": f"""Follow the following steps to create a post:
                        1. Understand the template as to where you need to put what information.
                        2. Use {context} to understand what kind of information you need to put in the template.
                        3. Must replace the original template's content with the desired content only according to the provided context; it should not contain braces.
                        4. Make sure the post is properly indentated with proper line breaks ,commas and has proper punctuation.
                        5. Must  return the post created in the same format as the template.
                        
                    """
        },
        # {
        #     "role": "user",
        #     "content": """
        #                     {X} has changed
        #                     1. {before}
        #                     2. {before}
        #                     3. {before}
        #                     Exactly! It's a {what it is changed to}
        #                     1. {new}
        #                     2. {new}
        #                     3. {new}
        #                     Stop complaining and start {the right thing}. This is the 2023 way to {X}.
                            
                            
        #                     write a linkedin post on the  hiring in 2023 due to recession  according to the above format. 

        #                """
        # },
        # {
        #     "role": "assistant",
        #     "content": """
        #                     Hiring in 2023 has changed:

        #                     Companies used to hire based on experience alone
        #                     Job seekers used to rely on traditional resumes and cover letters
        #                     Recruiters used to spend hours manually reviewing applications
        #                     Exactly! It's a new era of hiring:

        #                     Companies are now focusing on skills and potential rather than just experience
        #                     Job seekers are showcasing their skills through portfolios, online profiles, and project examples
        #                     Recruiters are leveraging AI and automation to streamline the hiring process
        #                     Stop complaining and start adapting to the new hiring landscape. This is the 2023 way to land your dream job.

        #                     #hiring #jobsearch #2023trends #careeradvice 

        #             """
        # },

    ],
    max_tokens=400,
    temperature= 0.2,
    
    )
  
    return response.choices[0].message.content
def main():
    # Define the prompt
    prompt_template= st.text_area("Enter your template here")
    context= st.text_area("Enter your details here")
    if st.button("generate"):
        result= get_reply(prompt_template, context)
        print(result)
        st.write(result)
        
if __name__ == "__main__":
    main()
