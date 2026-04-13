#                                                   CONTACT BOOK APPLICATION USING PYTHON

contacts = {}

while True:
    print("Contact Book App")
    print("1. Create Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count Contact")
    print("7. Exit")

    choice = int(input("enter your choice: "))

    if choice == 1:
        name = input("Enter your name: ")
        if name in contacts:
            print('Contact name',{name},'already exists!')
        else:
            age = input("Enter age: ")
            email = input("Enter email: ")
            mobile = input("Enter mobile number: ")
            contacts[name] = {'age':int(age), 'email':email, 'mobile':mobile}
            print('Contact name ',{name},'has been created successuflly!')

    elif choice == 2:
        name = input ("Enter contact name to view: ")
        if name in contacts:
            contact = contacts[name] 
            print('Name:',{name},'\n''Age:',{age},'\n''Mobile Number:',{mobile},'\n''Email:',{email},)
        else:
            print("Contact not found!")

    elif choice == 3:
        name = input("Enter name to update contact: ")
        if name in contacts:
            name = input("Enter updated name: ")
            age = input("Enter updated age: ")
            email = input("Enter updated email: ")
            mobile = input("Enter updated mobile number: ")
            contacts[name] = {'age':int(age), 'email':email, 'mobile':mobile}

        else:
            print("Contact not found!")

    elif choice == 4:
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact name",{name},"has been deleted successfully!")
        else:
            print("Contact not found")

    elif choice == 5:
        search_name = input("Enter contact name to search: ")
        found = False
        for name,contact in contacts.items():
            if search_name.lower() in name.lower():
                print('Found - Name' ,{name},'\n''Age:',{age},'\n''Mobile Number:' ,{mobile},'\n''Email:',{email},)
        if not found:
            print("No contact found with that name")

    elif choice == 6:
        print("Total contacts in your book :", {len(contacts)})

    elif choice == 7:
        print("Good bye.....Closing the program")
        break

    else:
        print("invalid input")