class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str=''
        for i in strs:
            final_str += str(len(i)) + '#' + i
        return final_str

    def decode(self, s: str) -> List[str]:
        output_list =[]
        while '#' in s:
            length, _, s = s.partition('#')
            output_list.append(s[:int(length)])
            s = s[int(length):]
        return output_list