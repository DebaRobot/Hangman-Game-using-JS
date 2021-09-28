<!DOCTYPE html>
<html lang="en">
<head>
    <title>Hangman</title>
</head>
<body>
    <script>
        //create an array of words
        var words = ["rabbit", "snail", "carrot", "airports"];

        //pick a random words
        var word =  words[Math.floor(Math.random()* words.length)];

        //set up the answer Array
        //show how many letter are in the word
        var answerArray = [];
        for(var i = 0; i < word.length; i++){
            answerArray[i] = "_";
        }
        var remainingLetters = word.length;

        //          ******* THE MAIN GAME *****
      
        //while there are letter left to be guessed
        while(remainingLetters > 0){
            //show the player the progress

            alert(answerArray.join(" "))
            // - - - - - 

            //get a guess from the player
            var guess  = prompt("Guess a letter or Click cancel to stop the play")

            //if the guess is blank
            if(guess == null){
                //exit the game loop

                break;
            //if the guess is more than one letter
            }
            else if(guess.length != 1){
                //alert them to a single letter only
                alert("Please enter a single letter")

                //valid Guess
            }else{
                //update the game state with the guess
                for(var j = 0; j< word.length; j++){
                    //if the letter they guessed is in the word at that point
                    if(word[j] === guess){
                        //update the answer array with the letter they guessed
                        answerArray[j] = guess;
                        //substract one from remaining letter
                        remainingLetters--;
                    }

                }
            }

        //**********END OF THE GAME LOOP******
    }
    //LET  player know the word
    alert(answerArray.join(" "));
    //word akta akta kore join korche
    //congratulates the player
    alert("Good Job !! The answer was " + word);
    </script>
</body>
</html>
