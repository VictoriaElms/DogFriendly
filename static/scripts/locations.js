

function getLocations(){
    console.log("getting locations")
    const newDiv = document.createElement("div");
    const newContent  = document.createTextNode("locations");
    newDiv.appendChild(newContent);
    const currentDiv = document.getElementById("locations");
    document.body.insertBefore(newDiv, currentDiv);
}