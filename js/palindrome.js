const palindrome = function(word) {
    word = word.toString().replaceAll(/[^a-zA-Z0-9]/ig, '').toLowerCase();
    if (word.length < 2) return true
    if (word[0] === word.slice(-1)) {
        word = word.slice(1, word.length-1);
        return palindrome(word);
    }
    return false
};

module.exports = { palindrome }
