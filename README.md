# spell
Spell is a library for checking words similarity and spellchecking.

## Installing

Download spell package and `import spell`

## Usage

Here is a small example:

`
sp = spell.Spell()
sp.same_words(words_list=['сделонныый', 'сссделанный', 'хорошо'])
`

Here is the output:

`
{'сделонныый': ['сссделанный'], 'сссделанный': ['сделонныый'], 'хорошо': []}
`

So, the `same_words()` method returns dictionary, where keys are the word from `words_list`, values -- same (similar) words from this `words_list`
Another example -- detecting the correct word from given dictionary of correct words:

`
sp.word_from_dict('сделонний', ['сделанный', 'красивый', 'сделать'])
`

And the output:

`
['сделанный']
`

## Contributing

You can contribute to our repository via pushing your commits, it is absolutely open-source.
