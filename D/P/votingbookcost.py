'''Write a python program to get Inputs:
MyName(string), Adhar No(number), date_of_birth (date format), 2D List of 5 favourite Books with its cost (Rs.) using sublist, Tuples of voting parties with their acronyms.
Functions/Processes:
Write a function IdoVote() to check eligibility condition of voting
Write a function convert() a Rupees value into Dollars as US value.
Write a function Display() to display all information in neat format as given below using necessary format specifiers.'''

def get_inputs():
  """Prompts the user to enter their name, Aadhaar number, date of birth, favorite books, and voting parties."""

  # Get user name.
  name = input("Enter your name: ")

  # Get Aadhaar number.
  adhaar_number = int(input("Enter your Aadhaar number: "))

  # Get date of birth.
  date_of_birth = input("Enter your date of birth (DD-MM-YYYY): ")

  # Get favorite books.
  favorite_books = []
  for i in range(5):
    book_name = input("Enter your favorite book name {}: ".format(i + 1))
    book_cost = float(input("Enter the cost of {} in Rs.: ".format(book_name)))
    favorite_books.append([book_name, book_cost])

  # Get voting parties.
  voting_parties = []
  for i in range(5):
    party_name = input("Enter your favorite voting party name {}: ".format(i + 1))
    party_acronym = input("Enter the acronym of {}: ".format(party_name))
    voting_parties.append((party_name, party_acronym))

  return name, adhaar_number, date_of_birth, favorite_books, voting_parties


def ido_vote(age):
  """Checks the eligibility condition of voting.

  Args:
    age: The age of the user.

  Returns:
    True if the user is eligible to vote, False otherwise.
  """

  return age >= 18


def convert_to_dollars(rupees):
  """Converts a Rupees value into Dollars as US value.

  Args:
    rupees: The amount in Rupees.

  Returns:
    The equivalent amount in Dollars.
  """

  return rupees / 75


def display(name, adhaar_number, date_of_birth, favorite_books, voting_parties):
  """Displays all information in a neat format.

  Args:
    name: The user name.
    adhaar_number: The user Aadhaar number.
    date_of_birth: The user date of birth.
    favorite_books: A list of user favorite books.
    voting_parties: A list of user favorite voting parties.
  """

  # Calculate the total cost of books in Dollars.
  total_book_cost_in_dollars = 0
  for book in favorite_books:
    total_book_cost_in_dollars += convert_to_dollars(book[1])

  # Calculate the age of the user.
  from datetime import datetime
  today = datetime.today()
  date_of_birth = datetime.strptime(date_of_birth, "%d-%m-%Y")
  age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))

  # Display the information.
  print("""
My Name : {}                                                                           MyID: {}                                D-O-B: {} Eligible to vote: {}
My Fovourite Books                                                                                                   My Regional Parties                       Party Name
Book Name
Cost($)
                                                                                                                                                               ShortForm_of_Party
""".format(name, adhaar_number, date_of_birth, "Yes" if ido_vote(age) else "No"))

  for i in range(len(favorite_books)):
    print("{}. {} : {}".format(i + 1, favorite_books[i][0], convert_to_dollars(favorite_books[i][1])))

  print()

  for i in range(len(voting_parties)):
    print("{}. {} : {} {}".format(i + 1, voting_parties[i][0], voting_parties[i][1], " " * (10 - len(voting_parties[i][1]))))

  print()

  print("                                                                                                            Page  2")


def main():
  """The main function."""

  name, adhaar_number, date_of_birth, favorite_books, voting_parties = get_inputs()
  display(name, adhaar_number, date_of_birth, favorite_books, voting_parties)


if __name__ == "__main__":
  main()
