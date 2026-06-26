class TimeMap:

    def __init__(self):
        # Use a hashmap for storing key and values
        # for multiple values, we can use an array as the value of hashmap
        # map[key] = [(timestamp, val), (timestamp, val)...]
        self.struct = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        print("set: ", key, value, timestamp)
        if key in self.struct:
            self.struct[key].append((timestamp, value))
        else:
            self.struct[key] = [(timestamp, value)]
        print(self.struct)
        return

    def get(self, key: str, timestamp: int) -> str:
        print("get: ", key, timestamp)
        if key not in self.struct:
            return ""
        
        valarr = self.struct[key]
        if len(valarr) == 1:
            return valarr[0][1] if valarr[0][0] <= timestamp else ""
        
        result = None
        for val in valarr:
            if val[0] == timestamp: 
                result = val
                break
            if val[0] > timestamp: continue

            result = val if not result else max(val, result)
        if not result: result = (0, "")
        return result[1]

# class TimeMap:

#     def __init__(self):
#         self.keyStore = {}

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         if key not in self.keyStore:
#             self.keyStore[key] = {}
#         if timestamp not in self.keyStore[key]:
#             self.keyStore[key][timestamp] = []
#         self.keyStore[key][timestamp].append(value)

#     def get(self, key: str, timestamp: int) -> str:
#         if key not in self.keyStore:
#             return ""
#         seen = 0

#         for time in self.keyStore[key]:
#             if time <= timestamp:
#                 seen = max(seen, time)
#         return "" if seen == 0 else self.keyStore[key][seen][-1]