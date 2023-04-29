function toCamelCase(str){
    let finalString = ""
    const argArray = str.split('')
    for (let i = 0; i < argArray.length; i++){
        if (argArray[i] === '-' || argArray[i] === '_'){
            let nextLetter = argArray[i+1]

            let regExp = /[A-Z]/
            let isCapital = nextLetter.search(regExp)
            if (isCapital < 0) {
                nextLetter = nextLetter.toUpperCase()
            }
                finalString += nextLetter
                i += 1
        } else {
            finalString += argArray[i]
        }

    }
    return finalString
}


function toCamelCase(str){
    var regExp=/[-_]\w/ig;
    return str.replace( regExp, handleMatch );
}

function handleMatch( match ) {
    return match.charAt(1).toUpperCase()
}

/**
 * input: the-stealth-warrior
 *
 * return: theStealthWarrior
 *
 *
 *
 * input: The-stealth-warrior
 *
 * return: TheStealthWarrior
 *
 *
 * describe("Tests", () => {
    it("test", () => {
        assert.strictEqual(toCamelCase(''), '', "An empty string was provided but not returned")
        assert.strictEqual(toCamelCase("the_stealth_warrior"), "theStealthWarrior", "toCamelCase('the_stealth_warrior') did not return correct value")
        assert.strictEqual(toCamelCase("The-Stealth-Warrior"), "TheStealthWarrior", "toCamelCase('The-Stealth-Warrior') did not return correct value")
        assert.strictEqual(toCamelCase("A-B-C"), "ABC", "toCamelCase('A-B-C') did not return correct value")
    });
});
 */

function lg( ...msg ) {
    console.log( ...msg );
}

console.log( toCamelCase('The-stealth-warrior') );