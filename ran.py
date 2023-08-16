import streamlit as st
import random 
from PIL import Image

st.header("guessing app")
img=Image.open("fyn.jpeg")
st.image("fyn.jpeg")

b=st.number_input("please input a number from 1-6")
a = random.randint

def game(a,b):
    a=random.randint(1,6) 

    if b > 6:
       return("invalid input ,please select a number between 1 and 6")
    else:
      if a== b:
         return("correct")
      else:
          st.write(f"your selected number is {b}")
          st.write(f"random number is {a}")
          return("wrong ,try again")

if st.button ("try your luck"):
    st.write(game(a,b))


