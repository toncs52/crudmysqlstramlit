import streamlit as st
import pymysql
import connecttionmysql as con

st.title("CRUD MySQL App with Streamlit")

connection = con.connectdb()
cursor = connection.cursor()


def read_person():
    cursor.execute("SELECT * from person")
    persons = cursor.fetchall()
    return persons


def create_person(fullname="", email="", age=0):
    try:
        cursor.execute(
            "INSERT INTO person (fullname, email ,age) VALUES (%s,%s,%s)", (
                fullname, email, age)
        )
        connection.commit()
        st.success("Created person successfully")
    except pymysql.Error:
        st.error(f'เกิด Error : {pymysql.Error}')


def update_person(fullname="", email="", age=0, id=0):
    try:
        cursor.execute(
            "UPDATE person SET fullname=%s , email=%s ,age=%s WHERE id = %s", (
                fullname, email, age, id)
        )
        connection.commit()
        st.success("UPDATE person successfully")
    except pymysql.Error:
        st.error(f'เกิด Error : {pymysql.Error}')


def delete_person(id=0):
    try:
        cursor.execute(
            "DELETE from person WHERE id = %s", (
                id)
        )
        connection.commit()
        st.success("UPDATE person successfully")
    except pymysql.Error:
        st.error(f'เกิด Error : {pymysql.Error}')


menu = ["Home", "Insert", "Update", "Delete"]

choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.write("### Person List")

    persons = read_person()
    table_data = []
    if persons:
        for person in persons:
            row = person
            table_data.append(row)
        st.table(table_data)
    else:
        st.write("### ยังไม่มีข้อมูลใน table ")

elif choice == "Insert":
    st.write("Add new Person")
    fullname = st.text_input("Fullname")
    email = st.text_input("Email")
    age = st.number_input("Age", 1, 100, 1)

    if st.button("Create"):
        if fullname and email and age:
            create_person(fullname, email, age)
        else:
            st.warning("กรุณากรอก")

elif choice == "Update":
    st.write("Update")
    id = st.number_input("Id", 1, 1000, 1)
    fullname = st.text_input("Fullname")
    email = st.text_input("Email")
    age = st.number_input("Age", 1, 100, 1)

    if st.button("Update"):
        update_person(fullname, email, age, id)

elif choice == "Delete":
    st.write("Delete")
    id = st.number_input("Id", 1, 1000, 1)

    if st.button("Delete"):
        delete_person(id)
