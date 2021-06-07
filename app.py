import streamlit as st
from nav import Nav
# import your app modules here
from apps import dashboard, watchlist, telegram

app = Nav()

# Add all your application here
app.add_app("Dashboard", dashboard.app)
app.add_app("Watchlist", watchlist.app)
app.add_app("Telegram", telegram.app)

# The main app
app.run()
