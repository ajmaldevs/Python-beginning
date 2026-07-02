def main():
    spacecraft={
        "name":"PLUTO",

    }
    print(space_report(spacecraft))

def space_report(spacecraft):
    return f"""
    ============REPORT=============
    ...............................

    NAME : {spacecraft["name"]}
    DISTANCE : {spacecraft.get("distance","Unknown")} AU
    
    ...............................
    ===============================
    """

main()

#well in here even if we use {spacecraft["name"]} to call the key there is another way to do it 
# Using keyword .get() where it would be helpful for us to print something when the key is empty 
# the example is given above