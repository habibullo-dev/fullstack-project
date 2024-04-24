document.addEventListener('DOMContentLoaded', function () {
    const expertInput = document.querySelector('#expertSelect');
    const cityInput = document.querySelector('#citySelect');
    const searchBtn = document.querySelector('#searchButton');
    const textField = document.querySelector('#textField');
    const showBtn = document.querySelector('.showMore');

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
                // Clear Previous search results
                textField.innerHTML = '';

                // Display search results
                textField.innerHTML = `<p>Search results for: (Type): <strong>${expertValue}</strong> in (City): <strong>${cityValue}</strong></p>`;

                // Populate cards
                populateCards(data);
            })
            .catch(error => {
                console.error('Error fetching or processing data:', error.message);
                textField.innerHTML = `<p>${error.message}</p>`;
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

    // Add event listener to the search button
    searchBtn.addEventListener('click', performSearch);

    // Add event listener to the form submission
    searchForm.addEventListener('submit', performSearch);
});


