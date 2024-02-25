# %%
#pip install streamlit


# %%
# my_streamlit_app.py

import streamlit as st
import pandas as pd

# Load your CSV data (replace 'your_data.csv' with your actual file path)
df = pd.read_csv('ftahackathon24feb.csv')

# Sidebar filters
selected_sector = st.sidebar.selectbox('Select Sector', df['Sector'].unique())
selected_industry = st.sidebar.selectbox('Select Industry', df[df['Sector'] == selected_sector]['Industry'].unique())

# Filter data based on selections
filtered_df = df[(df['Sector'] == selected_sector) & (df['Industry'] == selected_industry)]

# Display companies and their outputvat as nodes
st.write(f"Companies in {selected_sector} - {selected_industry}:")
st.dataframe(filtered_df[['Company', 'OutputVat']])

# You can create visualizations here (e.g., plotly charts, graphs, etc.)

# Example: Display a bar chart of OutputVat
st.bar_chart(filtered_df.set_index('Company')['OutputVat'])

# Run the app
if __name__ == '__main__':
    st.title('TaX Neural Networks')
    st.write('Transformimg Taxation Through Tecchnology!')



