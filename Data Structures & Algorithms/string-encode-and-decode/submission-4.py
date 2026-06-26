class Solution:
    # For out encoding, we will use the following format
    # numOfStrs(N)|lenOfStr1|str1|lenofStr2|str2|...|lenOfStrN|strN
    def encode(self, strs: List[str]) -> str:
        N = len(strs)
        encoded_str = ""
        encoded_str += str(N)

        for s in strs:
            len_s = len(s)
            packet = f"|{len_s}|{s}"
            encoded_str += packet
        print(f"encoded: {encoded_str}")
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded = []
        if not s:
            print("No msg to decode")
            return []
        print(f"msg to decode: {s}")
        tmp = s.split("|", 1)
        N = int(tmp[0])
        if N == 0:
            return[]
        s = str(tmp[1])

        for i in range(N):
            # Split the lenOfStrN and rest of the string
            tmp = s.split("|", 1)
            l, part = int(tmp[0]), str(tmp[1])
            substr = part[:l]

            # check if decoding successful
            if not len(substr) == l:
                print("unsuccessful at breaking strings")

            if not i == N - 1:
                s = part[l + 1 :]
            decoded.append(substr)

        return decoded
