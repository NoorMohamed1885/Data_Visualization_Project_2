import streamlit as st

st.set_page_config(
    page_title="My Portfolio",
    page_icon="📊",
    layout="wide"
)

st.title("Navigation")

st.markdown(
    """
    - 📄 Bio: A summary about myself.
    - 📊 Charts Gallery: My dataset analysis gallery.
    - 📈 Dashboard: My dataset dashboard.
    - 🧭 Future Work: My future work.
    - 👥 Graph Visualization: Friendship network in a college class.
    """
)

st.caption("Use the left sidebar to switch pages.")