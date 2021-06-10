import streamlit as st
from shared import util

def app():
	st.title('Telegram')
	form = st.form(key='my_form')
	msg = form.text_input(label='Enter Message')
	submit_button = form.form_submit_button(label='Submit')

	if submit_button:
		res = util.notify(msg)
		# st.success('Success, message sent!')
		st.success(res)
