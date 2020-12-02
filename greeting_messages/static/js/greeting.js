let message_array = 
[
    
    {
        message: "Happy Diwali!",
        name: "Gopinath"
    },

    {
        message: "Happy New Year",
        name: "Sagar"
    },

    {
        message: "Hapy Holi!",
        name: "Yash"
    },

    {
        message: "Happy New Year!",
        name: "Bombay"
    },

    {
        message: "Happy Thanksgiving!",
        name: "Abhilash"
    },

    {
        message: "Happy Halloween!!!",
        name: "Prateek"
    },

    {
        message: "Happy Christmas!!",
        name: "Shafeeq"
    },

    {
        message: "Happy Easter!!",
        name: "Pranav"
    }
]
var div_string= "", index;
for (index=0; index<8; index++){

    div_string += "<div class='textarea'> <div class='title'> <h4>" + message_array[index].message + "</h4><p> (message)</p></div>"+"<div class='description'><h4> " +message_array[index].name + "</h4><p> (name)</p></div></div>";
}
document.getElementById("greetingcard").innerHTML = div_string;