const selectDoctor = document.querySelectorAll("h2.click");

selectDoctor.forEach(function (h2) {
    h2.addEventListener("click", function () {
        let selectedDiv = document.querySelector(".selectedCard");
        selectedDiv.style.display = "inline-block";
        selectedDiv.style.float = "right";

    });
});

// // Function to fetch data from the backend using fetch
// function fetchSearchData() {
//     // Make sure this matches your backend endpoint URL
//     // const url = '/search_data'; 
//     const url = `/search_data?input=${encodeURIComponent(input)}`

//     // Perform the fetch request
//     return fetch(url)
//         .then(response => {
//             if (response.ok) {
//                 return response.json(); // Parse JSON response
//             } else {
//                 console.error('HTTP error: ' + response.status);
//                 return { doctors: [], facilities: [] }; // Return empty data on error
//             }
//         })
//         .catch(error => {
//             console.error('Error fetching search data:', error);
//             return { doctors: [], facilities: [] }; // Return empty data on error
//         });
// }

// // Function to perform a search through doctors and facilities

// function doSearch(input, doctors, facilities) {
//     // Create an object to store the search results
//     const output = {
//         doctors: [],
//         facilities: []
//     };

//     const filteredDoctors = doctors.filter(doctor => {
//         return (
//             doctor.name.includes(input) ||
//             doctor.expertise.includes(input) ||
//             doctor.address.includes(input) ||
//             doctor.emergency.includes(input) ||
//             doctor.phone.includes(input)
//         );
//     });

//     const filteredFacilities = facilities.filter(facility => {
//         return (
//             facility.name.includes(input) ||
//             facility.speaker.includes(input) ||
//             facility.type.includes(input) ||
//             facility.address.includes(input) ||
//             facility.phone.includes(input) ||
//             facility.emergency.includes(input) ||
//             facility.services.includes(input)
//         );
//     });

//     return {
//         doctors: filteredDoctors,
//         facilities: filteredFacilities
//     };
// }

// // Function to perform a search and display the output
// function performSearch(event) {
//     event.preventDefault(); //Prevent form submission 

//     const inputElem = document.querySelector('#search-input');
//     const inputElement = inputElem.value.trim();

//     // Fetch data from the backend
//     fetchSearchData().then(data => {
//         if (data && data.doctors && data.facilities) {
//             // Perform search using the input and fetched data
//             const searchOutput = doSearch(inputElement, data.doctors, data.facilities);

//             // Display search results
//             const doctorsOutput = document.querySelector('#doctors-results');
//             const facilitiesOutput = document.querySelector('#facilities-results');

//             // Clear previous results
//             doctorsOutput.innerHTML = '';
//             facilitiesOutput.innerHTML = '';

//             // Display the results for doctors
//             searchOutput.doctors.forEach(doctor => {
//                 const liElem = document.createElement('li');
//                 liElem.textContent = `Name: ${doctor.name}, Phone: ${doctor.phone}, Address: ${doctor.address}, Expertise: ${doctor.expertise}`;
//                 doctorsOutput.appendChild(liElem);
//             });

//             // Display the results for facilities
//             searchOutput.facilities.forEach(facility => {
//                 const liElem = document.createElement('li');
//                 liElem.textContent = `Name: ${facility.name}, Phone: ${facility.speaker}, Type: ${facility.type}, Address: ${facility.address}, Phone: ${facility.phone}, Emergency Number: ${facility.emergency}, Facility: ${facility.services}`;
//                 facilitiesOutput.appendChild(liElem);
//             });

//             return (
//                 facility.name.includes(input) ||
//                 facility.speaker.includes(input) ||
//                 facility.type.includes(input) ||
//                 facility.address.includes(input) ||
//                 facility.phone.includes(input) ||
//                 facility.emergency.includes(input) ||
//                 facility.services.includes(input)
//             );
//         }
//     })
// }

// // Add event listener to the form to handle form submission
// const searchForm = document.querySelector('#search-form');
// searchForm.addEventListener('submit', performSearch);

// // JavaScript code to handle form submission and display search results
// const searchForm = document.getElementById('search-form');

// searchForm.addEventListener('submit', function (event) {
//     event.preventDefault(); // Prevent form submission

//     const inputElement = document.getElementById('search-input');
//     const inputValue = inputElement.value.trim();

//     fetch(`/search_data?input=${encodeURIComponent(inputValue)}`)
//         .then(response => response.json())
//         .then(data => {
//             const doctorsResults = document.getElementById('doctors-results');
//             const facilitiesResults = document.getElementById('facilities-results');

//             // Clear previous results
//             doctorsResults.innerHTML = '';
//             facilitiesResults.innerHTML = '';

//             // Display doctors results
//             data.doctors.forEach(doctor => {
//                 const listItem = document.createElement('li');
//                 listItem.textContent = `${doctor.Name} - ${doctor.Specialty} (${doctor['Hospital/Clinic']}) - ${doctor.Address} - ${doctor.Contact}`;
//                 doctorsResults.appendChild(listItem);
//             });

//             // Display facilities results
//             data.facilities.forEach(facility => {
//                 const listItem = document.createElement('li');
//                 listItem.textContent = `${facility.Name} - ${facility.Type} (${facility.Address}) - ${facility.Phone} - ${facility.Emergency}`;
//                 facilitiesResults.appendChild(listItem);
//             });
//         });
// });