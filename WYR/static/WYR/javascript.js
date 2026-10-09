document.addEventListener("DOMContentLoaded", function () {
function updateVoteBar() {
// Get the vote-count elements.
const blueVoteElement = document.getElementById("blueVotes");
const redVoteElement = document.getElementById("redVotes");

    // Get the two coloured sections of the bar.
    const blueBar = document.getElementById("meterBlue");
    const redBar = document.getElementById("meterRed");

    // Stop if any required element is missing.
    if (!blueVoteElement || !redVoteElement || !blueBar || !redBar) {
        return;
    }

    // Read the actual vote counts rendered by Django.
    const blueVotes = Math.max(0, Number(blueVoteElement.textContent.trim()) || 0);
    const redVotes = Math.max(0, Number(redVoteElement.textContent.trim()) || 0);

    const totalVotes = blueVotes + redVotes;

    // Calculate each option's percentage.
    let bluePercentage;
    let redPercentage;

    if (totalVotes === 0) {
        bluePercentage = 50;
        redPercentage = 50;
    } else {
        bluePercentage = (blueVotes / totalVotes) * 100;
        redPercentage = (redVotes / totalVotes) * 100;
    }

    // Update the widths of the coloured sections.
    blueBar.style.flexBasis = bluePercentage + "%";
    redBar.style.flexBasis = redPercentage + "%";

    // Display the rounded percentages.
    blueBar.textContent = Math.round(bluePercentage) + "%";
    redBar.textContent = Math.round(redPercentage) + "%";

    // Accessibility: describe the current percentages.
    blueBar.setAttribute("aria-label", "Blue option: " + Math.round(bluePercentage) + "%");
    redBar.setAttribute("aria-label", "Red option: " + Math.round(redPercentage) + "%");
}

updateVoteBar();

});