const express = require('express')
const app = express()
const port = 3010
const mongoose = require('mongoose');
const { Cat } = require('./model');

// mongodb connection
const connectDB = async() => {
    await mongoose.connect(`mongodb+srv://mongose_username:password@atlascluster.zirft53.mongodb.net/mydb`)

    console.log(`the db is connected with ${mongoose.connection.host}`);
}

connectDB()

app.get('/', async(req, res) => {
  const cat = new Cat({
    name: "Mehedi"
  })
  const data = await cat.save()
  res.send(data)
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})