class Solution:

    def encode(self, strs: List[str]) -> str:
        print(len(strs))
        if strs == []:
            return ""
        if strs == [""]:
            return "''"
        return '#@'.join(strs)
    
    def decode(self, s: str) -> List[str]:
        print(len(s))
        if s == "":
            return []
        if s == "''":
            return [""]
        
        return s.split('#@')