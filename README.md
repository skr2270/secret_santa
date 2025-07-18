# Secret Santa Game - Full Stack Developer Coding Challenge

## Overview
This project implements a **Secret Santa** assignment system for employees, where each employee is randomly assigned a Secret Santa (gift-giver) while following the rules:

1. No employee can be assigned to themselves.
2. No one can be assigned to the same person as last year.
3. Each employee has exactly one Secret Santa and one Secret Child.

The goal of this coding challenge is to write a program that processes employee data, assigns Secret Santa pairs, and outputs the assignments to a CSV file.

---

## Project Setup

### Prerequisites

Before you begin, ensure you have the following installed:

* Python 3.12+ (preferred)
* `pip` (Python package manager)

### Installation Steps

1. **Clone the Repository**:
   Clone the project repository to your local machine.

   ```bash
   git clone <your-repository-url>
   cd secret_santa
   ```

2. **Set Up the Virtual Environment**:
   Create a virtual environment to isolate your project dependencies.

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:

   * On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   * On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install Required Packages**:
   Install the required dependencies from `requirements.txt`.

   ```bash
   python -m pip install -r requirements.txt
   ```

   **Note**: If you encounter an SSL-related error (e.g., `Could not find a suitable TLS CA certificate bundle`), follow these steps:

---

## SSL Verification Issue Resolution

### Problem:

While installing packages, you might encounter the following error:

```bash
ERROR: Could not install packages due to an OSError: Could not find a suitable TLS CA certificate bundle, invalid path: C:\Program Files\PostgreSQL\16\ssl\certs\ca-bundle.crt
```

### Solution:

This error occurs because `pip` is attempting to use PostgreSQL's certificate path, which might not be configured correctly. To resolve this, you can bypass the SSL verification temporarily by using the `--trusted-host` option with `pip`:

```bash
python -m pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org -r requirements.txt
```

This will allow `pip` to install the required packages without checking SSL certificates.

Alternatively, you can set the correct SSL certificate path for Python to use during installation:

1. **Install `certifi` package**:

   ```bash
   python -m pip install certifi
   ```

2. **Locate the `cacert.pem` file**:

   Find the path to the `cacert.pem` file by running:

   ```bash
   python -m certifi
   ```

3. **Set the `SSL_CERT_FILE` environment variable** to the correct path:

   ```bash
   set SSL_CERT_FILE=C:\path\to\certifi\cacert.pem
   ```

4. **Try the installation again**:

   ```bash
   python -m pip install -r requirements.txt
   ```

After these steps, you should be able to install the dependencies successfully.

---

## Running the Application

After installing the dependencies and resolving any SSL issues, you can run the application as follows:

1. **Run the Main Script**:
   Execute the main script to read employee data, assign Secret Santa pairs, and generate the output CSV.

   ```bash
   python main.py
   ```

2. **Output**:
   The result will be saved to `New_Secret_Santa_Assignments.csv` containing the following columns:

   * `Employee_Name`
   * `Employee_EmailID`
   * `Secret_Child_Name`
   * `Secret_Child_EmailID`

---

## Project Structure

Here’s an overview of the project structure:

```
secret_santa/
├── main.py                     # Main script to run the application
├── models/
│   └── employee.py             # Employee model class
├── services/
│   └── santa_assigner.py       # Logic for assigning Secret Santa
├── utils/
│   └── file_handler.py         # Utility functions for file I/O
├── tests/
│   └── test_santa_assigner.py  # Unit tests for the application
├── requirements.txt            # Required Python packages
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore file
└── venv/                       # Virtual environment
```

---

## Testing

The project includes unit tests to verify the correctness of the Secret Santa assignment logic.

To run the tests, use the following command:

```bash
python -m unittest discover tests/
```

---

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
