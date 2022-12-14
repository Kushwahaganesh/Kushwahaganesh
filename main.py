import streamlit as st
import pandas as pd
import numpy as np
st.title("ganesh kushwaha")
st.write("mscdsit")
st.header("hey")
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
st.caption('This is a string that explains something above.')
df = pd.DataFrame(
   np.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))

st.table(df)
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)
st.area_chart(chart_data)
