def main():
    spacecraft={
        "name":"PLUTO",

    }
    spacecraft.update({
        "Distance": 0.11,
        "Orbit": "sun"
    })
    print(space_report(spacecraft))

def space_report(spacecraft):
    return f"""
    ============REPORT=============
    ...............................

    NAME : {spacecraft["name"]}
    DISTANCE : {spacecraft.get("distance","Unknown")}AU
    ORBIT : {spacecraft.get("Orbit")}
    
    ...............................
    ===============================
    """

main()

#Here what i used .update() is another method to add key to the dictionary what .update helps us with is that it can add upto 2
#or more keys to infinity