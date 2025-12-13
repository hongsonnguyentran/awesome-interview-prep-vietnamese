# Madlibs là 1 trò chơi, điền từ bất kỳ vào các khoảng trắng trong 1 câu truyện.

story = """
One late night, a [ADJECTIVE_1] programmer named [PROPER NOUN] was debugging code at [PLACE_1].
Out of nowhere, a mysterious [NOUN_1] appeared and began to [VERB_1] [ADVERB], causing pure chaos.

Without hesitation, [PROPER NOUN] grabbed a trusty [OBJECT] and [VERB_2] straight toward the [NOUN_2].
The outcome was completely [ADJECTIVE_2]: everyone nearby started to [VERB_3] because they felt incredibly [EMOTION].

In the end, the whole team chose to [VERB_4] together at [PLACE_2], realizing that [SHORT QUOTE].
"""

print(story)

# Input words with prompts
adj_1 = input("Enter an adjective: ")
proper_noun = input("Enter a proper noun (name): ")
place_1 = input("Enter a place: ")
noun_1 = input("Enter a noun: ")
verb_1 = input("Enter a verb: ")
adv = input("Enter an adverb: ")
obj = input("Enter an object: ")
verb_2 = input("Enter another verb: ")
noun_2 = input("Enter another noun: ")
adj_2 = input("Enter another adjective: ")
verb_3 = input("Enter another verb: ")
emotion = input("Enter an emotion: ")
verb_4 = input("Enter another verb: ")
place_2 = input("Enter another place: ")
short_quote = input("Enter a short quote or saying: ")

print(f"""
One late night, a {adj_1} programmer named {proper_noun} was debugging code at {place_1}.
Out of nowhere, a mysterious {noun_1} appeared and began to {verb_1} {adv}, causing pure chaos.

Without hesitation, {proper_noun} grabbed a trusty {obj} and {verb_2} straight toward the {noun_2}.
The outcome was completely {adj_2}: everyone nearby started to {verb_3} because they felt incredibly {emotion}.

In the end, the whole team chose to {verb_4} together at {place_2}, realizing that {short_quote}.
""")
