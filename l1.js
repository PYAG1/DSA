console.log('apple')

function apple(cards,query){
    let position = 0;
    for(let x =0; x < cards.length; x++){
        if(cards[position]=== query){
            return position
        }
        else{
            position++
        }
    }
}

console.log(apple([1,2,3,4],4))