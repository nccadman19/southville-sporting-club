document.addEventListener('DOMContentLoaded', function () {
    // JavaScript to toggle form fields' editability
    var editableFields = document.getElementById('editable-fields');
    var editButton = document.getElementById('edit-button');

    editButton.addEventListener('click', () => {
        var formElements = editableFields.getElementsByTagName('input');
        for (let i = 0; i < formElements.length; i++) {
            formElements[i].disabled = !formElements[i].disabled;
        }
    });
    // Disable form fields initially
    var formElements = editableFields.getElementsByTagName('input');
    for (let i = 0; i < formElements.length; i++) {
        formElements[i].disabled = true;
    }
});