def fizzbuzz():
    current = 1
    while True:
        result = ""
        #Ik doe += result als zodat het fizzbuzz wordt als current 
        #deelbaar is door zowel 3 als 5
        if current%3 == 0:
            result += "fizz"
        if current%5 == 0:
            result += "buzz"
        # als result nu nog leeg is dan wordt het str(current)
        result = result or str(current)
        yield result
        current += 1


