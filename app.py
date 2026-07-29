import streamlit as st

# Initialize Session State
if "balance" not in st.session_state:
    st.session_state.balance = 5000

if "login" not in st.session_state:
    st.session_state.login = False

# Functions
def check_balance():
    return st.session_state.balance

def deposit(amount):
    st.session_state.balance += amount

def withdraw(amount):
    if amount > st.session_state.balance:
        return False
    st.session_state.balance -= amount
    return True

# Title
st.title("🏧 ATM Management System")

# Login
if not st.session_state.login:

    pin = st.text_input("Enter ATM PIN", type="password")

    if st.button("Login"):
        if pin == "1234":
            st.session_state.login = True
            st.success("Login Successful")
            st.rerun()
        else:
            st.error("Invalid PIN")

# ATM Menu
else:

    st.subheader("ATM Menu")

    option = st.selectbox(
        "Select Transaction",
        ["Balance", "Deposit", "Withdraw", "Logout"]
    )

    if option == "Balance":

        st.info(f"Current Balance : ₹{check_balance()}")

    elif option == "Deposit":

        amount = st.number_input(
            "Enter Deposit Amount",
            min_value=1,
            step=1
        )

        if st.button("Deposit"):

            deposit(amount)

            st.success("Amount Deposited Successfully")
            st.write("New Balance : ₹", check_balance())

    elif option == "Withdraw":

        amount = st.number_input(
            "Enter Withdraw Amount",
            min_value=1,
            step=1
        )

        if st.button("Withdraw"):

            if withdraw(amount):
                st.success("Withdrawal Successful")
                st.write("Remaining Balance : ₹", check_balance())
            else:
                st.error("Insufficient Balance")

    elif option == "Logout":

        if st.button("Logout"):
            st.session_state.login = False
            st.success("Thank You For Using ATM")
            st.rerun()