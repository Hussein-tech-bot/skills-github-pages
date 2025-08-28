# ==============================
# Interactive File Handling Master Program 🗂️
# ==============================

def modify_content(content):
    """
    Example modification function.
    Currently converts content to uppercase.
    You can change this to any modification you like.
    """
    return content.upper()


def process_file():
    # Ask user for the input filename
    filename = input("\nEnter the filename to read (or type 'quit' to exit): ")
    if filename.lower() == "quit":
        return False  # signal to exit the loop

    try:
        # Open the original file for reading
        with open(filename, "r") as infile:
            content = infile.read()
        print("File read successfully!")

        # Modify the content
        modified_content = modify_content(content)

        # Ask user for output filename
        output_filename = input("Enter the filename to save the modified content: ")

        # Write the modified content to a new file
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)
        print(f"Modified content written to '{output_filename}' successfully!")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read/write '{filename}'.")
    except Exception as e:
        print("An unexpected error occurred:", e)

    return True  # continue loop


def main():
    print("=== Interactive File Handling Program ===")
    print("You can read, modify, and save multiple files.")
    print("Type 'quit' as the filename to exit.")

    while True:
        if not process_file():
            break

    print("\nGoodbye! 👋")


if __name__ == "__main__":
    main()
