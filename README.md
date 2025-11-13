# Account Personal Invoices

[![License: GNU/GPL-3](https://img.shields.io/badge/licence-GPL--3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0-standalone.html)


## Description

This Odoo addon allows users to see only their own invoices. It's designed to work with the Argentinian localization.

Key features include:
*   Restricts users to view only their own invoices.
*   Adds a new security group "Personal Invoices" for this purpose.
*   Integrates with the Argentinian localization to validate invoices.

## Installation

To install this module, you need to:

1.  Copy the `account_personal_invoices` folder to your Odoo addons path.
2.  Restart the Odoo server.
3.  Go to `Apps` > `Update Apps List`.
4.  Search for "Account Personal Invoices" and click "Install".

## Configuration

After installation, you can configure the module by following these steps:

1.  Go to `Settings` > `Users & Companies` > `Users`.
2.  Select the user you want to restrict.
3.  In the `Access Rights` tab, under the "Accounting" Section, select the "Personal Invoices" dropdown.
4.  Save the user.

## Usage

To use this module:

1.  Assign the "Personal Invoices" group to a user.
2.  Log in as that user.
3.  The user will only be able to see the invoices where they are the salesperson.

## Bug Tracker

Bugs are tracked on the project's repository. If you have any issues, please open an issue there.

## Credits

### Authors

*   **Alitux** [www.alitux.com.ar](https://www.alitux.com.ar)

### Maintainers

This module is maintained by Alitux.
