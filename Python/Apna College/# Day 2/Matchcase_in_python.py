#Match case ---------->alternate for if,elif,else
from annotated_types.test_cases import cases

color = input("enter the color: ")
match color:
    case "green":
        print("GO!")
    case "red":
        print("Stop")
    case "Orange":
        print("Get Ready")
    case _ :
        print("invalid input")


color = input("enter the color: ")
match color:
    case "green":
        print("GO!")
    case "red":
        print("Stop")
    case "Orange":
        print("Get Ready")
    case _ :
        print("invalid input")
