import streamlit as st
import config
from ptldev1190.pylib.Telegram import Telegram

def app():
	st.title('Telegram')
	form = st.form(key='my_form')
	msg = form.text_input(label='Enter Message')
	submit_button = form.form_submit_button(label='Submit')

	to = config._Telegram_Chat_Id['Dhaval']
	token = config._Telegram_Bot_Token

	if submit_button:
		res = Telegram.sendMessage(msg, to, token)
		# print(test)
		# st.success('Success, message sent!')
		st.success(res)
