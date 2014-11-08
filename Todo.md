# To do for timeline and PE replay #
1. when `dword ptr [xxx]` encountered, we need to do the evaluation to get the value of **xxx**.
2. when a memory pointer is pointing **ASCII** or **Unicode** string, we should log the mapping between pointer and string.
3. when a TRACE is present at the end of another TRACE but not encountered, we should also record it.
4. we should make it clear the exact control path of the whole program.
