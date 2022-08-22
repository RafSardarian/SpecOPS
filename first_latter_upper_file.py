with open("Lorem_Ipsum", "r") as file1:
    with open("upper_file", "w") as file2:
        new_text = file1.read()
        new_text = new_text.title()
        file2.write(new_text)
    print(file2)