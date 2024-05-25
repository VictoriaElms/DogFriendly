function validate(){
    let name = 
        document.getElementById("name").value;
    let email =
        document.getElementById("email").value;
    let subjectTitle=
        document.getElementById("subjectTitle").value;
    let comments = 
        document.getElementById("comments").value;
    let error_message= 
        document.getElementById("error_message");

    error_message.style.padding = "10px";

    let errors = [];

    if (name.length <3) {
        errors.push("Please Enter a valid Name");}
    if (email.indexOf("@") == -1 || email.length < 6){
        errors.push("Please Enter a Valid Email");}
    if (subjectTitle.length < 5){
        errors.push("Please Enter a Correct Subject");}
    if (comments.length <= 30) {
        errors.push("Please Enter more than 40 Characters");}
    if (errors.length > 0){
        error_message.innerHTML = errors.join("<br>");
        return false;}
    else {
        alert("Form Submitted Successfully!");
        return true; }
     
    }
    document.addEventListener("DOMContentLoaded", function() {
        const filterFavoritesButton = document.getElementById("filterFavoritesButton");
        const favoritesResultsContainer = document.getElementById("favoritesResults");
    
        filterFavoritesButton.addEventListener("click", function() {
            // Send AJAX request to Flask backend to fetch favorite locations
            fetch('/api/locations/favorites')
                .then(response => response.json())
                .then(data => {
                    // Clear previous results
                    favoritesResultsContainer.innerHTML = "";
    
                    // Display favorite locations
                    if (data.length > 0) {
                        data.forEach(location => {
                            const locationElement = document.createElement("div");
                            locationElement.textContent = location.name;
                            favoritesResultsContainer.appendChild(locationElement);
                        });
                    } else {
                        const noResultsMessage = document.createElement("div");
                        noResultsMessage.textContent = "No favorites found.";
                        favoritesResultsContainer.appendChild(noResultsMessage);
                    }
                })
                .catch(error => {
                    console.error("Error fetching favorite locations:", error);
                });
        });
    });

   
    document.addEventListener("DOMContentLoaded", function() {
        const searchButton = document.getElementById("searchButton");
        const searchInput = document.getElementById("searchInput");
        const searchResultsContainer = document.getElementById("searchResults");

    searchButton.addEventListener("click", function() {
        const query = searchInput.value;

        // Send AJAX request to Flask backend to fetch search results
        fetch(`/api/locations/search?q=${encodeURIComponent(query)}`)
            .then(response => response.json())
            .then(data => {
                // Clear previous results
                searchResultsContainer.innerHTML = "";

                // Display search results
                if (data.length > 0) {
                    data.forEach(location => {
                        const locationElement = document.createElement("div");
                        locationElement.classList.add("card", "mb-2");
                        locationElement.innerHTML = `
                            <div class="card-body">
                                <h5 class="card-title">${location.name}</h5>
                                <p class="card-text">${location.address}</p>
                                <p class="card-text">${location.category}</p>
                            </div>
                        `;
                        searchResultsContainer.appendChild(locationElement);
                    });
                } else {
                    const noResultsMessage = document.createElement("div");
                    noResultsMessage.textContent = "No locations found.";
                    searchResultsContainer.appendChild(noResultsMessage);
                }
            })
            .catch(error => {
                console.error("Error fetching search results:", error);
            });
    });
});


