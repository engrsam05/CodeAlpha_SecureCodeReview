# Security Audit Report

## CodeAlpha Cybersecurity Internship - Task 3

**Date:** July 2026
**Application:** User Management System
**Language:** Python

---

## Summary

I reviewed a Python application and found 10 security vulnerabilities.

---

## Vulnerabilities Found

### 1. Hardcoded Credentials
- **Severity:** CRITICAL
- **Location:** `ADMIN_USERNAME`, `ADMIN_PASSWORD`
- **Problem:** Username and password are written directly in the code.
- **Fix:** Use environment variables.

### 2. SQL Injection
- **Severity:** CRITICAL
- **Location:** `get_user_by_username()`
- **Problem:** User input is added directly to SQL queries.
- **Fix:** Use parameterized queries.

### 3. Command Injection
- **Severity:** CRITICAL
- **Location:** `ping_host()`
- **Problem:** User input is passed directly to the system command line.
- **Fix:** Use subprocess with arguments and validate input.

### 4. Weak Password Storage
- **Severity:** HIGH
- **Location:** `store_password()`
- **Problem:** Passwords are hashed using MD5.
- **Fix:** Use bcrypt.

### 5. Path Traversal
- **Severity:** HIGH
- **Location:** `read_file()`
- **Problem:** File paths are not validated.
- **Fix:** Validate paths and restrict access.

### 6. Hardcoded API Key
- **Severity:** HIGH
- **Location:** `API_KEY`
- **Problem:** API key is written in the code.
- **Fix:** Use environment variables.

### 7. Division by Zero
- **Severity:** MEDIUM
- **Location:** `divide_numbers()`
- **Problem:** No error handling for division.
- **Fix:** Add try-catch.

### 8. Information Disclosure
- **Severity:** MEDIUM
- **Location:** `show_error_details()`
- **Problem:** Full error details are shown to users.
- **Fix:** Show generic error messages.

### 9. Unvalidated Input
- **Severity:** MEDIUM
- **Location:** `process_age()`
- **Problem:** Age input is not validated.
- **Fix:** Validate input.

### 10. Insecure Session IDs
- **Severity:** MEDIUM
- **Location:** `create_session()`
- **Problem:** Session IDs are predictable.
- **Fix:** Use secure random generation.

---

## Severity Summary

| Severity | Count |
|----------|-------|
| CRITICAL | 3 |
| HIGH | 3 |
| MEDIUM | 4 |
| TOTAL | 10 |

---

## Recommendations

1. Store secrets in environment variables
2. Use parameterized SQL queries
3. Validate all user input
4. Use strong hashing (bcrypt)
5. Hide internal error details
6. Use secure random generation

---

**Prepared By:**  
ADESIYAN ADEOLA SAMUEL  
CodeAlpha Cybersecurity Intern  
July 2026