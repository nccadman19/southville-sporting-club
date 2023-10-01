document.addEventListener('DOMContentLoaded', function () {
    // Get the dropdown element and its associated label
    var countryDropdown = document.getElementById('id_country');
    var selectedCountry = null;

    // Attach a change event listener to the select element
    countryDropdown.addEventListener('change', function (e) {
        // Get the selected option
        var selectedOption = countryDropdown.options[countryDropdown.selectedIndex];

        // Store the selected country value
        selectedCountry = selectedOption.value;

        // Update the hidden input field immediately
        document.getElementById("selected-country").value = selectedCountry;
    });
});
