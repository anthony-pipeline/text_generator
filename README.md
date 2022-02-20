## Generate sentences based on trigrams

# Objectives
The algorithm should be extended so that it can use not only bigrams but also trigrams. Tails should stay the same length as before since we are still aiming to predict the next word in the chain.

This change implies the following tasks:

The list of bigrams should be transformed into a list of trigrams. It should still consist of heads and tails, but now, heads should consist of two space-separated tokens concatenated into a single string. The tails should still consist of one token. For example: head — winter is, tail — coming.
The model should be trained based on the list of trigrams. The model creation requires no modifications since trigrams still consist of a head and a tail.
The beginning of the chain should be a randomly chosen head from the model, not just any word from the corpus.
When predicting the next word, the model should be fed the concatenation of the last two tokens of the chain separated by a space.
After making all these modifications, the output should look rather similar to the result of the previous stage, but now the generated pseudo-sentences should make a little more sense.
