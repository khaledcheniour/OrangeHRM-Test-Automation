# Test Steps

## Login (tests/test_login.py)

### test_login_with_valid_credentials
1. Open the login page.
2. Enter username `Admin`.
3. Enter password `admin123`.
4. Click Login.
5. Land on the Dashboard.

### test_login_with_invalid_credentials
1. Open the login page.
2. Enter username `Admin`.
3. Enter password `wrong_password`.
4. Click Login.
5. See the "Invalid credentials" error banner.

### test_login_with_empty_credentials
1. Open the login page.
2. Leave username empty.
3. Leave password empty.
4. Click Login.
5. See 2 "Required" field errors.

## Dashboard (tests/test_dashboard.py)

### test_dashboard_loads_after_login
1. Log in as `Admin` / `admin123`.
2. See the Dashboard header.

### test_navigate_to_pim
1. Log in as `Admin` / `admin123`.
2. Click the `PIM` side-menu item.
3. Breadcrumb header becomes `PIM` and URL contains `/pim/`.

### test_logout_returns_to_login
1. Log in as `Admin` / `admin123`.
2. Open the user dropdown (top-right).
3. Click Logout.
4. Land back on the login page.

## Employee List (tests/test_employee_list.py)

### test_employee_list_loads
1. Log in as `Admin` / `admin123`.
2. Go to the Employee List page.
3. Page loads and reports a record count.

### test_every_visible_row_has_an_id
1. Log in as `Admin` / `admin123`.
2. Go to the Employee List page.
3. Read the Id of every visible row.
4. Every Id is non-empty.

## Add Employee (tests/test_add_employee.py)

### test_add_new_employee
1. Log in as `Admin` / `admin123`.
2. Go to the Add Employee page.
3. Capture the auto-generated Employee Id.
4. Fill First Name.
5. Fill Last Name.
6. Fill Middle Name (optional).
7. Click Save.
8. Go to the Employee List page.
9. Search by the captured Employee Id.
10. The new employee appears in the list.

## Admin User Search (tests/test_admin_user_search.py)

### test_search_user_by_username
1. Log in as `Admin` / `admin123`.
2. Go to the User Management page.
3. Fill the Username filter with `Admin`.
4. Click Search.
5. Wait for results to reload.
6. `Admin` is in the results and the result count is at least 1.

## Add Candidate (tests/test_add_candidate.py)

### test_add_new_candidate
1. Log in as `Admin` / `admin123`.
2. Go to the Add Candidate page.
3. Fill First Name.
4. Fill Last Name.
5. Fill Email (unique).
6. Click Save.
7. The candidate is saved successfully.
