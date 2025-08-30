import google.generativeai as gg
import streamlit as st

gg.configure(api_key="AIzaSyAjxcWvjDxmvyy_bJWh6z54Vgusr3yMh-Y")

model=gg.GenerativeModel(
    "gemini-2.0-flash",
    generation_config={
        "temperature": 0.5,
        "max_output_tokens":1500,
    }   
)

def blog_creater(user_input):
    messages=f"""
             You are a blog creater.You will create a blog of 1000 to 1500.The blog should not less than 100 words

             Title of the blog(less than one line)
             introduction in one line
             10 sub heading but shortly explain
             important mcqs
             conclusion of the blog in 3 sentences : {user_input}
            """
    
    response=model.generate_content(messages)
    response_text=response.text.strip()
    return response_text


# user_input=input("Enter the name of the blog: ")

# blog=blog_creater(user_input)

# print(blog)

st.set_page_config(page_title="AI Blog Generator", page_icon="✍️", layout="wide")

st.title("✍️ AI Blog Generator")
st.write("Generate SEO-friendly blogs using Google Gemini API")

# Input from user
user_input = st.text_input("Enter the topic of the blog:")

if st.button("Generate Blog"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a topic first.")
    else:
        with st.spinner("⏳ Generating your blog..."):
            blog = blog_creater(user_input)
        st.success("✅ Blog Generated Successfully!")
        st.markdown(blog)
        
        # Optional: Download button
        st.download_button("📥 Download Blog", blog, file_name=f"{user_input}_blog.txt")
