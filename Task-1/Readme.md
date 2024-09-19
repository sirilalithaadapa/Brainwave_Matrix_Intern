# ATM System

A Python-based **ATM System** that allows users to deposit, withdraw, and check their balance, along with an admin panel for user management. The system mimics a real-world ATM by supporting multiple users, enforcing daily withdrawal limits, and providing an administrative mode for managing users.

## Features

- **Multi-User System**: Each user is identified by their unique card number and PIN.
- **Account Balance**: Users can check their account balance.
- **Deposits and Withdrawals**: Users can deposit money or withdraw up to their daily withdrawal limit.
- **Daily Withdrawal Limit**: Each user has a daily withdrawal limit that resets at midnight.
- **Incorrect PIN Lockout**: Users are allowed a limited number of PIN attempts before their session is locked.
- **Admin Panel**: Special admin mode (`0000` PIN) to view users or reset PINs.
- **Transaction Logs**: Users can view their transaction history in a real-world extension.

## Requirements

This system runs on **Python 3.x**.

Ensure you have the following installed:
- Python 3.x (https://www.python.org/downloads/)
- No additional Python libraries are required.

## Installation and Setup

1. Run the script:

   ```bash
   python atm.py
   ```

## How to Use

### User Mode

1. **Insert Card**: You will be prompted to enter your card number (e.g., `1234` for John Doe or `5678` for Jane Smith).
2. **Authenticate with PIN**: Enter your 4-digit PIN. After successful authentication, you can:
   - **Check Balance**: View your current account balance.
   - **Deposit**: Deposit money into your account.
   - **Withdraw**: Withdraw up to your daily withdrawal limit. If you exceed this limit or your balance, the transaction will be denied.
   - **Exit**: Finish your session and eject your card.

### Admin Mode

1. To access admin mode, enter the admin PIN (`0000`) when prompted.
2. Admin options include:
   - **View All User Data**: See all users' names, balances, and card numbers.
   - **Reset User PIN**: Change any user's PIN by entering their card number and the new 4-digit PIN.

### User Data

The following test users are available by default:

| Card Number | User        | PIN  | Balance |
|-------------|-------------|------|---------|
| 1234        | John Doe    | 1111 | $1000.0 |
| 5678        | Jane Smith  | 2222 | $1500.0 |

You can also reset these values via the **Admin Panel**.

## Future Enhancements

Some possible future enhancements include:
- **Interest Rate Calculation**: Add interest accumulation for savings.
- **Transaction History**: Save and display detailed transaction logs.
- **Session Timeout**: Automatically log users out after a period of inactivity.
- **Database Integration**: Store user data in a database for persistence.
  
## Contribution

Feel free to open issues or submit pull requests if you'd like to improve the ATM system!
