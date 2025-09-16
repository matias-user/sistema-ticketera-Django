import  addBadge from "./addBadge.js"

const tdPriority = document.querySelector("#priority");
const badgeTdPriorityMap = {
    'Low': ["badge", "rounded-pill", "text-bg-light"],
    'Medium': ["badge", "rounded-pill", "text-bg-info"],
    'High': ["badge", "rounded-pill", "text-bg-warning"],
    'Critic': ["badge", "rounded-pill", "text-bg-danger"]
};
// Add bagde to td Priority in list_tickets.html
addBadge(tdPriority, badgeTdPriorityMap);

// Add bagde to td State in list_tickets.html
const badgeTdStatetyMap = {
    'In progress': ["badge", "rounded-pill", "text-bg-info"],
    'Finished': ["badge", "rounded-pill", "text-bg-success"],
};
const tdState = document.querySelector("#state");

addBadge(tdState, badgeTdStatetyMap);
