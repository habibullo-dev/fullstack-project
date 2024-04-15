const selectDoctor = document.querySelectorAll("h2.click");

selectDoctor.forEach(function (h2) {
    h2.addEventListener("click", function () {
        let selectedDiv = document.querySelector(".selectedCard");
        selectedDiv.style.display = "inline-block";
        selectedDiv.style.float = "right";

    });
});


// code for the search input and fetch data from the backend(Python) with database(MariaDB)

document.addEventListener('DOMContentLoaded', function () {
    const searchForm = document.querySelector('#searchForm');
    const searchInput = document.querySelector('#searchInput');
    const searchBtn = document.querySelector('#searchButton');
    const searchResults = document.querySelector('#searchResults');

    if (!searchForm || !searchInput || !searchBtn || !searchResults) {
        console.error('One or more required elements were not found in the document.');
        return;
    }

    // Function to handle the search action
    function performSearch(e) {
        e.preventDefault();

        const inputValue = searchInput.value.trim();

        if (!inputValue) {
            searchResults.innerHTML = '<p>Please enter a search term.</p>';
            return;
        }

        fetch('/search_input', {
            method: 'POST',
            body: JSON.stringify({ search_input: inputValue }),
            headers: {
                'Content-Type': 'application/json',
            },
        })
            .then(response => response.json()) // Parse the JSON response
            .then(data => {
                searchResults.innerHTML = ''; // Clear previous search results

                // Display search results
                searchResults.innerHTML = `<p>Search results for: <strong>${inputValue}</strong></p>`;

                // Display doctor results
                if (Array.isArray(data.Doctors) && data.Doctors.length > 0) {
                    const doctorsSection = document.createElement('div');
                    doctorsSection.innerHTML = '<h3>Doctors:</h3>';
                    data.Doctors.forEach(doctor => {
                        const doctorDiv = document.createElement('div');
                        doctorDiv.innerHTML = `
                            Name: ${doctor.Name},
                            Specialty: ${doctor.Specialty},
                            Company: ${doctor.Company},
                            Address: ${doctor.Address},
                            Phone: ${doctor.Phone}
                        `;
                        doctorsSection.appendChild(doctorDiv);
                    });
                    searchResults.appendChild(doctorsSection);
                } else {
                    searchResults.innerHTML += '<p>No doctors found.</p>';
                }

                // Display facilities results
                if (Array.isArray(data.Facilities) && data.Facilities.length > 0) {
                    const facilitiesSection = document.createElement('div');
                    facilitiesSection.innerHTML = '<h3>Facilities:</h3>';
                    data.Facilities.forEach(facility => {
                        const facilityDiv = document.createElement('div');
                        facilityDiv.innerHTML = `
                            Name: ${facility.Name},
                            Speaker: ${facility.Speaker},
                            Type: ${facility.Type},
                            Address: ${facility.Address},
                            Phone: ${facility.Phone},
                            Emergency: ${facility.Emergency},
                            Services: ${facility.Services}
                        `;
                        facilitiesSection.appendChild(facilityDiv);
                    });
                    searchResults.appendChild(facilitiesSection);
                } else {
                    searchResults.innerHTML += '<p>No facilities found.</p>';
                }
            })
            .catch(error => {
                console.error('Error:', error);
                searchResults.innerHTML = '<p>There was an error fetching the data. Try again later!</p>';
            });
    }

    // Add event listener to the search button
    searchBtn.addEventListener('click', performSearch);

    // Add event listener to the search input for the "Enter" key press
    searchInput.addEventListener('keydown', function (e) {
        // Check if the pressed key is "Enter" (key code 13)
        if (e.keyCode === 13) {
            e.preventDefault(); // Prevent the form from submitting in the default way
            performSearch(e); // Trigger the search function
        }
    });
});
