import json


# Load saved patient data when the program starts
try:
    with open("patients.json", "r") as file:
        patients = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    patients = []


while True:
    print("\nDENTAL TREATMENT TRACKER")
    print("1. Add patient")
    print("2. View patients")
    print("3. Search patient")
    print("4. Update treatment status")
    print("5. View pending treatment total")
    print("6. Save and exit")

    choice = input("Choose an option: ")


    # OPTION 1 - ADD PATIENT
    if choice == "1":
        name = input("Enter patient name: ")
        treatment = input("Enter treatment: ")
        cost = input("Enter treatment cost: ")
        status = input("Enter treatment status: ")

        patient = {
            "name": name,
            "treatment": treatment,
            "cost": cost,
            "status": status
        }

        patients.append(patient)

        print("\nPatient added!")
        print("Name: " + patient["name"])
        print("Treatment: " + patient["treatment"])
        print("Cost: $" + patient["cost"])
        print("Status: " + patient["status"])


    # OPTION 2 - VIEW PATIENTS
    elif choice == "2":
        if len(patients) == 0:
            print("No patients found.")
        else:
            print("\nPATIENT LIST")

            for patient in patients:
                print("--------------------")
                print("Name: " + patient["name"])
                print("Treatment: " + patient["treatment"])
                print("Cost: $" + patient["cost"])
                print("Status: " + patient["status"])


    # OPTION 3 - SEARCH PATIENT
    elif choice == "3":
        if len(patients) == 0:
            print("No patients available to search.")

        else:
            print("\nCurrent patients:")

            for patient in patients:
                print(patient["name"])

            search_name = input("\nEnter patient name to search: ")

            found = False

            for patient in patients:
                if patient["name"].lower() == search_name.lower():
                    print("\nPatient found:")
                    print("Name: " + patient["name"])
                    print("Treatment: " + patient["treatment"])
                    print("Cost: $" + patient["cost"])
                    print("Status: " + patient["status"])

                    found = True

            if found == False:
                print("Patient not found.")


    # OPTION 4 - UPDATE TREATMENT STATUS
    elif choice == "4":
        if len(patients) == 0:
            print("No patients available to update.")

        else:
            print("\nCurrent patients:")

            for patient in patients:
                print(patient["name"])

            update_name = input("\nEnter patient name to update: ")

            found = False

            for patient in patients:
                if patient["name"].lower() == update_name.lower():
                    new_status = input("Enter new treatment status: ")

                    patient["status"] = new_status

                    print("\nStatus updated!")
                    print("Name: " + patient["name"])
                    print("Treatment: " + patient["treatment"])
                    print("Cost: $" + patient["cost"])
                    print("Status: " + patient["status"])

                    found = True

            if found == False:
                print("Patient not found.")


    # OPTION 5 - PENDING TREATMENT TOTAL
    elif choice == "5":
        total = 0

        for patient in patients:
            if patient["status"].lower() == "pending":
                total += float(patient["cost"])

        print(f"\nPending treatment total: ${total:,.2f}")


    # OPTION 6 - SAVE AND EXIT
    elif choice == "6":
        with open("patients.json", "w") as file:
            json.dump(patients, file, indent=4)

        print("\nPatient data saved!")
        print("Goodbye!")
        break


    # INVALID MENU OPTION
    else:
        print("Invalid choice. Please choose 1-6.")