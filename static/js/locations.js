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
    let locationName = document.createTextNode("Name: " + location.name);
    let br1 = document.createElement("br");
    let locationCategory = document.createTextNode("Category: " + location.category);
    let br2 = document.createElement("br");
    let locationAddress = document.createTextNode("Address: " + location.address);
    let br3 = document.createElement("br");
    let locationHours = document.createTextNode("Hours: " + location.hours);
    let br4 = document.createElement("br")
    let locationButton = document.createElement("button")
    locationButton.onclick = () => saveLocation(location.name)
    para.appendChild(locationName);
    para.appendChild(br1);
    para.appendChild(locationCategory);
    para.appendChild(br2);
    para.appendChild(locationAddress);
    para.appendChild(br3);
    para.appendChild(locationHours);
    para.appendChild(br4)
    para.appendChild(locationButton)
    return para;
}

function saveLocation(id) {
    fetch(`http://127.0.0.1:5000/api/locations/save?id=${id}`);
}

document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('searchInput');
    const locationsList = document.getElementById('locationsList');

    searchInput.addEventListener('input', function (event) {
        const searchQuery = event.target.value.toLowerCase();
    });
});