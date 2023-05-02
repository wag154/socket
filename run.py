from applications import app,socketio


if __name__ == "__main__":
    #so it can be switched between chatroom and server for production
    choice = int(input("Please Enter For Server[1] Or Chatroom[2] :"))
    if choice == 1:
        app.run(debug=True)
    elif choice == 2:
        socketio.run(app,debug= True)
    else:
        print("Please Enter Correct")   