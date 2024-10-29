const express = require("express");
const app = express();   // assigning the express into the app variable


// app.get("root_url", callback_function)     callback function is standerd code of node js
app.get("/", (req, res)=>{
res.json([
    {
        id : 1,
        name : "sam",
        age : 23
    },
    {
        id : 2,
        name : "jay",
        age : 22
    }, 
    {
        id : 3,
        name : "may",
        age : 27
    }, 
    {
        id : 4,
        name : "roy",
        age : 29
    }, 
    {
        id : 5,
        name : "sid",
        age : 27
    }
])
});

// app.listen(Port Number, callback_function)     callback function is standerd code of node js
app.listen(5000, ()=>{
    console.log("app is running on 5000 port")
})