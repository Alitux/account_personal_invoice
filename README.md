# Account Personal Invoices

[![License: GNU/GPL-3](https://img.shields.io/badge/licence-GPL--3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0-standalone.html)

## Description

This Odoo addon restricts the visibility and actions on sales invoices (`out_invoice`, `out_refund`) to only those invoices where the current user is assigned as the responsible salesperson (`invoice_user_id`). It also allows users to see invoices that do not have any responsible user assigned.

It's primarily designed to enhance data privacy and control in Odoo's Accounting module, especially in environments utilizing the Argentinian localization.

Key features include:
*   **Restricts access**: Users assigned to the "Personal Invoices" group will only see sales invoices where they are the `invoice_user_id` or if no `invoice_user_id` is set.
*   **New Security Group**: Introduces a dedicated "Personal Invoices" security group.
*   **Integrated Permissions**: Automatically grants access to the standard Odoo "Facturación/Contabilidad" menu for users in the "Personal Invoices" group.
*   **Compatibility**: Designed to integrate smoothly with the Argentinian localization (`l10n_ar_afipws_fe`).

## Installation

To install this module, you need to:

1.  Copy the `account_personal_invoice` folder to your Odoo addons path.
2.  Restart the Odoo server.
3.  Go to `Apps` > `Update Apps List`.
4.  Search for "Account Personal Invoices" and click "Install".
    *   **Important**: If you encounter issues or previous updates didn't apply correctly, try to **uninstall the module first, then reinstall it**. This ensures all XML changes and hooks are properly applied.

## Configuration

After installation, configure the module for your users:

1.  Go to `Settings` > `Users & Companies` > `Users`.
2.  Select the user you want to restrict.
3.  In the `Access Rights` tab:
    *   Assign the **"Personal Invoices"** group (found under "Accounting"). This group will automatically grant access to the "Facturación/Contabilidad" menu.
    *   **Crucially**: Ensure this user **does NOT** have administrator privileges (e.g., "Administration / Access Rights") or any other group that grants full access to invoices (like "Facturación / Ver todos los documentos"), as these will bypass the restrictions. This module is intended for non-administrator users.
4.  Save the user.

## Usage

To effectively use this module:

1.  Ensure the users who should only see their own invoices are assigned to the "Personal Invoices" security group (and no conflicting groups, as mentioned above).
2.  Log in as a restricted user. They will now only see sales invoices (customer invoices and refunds) where:
    *   They are specified as the `Responsable de Factura` (`invoice_user_id`).
    *   The `Responsable de Factura` field is empty (no user assigned).
3.  Access to actions like "Validar" (Validate) will be controlled by their membership in the "Personal Invoices" group (which implies standard invoicing permissions).

## Bug Tracker

Bugs are tracked on the project's repository. If you have any issues, please open an issue there.

## Credits

### Authors

*   **Alitux** [www.alitux.com.ar](https://www.alitux.com.ar)

### Maintainers

This module is maintained by Alitux.