import streamlit as st

st.set_page_config(page_title="Dan Becerro's Website", page_icon=":tada:",layout="wide")

#---------------------------------------------------------- #divider

st.header("Welcome To Dan's Website")

column1, column2, column3 = st.columns(3)

with column1:
     st.write("Autobiography")
     st.write("Hi my name is dan becerro, 19 years old computer engineeering student, How can I help you today?")
with column2:
     st.write("SAY SOMETHING")
with column3:
     st.write("say")

st.write ("contact me:")

st.markdown("""
            
<form action="https://formsubmit.co/becerrodanilo5@gmail.com" methods="POST">
            <input type="text" name="name" placeholder="your name" required>
            <input type="email" name="email" placeholder="your email" required>
            <textarea name="message" placeholder="your message"></textarea>
            <button type="submit>/button>
</form>
            
            
""",unsafe_allow_html=True)                        
          