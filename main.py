import streamlit as st

# Hauptüberschrift
st.title("Geräteverwaltungssoftware für Hochschulen")

# Navigation für die Module
tabs = st.sidebar.radio("Navigation", [
    "Geräteverwaltung",
    "Nutzerverwaltung",
    "Reservierungssystem",
    "Wartungs-Management"
])

# Geräte-Verwaltung
if tabs == "Geräteverwaltung":
    st.header("Geräteverwaltung")
    st.subheader("Gerät anlegen")
    device_name = st.text_input("Gerätename eingeben")
    if st.button("Gerät speichern"):
        st.write(f"Gerät '{device_name}' wurde gespeichert.")

    st.subheader("Gerät ändern")
    device_list = ["Laser-Cutter", "3D-Drucker", "Fräsmaschine"]
    selected_device = st.selectbox("Gerät auswählen", device_list)
    new_name = st.text_input("Neuen Namen eingeben", value=selected_device)
    if st.button("Änderungen speichern"):
        st.write(f"Gerät '{selected_device}' wurde in '{new_name}' umbenannt.")

# Nutzer-Verwaltung
elif tabs == "Nutzerverwaltung":
    st.header("Nutzerverwaltung")
    st.subheader("Nutzer anlegen")
    user_name = st.text_input("Nutzername eingeben")
    if st.button("Nutzer speichern"):
        st.write(f"Nutzer '{user_name}' wurde hinzugefügt.")

# Reservierungssystem
elif tabs == "Reservierungssystem":
    st.header("Reservierungssystem")
    st.subheader("Reservierungen anzeigen")
    reservations = [
        {"Gerät": "Laser-Cutter", "Datum": "2025-01-10", "Nutzer": "Max Mustermann"},
        {"Gerät": "3D-Drucker", "Datum": "2025-01-11", "Nutzer": "Anna Müller"}
    ]
    for res in reservations:
        st.write(f"Gerät: {res['Gerät']}, Datum: {res['Datum']}, Nutzer: {res['Nutzer']}")

    st.subheader("Reservierung eintragen")
    selected_device = st.selectbox("Gerät auswählen", ["Laser-Cutter", "3D-Drucker", "Fräsmaschine"])
    reservation_date = st.date_input("Datum auswählen")
    reservation_user = st.text_input("Nutzername eingeben")
    if st.button("Reservierung speichern"):
        st.write(f"Reservierung für '{selected_device}' am '{reservation_date}' für Nutzer '{reservation_user}' wurde gespeichert.")

# Wartungs-Management
elif tabs == "Wartungs-Management":
    st.header("Wartungs-Management")
    st.subheader("Wartungen anzeigen")
    maintenances = [
        {"Gerät": "Laser-Cutter", "Datum": "2025-01-05", "Kosten": "100 EUR"},
        {"Gerät": "3D-Drucker", "Datum": "2025-01-08", "Kosten": "150 EUR"}
    ]
    for main in maintenances:
        st.write(f"Gerät: {main['Gerät']}, Datum: {main['Datum']}, Kosten: {main['Kosten']}")

    st.subheader("Wartungskosten anzeigen")
    selected_device = st.selectbox("Gerät auswählen", ["Laser-Cutter", "3D-Drucker", "Fräsmaschine"], key="maintenance")
    maintenance_cost = st.number_input("Wartungskosten eingeben (EUR)", min_value=0)
    if st.button("Kosten speichern"):
        st.write(f"Wartungskosten für '{selected_device}' wurden auf {maintenance_cost} EUR gesetzt.")
