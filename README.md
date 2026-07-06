# Secure Code Review

## CodeAlpha Cybersecurity Internship - Task 3

---

### Project Description

I reviewed a Python application and found 10 security vulnerabilities. This project contains both the vulnerable code and the secure version with all fixes applied.

---

### Vulnerabilities Found

| # | Vulnerability | Severity |
|---|---------------|----------|
| 1 | Hardcoded Credentials | CRITICAL |
| 2 | SQL Injection | CRITICAL |
| 3 | Command Injection | CRITICAL |
| 4 | Weak Password Storage (MD5) | HIGH |
| 5 | Path Traversal | HIGH |
| 6 | Hardcoded API Key | HIGH |
| 7 | Division by Zero | MEDIUM |
| 8 | Information Disclosure | MEDIUM |
| 9 | Unvalidated Input | MEDIUM |
| 10 | Insecure Session IDs | MEDIUM |

---

### Project Structure
CodeAlpha_SecureCodeReview/
├── README.md
├── vulnerable_code.py
├── secure_code.py
└── security_audit_report.md

text

---

### How to Run

1. Run the vulnerable version:

```bash
python vulnerable_code.py
Run the secure version:

bash
python secure_code.py
Fixes Applied
Vulnerability	Fix
Hardcoded Credentials	Environment variables
SQL Injection	Parameterized queries
Command Injection	Subprocess with arguments
Weak Password Storage	bcrypt with salt
Path Traversal	Path validation
Hardcoded API Key	Environment variables
Division by Zero	Try-catch error handling
Information Disclosure	Generic error messages
Unvalidated Input	Input validation
Insecure Session IDs	Secure random generation
Technologies Used
Python 3.12

bcrypt

subprocess

sqlite3

Author
ADESIYAN ADEOLA SAMUEL

CodeAlpha Cybersecurity Intern

Date
July 2026
