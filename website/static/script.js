// JavaScript code to handle form submission and display search results
const searchForm = document.getElementById('search-form');

searchForm.addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent form submission

    const inputElement = document.getElementById('search-input');
    const inputValue = inputElement.value.trim();

    fetch(`/search_data?input=${encodeURIComponent(inputValue)}`)
        .then(response => response.json())
        .then(data => {
            const doctorsResults = document.getElementById('doctors-results');
            const facilitiesResults = document.getElementById('facilities-results');

            // Clear previous results
            doctorsResults.innerHTML = '';
            facilitiesResults.innerHTML = '';

            // Display doctors results
            data.doctors.forEach(doctor => {
                const listItem = document.createElement('li');
                listItem.textContent = `${doctor.Name} - ${doctor.Specialty} (${doctor['Hospital/Clinic']}) - ${doctor.Address} - ${doctor.Contact}`;
                doctorsResults.appendChild(listItem);
            });

            // Display facilities results
            data.facilities.forEach(facility => {
                const listItem = document.createElement('li');
                listItem.textContent = `${facility.Name} - ${facility.Type} (${facility.Address}) - ${facility.Phone} - ${facility.Emergency}`;
                facilitiesResults.appendChild(listItem);
            });
        });
});