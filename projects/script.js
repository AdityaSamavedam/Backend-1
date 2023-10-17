// Define an array of Shakespearean quotes or text.
const shakespeareanTexts = [
    "To be or not to be, that is the question.",
    "All the world's a stage, and all the men and women merely players.",
    "Love all, trust a few, do wrong to none.",
    // Add more Shakespearean texts here
];

// Function to display a random Shakespearean text when the button is clicked.
function printShakespeare() {
    const shakespeareTextElement = document.getElementById("shakespeareText");
    const randomIndex = Math.floor(Math.random() * shakespeareanTexts.length);
    const randomText = shakespeareanTexts[randomIndex];
    shakespeareTextElement.textContent = randomText;
}

// Attach the click event listener to the button.
document.getElementById("printButton").addEventListener("click", printShakespeare);
