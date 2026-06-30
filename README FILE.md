# Clinic Queue Management System

![Clinic Queue Management System Banner](https://private-us-east-1.manuscdn.com/sessionFile/KmvY4nRQ60EmRjvQiD99q1/sandbox/Lugk05sMzVQyFRXdnkmOOO-images_1782857080885_na1fn_L2hvbWUvdWJ1bnR1L3JlcG9fYmFubmVy.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvS212WTRuUlE2MEVtUmp2UWlEOTlxMS9zYW5kYm94L0x1Z2swNXNNelZReUZSWGRua21PT08taW1hZ2VzXzE3ODI4NTcwODA4ODVfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzSmxjRzlmWW1GdWJtVnkucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzk4NzYxNjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=hoHsfziS94dS~4x5K6yCf0rsB7IY6z46K7La44sBk2IesFzrTuFD-Uimg8wDVGYFcvPN9H886eMhC4j3D2r0kvo7UN9nWWk0dSEOV14oBknjuse4JxuFKO7DWwr94xB6ZGdWCNHfrUZDj0betHa3NNRwAzJhf-meGfyo0EukwA5B2~19VL5JeUFaigwoAua0XJDJdeeU2PtncF1u2Mi510txajkQpYPD8lJhi4xsdy6VhfcKeQVh1ebvJl-FTLRT8gigwCBCMR-cQzt40zf~oS8amDc6gBigdQyOkVzWjE2oUyK264KH-xdHcjOWrhCmQqyY6NeU7Wbf~ooRusa~8Q__)

## Overview

The Clinic Queue Management System (CQMS) is a terminal-based Python application designed to efficiently manage patient queues in a small clinic. This system demonstrates fundamental structured programming principles through its use of functions, decision structures, loops, variables, constants, and formatted output. It allows clinic staff to register new patients, view the current queue, search for specific patients, serve the next patient based on priority, and view a daily summary of clinic activity.

## Features

*   **Patient Registration**: Easily add new patients to the queue with details such as name, age, gender, complaint, and illness severity.
*   **Priority-Based Queuing**: Patients are prioritized based on severity, emergency status, and age (children and elderly receive higher priority). The queue is dynamically sorted to ensure critical cases are attended to promptly.
*   **Estimated Wait Times**: The system calculates and updates estimated waiting times for all patients in the queue.
*   **Queue Management**: View the entire patient queue, serve the next patient, and search for patients by name.
*   **Daily Summary**: Get an overview of clinic operations, including total registered patients, served patients, critical cases waiting, and average wait times.
*   **User-Friendly Interface**: A simple, interactive command-line interface guides users through various options.

## How to Run

To run the Clinic Queue Management System, ensure you have Python 3 installed on your system. 

1.  **Save the file**: Save the provided `ClinicQueueManagementSystem.py` file to your local machine.
2.  **Open a terminal**: Navigate to the directory where you saved the file.
3.  **Execute the script**: Run the following command:

    ```bash
    python ClinicQueueManagementSystem.py
    ```

4.  **Follow the prompts**: Interact with the system by choosing options from the menu.

## Usage

Upon running the script, you will be presented with a main menu:

```
========================================================================
                          HOPE Community Clinic                         
                     Clinic Queue Management System                     
========================================================================
1. Register patient
2. View clinic queue
3. Search patient
4. Serve next patient
5. View daily summary
6. Exit program

Enter your choice (1-6): 
```

Select an option by entering the corresponding number and pressing Enter.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
