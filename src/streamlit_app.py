import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Create a sidebar

st.sidebar.header("Sidebar")

    # Sidebar widgets
# selected_option = st.sidebar.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])

    # Main content area
# st.subheader("Main Content")

    # Conditional content based on the selected option
# if selected_option == "Option 1":
#     st.write("You selected Option 1.")
# elif selected_option == "Option 2":
#     st.write("You selected Option 2.")
# else:
#     st.write("You selected Option 3.")

    # Create a row layout
c1, c2= st.columns(2)
c3, c4= st.columns(2)

with st.container():
    c1.write("c1")
    c2.write("c2")

with st.container():
    c3.write("c3")
    c4.write("c4")

with c1:
    chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

with c2:
    chart_data = pd.DataFrame(np.random.randn(20, 3),columns=["a", "b", "c"])
    st.bar_chart(chart_data)

with c3:
    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)
    st.pyplot(fig)
    
    # chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
    # st.line_chart(chart_data)

with c4:
    chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
    st.line_chart(chart_data)
    



