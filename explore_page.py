import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def show_explore_page():
    dataset = pd.read_csv('LoanDataset.csv')

    st.write("""### Count of Loan Status""")
    dataset['Loan_Status'].value_counts().plot(kind='bar')
    st.pyplot(plt.gcf())

    st.subheader("", divider="rainbow")

    st.write("""### Loan Status by Education""")
    colors = ['#4D3425','#E4512B']
    contract_churn = dataset.groupby(['Education','Loan_Status']).size().unstack()

    ax = (contract_churn.T*100.0 / contract_churn.T.sum()).T.plot(kind='bar',
                                                                    width = 0.3,
                                                                    stacked = True,
                                                                    rot = 0,
                                                                    figsize = (10,6),
                                                                    color = colors)
    ax.legend(loc='best',prop={'size':14},title = 'Loan_Status')

    # Code to add the data labels on the stacked bar chart
    for p in ax.patches:
        width, height = p.get_width(), p.get_height()
        x, y = p.get_xy()
        ax.annotate('{:.0f}%'.format(height), (p.get_x()+.25*width, p.get_y()+.4*height),
                    color = 'white',
                weight = 'bold',
                size = 14)
    st.pyplot(plt.gcf())
    
    st.subheader("", divider="rainbow")

    st.write("""### Loan Status by Gender""")
    colors = ['#4D3425','#E4512B']
    contract_churn = dataset.groupby(['Gender','Loan_Status']).size().unstack()

    ax = (contract_churn.T*100.0 / contract_churn.T.sum()).T.plot(kind='bar',
                                                                    width = 0.3,
                                                                    stacked = True,
                                                                    rot = 0,
                                                                    figsize = (10,6),
                                                                    color = colors)
    ax.legend(loc='best',prop={'size':14},title = 'Loan_Status')

    # Code to add the data labels on the stacked bar chart
    for p in ax.patches:
        width, height = p.get_width(), p.get_height()
        x, y = p.get_xy()
        ax.annotate('{:.0f}%'.format(height), (p.get_x()+.25*width, p.get_y()+.4*height),
                    color = 'white',
                weight = 'bold',
                size = 14)
    
    st.pyplot(plt.gcf())

    st.subheader("", divider="rainbow")

    st.write("""### Loan Status by Marriage""")
    colors = ['#4D3425','#E4512B']
    contract_churn = dataset.groupby(['Married','Loan_Status']).size().unstack()

    ax = (contract_churn.T*100.0 / contract_churn.T.sum()).T.plot(kind='bar',
                                                                    width = 0.3,
                                                                    stacked = True,
                                                                    rot = 0,
                                                                    figsize = (10,6),
                                                                    color = colors)
    ax.legend(loc='best',prop={'size':14},title = 'Loan_Status')

    # Code to add the data labels on the stacked bar chart
    for p in ax.patches:
        width, height = p.get_width(), p.get_height()
        x, y = p.get_xy()
        ax.annotate('{:.0f}%'.format(height), (p.get_x()+.25*width, p.get_y()+.4*height),
                    color = 'white',
                weight = 'bold',
                size = 14)
    st.pyplot(plt.gcf())

    st.subheader("", divider="rainbow")

    st.write("""### Loan Status by Dependents""")
    colors = ['#4D3425','#E4512B']
    contract_churn = dataset.groupby(['Dependents','Loan_Status']).size().unstack()

    ax = (contract_churn.T*100.0 / contract_churn.T.sum()).T.plot(kind='bar',
                                                                    width = 0.3,
                                                                    stacked = True,
                                                                    rot = 0,
                                                                    figsize = (10,6),
                                                                    color = colors)
    ax.legend(loc='best',prop={'size':14},title = 'Loan_Status')

    # Code to add the data labels on the stacked bar chart
    for p in ax.patches:
        width, height = p.get_width(), p.get_height()
        x, y = p.get_xy()
        ax.annotate('{:.0f}%'.format(height), (p.get_x()+.25*width, p.get_y()+.4*height),
                    color = 'white',
                weight = 'bold',
                size = 14)
    st.pyplot(plt.gcf())

    st.subheader("", divider="rainbow")

    st.write("""### Loan Status by Employment""")
    colors = ['#4D3425','#E4512B']
    contract_churn = dataset.groupby(['Self_Employed','Loan_Status']).size().unstack()

    ax = (contract_churn.T*100.0 / contract_churn.T.sum()).T.plot(kind='bar',
                                                                    width = 0.3,
                                                                    stacked = True,
                                                                    rot = 0,
                                                                    figsize = (10,6),
                                                                    color = colors)
    ax.legend(loc='best',prop={'size':14},title = 'Loan_Status')

    # Code to add the data labels on the stacked bar chart
    for p in ax.patches:
        width, height = p.get_width(), p.get_height()
        x, y = p.get_xy()
        ax.annotate('{:.0f}%'.format(height), (p.get_x()+.25*width, p.get_y()+.4*height),
                    color = 'white',
                weight = 'bold',
                size = 14)
    st.pyplot(plt.gcf())

    st.subheader("", divider="rainbow")

    st.write("""### Loan Status by Property""")
    colors = ['#4D3425','#E4512B']
    contract_churn = dataset.groupby(['Property_Area','Loan_Status']).size().unstack()

    ax = (contract_churn.T*100.0 / contract_churn.T.sum()).T.plot(kind='bar',
                                                                    width = 0.3,
                                                                    stacked = True,
                                                                    rot = 0,
                                                                    figsize = (10,6),
                                                                    color = colors)
    ax.legend(loc='best',prop={'size':14},title = 'Loan_Status')

    # Code to add the data labels on the stacked bar chart
    for p in ax.patches:
        width, height = p.get_width(), p.get_height()
        x, y = p.get_xy()
        ax.annotate('{:.0f}%'.format(height), (p.get_x()+.25*width, p.get_y()+.4*height),
                    color = 'white',
                weight = 'bold',
                size = 14)
    st.pyplot(plt.gcf())

    st.subheader("", divider="rainbow")