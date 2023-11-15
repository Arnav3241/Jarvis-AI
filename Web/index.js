console.log("Status: Connected!")

document.getElementById("Chat").className = "hidden";

const chat = () => {
    document.getElementById("Dashboard").className = "hidden";
    document.getElementById("Chat").className = "";
}


const dashboard = () => {
    document.getElementById("Dashboard").className = "";
    document.getElementById("Chat").className = "hidden";
}
