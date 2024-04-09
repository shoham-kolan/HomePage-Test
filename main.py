import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
with col1:
    st.image("images/3.png", width=450)
with col2:
    st.title("Shoham Kolan")
    content = """This is My Data"""
    st.write(content)










# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
