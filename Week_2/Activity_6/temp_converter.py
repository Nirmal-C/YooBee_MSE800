class Converter:
    # Convert Celsius to Fahrenheit
    def convertC(self, c):
        return round((c * 9 / 5) + 32, 2)

    # Convert Fahrenheit to Celsius
    def convertF(self, f):
        return round((f - 32) * 5 / 9, 2)


if __name__ == "__main__":
    while True:
        try:
            temp_input = input("Enter temperature in Celsius or Fahrenheit (e.g., C25 or F77): ")
            converter = Converter()

            if temp_input.startswith('C'):
                # Remove the 'C' and convert remaining text to a number
                temp = float(temp_input[1:])
                # Convert Celsius to Fahrenheit
                print(f"{temp_input} degrees Celsius is converted to {converter.convertC(temp)} degrees Fahrenheit.")

            # User entered a Fahrenheit value (e.g., F77)
            elif temp_input.startswith('F'):
                # Remove the 'F' and convert remaining text to a number
                temp = float(temp_input[1:])
                # Convert Fahrenheit to Celsius
                print(f"{temp_input} degrees Fahrenheit is converted to {converter.convertF(temp)} degrees Celsius.")

            else:
                raise ValueError

        except ValueError:
            print("Invalid input. Please enter a temperature starting with 'C' or 'F' (e.g., C25 or F77).")
