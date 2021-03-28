config = {
    "IOS":"exec-timeout 15 0",
    "NXOS":"exec-timeout 15"
}
get_choice = input("Please enter IOS type (IOS/NXOS) : ")
if (get_choice == "IOS"):
    print(config.get("IOS"))
if (get_choice == "NXOS"):
    print(config.get("NXOS"))
