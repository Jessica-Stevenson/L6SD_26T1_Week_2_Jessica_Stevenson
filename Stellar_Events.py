#Vendor Class
class Vendor:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

#The action menu
def action_menu():
    print("\nWhat would you like to do?")
    print("[1] View Vendors--------------------------------[4] Search for Vendor")
    print("[2] Add Vendor----------------------------------[5] Add Extra Details")
    print("[3] Remove Vendor-------------------------------[6] To Exit the program")
    return input("> ")

#View Vendors
def view_vendors(vendors):
    #Will show if there are no Vendors
    if not vendors:
        print("\nNo vendors found.")
        return

    #This will show all the vendors
    print("\n--- Vendor List ---")
    for i, vendor in enumerate(vendors, start=1):
        print(f"[{i}] Name: {vendor.name} | Phone: {vendor.phone} | Email: {vendor.email}")

#Add Vendors
def add_vendors(vendors):
    #Asks for Input
    name = input("Please enter the vendor's name: ").strip()
    phone = input("Please enter the vendor's phone number: ").strip()
    email = input("Please enter the vendor's email: ").strip()
    
    #Add's a new Vendor object
    new_vendor = Vendor(name, phone, email)
    #Adds it to the list
    vendors.append(new_vendor)

    #Success Message
    print(f"\nVendor '{name}' added successfully!")
    return



#Some Base Vendors
vendors = [
    Vendor("ABC Supplies", "021-555-111", "abc@example.com"),
    Vendor("Kiwi Tools", "021-555-222", "kiwitools@example.com")
]


#Make's sure you are viewing the Vendor menu
while True:
    choice = action_menu()

    if choice == "1":
        view_vendors(vendors)
        input("contiune press [enter]" )
    elif choice == "2":
        add_vendors(vendors)
        input("to contiune press [enter]" )

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Option not implemented yet.")
