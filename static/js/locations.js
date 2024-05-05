async function displayLocations() {
    console.log("getting locations")
    const loc_div = document.getElementById("locations-container")

    locations = getLocations().then((locations) => {
        for (let idx in locations) {
            let formatted = formatLocation(locations[idx])
            loc_div.appendChild(formatted)
        }
    });

    console.log(locations)
    console.log("done")
}


async function getLocations() {
    const response = await fetch("http://127.0.0.1:5000/api/locations");
    return response.json();
}

function formatLocation(location) {
    let para = document.createElement("p");
    let node = document.createTextNode(location.name);
    para.appendChild(node);
    return para
}


// <h3 align="left;">Patios</h3>
//     <p align="left" style="font-size: 20px;">
//         The Bicycle Thief
//         <br>
//         Dog Friendly Patio
//         <br>
//         1475 Lower Water St. Halifax
//         <br>
//         Monday – Sunday 11:30am – 11:00pm
//         </p>
//         <input type="checkbox" id="saveToProfile" name="saveToProfile" value="save">
//         <label for="saveToProfile"> Save to Profile</label><br>
// <br></br>