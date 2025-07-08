document.getElementById("submit-btn").addEventListener("click", async function () {
    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const data = {
        username: username,
        email: email,
        password: password
    };

    try {
        const response = await fetch("http://127.0.0.1:8000/api/register/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            alert("Registration successful!");
            console.log(result);
        } else {
            alert("Registration failed!");
            console.error(result);
        }
    } catch (error) {
        console.error("Error:", error);
        alert("An error occurred. See console.");
    }
});
