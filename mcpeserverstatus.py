def MCPEServerStatus():
    import requests

    response = "https://api.mcstatus.io/v2/status/bedrock/" + input("Type In Ip:Port - ")
    response = requests.get(response)
    answer = input("What Type Of Data Would You Like To See From This Server(PlayerCount,OnlineStatus,MaxPlayers,Protocol,Gamemode,Edition,MOTD) - ")
    if answer == "PlayerCount":
        print(response.json()["players"]["online"])
    elif answer == "OnlineStatus":
      print(response.json()["online"])
    elif answer == "MaxPlayers":
      print(response.json()["players"]["max"])
    elif answer == "Protocal":
      print(response.json()["version"]["protocol"])
    elif answer == "Gamemode":
      print(response.json()["gamemode"])
    elif answer == "Edition":
      print(response.json()["edition"])
    elif answer == "MOTD":
      print(response.json()["motd"]["raw"])
    answer2 = input("Would You Like To Restart This Program If So Type In 1 - ")
    if answer2 == "1":
        MCPEServerStatus()
MCPEServerStatus()
