def main():
    name=["Mario","Luigi","Daisy","Yoshi"]
    fro="Princess Peach"
    for n in (name):
        print(write_letter(n,fro))

def write_letter(name,fro):
        return f"""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     Dear {name},
     you are cordially invited to a ball 
     at Peatch's castle this evening at
     7:00 PM
     sincerely,{fro}
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

main()
