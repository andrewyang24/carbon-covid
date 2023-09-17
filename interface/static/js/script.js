document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("data-form");
    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const region = document.getElementById("region").value;
        const date = document.getElementById("date").value;
        const resultDiv = document.getElementById("result");
        
        try {
            const response = await fetch(`/api/combined_data?region=${region}&date=${date}`);
            const data = await response.json();
            
            if (response.status === 200) {
                const carbonIntensity = data.carbon_intensity;
                const covid19Data = data.covid_19;
                resultDiv.innerHTML = `
                    <h2>Carbon Intensity Data:</h2>
                    <pre>${JSON.stringify(carbonIntensity, null, 2)}</pre>
                    <h2>COVID-19 Data:</h2>
                    <pre>${JSON.stringify(covid19Data, null, 2)}</pre>
                `;
            } else {
                resultDiv.innerHTML = `<p>Error: ${data.error}</p>`;
            }
        } catch (error) {
            resultDiv.innerHTML = "<p>An error occurred while fetching data.</p>";
        }
    });
});
