import streamlit as st
import pandas as pd
import mysql.connector
from PIL import Image
import json

# MySQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="Electronic_Health_record"
)
cursor = conn.cursor(dictionary=True)

# ------------------ Utility Functions ------------------

def book_appointment(doctor_name, appointment_date, appointment_time):
    cursor.execute("""
        INSERT INTO appointments (doctor_name, date, time, user_id)
        VALUES (%s, %s, %s, %s)
    """, (doctor_name, appointment_date, appointment_time, 1))
    conn.commit()

def add_patient(name, age, gender, history):
    cursor.execute("""
        INSERT INTO patients (name, age, gender, medical_history, user_id)
        VALUES (%s, %s, %s, %s, %s)
    """, (name, age, gender, history, 1))
    conn.commit()

def get_patients(limit=20):
    cursor.execute("SELECT name, age, gender, medical_history FROM patients WHERE user_id = %s LIMIT %s", (1, limit))
    return cursor.fetchall()

def get_appointments(limit=20):
    cursor.execute("SELECT doctor_name, date, time FROM appointments WHERE user_id = %s LIMIT %s", (1, limit))
    return cursor.fetchall()

def get_doctors(limit=20):
    cursor.execute("SELECT name, schedule FROM doctors WHERE user_id = %s LIMIT %s", (1, limit))
    return cursor.fetchall()

def get_invoices():
    cursor.execute("SELECT * FROM invoices WHERE user_id = %s", (1,))
    return cursor.fetchall()

def pay_invoice(invoice_id, amount):
    cursor.execute("""
        UPDATE invoices SET status = 'paid', payment_amount = %s WHERE id = %s
    """, (amount, invoice_id))
    conn.commit()

def update_doctor_schedule(name, schedule):
    cursor.execute("UPDATE doctors SET schedule = %s WHERE name = %s", (schedule, name))
    conn.commit()

def insert_report(report_type, report_data):
    cursor.execute("INSERT INTO reports (report_type, data) VALUES (%s, %s)", (report_type, json.dumps(report_data)))
    conn.commit()

# ------------------ Streamlit App ------------------

def main():
    st.title("Electronic Health Record System")

    st.sidebar.subheader("Appointment Booking")
    doctor_name = st.sidebar.text_input("Doctor's Name")
    appointment_date = st.sidebar.date_input("Appointment Date")
    appointment_time = st.sidebar.time_input("Appointment Time")

    if st.sidebar.button("Book Appointment"):
        book_appointment(doctor_name, appointment_date, appointment_time)
        st.sidebar.success("Appointment booked successfully!")

    st.sidebar.subheader("Patient Records")
    pname = st.sidebar.text_input("Patient Name")
    page = st.sidebar.number_input("Patient Age", min_value=0)
    pgender = st.sidebar.selectbox("Patient Gender", ["Male", "Female", "Other"])
    phistory = st.sidebar.text_area("Medical History")

    if st.sidebar.button("Add Patient"):
        add_patient(pname, page, pgender, phistory)
        st.sidebar.success("Patient added successfully!")

    row_limit = st.number_input("Number of rows", min_value=1, value=20)
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Patient Records")
        patients = get_patients(row_limit)
        if patients:
            st.table(patients)
        else:
            st.info("No patient records found.")

    with col2:
        st.subheader("Appointments")
        appointments = get_appointments(row_limit)
        if appointments:
            st.table(appointments)
        else:
            st.info("No appointment records found.")

    st.sidebar.subheader("Doctor's Schedule")
    dname = st.sidebar.text_input("Doctor Name")
    dschedule = st.sidebar.text_area("Schedule")
    if st.sidebar.button("Update Schedule"):
        update_doctor_schedule(dname, dschedule)
        st.sidebar.success("Schedule updated")

    st.sidebar.subheader("Billing and Payments")
    if st.sidebar.button("View Invoices"):
        invoices = get_invoices()
        st.subheader("Invoices")
        for inv in invoices:
            st.write(f"Invoice ID: {inv['id']}, Amount: {inv['amount']}, Status: {inv['status']}")

    if st.sidebar.button("Make Payment"):
        st.subheader("Make Payment")
        inv_id = st.text_input("Invoice ID")
        amt = st.number_input("Payment Amount", min_value=0.0)
        if st.button("Submit Payment"):
            pay_invoice(inv_id, amt)
            st.success("Payment successful")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Doctors Schedule")
        doctors = get_doctors(row_limit)
        if doctors:
            st.table(doctors)
        else:
            st.info("No doctor schedules found.")

    with col2:
        st.subheader("Invoices")
        invoices = get_invoices()
        if invoices:
            st.table(invoices)
        else:
            st.info("No invoices found.")

    st.sidebar.subheader("Reports and Analytics")
    if st.sidebar.button("Generate Report"):
        report_type = st.selectbox("Select Report Type", ["Appointment", "Patient"])
        if st.button("Generate"):
            if report_type == "Appointment":
                data = get_appointments(row_limit)
            else:
                data = get_patients(row_limit)
            insert_report(report_type, data)
            st.success(f"{report_type} report generated!")

# ------------------ App Entry ------------------
if __name__ == "__main__":
    main()
