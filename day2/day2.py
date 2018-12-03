fp = r"C:\Users\Reid\Code\adventofcode\day2\input.txt"
inputs = []
with open(fp) as f:
	for line in f:
		inputs.append(line.strip())

		
## PART 1
twoLettersCt = 0
threeLettersCt = 0
for word in inputs:
	uniqs = set(word)
	hasTwoLetters = False
	hasThreeLetters = False
	for char in uniqs:
		ct = sum([1 for part in word if part == char])
		if ct == 2 and not hasTwoLetters:
			twoLettersCt += 1
			hasTwoLetters = True
		if ct == 3 and not hasThreeLetters:
			threeLettersCt += 1
			hasThreeLetters = True
		if hasTwoLetters and hasThreeLetters:
			break
			
print(f"Part 1 Answer:{twoLettersCt * threeLettersCt}")


## PART 2
checksums = []
for word in inputs:
	asciiCodes = [ord(c) for c in word]
	checksums.append(sum(asciiCodes))
	
checksums = sorted(enumerate(checksums), key=lambda x:x[1])
for idx1, (inputidx1, checksum1) in enumerate(checksums):
	word1 = inputs[inputidx1]
	for idx2, (inputidx2, checksum2) in enumerate(checksums[idx1+1:]):
		word2 = inputs[inputidx2]
		if checksum2 - checksum1 > 25:
			break
		else:
			matchingString = ''.join([char1 for char1,char2 in zip(word1,word2) if char1==char2])
			if len(matchingString) == 25:
				print(f"Part 2 Answer:{matchingString}")


