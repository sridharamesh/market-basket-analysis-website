import streamlit as st
import pandas as pd

df = pd.read_pickle('data_with_probability1.pkl')

def get_top_n_category_recommendations(user_id, categories, N=5):
    user_data = df[(df['user_id'] == user_id) | (df['Category'].isin(categories))]
    user_data = user_data.sort_values(by='reorder_probability', ascending=False)
    top_n_recommendations = user_data.head(N)
    return top_n_recommendations[['Product Id', 'Product Title', 'Category']]

st.title("RELATED PRODUCTS")
st.image('amazon.jpg')

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.sidebar.header('Set id:222643')
    st.sidebar.text('Market Basket Analysis for Amazon Data')
    st.sidebar.text('Realed products predictions')

    with st.form('Suggestions'):
        user_id = st.text_input("Enter User ID:")
        categories = st.multiselect("Select Categories:", df['Category'].unique())
        submit_button = st.form_submit_button("Get related products")

if submit_button:
    user_data = df[(df['user_id'] == user_id) | (df['Category'].isin(categories))]
    user_data = user_data.sort_values(by='reorder_probability', ascending=False)
    recommendations = user_data.head(5)

    st.subheader(f"Top Products for User {user_id} in Selected Categories:")
    # Style the recommendation boxes
    box_style = """
    border: 2px solid #3498db;
    background-color: #ecf0f1;
    padding: 15px;
    margin-bottom: 15px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    color: black;
      """

    # Display each recommendation in a styled box
    if not recommendations.empty:
        for i, row in recommendations.iterrows():
            st.markdown(
                f"""<div style="{box_style}">
                    <p><strong>Product Title:</strong> {row['Product Title']}</p>
                    <p><strong>Category:</strong> {row['Category']}</p>
                    <p><strong>Product ID:</strong> {row['Product Id']}</p>
                </div>""",
                unsafe_allow_html=True
            )
    else:
        st.warning("No data found for the given user ID and categories.")

    # Add a back button to reset the form
    if st.button("Go Back"):
        st.form_submit_button("Reset Form")
