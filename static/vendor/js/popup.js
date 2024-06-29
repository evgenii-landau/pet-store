document.addEventListener('DOMContentLoaded', function() {
    const popupButton = document.getElementById('popupButton');
    const popupPanel = document.getElementById('popupPanel');

    popupButton.addEventListener('click', function() {
        if (popupPanel.style.display === 'block') {
            popupPanel.style.display = 'none';
        } else {
            popupPanel.style.display = 'block';
        }
    });

    // Close the popup if clicked outside
    document.addEventListener('click', function(event) {
        if (!popupButton.contains(event.target) && !popupPanel.contains(event.target)) {
            popupPanel.style.display = 'none';
        }
    });
});
