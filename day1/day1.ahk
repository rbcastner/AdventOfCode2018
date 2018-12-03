#include C:\Users\Reid\Code\nexusce\classes\Utilities.ahk

;; PART 1
FileRead, FileContents, Input.txt
a := 0
Loop, Parse, FileContents, `n, `r
{
	a += A_LoopField
}
MsgBox % "Part 1 answer : " . a


;; PART 2
a := 0
b := []
loopindex := 0
while (true) {
	; MsgBox % loopindex
	Loop, Parse, FileContents, `n, `r
	{
		a += A_LoopField
		if (b.HasKey(a)) {	
			MsgBox % "First Frequency that repeats is " . a
			exitapp
		} else {
			b[a] := 1
		}
	}
	; MsgBox % a
	loopindex += 1
}