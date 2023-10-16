import streamlit as st

def show_about_page():
    st.write(
        """
        
Loan approval prediction is a process that leverages various applicant attributes and financial information to make informed decisions regarding whether to approve or deny a loan application. This predictive task uses a dataset with the following key parameters:

1. `Loan_ID`: A unique identifier for each loan application.

2. `Gender`: This parameter denotes the gender of the loan applicant, which can be "Male" or "Female."

3. `Marital Status`: The "Married" parameter indicates whether the applicant is married, with options "Yes" or "No."

4. `Dependents`: The number of dependents associated with the applicant is captured in this field, with values such as "0," "1," "2," or "3+."

5. `Education`: Indicates the education level of the applicant, with choices like "Graduate" or "Not Graduate."

6. `Self_Employed`: This parameter identifies whether the applicant is self-employed, with values "Yes" or "No."

7. `Applicant Income`: The income of the primary applicant plays a significant role in loan approval.

8. `Coapplicant Income`: If applicable, the income of the coapplicant is considered in the loan application.

9. `Loan Amount`: This parameter represents the requested loan amount by the applicant.

10. `Loan Amount Term`: The term or duration of the loan is provided, typically in months (e.g., "360" for a 30-year loan).

11. `Credit History`: The credit history of the applicant is considered, with values "1.0" for good credit history and "0.0" for poor credit history.

12. `Property Area`: This parameter indicates the residential location or property area of the applicant, with categories like "Urban," "Semiurban," or "Rural."

13. `Loan Status`: The ultimate decision on loan approval is reflected in this parameter, denoted as "Y" for approval or "N" for denial.

Using this dataset, a loan approval prediction model can be developed. Machine learning techniques can be applied to analyze historical loan application data, considering these parameters. The model aims to predict whether a new loan application is likely to be approved ("Y") or denied ("N") based on the applicant's information, thereby assisting in the efficient and data-driven decision-making process for loan approval.
        
        """
    )