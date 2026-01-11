const baseUrl = "http://127.0.0.1:8000";

function addVehicle() {
    fetch(`${baseUrl}/vehicles`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            name: document.getElementById("vname").value,
            model: document.getElementById("vmodel").value
        })
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message);

        // ✅ Clear inputs
        document.getElementById("vname").value = "";
        document.getElementById("vmodel").value = "";
    });
}

function addTelemetry() {
    fetch(`${baseUrl}/telemetry`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            vehicle_id: parseInt(document.getElementById("vid").value),
            speed: parseInt(document.getElementById("speed").value),
            fuel_level: parseInt(document.getElementById("fuel").value),
            engine_temp: parseInt(document.getElementById("temp").value)
        })
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message);

        // ✅ Clear inputs
        document.getElementById("vid").value = "";
        document.getElementById("speed").value = "";
        document.getElementById("fuel").value = "";
        document.getElementById("temp").value = "";
    });
}

function getTelemetry() {
    const id = document.getElementById("viewId").value;
      document.getElementById("output").innerText = "";

    fetch(`${baseUrl}/telemetry/${id}`)
        .then(res => res.json())
        .then(data => {
            document.getElementById("output").innerText =
                JSON.stringify(data, null, 2);
        });
}