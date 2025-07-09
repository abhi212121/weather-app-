<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Weather App</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: linear-gradient(to right, #6dd5fa, #2980b9);
      color: #fff;
      text-align: center;
      padding: 50px;
    }

    .weather-container {
      background: rgba(0, 0, 0, 0.2);
      padding: 30px;
      border-radius: 15px;
      display: inline-block;
    }

    input {
      padding: 10px;
      border-radius: 5px;
      border: none;
      width: 200px;
    }

    button {
      padding: 10px 15px;
      border: none;
      background-color: #1abc9c;
      color: white;
      border-radius: 5px;
      cursor: pointer;
      margin-left: 10px;
    }

    #result {
      margin-top: 20px;
      font-size: 20px;
    }
  </style>
</head>
<body>
  <div class="weather-container">
    <h1>Weather App</h1>
    <input type="text" id="locationInput" placeholder="Enter location" />
    <button onclick="getWeather()">Get Weather</button>
    <div id="result"></div>
  </div>

  <script>
    async function getWeather() {
      const location = document.getElementById("locationInput").value.trim();
      const resultDiv = document.getElementById("result");

      if (!location) {
        resultDiv.innerHTML = "Please enter a location.";
        return;
      }

      const apiKey = "ba3f0bbc2c444ce9a62201518252606";
      const url = `http://api.weatherapi.com/v1/current.json?key=${apiKey}&q=${location}&aqi=yes`;

      try {
        const response = await fetch(url);
        if (!response.ok) throw new Error("Location not found");

        const data = await response.json();
        const tempC = data.current.temp_c;
        const condition = data.current.condition.text;

        resultDiv.innerHTML = `
          <strong>${data.location.name}, ${data.location.country}</strong><br/>
          Temperature: ${tempC} °C<br/>
          Condition: ${condition}
        `;
      } catch (error) {
        resultDiv.innerHTML = `Error: ${error.message}`;
      }
    }
  </script>
</body>
</html>
