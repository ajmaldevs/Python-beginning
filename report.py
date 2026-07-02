def main():
    spacecraft={
        "name":"Aryabatta",
        "distance":"100"

    }
    print(space_report(spacecraft))

def space_report(spacecraft):
    return f"""
    ============REPORT=============
    ...............................
    NAME : {spacecraft["name"]}
    DISTANCE : {spacecraft["distance"]}
    ...............................
    ===============================
    """

main()