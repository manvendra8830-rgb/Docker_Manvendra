const express = require("express");
const path = require("path");

const app = express();
const PORT = 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use(express.static(path.join(__dirname, "public")));

app.post("/submit", async (req, res) => {
    try {
        const response = await fetch("http://backend:5000/submittodoitem", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                itemName: req.body.itemName,
                itemDescription: req.body.itemDescription
            })
        });

        const data = await response.json();

        if (!response.ok) {
            return res.status(response.status).json(data);
        }

        res.status(201).json(data);
    } catch (error) {
        res.status(500).json({
            error: "Unable to connect to Flask backend.",
            details: error.message
        });
    }
});

app.listen(PORT, "0.0.0.0", () => {
    console.log(`Frontend server running on port ${PORT}`);
});
