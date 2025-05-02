"""

Create a Contact book which will store the person's name and their respective contact number
the book will have following features:
1. Add contact
2. View contact
3. Delete contact
4. Search contact by name

"""
import os
import json

class ContactBook:
  def __init__(self):
    self.contact_file = "data.json"

  def load_contact(self):
    if not os.path.exists(self.contact_file):
      return []
    with open(self.contact_file, 'r') as file:
      return json.load(file)

  def save_contact(self, contacts):
    with open(self.contact_file, 'w') as file:
      json.dump(contacts, file, indent=1)

  def add_contact(self):
    name = input("Enter name: ")
    phone = input("Enter contact: ")
    email = input("Enter email: ")
    contacts = self.load_contact()
    contacts.append({ "name": name, "email": email, "phone": phone })
    self.save_contact(contacts=contacts)
    print("✅ Contact added!")

  def view_contacts(self):
    contacts = self.load_contact()
    if not contacts:
      print("📭 No contacts found.")
      return
    for idx, contact in enumerate(contacts, start=1):
      print(f"{idx}. {contact['name']} | 📞 {contact['phone']} | ✉️ {contact['email']}")

  def delete_contact(self):
    self.view_contacts()
    num = int(input("Enter contact number to delete: "))
    contacts = self.load_contact()
    if 1 <= num <= len(contacts):
      removed = contacts.pop(num - 1)
      self.save_contact(contacts=contacts)
      print(f"🗑️ Deleted: {removed['name']}")
    else:
      print("❌ Invalid contact number.")

  def update_contact(self):
    self.view_contacts()
    num = int(input("Enter contact number to update: "))
    contacts = self.load_contact()
    if 1 <= num <= len(contacts):
        contact = contacts[num - 1]
        print("Leave field blank to keep current value.")
        name = input(f"Enter new name [{contact['name']}]: ") or contact['name']
        phone = input(f"Enter new phone [{contact['phone']}]: ") or contact['phone']
        email = input(f"Enter new email [{contact['email']}]: ") or contact['email']
        contacts[num - 1] = {"name": name, "phone": phone, "email": email}
        self.save_contact(contacts=contacts)
        print("✅ Contact updated.")
    else:
        print("❌ Invalid contact number.")

  def search_contact(self):
    query = input("🔍 Enter name to search: ").lower()
    contacts = self.load_contact()
    results = [c for c in contacts if query in c['name'].lower()]
    if results:
        for contact in results:
            print(f"👤 {contact['name']} | 📞 {contact['phone']} | ✉️ {contact['email']}")
    else:
        print("❌ No matching contact found.")

  def show_menu(self):
    print("\n📒 Contact Book Menu")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

  def menu(self):
    while True:
      self.show_menu()
      choice = input("Choose an option (1-6): ")
      if choice == '1':
        self.add_contact()
      elif choice == '2':
        self.view_contacts()
      elif choice == '3':
        self.search_contact()
      elif choice == '4':
        self.update_contact()
      elif choice == '5':
        self.delete_contact()
      elif choice == '6':
        print("👋 Goodbye!")
        break
      else:
        print("⚠️ Invalid choice. Try again.")

contact_book = ContactBook()
contact_book.menu()