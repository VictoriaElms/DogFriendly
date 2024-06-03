async function displayLocations() {
    const loc_div = document.getElementById("locations-container")
    loc_div.innerHTML = ""

    locations = getLocations().then((locations) => {
        for (let idx in locations) {
            let formatted = formatLocation(locations[idx])
            loc_div.appendChild(formatted)
        }
    });

    const favButton = document.getElementById("filterFavoritesButton")
    favButton.innerHTML = "Show Favourites"
    favButton.onclick = () => { getSavedLocations() }
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
    if (location.saved) {
        locationButton.innerText = "Remove from favourites";
    } else {
        locationButton.innerText = "Save to favourites";
    }
    locationButton.style.borderRadius = "10px";
    locationButton.style.boxShadow = "0 4px 8px 0 rgba(0, 0, 0, 0.2)";
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
    const loc_div = document.getElementById("locations-container")

    const favButton = document.getElementById("filterFavoritesButton")
    if (favButton.innerHTML == "Hide Favourites") {
        locations = savedLocations().then((locations) => {
            loc_div.innerHTML = ""
            for (let idx in locations) {
                let formatted = formatLocation(locations[idx])
                loc_div.appendChild(formatted)
            }
        });
    } else {
        locations = getLocations().then((locations) => {
            loc_div.innerHTML = ""
            for (let idx in locations) {
                let formatted = formatLocation(locations[idx])
                loc_div.appendChild(formatted)
            }
        });
    }

}

function getSavedLocations() {
    const loc_div = document.getElementById("locations-container")
    loc_div.innerHTML = ""

    locations = savedLocations().then((locations) => {
        for (let idx in locations) {
            let formatted = formatLocation(locations[idx])
            loc_div.appendChild(formatted)
        }
    });
    const favButton = document.getElementById("filterFavoritesButton")
    favButton.innerHTML = "Hide Favourites"
    favButton.onclick = () => { displayLocations() }
}

async function savedLocations() {
    const response = await fetch("http://127.0.0.1:5000/api/locations/favourites");
    return response.json();
}

