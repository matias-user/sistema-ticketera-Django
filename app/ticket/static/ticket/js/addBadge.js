

export default addBadge = (element) => {
    elementHtml = document.querySelector(element);
    textElement = elementHtml.textContent;

    switch(textElement){
        case 'Low': elementHtml.classList.add("badge rounded-pill text-bg-light");
        break;
        case 'Medium': elementHtml.classList.add("badge rounded-pill text-bg-info");
        break;
        case 'High': elementHtml.classList.add("badge rounded-pill text-bg-warning");
        break;
        case 'Critic': elementHtml.classList.add("badge rounded-pill text-bg-danger");
        break;
           
    }

}