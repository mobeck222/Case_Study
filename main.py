import streamlit as st
from devices import Device
from serializer import serializer

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
    
    # Geräte anlegen
    st.subheader("Gerät anlegen")
    device_name = st.text_input("Gerätename eingeben", key="add_device")
    managed_by = st.text_input("Verantwortlicher Nutzer (E-Mail)", key="add_user")
    if st.button("Gerät speichern"):
        if device_name and managed_by:
            # Neues Gerät erstellen und speichern
            device = Device(device_name, managed_by)
            device.store_data()
            st.success(f"Gerät '{device_name}' wurde gespeichert.")
            st.experimental_rerun()  # Seite neu laden, um Dropdown-Liste zu aktualisieren
        else:
            st.error("Bitte sowohl einen Gerätenamen als auch einen Nutzer angeben.")

    # Gerät umbenennen
    st.subheader("Gerät ändern")
    devices = Device.find_all()  # Alle Geräte aus der Datenbank laden
    device_list = [d.device_name for d in devices]  # Nur die Namen extrahieren
    
    if device_list:
        selected_device = st.selectbox("Gerät auswählen", device_list, key="edit_device")
        new_name = st.text_input("Neuen Namen eingeben", value=selected_device, key="new_device_name")
        if st.button("Änderungen speichern"):
            if new_name:
                # Gerät aus der Datenbank laden
                device = Device.find_by_attribute("device_name", selected_device)
                if device:
                    device.device_name = new_name  # Namen ändern
                    device.store_data()  # Änderungen speichern
                    st.success(f"Gerät '{selected_device}' wurde in '{new_name}' umbenannt.")
                    st.experimental_rerun()  # Seite neu laden, um Änderungen anzuzeigen
                else:
                    st.error(f"Gerät '{selected_device}' konnte nicht gefunden werden.")
            else:
                st.error("Bitte einen neuen Namen eingeben.")
    else:
        st.warning("Es sind keine Geräte vorhanden.")

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
#test
