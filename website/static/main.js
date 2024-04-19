document.addEventListener('DOMContentLoaded', function () {
    const searchForm = document.querySelector('#searchForm');
    const typeInput = document.querySelector('#typeSelect');
    const cityInput = document.querySelector('#citySelect');
    const expertiseInput = document.querySelector('#expertSelect');
    const searchBtn = document.querySelector('#searchButton');
    const textField = document.querySelector('#textField');

    if (!searchForm || !typeInput || !cityInput || !expertInput || !searchBtn) {
        console.error('One or more required elements were not found in the document.');
        return;
    }


    // New function to fetch information from the backend(python) and database(mariadb)
    function performSearch(evt) {
        evt.preventDefault();

        // Get input values
        const typeValue = type.Input.value.trim();
        const cityValue = cityInput.value.trim();
        const expertValue = expertiseInput.value.trim();

        // Validate inputs
        if (!typeValue || !cityValue || !expertValue) {
            textField.innerHTML = '<p>Please provide type, city, expertise.</p>';
            return;
        }

        // Prepare the request payload
        const requestData = {
            type: typeValue,
            city: cityValue,
            expert: expertValue,
        };

        // Send POST request to the backend (python) using fetch 
        fetch('/search_input', {
            method: 'POST',
            body: JSON.stringify(requestData), // coverts JS value to JSON string
            headers: {
                'Content-type': 'application/json'
            },
        })
            .then(response => {
                if (!response.ok) {
                    console.error(`Network response was not ok: ${response.status} ${response.statusText}`);
                    textField.innerHTML = '<p>There was an error fetching the data. Please try again later!</p>';
                    return;
                }
                return response.json(); // Parse JSON response
            })
            .then(data => {
                if (!data) {
                    textField.innerHTML = '<p>There was an error processing the response data.</p>';
                    return;
                }

                // Clear previous search results
                textField.innerHTML = '';

                // Display search results after certain time
                setTimeout(() => {
                    textField.innerHTML = `<p>Search results for: (Type): <strong>${typeValue}</strong> in (City): <strong>${cityValue}</strong> with (Expertise): <strong>${expertValue}</strong></p>`;
                }, 4000);

                // Function to populate the cards on the left side of mvp page
                function populateCards(data) {
                    // identifiers for the card elements
                    const doctorCards = document.querySelectorAll('.doctorCard'); // 3 cards total
                    const facilitiesCard = document.querySelector('.facility.card'); // 1 card only

                    // Populate the doctor cards in the left side (first 3 cards)
                    if (data.Doctors && data.Doctors.length > 0) {
                        for (let idx = 0; idx < doctorCards.length; idx++) {
                            if (idx >= data.Doctors.length) {
                                break; // Stop the loop if there is no more doctors data to display
                            }

                            const doctor = data.Doctors[idx];
                            const doctorCard = doctorCards[idx];


                            // Populate card with doctor information
                            doctorCard.querySelector('.nameElem').textContent = doctor.Name;
                            // card.querySelector('.hospName').textContent = doctor.Company;
                            doctorCard.querySelector('.hospInfo').innerHTML = `
                                <p>Expertise: ${doctor.Expertise}</p>
                                <p>Hospital: ${doctor.Company}</p>
                            `;

                            doctorCard.querySelector('.hospInfo').innerHTML = `
                                <p>Expertise: ${doctor.Expertise}</p>
                                <p>Hospital: ${doctor.Company}</p>
                            `;

                            // Blurb => is a kiwi thing and a short description of a book, movie, or other product written for promotional purposes 
                            // and appearing on the cover of a book or in an advertisement.

                            card.querySelector('.blurb').textContent = `This is the official information of '${doctor.Name}'. Please click the card for additional inquiry!`;
                        }
                    }

                    //  Populate the facility card on left side (last bottom card)
                    if (data.Facilities && data.Facilities.length > 0) {
                        for (let idx = 0; idx < facilitiesCard.length; idx++) {
                            if (idx >= data.Facilities.length) {
                                break;
                            }
                            const facility = data.Facilities[idx];
                            // const facilityCard = 
                        }
                    }
                    if (data.Facilities && data.Facilities.length > 0 && facilityCard) {
                        const facility = data.Facilities[idx];

                        // Populate card with facility information
                        facilityCard.querySelector('.nameElem').textContent = facility.Name;
                        facilityCard.querySelector('.hospAddress').textContent = `Address: ${facility.Address} `;
                        facilityCard.querySelector('.hospPhone').textContent = `Phone: ${facility.Phone} `;
                        facilityCard.querySelector('.blurb').textContent = `This the official data of the '${facility.Name}'. Please select the card for more additional information`;
                    }
                }
            })
    }
});
