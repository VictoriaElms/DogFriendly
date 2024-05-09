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
    let node = document.createTextNode("Name: " + location.name);
    let br1 = document.createElement("br");
    let node2 = document.createTextNode("Category: " + location.category);
    let br2 = document.createElement("br");
    let node3 = document.createTextNode("Address: " + location.address);
    let br3 = document.createElement("br");
    let node4 = document.createTextNode("Hours: " + location.hours);
    para.appendChild(node);
    para.appendChild(br1);
    para.appendChild(node2);
    para.appendChild(br2);
    para.appendChild(node3);
    para.appendChild(br3);
    para.appendChild(node4);
    return para;
}

document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const locationsList = document.getElementById('locationsList');

    searchInput.addEventListener('input', function(event) {
        const searchQuery = event.target.value.toLowerCase();

        // Filter locations based on search query
        const filteredLocations = locations.filter(function(location) {
            return location.name.toLowerCase().includes(searchQuery) || 
                   location.category.toLowerCase().includes(searchQuery) ||
                   location.address.toLowerCase().includes(searchQuery);
        });

        // Render filtered locations
        renderLocations(filteredLocations);
    });

    // Function to render locations
    function renderLocations(locations) {
        locationsList.innerHTML = ''; // Clear previous content
        
        locations.forEach(function(location) {
            const locationElement = formatLocation(location);
            locationsList.appendChild(locationElement);
        });
    }
});