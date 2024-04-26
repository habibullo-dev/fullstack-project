// code for the search input and fetch data from the backend(Python) with database(MariaDB)

// Execute the code when the DOM content is loaded
document.addEventListener('DOMContentLoaded', function () {
    // Selecting necessary DOM elements
    const expertInput = document.querySelector('#expertSelect');
    const cityInput = document.querySelector('#citySelect');
    const searchBtn = document.querySelector('#searchButton');
    const textField = document.querySelector('#textField');
    const showBtn = document.querySelector('.showMore');

    // Initialize searchData as an empty object to store fetched data
    let searchData = {}; // incoming data from backend is JSON

    // Check if all required DOM elements are present, if not present, program will not run
    if (!expertInput || !cityInput || !searchBtn || !showBtn) {
        console.error('One or more required elements were not found in the document.')
        return;
    }

    // Function to fetch data from the backend
    function performSearch(evt) {
        evt.preventDefault();

        // Get input values
        const expertValue = expertInput.value.trim();
        const cityValue = cityInput.value.trim();

        // Validate inputs
        if (!cityValue || !expertValue) {
            textField.innerHTML = '<p>Please provide city and expertise.</p>';
            return;
        }

        // Prepare the request payload
        const requestData = {
            city: cityValue,
            expert: expertValue
        };

        // Send a POST request to the backend using fetch
        fetch('/search_input', {
            method: 'POST',
            body: JSON.stringify(requestData), // JS value converted to JSON string
            headers: {
                'Content-Type': 'application/json'
            },
        })
            .then(response => {
                // Handle network errors
                if (!response.ok) {
                    console.error(`Network response was not ok: ${response.status} ${response.statusText}`);
                }
                return response.json(); // Parse response JSON
            })
            .then(data => {
                // Handle empty response
                if (!data) {
                    console.error('Empty response received from the server.');
                }

                // Store fetched data
                searchData = data;

                // Display search results message
                textField.innerHTML = `<p>Search results for: (Type): <strong>${expertValue}</strong> in (City): <strong>${cityValue}</strong></p>`;

                // Clear Previous search results after 3 seconds
                setTimeout(() => {
                    textField.innerHTML = '';
                }, 3000)

                // Populate initial cards with fetched data
                populateLeftCards(data);
            })
            .catch(error => {
                // Handle fetch or processing errors
                console.error('Error fetching or processing data:', error);
                textField.innerHTML = `<p>${error.message}</p>`;
                setTimeout(() => {
                    textField.innerHTML = '';
                }, 3000);
            });
    }

    // Function to populate initial cards (3 doctor cards and 1 facility card)
    function populateLeftCards(data) {
        const cardsContainer = document.querySelector('.cards');
        cardsContainer.innerHTML = ''; // Clear previous cards

        // Create doctor cards if data.Doctors exists
        if (data.Doctors && data.Doctors.length > 0) {
            for (let idx = 0; idx < 3 && idx < data.Doctors.length; idx++) {
                const doctor = data.Doctors[idx];
                createDoctorCard(doctor, cardsContainer);
            }
        }

        // Create facility card if data.Facilities exists
        if (data.Facilities && data.Facilities.length > 0) {
            const facility = data.Facilities[0];
            createFacilityCard(facility, cardsContainer);
        }
    }

    // Function to create doctor card
    function createDoctorCard(doctor, container) {
        const doctorCard = document.createElement('div');
        doctorCard.classList.add('doctor', 'card');
        doctorCard.innerHTML = `
            <div class='left'>
                <div class='hospL'>
                    <img class='hospLogo' src='../static/images/logoInBlue.png' alt='Hospital Logo'>
                </div>
                <p class='rating'>3.5/5</p>
            </div>
            <div class='middle'>
                <h2 class='nameElem'>${doctor.Name}</h2>
                <div class='hospInfo'>
                    <p class='hospName'>Expertise: ${doctor.Expertise}</p>
                    <p class='hospLocation'>Hospital: ${doctor.Address}</p>
                </div>
                <div class='blurb'>
                    <p>This is the official information of ${doctor.Name}. Please click the card for additional inquiry!</p>
                </div>
            </div>
        `;
        // Add click event listener for each card
        doctorCard.addEventListener('click', () => {
            // Call function to populate the right card with full data of the selected doctor
            updateRightCard(doctor);
        });
        container.appendChild(doctorCard);
    }

    // Function to create facility card
    function createFacilityCard(facility, container) {
        const facilityCard = document.createElement('div');
        facilityCard.classList.add('facility', 'card');
        facilityCard.innerHTML = `
            <div class='left'>
                <div class='hospL'>
                    <img class='hospLogo' src='../static/images/logoInBlue.png' alt='Hospital Logo'>
                </div>
                <p class='rating'>3.5/5</p>
            </div>
            <div class='middle'>
                <h2 class='nameElem' style='font-size:1.8rem;'>${facility.Name}</h2>
                <div class='hospInfo'>
                    <p class='hospAddress'>Address: ${facility.Address}</p>
                    <p class='hospPhone'>Phone: ${facility.Phone}</p>
                </div>
                <div class='blurb'>
                    <p>This is the official data of the ${facility.Name}. Please select the card for more additional information</p>
                </div>
            </div>
        `;
        container.appendChild(facilityCard);
    }

    // Function to populate the right card with full data of the selected doctor
    function updateRightCard(doctor) {
        const selectedCard = document.querySelector('.selectedCard');
        // Populate the right card with the doctor's information
        selectedCard.querySelector('.drName').textContent = doctor.Name;
        selectedCard.querySelector('.hospCompany').textContent = doctor.Company;
        selectedCard.querySelector('.hospExpertise').textContent = doctor.Expertise;
        selectedCard.querySelector('.hospAddresses').textContent = `${doctor.Address}`;
        selectedCard.querySelector('.hospPhones').textContent = `${doctor.Phone}`;
        selectedCard.querySelector('.blurbs').innerHTML = `
            This is the official information of '${doctor.Name}'. 
            For more information, please contact the provided email or ${doctor.Phone}.
        `;
    }

    // Define a global variable to keep track of the current facility index
    let facilityIndex = 0;

    // Function to handle 'Show More' button click
    function handleShowMoreClick() {
        // Check if searchData is not null
        if (searchData) {
            const cardsContainer = document.querySelector('.cards');

            // Create more doctor cards
            if (searchData.Doctors && searchData.Doctors.length > 0) {
                const startIndex = cardsContainer.querySelectorAll('.doctor.card').length;
                for (let idx = startIndex; idx < startIndex + 3 && idx < searchData.Doctors.length; idx++) {
                    const doctor = searchData.Doctors[idx];
                    createDoctorCard(doctor, cardsContainer);
                }
            }

            // Create one more facility card
            if (searchData.Facilities && searchData.Facilities.length > 1) {
                // Use the current facility index to select the facility data
                const facility = searchData.Facilities[facilityIndex];
                createFacilityCard(facility, cardsContainer);

                // Increment the facility index for the next card creation
                // facilityIndex will be incremented by 1,
                // if it is equal or greater than searchData.length, reset facilityIndex to 0
                // this makes sure that facilityIndex cycles through the available facility data.
                facilityIndex = (facilityIndex + 1 >= searchData.Facilities.length) ? 0 : facilityIndex + 1;
            }
        }
    }


    // Add event listener to the search button
    searchBtn.addEventListener('click', performSearch);

    // Add event listener to the 'Show More' button
    showBtn.addEventListener('click', handleShowMoreClick);
});

// End of the js code for the mvp search input and result
