// Nina - Recommended Doctors event listener to populate selected card on the right
const docOne = document.querySelector("#docOne");
docOne.addEventListener("click", displayRightCard1);
function displayRightCard1() {
    const selectedCard = document.querySelector('.selectedCard');
    // Populate the right card with the doctor's information
    selectedCard.querySelector('.drImg').src = "../static/doctors/Dr. Shin Ho-Chul.jpeg";
    selectedCard.querySelector('.drName').textContent = "Dr. Shin Ho-Chul";
    selectedCard.querySelector('.hospAbout').textContent = "Over 15 years of experience, provides compassionate care, emphasizing preventive health, patient relationships, holistic wellness, and actively contributes to community outreach and medical education";
    selectedCard.querySelector('.hospCompany').textContent = "Kangbuk Samsung Hospital";
    selectedCard.querySelector('.hospExpertise').textContent = "General Practice";
    selectedCard.querySelector('.hospAddresses').textContent = "108 Pyong-dong, Chung-ku, Seoul";
    selectedCard.querySelector('.hospPhones').textContent = "2001-2911, 5100";
    selectedCard.querySelector('.hospRating').textContent = "5/5"
    selectedCard.querySelector('.blurbs').innerHTML = `
        This is the official information of Dr. Shin Ho-Chul.
        For more information, please contact the provided email or doctor's phone #.
    `;
};

const docTwo = document.querySelector("#docTwo");
docTwo.addEventListener("click", displayRightCard2);
function displayRightCard2() {
    const selectedCard = document.querySelector('.selectedCard');
    // Populate the right card with the doctor's information
    selectedCard.querySelector('.drImg').src = "../static/doctors/Dr. Yoo Shin-ae.jpeg";
    selectedCard.querySelector('.drName').textContent = "Dr. Yoo Shin-ae";
    selectedCard.querySelector('.hospAbout').textContent = "Specializes in allergic diseases and immunology, creating supportive environments for children's health";
    selectedCard.querySelector('.hospCompany').textContent = "Samsung Medical Centre";
    selectedCard.querySelector('.hospExpertise').textContent = "Paediatrics / Allergy";
    selectedCard.querySelector('.hospAddresses').textContent = "50 Ilwon-dong, Kangnam-ku, Seoul";
    selectedCard.querySelector('.hospPhones').textContent = "3410-0200";
    selectedCard.querySelector('.hospRating').textContent = "5/5"
    selectedCard.querySelector('.blurbs').innerHTML = `
    This is the official information of Dr. Yoo Shin-ae.
    For more information, please contact the provided email or doctor's phone #.
    `;
};

const docThree = document.querySelector("#docThree");
docThree.addEventListener("click", displayRightCard3);
function displayRightCard3() {
    const selectedCard = document.querySelector('.selectedCard');
    // Populate the right card with the doctor's information
    selectedCard.querySelector('.drImg').src = "../static/doctors/Dr. Kwak.jpeg";
    selectedCard.querySelector('.drName').textContent = "Dr. Kwak";
    selectedCard.querySelector('.hospAbout').textContent = "Dedicated to comprehensive care, emphasizing open communication and patient empowerment";
    selectedCard.querySelector('.hospCompany').textContent = "Seoul Chungang Hospital";
    selectedCard.querySelector('.hospExpertise').textContent = "General Practice";
    selectedCard.querySelector('.hospAddresses').textContent = "388-1 Poongnap-dong, Songpa-ku, Seoul";
    selectedCard.querySelector('.hospPhones').textContent = "3010-5001/2";
    selectedCard.querySelector('.hospRating').textContent = "5/5"
    selectedCard.querySelector('.blurbs').innerHTML = `
    This is the official information of Dr. Kwak.
    For more information, please contact the provided email or doctor's phone #.
    `;
};

// Something Nik did
const selectDoctor = document.querySelectorAll("h2.click");

selectDoctor.forEach(function (h2) {
    h2.addEventListener("click", function () {
        let selectedDiv = document.querySelector(".selectedCard");
        selectedDiv.style.display = "inline-block";
        selectedDiv.style.float = "right";

    });
});

// js for styling clicked listings //

const cards = document.querySelectorAll('.card');
const selectedCardContainer = document.querySelector('.selectedCard');

const rootStyles = getComputedStyle(document.documentElement);
const primaryColor = rootStyles.getPropertyValue('--color-primary').trim();
const secondaryColor = rootStyles.getPropertyValue('--color-secondary').trim();

let selectedCard = null;
let originalBorderColor = `3px solid ${primaryColor}`;

cards.forEach(card => {
    card.addEventListener('click', () => {
        if (!originalBorderColor) {
            originalBorderColor = getComputedStyle(card).borderColor;
        }

        if (selectedCard && selectedCard !== card) {
            selectedCard.style.border = originalBorderColor;
        }

        card.style.border = `4px solid ${secondaryColor}`;
        selectedCard = card;

        selectedCardContainer.style.border = `4px solid ${secondaryColor}`
    });
});

// js for styling clicked listings end//





// code for the search input and fetch data from the backend python and database Mariadb

// Execute the code when the DOM Content is loaded
document.addEventListener('DOMContentLoaded', function () {
    // Select the necessary DOM elements
    const expertInput = document.querySelector('#expertSelect');
    const cityInput = document.querySelector('#citySelect');
    const searchBtn = document.querySelector('#searchButton');
    const textField = document.querySelector('#textField');
    const showBtn = document.querySelector('.showMore');

    // Initialize a variable(searchData) as an empty object to store fetched data
    let searchData = {}; // incoming data from the backend is JSON 

    // Check if all require DOM elements are presents
    // If not, program will not run or start
    if (!searchBtn || !expertInput || !cityInput || !showBtn) {
        console.error('One or more required elements were not found in the document.')
        return;
    }

    // Function to fetch data from the backend 
    function performSearch(evt) {
        evt.preventDefault(); // prevent form submission

        // Get input values
        const expertValue = expertInput.value.trim() // remove whitespace
        const cityValue = cityInput.value.trim();

        // Validate input values
        if (!cityValue || !expertValue) {
            textField.innerHTML = 'Please provide city and expertise.</p>';
            // set timeout to clear textField innerHtml
            setTimeout(() => {
                textField.innerHTML = '';
            });
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
            body: JSON.stringify(requestData), // JS value is converted to a JSON string
            headers: {
                'Content-Type': 'application/json'
            },
        })
            .then(response => {
                // Handle network errors
                if (!response.ok) {
                    console.error(`Network response was not ok: ${response.status} - ${response.statusText}`);
                } else {
                    return response.json(); // Parse response JSON
                }
            })
            .then(data => {
                // Handle empty response
                if (!data) {
                    console.error('Empty response received from the server.')
                }

                // Save and store fetched data into a variable
                searchData = data;

                // Clear Previous results
                textField.innerHTML = ''

                // Display search results message
                textField.innerHTML = `<p>Search results for (Expertise):  <strong>${expertValue}</strong> in (City): <strong>${cityValue}</strong></p>`;

                // Clear message results
                setTimeout(() => {
                    textField.innerHTML = '';
                }, 3000);

                // Populate initial cards (left side) with fetched data
                populateLeftCards(data);
            })
            .catch(error => {
                // Handle fetch or processing errors
                console.error('Error fetching or processing data:', error);
                textField.innerHTML = `<p>${error}</p>`;
                setTimeout(() => {
                    textField.innerHTML = '';
                }, 3000);
            });
    }

    // Function to populate initial cards on the left side (3 doctor cards and 1 facility card)
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
            const facility = data.Facilities[0]; // access first element of the array Facilities within object(data)
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
                    <img class='hospLogo' src='../static/doctors/${doctor.Name}.jpeg' alt='Hospital Logo'>
                </div>
                <p class='rating'>${doctor.Ratings}/5</p>
            </div>
            <div class='middle'>
                <h2 class='nameElem'>${doctor.Name}</h2>
                <div class='hospInfo'>
                    <p class='hospName'>Expertise: ${doctor.Expertise}</p>
                    <p class='hospLocation'>Hospital: ${doctor.Address}</p>
                </div>
                <div class='blurb'>
                    <p>This is official information of ${doctor.Name}. Please click the card for additional inquiry!</p>
                </div>
            </div>
        `;
        // Add click event listener for each card
        doctorCard.addEventListener('click', () => {
            // Call function to populate the right card with full data of the selected doctor card
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
                <img class='hospLogo' src='../static/images/medicalLogo.png' alt='Hospital Logo'>
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
        selectedCard.querySelector('.drImg').src = `../static/doctors/${doctor.Name}.jpeg`;
        selectedCard.querySelector('.drName').textContent = doctor.Name;
        selectedCard.querySelector('.hospAbout').textContent = doctor.About;
        selectedCard.querySelector('.hospCompany').textContent = doctor.Company;
        selectedCard.querySelector('.hospExpertise').textContent = doctor.Expertise;
        selectedCard.querySelector('.hospAddresses').textContent = `${doctor.Address}`;
        selectedCard.querySelector('.hospPhones').textContent = `${doctor.Phone}`;
        selectedCard.querySelector('.hospRating').textContent = `${doctor.Ratings}`
        selectedCard.querySelector('.blurbs').innerHTML = `
            This is the official information of '${doctor.Name}'.
            For more information, please contact the provided email or doctor ${doctor.Phone}.
        `;
    }

    // Define a global variable to keep track of the current facility index
    let facilityIdx = 0;

    // Function to handle 'Show More' button click
    function handleButtonClick() {
        // Check if searchData is not null
        if (searchData) {
            const cardsContainer = document.querySelector('.cards');

            // Create more doctor cards
            if (searchData.Doctors && searchData.Doctors.length > 0) {
                const doctorIdx = cardsContainer.querySelectorAll('.doctor.card').length;
                for (let idx = doctorIdx; idx < doctorIdx + 3 && idx < searchData.Doctors.length; idx++) {
                    const doctor = searchData.Doctors[idx];
                    createDoctorCard(doctor, cardsContainer);
                }
            }

            // Create one more facility card
            if (searchData.Facilities && searchData.Facilities.length > 1) {
                // Use the current facility index to select the facility 
                const facility = searchData.Facilities[facilityIdx];
                createFacilityCard(facility, cardsContainer);

                // Increment the facility index for the next card creation
                // facilityIdx will be incremented by 1,
                // If it is equal or greater than searchData.Facilities.length, reset facilityIdx to 0
                // this makes sure that facilityIdx cycles through the available facility data.
                facilityIdx = (facilityIdx + 1 >= searchData.Facilities.length) ? 0 : facilityIdx + 1;
            }
        }
    }

    // Add event listener to the search button
    searchBtn.addEventListener('click', performSearch);

    // Add event listener to the 'Show More' button
    showBtn.addEventListener('click', handleButtonClick);
})
// End of the js code for the mvp search input and result




// function for burgermenu//
// function toggleMenu() {
//     const menu = document.querySelector('.buttons');
//     const screenWidth = window.innerWidth;
//     if (screenWidth <= 600) {
//         menu.style.display = menu.style.display === 'none' ? 'block' : 'none';
//     }
// }
// burgermenu function END//


