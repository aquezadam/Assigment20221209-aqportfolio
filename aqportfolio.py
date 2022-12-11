import os
import streamlit as st
from streamlit_option_menu import option_menu

path = os.path.dirname(__file__)

with st.sidebar:
    profile_photo = st.sidebar.image(path+'/CV Foto AQ.jpg', use_column_width=True)
    profile_phone = st.sidebar.subheader("Alejandra Quezada")
    profile_name = st.sidebar.markdown('''<h5
                                            style = "color:#ff4b4b;">
                                            Phone: +31 6 1234 5678 
                                            <br/>
                                            Email: ale@ale.com 
                                            <br/>
                                            Git: github.com/aquezadam 
                                            <br/>
                                            Web: aqportfolio.heroku.app
                                            </h5>''',unsafe_allow_html=True)

main_columns = st.columns(2)
title = st.markdown('''<h3 style = "background-color:#F6DADE; text-align:center; color:#ff4b4b;">
                         HOME
                         </h3>''',
                        unsafe_allow_html=True)
main_options = option_menu("", ["About me", "Python Projects"],orientation="horizontal")
if main_options == "About me":
    about_me_text = st.markdown('''  
                                **SUMMARY**       
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                                sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                                Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
                                nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
                                reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
                                pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
                                culpa qui officia deserunt mollit anim id est laborum. \n
                                **ACHIEVEMENTS** \n
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                                sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                                Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
                                nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
                                reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
                                pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
                                culpa qui officia deserunt mollit anim id est laborum. \n
                                **EXPERIENCE** \n
                                🪄Lorem ipsum dolor sit amet, consectetur adipiscing elit \n
                                🪄Lorem ipsum dolor sit amet, consectetur adipiscing elit                          
                                ''')
elif main_options == "Python Projects":
    projects = st.markdown("• Calculators\n\n• News Aggregator")


