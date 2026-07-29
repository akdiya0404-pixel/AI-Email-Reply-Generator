const generateButton = document.getElementById("generate");
const emailInput = document.getElementById("email");
const toneInput = document.getElementById("tone");
const replyOutput = document.getElementById("reply");

generateButton.addEventListener("click", async function () {
    const email = emailInput.value.trim();
    const tone = toneInput.value;

    if (email === "") {
        alert("Please paste an email first.");
        return;
    }

    generateButton.disabled = true;
    generateButton.textContent = "Generating...";
    replyOutput.value = "Please wait...";

    try {
        const response = await fetch("/generate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email: email,
                tone: tone
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Failed to generate reply.");
        }

        replyOutput.value = data.reply;

    } catch (error) {
        replyOutput.value = "Error: " + error.message;
    } finally {
        generateButton.disabled = false;
        generateButton.textContent = "Generate Reply";
    }
});