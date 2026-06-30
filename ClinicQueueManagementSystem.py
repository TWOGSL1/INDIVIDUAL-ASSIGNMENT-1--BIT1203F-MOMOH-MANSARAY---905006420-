print("Hello World")

"""
Clinic Queue Management System (CQMS)

Terminal-based Python application for managing patient queues
in a small clinic.

The design demonstrates structured programming principles
through functions, decision structures, loops, variables,
constants, and formatted output.
"""

from datetime import datetime

# =========================
# CONSTANTS
# =========================

CLINIC_NAME = "HOPE Community Clinic"
CONSULTATION_TIME_MINUTES = 15
SEVERE_CASE_THRESHOLD = 8
MODERATE_CASE_THRESHOLD = 5


# =========================
# HELPER FUNCTIONS
# =========================

def print_header(title):
    """Display a consistent screen header."""
    print("\n" + "=" * 72)
    print(f"{CLINIC_NAME:^72}")
    print(f"{title:^72}")
    print("=" * 72)


def get_non_empty_input(prompt):
    """Collect non-empty text input from the user."""
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def get_valid_age(prompt):
    """Collect a realistic patient age."""
    while True:
        age_text = input(prompt).strip()

        if age_text.isdigit():
            age = int(age_text)

            if 0 < age <= 130:
                return age

        print("Please enter a valid age between 1 and 130.")


def get_valid_choice(prompt, allowed_choices):
    """Collect a menu choice from a known set of options."""
    while True:
        choice = input(prompt).strip().upper()

        if choice in allowed_choices:
            return choice

        print(f"Invalid choice. Choose one of: {', '.join(sorted(allowed_choices))}")


def get_severity_level():
    """Collect illness severity level from 1 to 10."""
    while True:
        severity_text = input("Enter severity level (1-10): ").strip()

        if severity_text.isdigit():
            severity = int(severity_text)

            if 1 <= severity <= 10:
                return severity

        print("Severity must be a number from 1 to 10.")


# =========================
# PRIORITY FUNCTIONS
# =========================

def calculate_priority_score(severity, emergency_case, age):
    """
    Calculate patient priority based on severity,
    emergency status, and age.
    """
    priority_score = severity * 10

    if emergency_case == "Y":
        priority_score += 50

    if age <= 5 or age >= 65:
        priority_score += 10

    return priority_score


def get_priority_label(severity, emergency_case):
    """Convert severity into a simple triage label."""

    if emergency_case == "Y" or severity >= SEVERE_CASE_THRESHOLD:
        return "Critical"

    if severity >= MODERATE_CASE_THRESHOLD:
        return "Moderate"

    return "Stable"


# =========================
# QUEUE FUNCTIONS
# =========================

def update_wait_times(queue):
    """Recalculate waiting time estimates."""
    for index, patient in enumerate(queue):
        patient["estimated_wait"] = index * CONSULTATION_TIME_MINUTES


def sort_queue(queue):
    """Sort queue by highest priority score."""
    queue.sort(
        key=lambda patient: (
            -patient["priority_score"],
            patient["arrival_number"]
        )
    )

    update_wait_times(queue)


def add_patient(queue, next_arrival_number):
    """Add a patient record to the clinic queue."""

    print_header("Register New Patient")

    patient_name = get_non_empty_input(
        "Enter patient name: "
    ).title()

    patient_age = get_valid_age(
        "Enter patient age: "
    )

    patient_gender = get_valid_choice(
        "Enter gender (M/F): ",
        {"M", "F"}
    )

    complaint = get_non_empty_input(
        "Enter main complaint: "
    ).capitalize()

    severity = get_severity_level()

    emergency_case = get_valid_choice(
        "Emergency case? (Y/N): ",
        {"Y", "N"}
    )

    priority_score = calculate_priority_score(
        severity,
        emergency_case,
        patient_age
    )

    priority_label = get_priority_label(
        severity,
        emergency_case
    )

    patient_record = {
        "arrival_number": next_arrival_number,
        "name": patient_name,
        "age": patient_age,
        "gender": patient_gender,
        "complaint": complaint,
        "severity": severity,
        "emergency_case": emergency_case,
        "priority_score": priority_score,
        "priority_label": priority_label,
        "estimated_wait": 0,
        "registered_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    queue.append(patient_record)

    sort_queue(queue)

    print("\nPatient registered successfully.")
    print(f"Assigned priority level: {priority_label}")
    print(
        f"Estimated waiting time: "
        f"{patient_record['estimated_wait']} minutes."
    )

    return next_arrival_number + 1


def view_queue(queue):
    """Display all waiting patients."""

    print_header("Current Clinic Queue")

    if not queue:
        print("No patients are currently in the queue.")
        return

    print(
        f"{'Pos':<5}"
        f"{'Name':<22}"
        f"{'Age':<6}"
        f"{'Gender':<8}"
        f"{'Severity':<10}"
        f"{'Priority':<12}"
        f"{'Wait(min)':<10}"
    )

    print("-" * 72)

    for position, patient in enumerate(queue, start=1):

        print(
            f"{position:<5}"
            f"{patient['name']:<22}"
            f"{patient['age']:<6}"
            f"{patient['gender']:<8}"
            f"{patient['severity']:<10}"
            f"{patient['priority_label']:<12}"
            f"{patient['estimated_wait']:<10}"
        )


def search_patient(queue):
    """Search for a patient by name."""

    print_header("Search Patient")

    if not queue:
        print("No patient records available to search.")
        return

    keyword = get_non_empty_input(
        "Enter patient name to search: "
    ).lower()

    matches = [
        patient for patient in queue
        if keyword in patient["name"].lower()
    ]

    if not matches:
        print("No matching patient found.")
        return

    print("\nSearch Results:")
    print("-" * 72)

    for patient in matches:

        print(
            f"Name: {patient['name']} | "
            f"Complaint: {patient['complaint']} | "
            f"Priority: {patient['priority_label']} | "
            f"Wait: {patient['estimated_wait']} minutes"
        )


def serve_next_patient(queue, served_patients):
    """Serve the next patient in line."""

    print_header("Serve Next Patient")

    if not queue:
        print("There are no patients waiting.")
        return

    next_patient = queue.pop(0)

    next_patient["served_at"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    served_patients.append(next_patient)

    update_wait_times(queue)

    print(f"Now serving: {next_patient['name']}")
    print(f"Complaint: {next_patient['complaint']}")
    print(f"Priority level: {next_patient['priority_label']}")
    print(f"Registration time: {next_patient['registered_at']}")


def show_daily_summary(queue, served_patients):
    """Display clinic queue activity summary."""

    print_header("Daily Summary")

    total_waiting = len(queue)
    total_served = len(served_patients)
    total_registered = total_waiting + total_served

    critical_waiting = 0

    for patient in queue:
        if patient["priority_label"] == "Critical":
            critical_waiting += 1

    if total_waiting > 0:

        total_wait_time = 0

        for patient in queue:
            total_wait_time += patient["estimated_wait"]

        average_wait = total_wait_time / total_waiting

    else:
        average_wait = 0

    print(f"Total patients registered: {total_registered}")
    print(f"Patients already served  : {total_served}")
    print(f"Critical cases waiting   : {critical_waiting}")
    print(f"Average wait time        : {average_wait:.1f} minutes")
    print(f"Patients still waiting   : {total_waiting}")


# =========================
# MENU FUNCTIONS
# =========================

def display_menu():
    """Display the main menu."""

    print_header("Clinic Queue Management System")

    print("1. Register patient")
    print("2. View clinic queue")
    print("3. Search patient")
    print("4. Serve next patient")
    print("5. View daily summary")
    print("6. Exit program")


# =========================
# MAIN PROGRAM
# =========================

def main():
    """Run the Clinic Queue Management System."""

    queue = []
    served_patients = []
    next_arrival_number = 1

    while True:

        display_menu()

        option = input(
            "\nEnter your choice (1-6): "
        ).strip()

        if option == "1":

            next_arrival_number = add_patient(
                queue,
                next_arrival_number
            )

        elif option == "2":

            view_queue(queue)

        elif option == "3":

            search_patient(queue)

        elif option == "4":

            serve_next_patient(
                queue,
                served_patients
            )

        elif option == "5":

            show_daily_summary(
                queue,
                served_patients
            )

        elif option == "6":

            print_header("Exit")
            print(
                "Thank you for using our "
                "Clinic Queue Management System."
            )

            break

        else:
            print(
                "Invalid menu option. "
                "Please choose a number between 1 and 6."
            )


# =========================
# PROGRAM ENTRY POINT
# =========================

if __name__ == "__main__":
    main()