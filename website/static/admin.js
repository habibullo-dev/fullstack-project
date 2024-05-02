// Function to show tables when button is click ( using click event ), not using event listener
function toggleBtn(tableIndex) {
    let tables = document.querySelectorAll('.adminTable');
    tables.forEach((table, idx) => {
        if (idx === tableIndex) {
            if (table.style.display === 'none' || table.style.display === '') {
                table.style.display = 'table';
                // If the table is hidden or not explicitly displayed, the line above sets its display property to 'table', making it visible.
            } else {
                table.style.display = 'none';
            }
        } else {
            table.style.display = 'none';
        }
    });
}
