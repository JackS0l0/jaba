// dark mode
document.addEventListener('DOMContentLoaded', (event) => {
    const button = document.getElementById('night-mode-toggle');
    const icon = document.getElementById('night-mode-icon');
    const moonIcon = "../../static/media/moon.png";
    const sunIcon = "../../static/media/sun.png";
    const updateIcon = () => {
        if (document.body.classList.contains('night-mode')) {
            icon.src = sunIcon;
        } else {
            icon.src = moonIcon;
        }
    };
    if (localStorage.getItem('nightMode') === 'true') {
        document.body.classList.add('night-mode');
        updateIcon();
    }
    button.addEventListener('click', () => {
        document.body.classList.toggle('night-mode');
        if (document.body.classList.contains('night-mode')) {
            localStorage.setItem('nightMode', 'true');
        } else {
            localStorage.setItem('nightMode', 'false');
        }
        updateIcon();
    });
});
// close float0
document.addEventListener('DOMContentLoaded', function() {
    const button = document.querySelector('.float0 .btn');
    button.addEventListener('click', function() {
        const floatDiv = button.closest('.float0');
        floatDiv.style.display = 'none';
    });
});
