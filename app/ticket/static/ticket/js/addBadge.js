

const addBadge = (elementHtml, badgeMap) => {
    const childElement = elementHtml.firstElementChild;
    const classes = badgeMap[elementHtml.textContent];
    
    if(classes){
        childElement.classList.add(...classes)
    }
}

export default addBadge;