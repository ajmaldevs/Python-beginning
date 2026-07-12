def total(galleons,sickles,knuts):
    return ((galleons* 17+sickles)* 29+knuts)


coins=[100,23,40]
print(total(*coins),'knuts')