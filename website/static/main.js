// Code for the mvp page without the button to click and create new div cards

// code for the search input and fetch data from the backend(Python) with database(MariaDB)
document.addEventListener('DOMContentLoaded', function () {
    const expertInput = document.querySelector('#expertSelect');
    const cityInput = document.querySelector('#citySelect');
    const searchBtn = document.querySelector('#searchButton');
    const textField = document.querySelector('#textField');

    if (!expertInput || !cityInput || !searchBtn) {
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
            body: JSON.stringify(requestData),
            headers: {
                'Content-Type': 'application/json'
            },
        })
            .then(response => {
                if (!response.ok) {
                    console.error(`Network response was not ok: ${response.status} ${response.statusText}`);
                }
                return response.json();
            })
            .then(data => {
                if (!data) {
                    console.error('Empty response received from the server.');
                }

                // Display search results
                textField.innerHTML = `<p>Search results for: (Type): <strong>${expertValue}</strong> in (City): <strong>${cityValue}</strong></p>`;

                // Clear Previous search results after 3 seconds
                setTimeout(() => {
                    textField.innerHTML = '';
                }, 3000)

                // Populate cards
                populateCards(data);

                // Create more cards
                createCard(data);
            })
            .catch(error => {
                console.error('Error fetching or processing data:', error);
                textField.innerHTML = `<p>${error.message}</p>`;
                setTimeout(() => {
                    textField.innerHTML = '';
                }, 3000);
            });
    }

    // Function to populate cards
    function populateCards(data) {
        const doctorCards = document.querySelectorAll('.doctor.card');
        const facilityCard = document.querySelector('.facility.card');

        // Populate doctor cards
        if (data.Doctors && data.Doctors.length > 0) {
            for (let idx = 0; idx < doctorCards.length && idx < data.Doctors.length; idx++) {
                const doctor = data.Doctors[idx];
                const card = doctorCards[idx];

                // Populate card with doctor information
                card.querySelector('.nameElem').textContent = doctor.Name;
                card.querySelector('.hospInfo').innerHTML = `
                    <p>Expertise: ${doctor.Expertise}</p>
                    <p>Hospital Name: ${doctor.Company}</p>
                `;
                card.querySelector('.blurb').textContent = `This is the official information of '${doctor.Name}'. Please click the card for additional inquiry!`;

                // Add click event listener for each card
                card.addEventListener('click', () => {
                    // Call function to populate the right card with full data of the selected doctor
                    updateRightCard(doctor);
                });
            }
        }

        // Populate facility card
        if (data.Facilities && data.Facilities.length > 0 && facilityCard) {
            const facility = data.Facilities[0];
            // Populate card with facility information
            facilityCard.querySelector('.nameElem').textContent = facility.Name;
            facilityCard.querySelector('.hospAddress').textContent = `Address: ${facility.Address}`;
            facilityCard.querySelector('.hospPhone').textContent = `Phone: ${facility.Phone}`;
            facilityCard.querySelector('.blurb').textContent = `This the official data of the '${facility.Name}'. Please select the card for more additional information`;
        }
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

    // Function to create more Div / Cards for doctors(3) and facility(1)
    function createCard(data) {
        const cardsContainer = document.querySelector('.cards');

        // Create doctor cards
        if (data.Doctors && data.Doctors.length > 0) {
            for (let idx = 0; idx < data.Doctors.length; idx++) {
                const doctor = data.Doctors[idx];
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
                    updateRightCard(doctor);
                });
                cardsContainer.appendChild(doctorCard);
            }
        }

        // Create Facility Card
        if (data.Facilities && data.Facilities.length > 0) {
            const facility = data.Facilities[0]; // facility 
            console.log(facility);
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
            cardsContainer.appendChild(facilityCard);
        }
    }
    // Perform the search again to fetch more data
    // Call the function to fetch and create new cards
    const showBtn = document.querySelector('.showMore');
    // Add event listener to the 'More' Button
    showBtn.addEventListener('click', performSearch);

    // Add event listener to the search button
    searchBtn.addEventListener('click', performSearch);

    // Add event listener to the form submission
    searchForm.addEventListener('submit', performSearch);

    // Scroll to the bottom of the page when it loads
    window.scrollTo(0, document.body.scrollHeight);
});
