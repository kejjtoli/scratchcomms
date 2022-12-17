import scratchcomms

exampleText = "Witaj Świecie! Ten tekst został zakodowany i odkodowany za pomocą scratchcomms!"

exampleText = scratchcomms.encode(exampleText)

print("Encoded text: " + exampleText)

exampleText = scratchcomms.decode(exampleText)

print("Decoded text: " + exampleText)