var express = require("express")
var bodyParser = require("body-parser")
const { Socket } = require("socket.io")
var app = express()
var http = require('http').Server(app)
var io = require('socket.io')(http)

app.use(express.static(__dirname))
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended: false}))

var messages = [
    {name: "jane", message: "Hello"},
    {name: "John", message: "Hi"}
] 

app.get('/messages', (req, res) => { // route and res and req
    res.send(messages)
})

app.post('/messages', (req, res) => { // route and res and req
    messages.push(req.body)
    io.emit('message', req.body)
    res.sendStatus(200)
})

io.on('connection', (Socket) => {
    console.log(' user connected')
})

var server = http.listen(3010, () => {

    console.log("Server is listening on port ", server.address().port)

})