document.addEventListener('DOMContentLoaded', function() {
    fetch('/player_stats', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'username=' + encodeURIComponent('YourUsernameHere')
    })
    .then(response => response.json())
    .then(data => {
        const soloWinRateData = data.find(dataset => dataset.label === 'Solo Win Rate');
        if (!soloWinRateData) {
            console.error('Solo Win Rate data not found');
            return;
        }

        const ctx2 = document.getElementById('doughnut').getContext('2d');
        new Chart(ctx2, {
            type: 'doughnut',
            data: {
                labels: soloWinRateData.data.labels,
                datasets: [{
                    label: 'Win Rate Comparison',
                    data: soloWinRateData.data.values,
                    backgroundColor: ['rgba(75, 192, 192, 0.2)', 'rgba(153, 102, 255, 0.2)'],
                    borderColor: ['rgba(75, 192, 192, 1)', 'rgba(153, 102, 255, 1)'],
                    borderWidth: 1
                }]
            }
        });
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
});
