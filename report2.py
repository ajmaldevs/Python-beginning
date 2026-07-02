def main():
    spacecraft={
        "name":"PLUTO",

    }
    #here i havent given the key "distance" but i use it there is another way to use it even if its not given what we could is
    #save the key distance as another one like 
    spacecraft["distance"]=329
    # this is the way which we could save a key in a distionary
    print(space_report(spacecraft))

def space_report(spacecraft):
    return f"""
    ============REPORT=============
    ...............................
    NAME : {spacecraft["name"]}
    DISTANCE : {spacecraft["distance"]}AU
    ...............................
    ===============================
    """

main()