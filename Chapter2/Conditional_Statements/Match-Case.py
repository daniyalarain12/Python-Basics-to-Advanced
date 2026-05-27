# MATCH CASE

color = input("ENTER COLOR : ")

match color:                       # MATCH THE COLOR WITH DIFFERENT CASES
    case "green":
        print("GO")
    case "red":
        print("STOP")
    case "yellow":
        print("LOOK")
    case _:                        # DEFAULT CASE IF NO COLOR MATCHES
        print("LIGHT IS BROKEN")
