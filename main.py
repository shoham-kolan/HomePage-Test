import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
with col1:
    st.image("images/3.png", width=450)
with col2:
    st.title("Shoham Kolan")
    content = """This is My Data"""
    st.write(content)

st.info("testing")

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=",")

for index, row in df.iterrows():
    if (index%2 == 0 ) :
        with col3:
            st.header(row["Title"])
            st.write(row["Description"])
            st.image("images/" + row["Image"], width=400)
            st.write(f"[Source Code]({row['URL']})")
    else:
        with col4:
            st.header(row["Title"])
            st.write(row["Description"])
            st.image("images/" + row["Image"],width=400)
            st.write(f"[Source Code]({row['URL']})")









# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
