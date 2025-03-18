def read_and_modify_file():
    """
    Reads a user-specified file, converts its content to uppercase,
    and writes it to a new file while handling errors gracefully.
    """
    filename = input("Enter the filename to read: ")

    try:
        # Read the content of the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content (convert to uppercase)
        modified_content = content.upper()

        # Define the new filename
        new_filename = "modified_" + filename

        # Write the modified content to the new file
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"File processed successfully! Modified content saved in '{new_filename}'.")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: You don’t have permission to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
