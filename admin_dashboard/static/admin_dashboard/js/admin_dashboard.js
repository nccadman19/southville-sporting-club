// Function to set the checkbox state in local storage
function updateLocalStorage(orderNumber, completed) {
    localStorage.setItem(orderNumber, completed);
}

// Function to load and set the checkbox state on page load
function setCheckboxState(orderNumber) {
    var completed = localStorage.getItem(orderNumber) === 'true';
    var checkbox = document.querySelector('input[value="' + orderNumber + '"]');
    if (checkbox) {
        checkbox.checked = completed;
    }
}

// Attach event listeners to the checkboxes
var checkboxes = document.querySelectorAll('.checkbox-order-list input');
checkboxes.forEach(function (checkbox) {
    checkbox.addEventListener('change', function (event) {
        var orderNumber = event.target.value;
        var completed = event.target.checked;
        updateLocalStorage(orderNumber, completed);
    });
});

// Set the checkbox states on page load
checkboxes.forEach(function (checkbox) {
    var orderNumber = checkbox.value;
    setCheckboxState(orderNumber);
});