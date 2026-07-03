function toggleSidebar() {
    document.getElementById('sidebar').classList.toggle('open');
}

function toggleUserMenu() {
    document.getElementById('userMenu').classList.toggle('show');
}

document.addEventListener('click', function(e) {
    const menu = document.getElementById('userMenu');
    if (!e.target.closest('.user')) {
        menu.classList.remove('show');
    }
});

document.addEventListener('DOMContentLoaded', function() {
    particlesJS("particles-js", {
        "particles": {
            "number": { "value": 60, "density": { "enable": true, "value_area": 800 } },
            "color": { "value": "#2d7aff" },
            "shape": { "type": "circle" },
            "opacity": { "value": 0.4, "random": true },
            "size": { "value": 2, "random": true },
            "line_linked": { "enable": true, "distance": 150, "color": "#2d7aff", "opacity": 0.2, "width": 1 },
            "move": { "enable": true, "speed": 1.2, "direction": "none", "random": true, "straight": false, "out_mode": "out" }
        },
        "interactivity": {
            "detect_on": "canvas",
            "events": { "onhover": { "enable": true, "mode": "repulse" }, "onclick": { "enable": true, "mode": "push" } }
        },
        "retina_detect": true
    });

    const canvas = document.getElementById('chart');
    if (canvas) {
        new Chart(canvas.getContext('2d'), {
            type: 'line',
            data: {
                labels: ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'],
                datasets: [{
                    label: 'Acessos',
                    data: [45, 60, 75, 90, 85, 70, 50],
                    borderColor: '#2d7aff',
                    backgroundColor: 'rgba(45, 122, 255, 0.1)',
                    tension: 0.3,
                    fill: true,
                    pointBackgroundColor: '#2d7aff',
                    pointBorderColor: '#fff',
                    pointBorderWidth: 2
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { labels: { color: '#8b9bb5', font: { size: 12 } } } },
                scales: {
                    x: { ticks: { color: '#8b9bb5' }, grid: { color: '#1e252b' } },
                    y: { ticks: { color: '#8b9bb5' }, grid: { color: '#1e252b' } }
                }
            }
        });
    }
});