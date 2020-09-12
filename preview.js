const genreInput = document.querySelector('#genre > input');
const descriptInput = document.querySelector('#descript > input');
const tagInput = document.querySelector('#tag > input');
// const descripInput
const cardGenreInput = document.querySelector('#genrename > input');
const cardTagInput = document.querySelector('#cardTag > input');
const cardDescriptInput = document.querySelector('#descriptName > input');


console.log(cardGenreInput)
console.log(cardDescriptInput)


function showOnCardTitle() {
    const genreTitle = genreInput.value;
    cardGenreInput.value = genreTitle;
    console.log(cardGenreInput.value);
}

function showOnCardTag() {
    const tagTitle = tagInput.value;
    cardTagInput.value = tagTitle;
    console.log(cardTagInput.value)
}

function showOnCardDescript() {
    const descriptTitle = descriptInput.value;
    cardDescriptInput.value = descriptTitle;
}


function main() {
    console.log("yoo")
    genreInput.addEventListener('input', showOnCardTitle);
    descriptInput.addEventListener('input', showOnCardDescript);
    // tagInput.addEventListener('input', showOnCardTag);
}

main();