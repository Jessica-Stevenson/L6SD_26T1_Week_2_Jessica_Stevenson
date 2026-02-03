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
    print("\nVendor List")
    for i, vendor in enumerate(vendors, start=1):
        print(f"[{i}] Name: {vendor.name} | Phone: {vendor.phone} | Email: {vendor.email}")
    
    #Shows any extra attributes
    extras = {key: details for key, details in vendor.__dict__.items() if key not in ("name", "phone", "email")}
    if extras:
        for key, details in extras.items():
            print(f"    - {key}: {details}")


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

#Remove Vendors
def remove_vendor(vendors):
    if not vendors:
        print("\nNo vendors to remove.")
        return
    
    #Shows a list of Vendors
    print("\nRemove Vendor")
    view_vendors(vendors)

    #User Input
    choice = input("\nEnter the number of the vendor to remove (or press Enter to cancel): ").strip()

    #Cancel if they press Enter
    if choice == "":
        print("Cancelled.")
        return

    #check it's a number
    if not choice.isdigit():
        print("Invalid input. Please enter a number.")
        return

    #Make sure it works with the lists
    index = int(choice) - 1  

    #Check range
    if index < 0 or index >= len(vendors):
        print("That number is out of range.")
        return

    vendor_to_remove = vendors[index]

    #Confirmation Message
    confirm = input(f"Are you sure you want to remove '{vendor_to_remove.name}'? (y/n): ").strip().lower()
    if confirm != "y":
        print("Cancelled")
        return
    
    #The removal
    removed = vendors.pop(index)
    print(f"\nVendor '{removed.name}' removed successfully!")

#Search Vendors
def search_vendor(vendors):
    #Checks if there are no vendors
    if not vendors:
        print("\nNo vendors to search.")
        return

    #Search Input
    print("\nSearch Vendor")
    search = input("Enter name, phone, or email to search: ").strip().lower()

    #Cancels if enter is pressed with no other input
    if search == "":
        print("Search cancelled (empty search).")
        return
    
    #Checks for Matches
    matches = []
    for vendor in vendors:
        #Combie all searchable parts
        haystack = f"{vendor.name} {vendor.phone} {vendor.email}".lower()
        if search in haystack:
            matches.append(vendor)

    #If there are no matches
    if not matches:
        print(f"\nNo vendors found matching: '{search}'")
        return

    #Prints the matches
    print(f"\nFound {len(matches)} match(es):")
    for i, vendor in enumerate(matches, start=1):
        print(f"[{i}] Name: {vendor.name} | Phone: {vendor.phone} | Email: {vendor.email}")

#Add Details
def add_details():
    #checks if there are vendors
    if not vendors:
        print("\nNo vendors available to update.")
        return

    #Shows a list of vendors
    print("\nAdd Extra Details")
    view_vendors(vendors)

    #Asks what vendor to add details too
    choice = input("\nEnter vendor number to update (or press Enter to cancel): ").strip()
    if choice == "":
        print("Cancelled.")
        return
    #Checks if the input is vaild
    if not choice.isdigit():
        print("Invalid input. Please enter a number.")
        return

    #Checks if there is a vendor on the inputted Index
    index = int(choice) - 1
    if index < 0 or index >= len(vendors):
        print("That number is out of range.")
        return

    vendor = vendors[index]

    # Ask user for attribute name
    attr = input("Enter the attribute name to: ").strip()

    #Cancles if Space is pressed without anything else
    if attr == "":
        print("Cancelled (no attribute name).")
        return

    #Prevent overwriting base fields
    protected = {"name", "phone", "email"}
    if attr.lower() in protected:
        print(f"'{attr}' is a protected field and cannot be added/changed here.")
        return

    #makes sure the name is valid
    if not attr.isidentifier():
        print("Invalid attribute name. Use letters/numbers/underscore and don't start with a number please")
        return

    #This is for inputting the details
    details = input(f"Enter details: '{attr}': ").strip()
    if details == "":
        print("Cancelled (no details).")
        return

    #Add/update attribute
    setattr(vendor, attr, details)

    print(f"Saved extra detail for '{vendor.name}': {attr} = {details}")

#Some Base Vendors
vendors = [
    Vendor("Revoultionary Supplies", "021-555-111", "Revoultionary@example.com"),
    Vendor("Kiwi Tools", "021-555-222", "kiwitools@example.com")
]


#Make's sure you are viewing the Vendor menu whenever nothing else is happening
while True:
    choice = action_menu()

    #View Vendors
    if choice == "1":
        view_vendors(vendors)
        input("contiune press [enter]" )
    
    #Add Vendors
    elif choice == "2":
        add_vendors(vendors)
        input("to contiune press [enter]" )

    #Remove Vendors
    elif choice == "3":
        print("please choose a vendor to remove")
        remove_vendor(vendors)
        input("to contiune press [enter]" )

    #Search Vendors
    elif choice == "4":
        search_vendor(vendors)
        input("to contiune press [enter]" )

    #Add Extra details
    elif choice == "5":
        add_details()
        input("to contiune press [enter]" )

    #Exit
    elif choice == "6":
        print("Goodbye!")
        break
    
    #Appears when user is being stupid and puts an invalid input
    else:
        print("no.")
