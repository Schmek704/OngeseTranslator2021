# Ongese Translator

import streamlit as st

# Defining the Function
def trans(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "bcdfghjklmnpqrstvwxyz":  # Checking for consonants to add "ong" to the end
            translation = translation + letter + "ong "
        else:
            translation = translation + letter + " "  # if not a consonant then letter in the word remains unchanged
    return translation
# Asking the User for Input

# Introducing the user to the newest language in town!
st.title("Ongese Language Translator")
st.write("This function is made available publicly by Dan McKeon and his helper E")

word = st.text_input("\n\nPlease enter a word or phrase:  ")
if word:
    st.write("\nWelcome to the world of Ongese!!!")
    st.write("\nThe translation of your phrase in Ongese is:")
    st.header("\n\n" + trans(word))
# Introducing the user to the newest language in town!

