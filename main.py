print("Ticket System Started")

from database import create_table, connect_db
from utils import log_action

log_action("PROGRAM STARTED")
# Ensure database table exists
create_table()


def create_ticket():
    try:
        name = input("Enter your name: ")
        issue = input("Describe your issue: ")
        priority = input("Priority (Low/Medium/High): ")

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO tickets (name, issue, priority, status)
            VALUES (?, ?, ?, ?)
        """, (name, issue, priority, "Open"))

        conn.commit()
        conn.close()

        log_action(f"Ticket created by {name}")

        print("\nTicket saved successfully!\n")

    except Exception as e:
        print("Error creating ticket:", e)
        log_action(f"Error creating ticket: {e}")


def view_tickets():
    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tickets")
        tickets = cursor.fetchall()

        if not tickets:
            print("No tickets found.")
        else:
            for ticket in tickets:
                print(ticket)

        conn.close()

    except Exception as e:
        print("Error viewing tickets:", e)
        log_action(f"Error viewing tickets: {e}")


def update_ticket():
    try:
        ticket_id = input("Enter ticket ID to update: ")

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,))
        ticket = cursor.fetchone()

        if not ticket:
            print("Ticket not found.")
            conn.close()
            return

        print("\nCurrent Ticket:", ticket)

        new_status = input("Enter new status (Open/In Progress/Closed): ")

        cursor.execute("""
            UPDATE tickets
            SET status = ?
            WHERE id = ?
        """, (new_status, ticket_id))

        conn.commit()
        conn.close()

        log_action(f"Ticket {ticket_id} updated to {new_status}")

        print("Ticket updated successfully!")

    except Exception as e:
        print("Error updating ticket:", e)
        log_action(f"Error updating ticket: {e}")


def search_tickets():
    try:
        keyword = input("Enter name or issue keyword: ")

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM tickets
            WHERE name LIKE ? OR issue LIKE ?
        """, ('%' + keyword + '%', '%' + keyword + '%'))

        results = cursor.fetchall()

        if not results:
            print("No matching tickets found.")
        else:
            for ticket in results:
                print(ticket)

        conn.close()

        log_action(f"Search performed for keyword: {keyword}")

    except Exception as e:
        print("Error searching tickets:", e)
        log_action(f"Error searching tickets: {e}")


# Main menu loop
while True:
    print("\n===== IT SUPPORT TICKET SYSTEM =====")
    print("1. Create Ticket")
    print("2. View Tickets")
    print("3. Update Ticket Status")
    print("4. Search Tickets")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        create_ticket()
    elif choice == "2":
        view_tickets()
    elif choice == "3":
        update_ticket()
    elif choice == "4":
        search_tickets()
    elif choice == "5":
        print("Exiting system...")
        break
    else:
        print("Invalid choice. Please try again.")