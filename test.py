import scratchcomms

exampleText = "Hello world! This text just got encoded and decode^d using scratchcomms."

exampleText = scratchcomms.encode(exampleText)

print("Encoded text: " + exampleText)

exampleText = scratchcomms.decode(exampleText)

print("Decoded text: " + exampleText)