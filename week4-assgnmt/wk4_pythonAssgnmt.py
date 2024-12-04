# File Read & Write with Error Handling

# Step 1: Ask for the input filename
input_filename = input("Enter the input filename to read: ")

try:
    # Step 2: Read from the input file
    with open('myData.txt', "r") as file:
        content = file.read()
        print("Original Content:", content)

    # Step 3: Modify the content
    modified_content = content.upper()  

    # Step 4: Write to a new file
    output_filename = "output_file.txt"
    with open(output_filename, "w") as file:
        file.write(modified_content)
        print(f"Modified content written to '{output_filename}'.")

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' does not exist.")
except PermissionError:
    print(f"Error: You do not have permission to read the file '{input_filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
