import { useState,useEffect } from 'react'
import axios from 'axios'
import './App.css'
//npm install socket.io-client for this import, needed to connect back and frontend
import io from "socket.io-client"

function App() {
  const [count, setCount] = useState(0)
  const [messages, setMessages] = useState([])
  //This will connect to the socket
  const socket = io("http://127.0.0.1:5000")

  //Asks whether the request to connect above(io(url) has been successful)
  socket.on('connect',()=>{
    console.log('connected!')
  })
  const sendMessage =async()=>{
    try{
      //This is a socket equivalent of a POST method
      socket.emit('message',{text: "Hello"})
    }
    catch{
      console.log("Error")
    }
  }
  const getTest = async()=>{
    try{
      resp = await axios.get()
    }
    catch(e){
      console.log(e)
    }
  }
  return (
    <>
   <button onClick={sendMessage}>Send</button>
    </>
  )
}

export default App
