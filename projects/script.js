const shakespeareanTexts = [
    "To be or not to be, that is the question.",
    "All the world's a stage, and all the men and women merely players.",
    "Love all, trust a few, do wrong to none.",
    // Add more Shakespearean texts here
];

function printShakespeare() {
    const shakespeareTextElement = document.getElementById("shakespeareText");
    const randomIndex = Math.floor(Math.random() * shakespeareanTexts.length);
    const randomText = shakespeareanTexts[randomIndex];
    shakespeareTextElement.textContent = randomText;
}

document.getElementById("printButton").addEventListener("click", printShakespeare);